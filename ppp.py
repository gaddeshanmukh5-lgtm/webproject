import pandas as pd

file_path = "sales_data.xlsx"
df = pd.read_excel(r"C:\Users\HP\Downloads\sales_data.xlsx")

df['TotalSales'] = df['Units'] * df['UnitPrice']

total_sales_by_region = df.groupby('Region')['TotalSales'].sum()
print("\nTotal Sales by Region:\n", total_sales_by_region)

top_3_salespersons = df.groupby('SalesPerson')['TotalSales'].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Salespersons by Total Sales:\n", top_3_salespersons)

high_value_transactions = df[df['TotalSales'] > 5000]
print("\nTransactions where TotalSales > 5000:\n", high_value_transactions)

product_stats = df.groupby('Product').agg({'Units': 'sum', 'UnitPrice': 'mean'})
print("\nProduct Statistics (Units Sold & Avg Price):\n", product_stats)

df_sorted = df.sort_values(by='TotalSales', ascending=False)

output_file = "sales_report.xlsx"
df_sorted.to_excel(output_file, index=False)
print(f"\nReport exported successfully as {output_file}")