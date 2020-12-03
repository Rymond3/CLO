from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, avg
import string

spark = SparkSession.builder.master("local").appName("StockSummary").getOrCreate()

df = spark.read.csv("GOOGLE.csv")

dfsel = df.select(col("_c0").alias("date"), col("_c5").alias("cost"))

df_split = dfsel.withColumn("year", split(col("date"), '-').getItem(0))

df_final = df_split.groupBy("year").agg(avg(col("cost"))).sort("year", ascending=True)

df_final.show()