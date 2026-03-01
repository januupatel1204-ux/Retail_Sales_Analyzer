import pandas as pd

def load_data():
    df = pd.read_csv("sales_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


def total_revenue(df):
    return df["Revenue"].sum()


def yearly_revenue(df):
    df["Year"] = df["Date"].dt.year
    return df.groupby("Year")["Revenue"].sum()


def monthly_revenue(df):
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Revenue"].sum()


def monthly_units_sold(df):
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Quantity"].sum()


def category_analysis(df):
    return df.groupby("Category")["Revenue"].sum()