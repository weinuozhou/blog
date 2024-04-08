from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[*]').appName("example").getOrCreate()

"""
使用集合创建RDD
"""

data = [1, 2, 3, 4, 5]
num_slices = 2 # 指定分区数量
# 使用 parallelize 将本地集合转换为 RDD，并指定分区数量
rdd = spark.sparkContext.parallelize(c=data, numSlices=num_slices)
print(f'rdd中的内容:{rdd.collect()}')

"""
使用本地文件系统创建RDD
"""

rdd = spark.sparkContext.textFile('file:///home/weno/blog/data/local/word1', 2)
print(f'rdd中的内容:{rdd.collect()}')

"""
使用HDFS文件系统创建RDD
"""

rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(f'rdd中的内容:{rdd.collect()}')

"""
创建一个空的RDD
"""

emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)
# 等价于下面这种写法
emptyRDD = spark.sparkContext.parallelize([])
print(emptyRDD)