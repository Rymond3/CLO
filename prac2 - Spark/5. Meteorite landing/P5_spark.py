from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

conf = SparkConf().setMaster('local').setAppName('MeteoriteLandings')
sc = SparkContext(conf = conf)
spark = SparkSession(sc)

rdd = sc.textFile("Meteorite_Landings.csv")

data = rdd.map(lambda x: x.split(','))

compound_name = data.filter(lambda x: x[3][0] == '"')

rdd1 = compound_name.map(lambda x: ((x[3][1:] + x[4][:-1]), x[5]))

single_name = data.filter(lambda x: x[3][0] != '"')

rdd2 = single_name.map(lambda x: (x[3], x[4]))

df = rdd1.union(rdd2).toDF(["type", "mass"]).sort("type", ascending=True)

final = df.groupBy("type").agg(avg(col("mass"))).rdd

final.saveAsTextFile("output5.txt")
