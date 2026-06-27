# Retail Sales Data Analysis Dashboard

A modular Python data pipeline designed to ingest, clean, analyze, and visualize corporate sales performance data. This project simulates a real-world analytics engineering workflow by transforming raw transactional data into high-level business intelligence.

##  Project Structure

Sales-Data-Dashboard/
│
├── data/
│   └── sales.csv             # Raw transactional dataset (contains missing fields)
│
├── images/
│   └── product_revenue.png   # Generated data visualizations
│
├── reports/
│   └── sales_summary_report.txt  # Automated executive text summary
│
├── src/
│   ├── main.py               # Application entry point & workflow coordinator
│   ├── analysis.py           # Data cleaning & business metric calculations
│   ├── charts.py             # Data visualization generation (Matplotlib)
│   └── utils.py              # Export and utility actions
│
└── requirements.txt          # Project dependencies


## Core Features

- Automated Data Cleaning: Imputes missing order quantity details gracefully via Pandas vectorization.
- Granular Grouping Operations: Dynamically aggregates total revenue performance by specific product categories and regional footprints.
- Visual Analytics: Generates programmatic bar charts using Matplotlib to instantly highlight top profit drivers.
- Automated Reporting: Generates an executive text summary report exported directly into a dedicated folder for stakeholder distribution.

## Technologies Used

- **Language:** Python
- **Libraries:** Pandas, Matplotlib

## Installation & How to Run

1. Clone the repository to your local machine.
2. Ensure you have the dependencies installed:
   ```bash
   pip install -r requirements.txt