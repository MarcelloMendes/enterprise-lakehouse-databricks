# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 04 — SQL Analytics
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Create business queries using Gold tables.
# MAGIC
# MAGIC Tables:
# MAGIC
# MAGIC - sales_fact
# MAGIC - sales_summary

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     ROUND(SUM(total_amount),2) AS total_revenue
# MAGIC FROM gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     product_name,
# MAGIC     SUM(quantity) AS units_sold
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC GROUP BY product_name
# MAGIC ORDER BY units_sold DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     state,
# MAGIC     ROUND(SUM(total_amount),2) AS revenue
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC GROUP BY state
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gizmobox.gold.sales_summary
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     first_name,
# MAGIC     last_name,
# MAGIC     ROUND(SUM(total_amount),2) AS total_spent
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC GROUP BY
# MAGIC     customer_id,
# MAGIC     first_name,
# MAGIC     last_name
# MAGIC ORDER BY total_spent DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     ROUND(AVG(total_amount),2) AS average_ticket
# MAGIC FROM gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     status,
# MAGIC     COUNT(*) AS total_orders
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC GROUP BY status;