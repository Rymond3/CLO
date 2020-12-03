from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster('local').setAppName('CountURL')
sc = SparkContext(conf = conf)

rdd = sc.textFile("access_log")

words = rdd.flatMap(lambda x: x.split())

urls = words.filter(lambda x: x[0] == '/')

mapurls = urls.map(lambda x: (x, 1))

reducedurls = mapurls.reduceByKey(lambda x,y: x+y)

reducedurls.saveAsTextFile("output2.txt")
