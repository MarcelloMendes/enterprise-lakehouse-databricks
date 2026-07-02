# Databricks notebook source
# MAGIC %md
# MAGIC # Enterprise Lakehouse on Databricks
# MAGIC
# MAGIC ## Notebook 01 — Data Ingestion
# MAGIC
# MAGIC ### Objective
# MAGIC
# MAGIC Ingest raw CSV datasets into the Bronze Layer using Apache Spark and Delta Lake.
# MAGIC
# MAGIC ### Source Files
# MAGIC
# MAGIC - customers.csv
# MAGIC - products.csv
# MAGIC - orders.csv
# MAGIC
# MAGIC ### Destination
# MAGIC
# MAGIC Bronze Delta Tables
# MAGIC
# MAGIC - customers_raw
# MAGIC - products_raw
# MAGIC - orders_raw
# MAGIC
# MAGIC ### Technologies
# MAGIC
# MAGIC - Databricks
# MAGIC - Apache Spark
# MAGIC - Delta Lake
# MAGIC - Unity Catalog
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC Author: Marcelo Mendes

# COMMAND ----------

# ==========================================
# Imports
# ==========================================

from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

# ==========================================
# Paths
# ==========================================

CUSTOMERS_PATH = "/Volumes/gizmobox/raw/landing/customers.csv"

PRODUCTS_PATH = "/Volumes/gizmobox/raw/landing/products.csv"

ORDERS_PATH = "/Volumes/gizmobox/raw/landing/orders.csv"

# COMMAND ----------

customers_df = (
    spark.read
         .schema(customers_schema)
         .option("header", True)
         .csv(CUSTOMERS_PATH)
)

products_df = (
    spark.read
         .option("header", True)
         .csv(PRODUCTS_PATH)
)

orders_df = (
    spark.read
         .option("header", True)
         .csv(ORDERS_PATH)
)

# COMMAND ----------

display(customers_df)
display(products_df)
display(orders_df)

# COMMAND ----------

customers_schema = StructType([
    StructField("customer_id", IntegerType(), False),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True)
])

# COMMAND ----------

customers_df.printSchema()

# COMMAND ----------

customers_df = (
    customers_df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", lit("customers.csv"))
)

products_df = (
    products_df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", lit("products.csv"))
)

orders_df = (
    orders_df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", lit("orders.csv"))
)

# COMMAND ----------

spark.table("gizmobox.bronze.customers_raw").printSchema()

# COMMAND ----------

customers_df.printSchema()

# COMMAND ----------

spark.sql("DROP TABLE gizmobox.bronze.customers_raw")
spark.sql("DROP TABLE gizmobox.bronze.products_raw")
spark.sql("DROP TABLE gizmobox.bronze.orders_raw")

# COMMAND ----------

customers_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.bronze.customers_raw")

# COMMAND ----------

products_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.bronze.products_raw")

# COMMAND ----------

orders_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.bronze.orders_raw")

# COMMAND ----------

display(spark.table("gizmobox.bronze.customers_raw"))

# COMMAND ----------

display(spark.table("gizmobox.bronze.products_raw"))

# COMMAND ----------

display(spark.table("gizmobox.bronze.orders_raw"))