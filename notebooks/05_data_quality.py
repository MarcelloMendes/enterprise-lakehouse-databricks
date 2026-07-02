# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 05 — Data Quality
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Validate Gold Layer data before it is consumed by analytics.
# MAGIC
# MAGIC Checks
# MAGIC
# MAGIC - Null values
# MAGIC - Duplicate keys
# MAGIC - Negative values
# MAGIC - Invalid business rules

# COMMAND ----------

from pyspark.sql.functions import *

sales = spark.table("gizmobox.gold.sales_fact")

# COMMAND ----------

null_check = sales.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in sales.columns
])

display(null_check)

# COMMAND ----------

duplicates = (
    sales.groupBy("order_id")
         .count()
         .filter(col("count") > 1)
)

display(duplicates)

# COMMAND ----------

negative_quantity = sales.filter(
    col("quantity") <= 0
)

display(negative_quantity)

# COMMAND ----------

negative_price = sales.filter(
    col("price") <= 0
)

display(negative_price)

# COMMAND ----------

invalid_total = sales.filter(
    col("total_amount") != col("price") * col("quantity")
)

display(invalid_total)

# COMMAND ----------

invalid_dates = sales.filter(
    col("order_date").isNull()
)

display(invalid_dates)

# COMMAND ----------

sales.groupBy("status").count()

# COMMAND ----------

print("Data Quality Validation Finished Successfully")