from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("accumulator").getOrCreate()

"""求和累加器"""
accum = spark.sparkContext.accumulator(0) # 创建累加器变量
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd.foreach(lambda x: accum.add(x))
print(accum.value)

"""计数器累加器"""
accum = spark.sparkContext.accumulator(0) # 创建累加器变量
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd.foreach(lambda x: accum.add(1))
print(accum.value)