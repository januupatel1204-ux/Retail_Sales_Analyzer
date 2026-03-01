import streamlit as st
import matplotlib.pyplot as plt
from backend import *

st.set_page_config(page_title="Retail Sales Analyzer", layout="centered")

# Landing Page State
if "start" not in st.session_state:
    st.session_state.start = False

# Landing Page
if not st.session_state.start:

    st.title("📊 Retail Sales Analytics Dashboard")

    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71",
        use_container_width=True
    )

    st.write("Analyze multi-year retail sales performance with interactive insights.")

    if st.button("Start Analysis 🚀"):
        st.session_state.start = True
        st.rerun()

else:

    df = load_data()

    st.title("Sales Performance Overview")

    # KPI Metrics (Medium Compact Layout)
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Revenue", f"₹ {total_revenue(df):,.2f}")

    with col2:
        st.metric("Total Units Sold", f"{df['Quantity'].sum():,}")

    st.divider()

    # ---------- Medium Size Graph Style ----------

    def show_plot(title, data, plot_type="line"):
        st.subheader(title)

        fig, ax = plt.subplots(figsize=(7, 4))   # Medium graph size

        if plot_type == "bar":
            data.plot(kind="bar", ax=ax)
        elif plot_type == "pie":
            data.plot(kind="pie", autopct="%1.1f%%", ax=ax)
            ax.set_ylabel("")
        else:
            data.plot(ax=ax)

        ax.grid(True, alpha=0.2)
        st.pyplot(fig)

    # Yearly Revenue
    show_plot("📈 Yearly Revenue Growth", yearly_revenue(df), "bar")

    # Monthly Revenue Trend
    show_plot("📊 Monthly Revenue Trend", monthly_revenue(df))

    # Monthly Units Sold
    show_plot("📦 Monthly Units Sold", monthly_units_sold(df))

    # Category Analysis
    show_plot("🛍️ Revenue by Category", category_analysis(df), "pie")

    # Summary Section
    st.divider()
    st.subheader("📌 Summary Analysis")

    yearly_data = yearly_revenue(df)
    monthly_data = monthly_revenue(df)
    category_data = category_analysis(df)

    st.write(f"✅ Total revenue generated is ₹ {total_revenue(df):,.2f}")
    st.write(f"⭐ Highest revenue year → **{yearly_data.idxmax()}**")
    st.write(f"🔥 Peak revenue month → **{str(monthly_data.idxmax())}**")
    st.write(f"🏆 Best category → **{category_data.idxmax()}**")

    st.success("Analysis Completed Successfully")