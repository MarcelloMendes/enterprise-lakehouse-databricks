# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 06 — Structured Streaming
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Ingest new CSV files continuously using Spark Structured Streaming.
# MAGIC
# MAGIC Source:
# MAGIC
# MAGIC /Volumes/gizmobox/raw/landing

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

customer_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("city", StringType(), True),
    StructField("state", StringType(), True)
])

# COMMAND ----------

stream_df = (
    spark.readStream
         .format("csv")
         .option("header", True)
         .schema(customer_schema)
         .load("/Volumes/gizmobox/raw/landing")
)

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

stream_df = stream_df.withColumn(
    "ingestion_timestamp",
    current_timestamp()
)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME gizmobox.raw.checkpoints;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW VOLUMES IN gizmobox.raw;

# COMMAND ----------

query = (
    stream_df.writeStream
        .format("delta")
        .outputMode("append")
        .trigger(availableNow=True)
        .option(
            "checkpointLocation",
            "/Volumes/gizmobox/raw/checkpoints/customers_stream"
        )
        .toTable("gizmobox.bronze.customers_stream")
)