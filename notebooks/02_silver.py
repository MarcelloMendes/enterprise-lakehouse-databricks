# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 02 — Silver Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Transform Bronze tables into clean and standardized Silver tables.
# MAGIC
# MAGIC ### Operations
# MAGIC
# MAGIC - Remove duplicates
# MAGIC - Trim text columns
# MAGIC - Standardize column names
# MAGIC - Validate business keys
# MAGIC
# MAGIC ### Source
# MAGIC
# MAGIC Bronze Layer
# MAGIC
# MAGIC ### Destination
# MAGIC
# MAGIC Silver Layer

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

customers_df = spark.table("gizmobox.bronze.customers_raw")

products_df = spark.table("gizmobox.bronze.products_raw")

orders_df = spark.table("gizmobox.bronze.orders_raw")

# COMMAND ----------

customers_df.printSchema()

# COMMAND ----------

customers_silver = (
    customers_df
        .dropDuplicates(["customer_id"])
        .withColumn("first_name", trim(col("first_name")))
        .withColumn("last_name", trim(col("last_name")))
        .withColumn("email", lower(trim(col("email"))))
        .withColumn("city", initcap(trim(col("city"))))
        .withColumn("state", upper(trim(col("state"))))
)

# COMMAND ----------

display(customers_silver)

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS gizmobox.silver.customers")

# COMMAND ----------

customers_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.silver.customers")

# COMMAND ----------

display(
    spark.table("gizmobox.silver.customers")
)

# COMMAND ----------

products_silver = (
    products_df
        .dropDuplicates(["product_id"])
        .withColumn("product_name", trim(col("product_name")))
        .withColumn("category", initcap(trim(col("category"))))
)

# COMMAND ----------

display(products_silver)

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS gizmobox.silver.products")

products_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.silver.products")

# COMMAND ----------

display(
    spark.table("gizmobox.silver.products")
)

# COMMAND ----------

orders_silver = (
    orders_df
        .dropDuplicates(["order_id"])
)

# COMMAND ----------

display(orders_silver)

# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS gizmobox.silver.orders")

# COMMAND ----------

orders_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.silver.orders")

# COMMAND ----------

display(
    spark.table("gizmobox.silver.orders")
)

# COMMAND ----------

