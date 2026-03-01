📊 Retail Sales Analytics Dashboard

A multi-year retail sales analysis dashboard built using Python and Streamlit.
This project simulates realistic retail sales data and transforms it into business insights through structured analytics and interactive visualization.

🚀 Project Overview

The Retail Sales Analyzer is designed to:
Simulate 4+ years of retail sales data (2019–2023)
Capture seasonal trends and year-over-year growth
Analyze revenue and units sold
Compare category-level performance
Present results via an interactive dashboard
The focus of this project is not just visualization — but clean architecture, analytical reasoning, and business insight extraction.

🧠 Key Features
📈 Yearly revenue growth analysis
📊 Monthly revenue trend
📦 Monthly units sold trends
🛍️ Category-wise revenue distribution
📌 Automated performance summary insights
🧩 Modular backend structure

🏗️ Project Architecture
Retail_Sales_Analyzer/
│
├── generate_data.py      # Synthetic multi-year dataset generation
├── backend.py            # Data processing & analytics logic
├── app.py                # Streamlit dashboard frontend
├── retail_sales_data.csv # Generated dataset
└── README.md

Architecture Principle Used
Separation of Concerns
Data generation layer
Analytics/business logic layer
Presentation/UI layer
This mirrors production-grade design thinking.

📊 Data Simulation Logic

The dataset includes:
2019–2023 daily sales records
4 product categories:
Electronics
Clothing
Home
Sports
Seasonal revenue spikes (Q4 boost)
Year-over-year growth factor
Randomized quantity variations
Libraries used:
NumPy
Pandas

📈 Dashboard Components
KPI Metrics
Total Revenue
Total Units Sold
Visualizations
Yearly Revenue (Bar Chart)
Monthly Revenue Trend (Line Chart)
Monthly Units Sold (Line Chart)
Category Revenue Distribution (Pie Chart)
Summary Section
Automatically identifies:
Highest revenue year
Peak performing month
Best performing category

🛠️ Tech Stack
Python 3.x
Pandas
NumPy
Matplotlib
Streamlit
`
🚀 Future Improvements
Interactive filters (Year / Category selection)
Forecasting model integration
Cloud deployment
Downloadable analytics reports
Interactive Plotly visualizations
REST API integration
