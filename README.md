<p align="center">
  <img src="images/banner.png" width="100%">
</p>

# Enterprise Lakehouse with Databricks

## Architecture
![Architecture](images/architecture.png)
![Databricks](https://img.shields.io/badge/Databricks-EF3E42?style=for-the-badge&logo=databricks&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-0A84FF?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge)
![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-FF3621?style=for-the-badge)

---

# Project Pipeline

The following diagram illustrates the complete end-to-end data flow implemented in this project.

<p align="center">
  <img src="images/pipeline.png" width="100%">
</p>

# Medallion Architecture

The Medallion Architecture organizes data into three logical layers that progressively improve data quality and business value.

<p align="center">
  <img src="images/medallion.png" width="95%">
</p>

### Bronze Layer
- Raw data ingestion
- Immutable source data
- Audit and replay support

### Silver Layer
- Cleansed and validated datasets
- Standardization and enrichment
- Business rules applied

### Gold Layer
- Curated analytical datasets
- Star schema modeling
- Business-ready tables for BI and dashboards

## Project Overview

This project demonstrates the implementation of a complete **Enterprise Lakehouse** using **Databricks**, **Apache Spark**, and **Delta Lake**.

The solution follows the **Medallion Architecture (Bronze → Silver → Gold)** and covers ingestion, transformation, optimization, data quality, streaming, dimensional modeling, and business analytics.

---

# Architecture

```
                CSV Files

                    │
                    ▼

           Unity Catalog Volume

                    │
                    ▼

            Bronze Layer (Raw)

                    │
                    ▼

       Silver Layer (Clean & Standardized)

                    │
                    ▼

        Gold Layer (Business Ready)

                    │
                    ▼

         SQL Analytics & Dashboard
```

---

# Technologies

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog
- Structured Streaming
- Python
- SQL

---

# Medallion Architecture

## Bronze

- Raw ingestion
- Immutable data
- Source preservation

---

## Silver

- Cleansing
- Standardization
- Data Quality
- Transformations

---

## Gold

- Business-ready tables
- Star Schema
- Analytics
- KPIs

---

# Project Structure

```
enterprise-lakehouse-databricks

├── datasets
├── docs
├── images
├── notebooks
├── sql
├── README.md
├── LICENSE
└── requirements.txt
```

---

# Notebooks

| Notebook | Description |
|----------|-------------|
| 01 | Data Ingestion |
| 02 | Silver Layer |
| 03 | Gold Layer |
| 04 | SQL Analytics |
| 05 | Data Quality |
| 06 | Structured Streaming |
| 07 | Change Data Capture |
| 08 | SCD Type 1 |
| 09 | SCD Type 2 |
| 10 | Delta Optimization |
| 11 | Business Dashboard |

---

# Implemented Features

- Medallion Architecture
- Unity Catalog
- Bronze / Silver / Gold Layers
- Structured Streaming
- Delta Lake
- Change Data Capture (CDC)
- Slowly Changing Dimension Type 1
- Slowly Changing Dimension Type 2
- Delta Optimization
- Business Dashboard
- SQL Analytics

---

# Business KPIs

- Total Revenue
- Average Ticket
- Revenue by State
- Revenue by Category
- Top Customers
- Top Products
- Order Status Analysis

---

# Future Improvements

- Auto Loader
- Delta Live Tables
- Lakeflow Pipelines
- CI/CD
- GitHub Actions
- Terraform Deployment
- Azure / AWS Integration

---

# Author

**Marcelo Mendes**

Databricks Certified Data Engineer Associate

GitHub:

https://github.com/MarcelloMendes

LinkedIn:

www.linkedin.com/in/marcelomendes-

---

## License

This project is licensed under the MIT License.
