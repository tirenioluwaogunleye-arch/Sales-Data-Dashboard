import matplotlib.pyplot as plt

def create_revenue_chart(product_summary):
    """
    Generates a bar chart of revenue by product and saves it to the images folder.
    """
    # 1. Create a figure/canvas for the chart
    plt.figure(figsize=(10, 6))
    
    # 2. Build the bar chart using our product data
    product_summary.plot(kind='bar', color='skyblue', edgecolor='black')
    
    # 3. Add labels and a title to make it professional
    plt.title('Total Revenue by Product', fontsize=16, fontweight='bold')
    plt.xlabel('Product Name', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    
    # 4. Clean up layout so nothing gets cut off
    plt.tight_layout()
    
    # 5. Save the chart directly into our images directory
    chart_path = "../images/product_revenue.png"
    plt.savefig(chart_path)
    
    # Clear the current figure to free up memory
    plt.close()
    
    print(f"--- Chart successfully saved to: {chart_path} ---")