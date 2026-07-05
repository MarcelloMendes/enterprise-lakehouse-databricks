# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 09 — Slowly Changing Dimension Type 2
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Implement Slowly Changing Dimension Type 2 using Delta Lake.
# MAGIC
# MAGIC Business Rules
# MAGIC
# MAGIC - Preserve history
# MAGIC - Close previous record
# MAGIC - Insert new version
# MAGIC - Keep only one active record
# MAGIC
# MAGIC Source
# MAGIC
# MAGIC Silver Customers
# MAGIC
# MAGIC Destination
# MAGIC
# MAGIC Gold Customer Dimension

# COMMAND ----------

from pyspark.sql.functions import *
from delta.tables import DeltaTable

# COMMAND ----------

spark.sql("""
DROP TABLE IF EXISTS gizmobox.gold.dim_customers
""")

# COMMAND ----------

customers = (
    spark.table("gizmobox.silver.customers")
    .withColumn("effective_date", current_timestamp())
    .withColumn("expiration_date", lit(None).cast("timestamp"))
    .withColumn("current_record", lit(True))
)

# COMMAND ----------

customers.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.gold.dim_customers")

# COMMAND ----------

display(
    spark.table("gizmobox.gold.dim_customers")
)

# COMMAND ----------

updates = spark.createDataFrame([
    (
        1,
        "João",
        "Silva",
        "joao@email.com",
        "São João del-Rei",
        "MG"
    )
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

dim = DeltaTable.forName(
    spark,
    "gizmobox.gold.dim_customers"
)

# COMMAND ----------

(
    dim.alias("target")
    .merge(
        updates.alias("source"),
        "target.customer_id = source.customer_id "
        "AND target.current_record = true"
    )
    .whenMatchedUpdate(
        set={
            "current_record": "false",
            "expiration_date": "current_timestamp()"
        }
    )
    .execute()
)

# COMMAND ----------

new_version = (
    updates
        .withColumn(
            "effective_date",
            current_timestamp()
        )
        .withColumn(
            "expiration_date",
            lit(None).cast("timestamp")
        )
        .withColumn(
            "current_record",
            lit(True)
        )
        .withColumn(
            "ingestion_timestamp",
            current_timestamp()
        )
        .withColumn(
            "source_file",
            lit("SCD2")
        )
)

# COMMAND ----------

spark.table("gizmobox.gold.dim_customers").printSchema()

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS gizmobox.gold.dim_customers;

# COMMAND ----------

customers = (
    spark.table("gizmobox.silver.customers")
        .select(
            "customer_id",
            "first_name",
            "last_name",
            "email",
            "city",
            "state",
            "ingestion_timestamp",
            "source_file"
        )
        .withColumn("effective_date", current_timestamp())
        .withColumn("expiration_date", lit(None).cast("timestamp"))
        .withColumn("current_record", lit(True))
)

# COMMAND ----------

customers.printSchema()

# COMMAND ----------

customers.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.gold.dim_customers")

# COMMAND ----------

spark.table("gizmobox.gold.dim_customers").printSchema()