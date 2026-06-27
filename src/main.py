import pandas as pd
from analysis import clean_data, calculate_metrics
from charts import create_revenue_chart
# Import our new export utility
from utils import export_text_report

def load_data():
    try:
        return pd.read_csv("../data/sales.csv")
    except FileNotFoundError:
        print("Error: sales.csv not found.")
        return None

if __name__ == "__main__":
    # 1. Loads the raw data
    raw_df = load_data()
    
    if raw_df is not None:
        # 2. Cleans the data
        cleaned_sales = clean_data(raw_df)
        
        # 3. Analyzes the data
        metrics, product_perf, region_perf = calculate_metrics(cleaned_sales)
        
        # 4. Prints to Console for a quick check
        print("\n" + "="*30)
        print("      EXECUTIVE SALES REPORT      ")
        print("="*30)
        print(f"Total Revenue Generated:  ${metrics['total_revenue']:,}")
        print(f"Total Orders Processed:   {metrics['total_sales_count']}")
        print(f"Average Order Value:      ${metrics['avg_order_value']:.2f}")
        print("-"*30)
        print(f"Top Product:              {metrics['best_product']} (${metrics['best_product_revenue']:,})")
        print(f"Top Performing Region:   {metrics['best_region']} region (${metrics['best_region_revenue']:,})")
        print("="*30 + "\n")
        
        # 5. Generate and Save Visual Charts
        create_revenue_chart(product_perf)
        
        # 6. Export the official Report File
        export_text_report(metrics)