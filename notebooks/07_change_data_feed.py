# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 07 — Change Data Feed (CDC)
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Simulate Change Data Capture (CDC) using Delta Lake MERGE.
# MAGIC
# MAGIC ### Business Scenario
# MAGIC
# MAGIC A source system sends:
# MAGIC
# MAGIC - Existing customers with updated information
# MAGIC - New customers that must be inserted
# MAGIC
# MAGIC ### Operations
# MAGIC
# MAGIC - Update existing records
# MAGIC - Insert new records
# MAGIC - Preserve Delta Lake consistency
# MAGIC
# MAGIC ### Source
# MAGIC
# MAGIC Silver Layer
# MAGIC
# MAGIC ### Destination
# MAGIC
# MAGIC Silver Layer (updated)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

updates = spark.createDataFrame([
    ("1","João","Silva","joao@email.com","Ouro Branco","MG"),
    ("6","Pedro","Souza","pedro@email.com","Congonhas","MG")
],[
    "customer_id",
    "first_name",
    "last_name",
    "email",
    "city",
    "state"
])

# COMMAND ----------

display(updates)

# COMMAND ----------

updates.createOrReplaceTempView("updates")

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO gizmobox.silver.customers AS target
# MAGIC
# MAGIC USING updates AS source
# MAGIC
# MAGIC ON target.customer_id = source.customer_id
# MAGIC
# MAGIC WHEN MATCHED THEN
# MAGIC UPDATE SET
# MAGIC     target.first_name = source.first_name,
# MAGIC     target.last_name = source.last_name,
# MAGIC     target.email = source.email,
# MAGIC     target.city = source.city,
# MAGIC     target.state = source.state
# MAGIC
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT (
# MAGIC     customer_id,
# MAGIC     first_name,
# MAGIC     last_name,
# MAGIC     email,
# MAGIC     city,
# MAGIC     state,
# MAGIC     ingestion_timestamp,
# MAGIC     source_file
# MAGIC )
# MAGIC VALUES (
# MAGIC     source.customer_id,
# MAGIC     source.first_name,
# MAGIC     source.last_name,
# MAGIC     source.email,
# MAGIC     source.city,
# MAGIC     source.state,
# MAGIC     current_timestamp(),
# MAGIC     'cdc_update'
# MAGIC );

# COMMAND ----------

display(
    spark.table("gizmobox.silver.customers")
)

# COMMAND ----------

spark.table("gizmobox.silver.customers").count()