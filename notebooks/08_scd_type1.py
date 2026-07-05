# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 08 — Slowly Changing Dimension Type 1
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Implement SCD Type 1 using Delta Lake MERGE.
# MAGIC
# MAGIC ### Characteristics
# MAGIC
# MAGIC - Overwrite existing values
# MAGIC - No historical tracking
# MAGIC - One current version per customer
# MAGIC
# MAGIC ### Source
# MAGIC
# MAGIC Customer updates
# MAGIC
# MAGIC ### Destination
# MAGIC
# MAGIC Silver Layer

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

scd_updates = spark.createDataFrame([
    ("1","João","Silva","joao@email.com","Conselheiro Lafaiete","MG"),
    ("3","Maria","Oliveira","maria@email.com","Belo Horizonte","MG")
],[
    "customer_id",
    "first_name",
    "last_name",
    "email",
    "city",
    "state"
])

# COMMAND ----------

display(scd_updates)

# COMMAND ----------

scd_updates.createOrReplaceTempView("scd_updates")

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO gizmobox.silver.customers target
# MAGIC
# MAGIC USING scd_updates source
# MAGIC
# MAGIC ON target.customer_id = source.customer_id
# MAGIC
# MAGIC WHEN MATCHED THEN
# MAGIC
# MAGIC UPDATE SET
# MAGIC
# MAGIC target.first_name = source.first_name,
# MAGIC target.last_name = source.last_name,
# MAGIC target.email = source.email,
# MAGIC target.city = source.city,
# MAGIC target.state = source.state

# COMMAND ----------

display(
    spark.table("gizmobox.silver.customers")
)

# COMMAND ----------

spark.table(
    "gizmobox.silver.customers"
).filter(
    col("customer_id")=="1"
).show()