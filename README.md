# Web Scraping Project - Job Listings Data Pipeline

## Overview
This project involves web scraping job listings from platforms like **Indeed** and processing the data for analysis and visualization. The pipeline follows a structured **ELT (Extract, Load, Transform) approach**, leveraging **Azure Data Lake Storage** for efficient data handling.

## Tools & Technologies Used
- **Tools:** VSC (Visual Studio Code), SSMS (SQL Server Management Studio), Airflow
- **Languages/Libraries:** Python, PySpark/Pandas, Selenium, SQL

## Data Pipeline Workflow

### 1. Scraping the Data (Extraction)
- **Selenium** is used to extract **job-related data** (job postings, company names, ratings, salaries, and locations) from web sources.
- **Three Types of sample data with Salary per Year, Month and No Salary**
   - **(Power BI & SQL Developer,Sanglob Business Services Private Limited,Pune, Maharashtra,480000 - 960000  year)**
   - **(Sr.AI/ML Engineer,Jobbycart Technologies,Tiruchchirappalli, Tamil Nadu,25000 - 100000  month)**
   - **(GBS Data Operations - Document Control & Engineering Data Senior Analyst,BP Energy,Hybrid work in Pune, Maharashtra,Not Mentioned)**

### 2. Processing & Storing as Raw Data (Bronze Layer)
- The extracted data is processed and stored locally as a **.txt file**, marking the **Bronze Layer** stage.
- As far as we used only **4 jobs to extract**, An **Average count of 766 rows/file**
    ![image](https://github.com/user-attachments/assets/564a5c99-c7ff-4e67-b618-0669f8633aab)

### 3. Loading Data into Azure Data Lake (Bronze → Silver Layer)
- The locally stored data is ingested into **Azure Data Lake Storage** for further processing.
- This transition ensures that raw data is securely stored and ready for transformation.
- ![image](https://github.com/user-attachments/assets/a93fd741-4825-4cb0-80fa-59e8da776ead)


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

