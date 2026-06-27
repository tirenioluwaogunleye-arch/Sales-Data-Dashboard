def export_text_report(metrics):
    """
    Takes the calculated metrics and exports them into a professional text file.
    """
    report_path = "../reports/sales_summary_report.txt"
    
    # Using 'with open' automatically closes the file when we are done writing
    with open(report_path, "w") as file:
        file.write("==========================================\n")
        file.write("          ANNUAL SALES REPORT             \n")
        file.write("==========================================\n\n")
        
        file.write(f"Total Revenue Generated:  ${metrics['total_revenue']:,}\n")
        file.write(f"Total Orders Processed:   {metrics['total_sales_count']}\n")
        file.write(f"Average Order Value:      ${metrics['avg_order_value']:.2f}\n")
        file.write("------------------------------------------\n")
        file.write(f"Top-Selling Product:      {metrics['best_product']} (${metrics['best_product_revenue']:,})\n")
        file.write(f"Top-Performing Region:    {metrics['best_region']} Region (${metrics['best_region_revenue']:,})\n\n")
        
        file.write("==========================================\n")
        file.write("Report generated automatically via Python.\n")
        file.write("==========================================\n")
        
    print(f"--- Text report successfully exported to: {report_path} ---")