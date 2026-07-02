# Databricks notebook source
# MAGIC %md
# MAGIC # Notebook 03 — Gold Layer
# MAGIC
# MAGIC ## Objective
# MAGIC
# MAGIC Build the first analytical table joining customers, orders and products.
# MAGIC
# MAGIC Output:
# MAGIC
# MAGIC sales_fact

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

customers = spark.table("gizmobox.silver.customers")

products = spark.table("gizmobox.silver.products")

orders = spark.table("gizmobox.silver.orders")

# COMMAND ----------

customers.printSchema()

products.printSchema()

orders.printSchema()

# COMMAND ----------

customers = customers.withColumn(
    "customer_id",
    col("customer_id").cast("string")
)

products = products.withColumn(
    "price",
    col("price").cast("double")
).withColumn(
    "stock",
    col("stock").cast("integer")
)

orders = (
    orders
    .withColumn("quantity", col("quantity").cast("integer"))
    .withColumn("order_date", to_date(col("order_date")))
)

# COMMAND ----------

sales_fact = (
    orders.alias("o")
    .join(
        customers.alias("c"),
        on="customer_id",
        how="inner"
    )
    .join(
        products.alias("p"),
        on="product_id",
        how="inner"
    )
)

# COMMAND ----------

display(sales_fact)

# COMMAND ----------

sales_fact = sales_fact.withColumn(
    "total_amount",
    col("price") * col("quantity")
)

# COMMAND ----------

sales_fact = sales_fact.select(
    "order_id",
    "order_date",
    "customer_id",
    "first_name",
    "last_name",
    "city",
    "state",
    "product_id",
    "product_name",
    "category",
    "quantity",
    "price",
    "total_amount",
    "status"
)

# COMMAND ----------

spark.sql("""
DROP TABLE IF EXISTS gizmobox.gold.sales_fact
""")

# COMMAND ----------

sales_fact.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gizmobox.gold.sales_fact")

# COMMAND ----------

display(
    spark.table("gizmobox.gold.sales_fact")
)

# COMMAND ----------

