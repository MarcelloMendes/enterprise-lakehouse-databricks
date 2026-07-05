# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 11 — Business Dashboard
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Create business KPIs from the Gold Layer.
# MAGIC
# MAGIC ### KPIs
# MAGIC
# MAGIC - Total Revenue
# MAGIC - Total Orders
# MAGIC - Average Ticket
# MAGIC - Top Customers
# MAGIC - Revenue by State
# MAGIC - Revenue by Category
# MAGIC - Top Products

# COMMAND ----------

sales = spark.table("gizmobox.gold.sales_fact")

display(sales.limit(10))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC ROUND(SUM(total_amount),2) AS Total_Revenue
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC COUNT(order_id) AS Total_Orders
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC ROUND(AVG(total_amount),2) AS Average_Ticket
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC state,
# MAGIC
# MAGIC ROUND(SUM(total_amount),2) AS Revenue
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY state
# MAGIC
# MAGIC ORDER BY Revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC category,
# MAGIC
# MAGIC ROUND(SUM(total_amount),2) AS Revenue
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY category
# MAGIC
# MAGIC ORDER BY Revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC customer_id,
# MAGIC
# MAGIC first_name,
# MAGIC
# MAGIC last_name,
# MAGIC
# MAGIC ROUND(SUM(total_amount),2) AS Total
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY
# MAGIC
# MAGIC customer_id,
# MAGIC
# MAGIC first_name,
# MAGIC
# MAGIC last_name
# MAGIC
# MAGIC ORDER BY Total DESC
# MAGIC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC product_name,
# MAGIC
# MAGIC SUM(quantity) AS Quantity
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY product_name
# MAGIC
# MAGIC ORDER BY Quantity DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC status,
# MAGIC
# MAGIC COUNT(*) AS Total
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY status;

# COMMAND ----------

# MAGIC %md
# MAGIC # Project Completed
# MAGIC
# MAGIC Enterprise Lakehouse built with:
# MAGIC
# MAGIC - Delta Lake
# MAGIC - Medallion Architecture
# MAGIC - Structured Streaming
# MAGIC - CDC
# MAGIC - SCD Type 1
# MAGIC - SCD Type 2
# MAGIC - Delta Optimization
# MAGIC - SQL Analytics
# MAGIC - Business Dashboard

# COMMAND ----------

