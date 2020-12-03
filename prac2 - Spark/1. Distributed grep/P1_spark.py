from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('DistributedGrep')
sc = SparkContext(conf = conf)

RDDvar = sc.textFile("input.txt")

grepWord = sys.argv[1]

linesWithWord = RDDvar.filter(lambda line: grepWord in line)

linesWithWord.saveAsTextFile("output1.txt")
