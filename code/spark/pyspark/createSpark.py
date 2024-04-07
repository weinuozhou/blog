from pyspark.sql import SparkSession

"""
创建SparkSession对象
"""
spark = SparkSession.builder.master("local[1]") .appName('SparkByExamples.com').getOrCreate()
print(spark)

"""
创建另一个SparkSession对象
"""

spark2 = SparkSession.newSession()
print(spark2)