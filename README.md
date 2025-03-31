# Web Scraping Project - Job Listings Data Pipeline

## Overview
This project involves web scraping job listings from platforms like **Indeed** and processing the data for analysis and visualization. The pipeline follows a structured **ELT (Extract, Load, Transform) approach**, leveraging **Azure Data Lake Storage** for efficient data handling.

## Tools & Technologies Used
- **Tools:** VSC (Visual Studio Code), SSMS (SQL Server Management Studio)
- **Technologies:** Python, PySpark/Pandas, Selenium, SQL

## Data Pipeline Workflow

### 1. Scraping the Data (Extraction)
- **Selenium** is used to extract **job-related data** (job postings, company names, ratings, salaries, and locations) from web sources.

### 2. Processing & Storing as Raw Data (Bronze Layer)
- The extracted data is processed and stored locally as a **.txt file**, marking the **Bronze Layer** stage.

### 3. Loading Data into Azure Data Lake (Bronze → Silver Layer)
- The locally stored data is ingested into **Azure Data Lake Storage** for further processing.
- This transition ensures that raw data is securely stored and ready for transformation.

### 4. Transforming the Data (Silver Layer)
- The **structured and refined data** is processed and stored in the **Silver Layer** of the Data Lake.
- This step ensures **data quality and consistency** for analytics.

### 5. Further Transformation & Storing in Data Warehouse (Gold Layer)
- The cleaned and optimized data is **further transformed** for **visualization** and stored in a **Data Warehouse (Gold Layer)**.

### 6. Visualization
- The final dataset is used for **graphical representation and analytics**.
- Various **charts and graphs** provide insights into job trends, salary distributions, and company ratings.

## Key Takeaways
- **Azure Data Lake Storage** is utilized for **managing different data layers (Bronze → Silver → Gold)**.
- **Python & PySpark/Pandas** handle data transformation efficiently.
- **SQL & SSMS** are used for querying and managing structured data.
- The structured pipeline ensures **scalability and automation** for job market analysis.

## Future Enhancements
- Automate the web scraping process using **scheduled jobs**.
- Implement **real-time data ingestion** using streaming technologies.
- Enhance **visualization dashboards** using Power BI or Tableau.

---

# Here is the Workflow of the Project Visually

![WebScrapping - Webscraping(Indeed)](https://github.com/user-attachments/assets/a4f464a8-e882-4de9-8f72-42b8344a25da)

