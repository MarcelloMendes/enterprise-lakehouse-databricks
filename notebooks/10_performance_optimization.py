# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 10 — Delta Lake Performance Optimization
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Optimize Delta Lake tables for better query performance.
# MAGIC
# MAGIC ## Topics
# MAGIC
# MAGIC - Table Statistics
# MAGIC - OPTIMIZE
# MAGIC - ZORDER
# MAGIC - VACUUM
# MAGIC - DESCRIBE DETAIL
# MAGIC - DESCRIBE HISTORY

# COMMAND ----------

sales_fact = spark.table("gizmobox.gold.sales_fact")

display(sales_fact.limit(10))

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC ANALYZE TABLE gizmobox.gold.sales_fact
# MAGIC COMPUTE STATISTICS;

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE gizmobox.gold.sales_fact;

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE gizmobox.gold.sales_fact
# MAGIC ZORDER BY (customer_id);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC WHERE customer_id = 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM gizmobox.gold.sales_fact RETAIN 168 HOURS;

# COMMAND ----------

# MAGIC %sql
# MAGIC EXPLAIN
# MAGIC
# MAGIC SELECT *
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC WHERE customer_id = 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC
# MAGIC customer_id,
# MAGIC
# MAGIC SUM(total_amount) AS total_sales
# MAGIC
# MAGIC FROM gizmobox.gold.sales_fact
# MAGIC
# MAGIC GROUP BY customer_id
# MAGIC
# MAGIC ORDER BY total_sales DESC;

# COMMAND ----------

