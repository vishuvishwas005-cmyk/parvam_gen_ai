# More Pandas Operations

import pandas as pd
import numpy as np

# Creating sample data
np.random.seed(42)
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'] * 4,
    'Sales': np.random.randint(100, 1000, 20),
    'Region': ['North', 'South', 'East', 'West'] * 5,
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'] * 5
}

df = pd.DataFrame(data)
print("Sales DataFrame:")
print(df.head(10))
print()

# Data cleaning
print("Missing values:")
print(df.isnull().sum())
print()

# Handling duplicates
df_no_duplicates = df.drop_duplicates()
print("Shape after removing duplicates:", df_no_duplicates.shape)
print()

# Sorting
sorted_df = df.sort_values(by='Sales', ascending=False)
print("Sorted by Sales (descending):")
print(sorted_df.head())
print()

# Pivot tables
pivot_table = pd.pivot_table(df, values='Sales', index='Product', columns='Region', aggfunc='sum')
print("Pivot table (Product vs Region):")
print(pivot_table)
print()

# Merging DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

merged_df = pd.merge(df1, df2, on='key', how='outer')
print("Merged DataFrames:")
print(merged_df)
print()

# Applying functions
def categorize_sales(sales):
    if sales > 700:
        return 'High'
    elif sales > 400:
        return 'Medium'
    else:
        return 'Low'

df['Sales_Category'] = df['Sales'].apply(categorize_sales)
print("DataFrame with Sales Category:")
print(df[['Product', 'Sales', 'Sales_Category']].head())
print()

# Exporting to CSV
# df.to_csv('sales_data.csv', index=False)
print("DataFrame exported to CSV (commented out)")