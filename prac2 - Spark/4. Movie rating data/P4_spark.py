from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, avg, ceil
import string

spark = SparkSession.builder.master("local[2]").appName("Ratings").getOrCreate()

df = spark.read.csv("ratings.csv")

dfsel = df.select(col("_c1").alias("id"), col("_c2").alias("rating"))

df_avg = dfsel.groupBy("id").agg(avg(col("rating")))

df_final = df_avg.select(ceil(col("avg(rating)")).alias("RatingRange"), col("id")).sort("RatingRange", ascending=True).rdd

rdd = df_final.map(lambda x: ("Range " + str(x["RatingRange"]), x["id"]))

rdd.saveAsTextFile("output4.txt")