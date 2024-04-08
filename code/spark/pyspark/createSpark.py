from pyspark.sql import SparkSession

"""
创建SparkSession对象, 输出Spark对象的配置信息
"""
spark = SparkSession.builder.master("local[1]") .appName('SparkByExamples.com').getOrCreate()
print(f'当前PySpark的版本为{spark.version}')
print(f"Spark App Name: {spark.sparkContext.appName}")
print(f"spark master: {spark.sparkContext.master}")
# 输出所有配置信息
configurations = spark.sparkContext.getConf().getAll()
for item in configurations:
    print(item)
"""
读取hdfs文件系统创建RDD
"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(f'rdd中的内容:{rdd.collect()}')

"""
使用wholeTextFiles读取一个目录下的所有文本文件
"""

rdd = spark.sparkContext.wholeTextFiles("file:///home/weno/blog/data/local/")
print(f'rdd中所有内容为:\n{rdd.collect()}')
for file in rdd.collect():
    print(f"File Name:{file[0]}")
    print(f"File Content:{file[1]}") 
"""
停止SparkContext
"""
spark.sparkContext.stop()
