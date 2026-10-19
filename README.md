# E-commerce Sales & Customer Analytics

## Project Overview

The **E-commerce Sales & Customer Analytics** project analyzes online retail transactions to understand sales performance, customer purchasing behavior, and customer loyalty.

The project uses Python for data cleaning and RFM customer segmentation, SQL for querying and analyzing data, and Power BI for building interactive dashboards.

## Objectives

- Analyze total revenue, orders, customers, and products.
- Identify top-performing countries and products.
- Identify high-value customers.
- Understand customer purchasing behavior.
- Segment customers using RFM analysis.
- Identify loyal customers and customers who may be at risk of becoming inactive.
- Present actionable business insights through interactive dashboards.

## Tools & Technologies

- **Python:** Data cleaning, data processing, and RFM analysis.
- **Pandas:** Data manipulation and analysis.
- **SQL / MySQL:** Data storage, querying, and analysis.
- **Microsoft Power BI:** Interactive dashboards and data visualization.
- **Microsoft Excel / CSV:** Dataset storage and data exchange.

## Dataset

**Dataset:** Online Retail Dataset

The dataset contains transaction-level information from an online retail business.

Important columns include:

- `InvoiceNo` — Invoice or transaction number.
- `StockCode` — Product identifier.
- `Description` — Product description.
- `Quantity` — Number of units purchased.
- `InvoiceDate` — Date and time of the transaction.
- `UnitPrice` — Price per unit.
- `CustomerID` — Customer identifier.
- `Country` — Customer's country.
- `Revenue` — Calculated transaction revenue.

## Project Workflow

1. **Data Collection:** Load the online retail dataset.
2. **Data Cleaning:** Handle missing customer IDs, invalid quantities, cancelled transactions, and other data-quality issues as appropriate.
3. **Data Processing:** Prepare the cleaned dataset for analysis.
4. **SQL Analysis:** Store and query transaction data using MySQL.
5. **RFM Analysis:** Calculate Recency, Frequency, and Monetary values for customer segmentation.
6. **Power BI Visualization:** Build interactive dashboards to explore sales performance and customer segments.
7. **Business Insights:** Use the analysis to understand sales trends and customer retention opportunities.

## RFM Customer Segmentation

RFM stands for:

- **Recency (R):** How recently a customer purchased.
- **Frequency (F):** How often a customer purchased.
- **Monetary (M):** How much a customer spent.

Customers are assigned scores and segments based on their RFM behavior.

Common customer segments may include:

- **Champions:** Recent, frequent, and high-value customers.
- **Loyal Customers:** Customers who purchase regularly.
- **Potential Loyalists:** Customers who show potential to become regular buyers.
- **New Customers:** Customers who have purchased recently.
- **At Risk:** Previously valuable customers who have not purchased recently.
- **Hibernating or Lost Customers:** Customers who have been inactive for a longer period.

The actual segments depend on the scoring and classification rules implemented in the project.

## Power BI Dashboard

### Page 1: Sales Dashboard

The first page provides an overview of the online store's sales performance.

**Key Performance Indicators (KPIs):**
- Total Revenue
- Total Orders
- Total Customers
- Total Products

**Visualizations:**
- Monthly Revenue Trend
- Top 10 Countries by Revenue
- Top 10 Products by Revenue
- Top 10 Customers by Revenue

**Interactive Filters:**
- Country slicer
- Invoice date range slicer

### Page 2: RFM Customer Analysis

The second page focuses on customer segmentation and purchasing behavior.

**Visualizations:**
- Customer Segment Distribution — Donut chart
- Customer Count by Segment — Bar chart
- Average Customer Spending by Segment — Column chart
- Average Days Since Last Purchase — Bar chart

These visuals help compare customer segments, understand spending behavior, and identify customers who may need retention campaigns.

## Business Insights

The project helps a business:

- Monitor overall sales performance.
- Identify high-performing countries and products.
- Recognize valuable and loyal customers.
- Understand differences in customer spending.
- Identify customers who may be at risk of becoming inactive.
- Develop targeted marketing and customer retention strategies.

## Project Structure

```text
Ecommerce_Sales_Customer_Analytics/
│
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx
│   └── processed/
│       ├── cleaned_online_retail.csv
│       └── rfm_customer_segments.csv
│
├── notebooks/
│   └── Data cleaning and RFM analysis notebooks
│
├── sql/
│   └── SQL analysis queries
│
├── powerbi/
│   └── Ecommerce_Sales_Customer_Analytics.pbix
│
├── requirements.txt
└── README.md
```

*Note: The folder structure describes the intended organization. Adjust filenames to match the files actually present in your project.*

## Expected Outcome

The project combines sales analytics and customer analytics in one solution. It transforms raw retail transactions into useful business insights using Python, MySQL, and Power BI.

The final dashboards help users explore sales performance, compare customer segments, and identify opportunities to improve customer retention.

## Future Enhancements

- Add customer retention and repeat-purchase analysis.
- Analyze monthly and yearly sales growth.
- Develop customer lifetime value estimates.
- Add automated data refresh.
- Build sales forecasting models.
- Deploy the dashboard for business users.

## Author

**Akshay Singh**

Computer Science Engineering Student | Aspiring Data Analyst

**Skills demonstrated:** Python, Pandas, SQL, MySQL, RFM Analysis, Data Cleaning, Data Visualization, and Power BI.
