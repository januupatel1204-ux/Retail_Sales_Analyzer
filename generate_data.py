# generate_data.py

import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2019-01-01", end="2023-12-31", freq="D")

categories = ["Electronics", "Clothing", "Home", "Sports"]

data = []

for date in dates:
    year_growth_factor = 1 + (date.year - 2019) * 0.08  # 8% yearly growth
    
    for category in categories:
        base_price = {
            "Electronics": 500,
            "Clothing": 50,
            "Home": 150,
            "Sports": 120
        }[category]
        
        seasonal_factor = 1.2 if date.month in [10,11,12] else 1
        quantity = np.random.randint(5, 50)
        
        revenue = quantity * base_price * seasonal_factor * year_growth_factor
        
        data.append([date, category, quantity, round(revenue,2)])

df = pd.DataFrame(data, columns=["Date", "Category", "Quantity", "Revenue"])

df.to_csv("retail_sales_data.csv", index=False)

print("Data generated successfully.")