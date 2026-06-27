import pandas as pd

def clean_data(df):
    """Cleans the raw sales data and calculates individual row revenue."""
    cleaned_df = df.copy()
    cleaned_df['Quantity'] = cleaned_df['Quantity'].fillna(1).astype(int)
    cleaned_df['Revenue'] = cleaned_df['Quantity'] * cleaned_df['Unit_Price']
    return cleaned_df

def calculate_metrics(df):
    """Calculates key business performance metrics using aggregation."""
    metrics = {}
    
    # 1. High-level totals
    metrics['total_revenue'] = df['Revenue'].sum()
    metrics['total_sales_count'] = df.shape[0]
    metrics['avg_order_value'] = df['Revenue'].mean()
    
    # 2. Grouping by Product to find the top seller
    # .groupby() aggregates data, .sum() adds up the columns for each group
    product_summary = df.groupby('Product')['Revenue'].sum()
    metrics['best_product'] = product_summary.idxmax() # idxmax returns the name of the highest value
    metrics['best_product_revenue'] = product_summary.max()
    
    # 3. Grouping by Region
    region_summary = df.groupby('Region')['Revenue'].sum()
    metrics['best_region'] = region_summary.idxmax()
    metrics['best_region_revenue'] = region_summary.max()
    
    return metrics, product_summary, region_summary