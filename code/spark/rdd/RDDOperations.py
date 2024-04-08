from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[*]').appName("example").getOrCreate()

"""map算子"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(rdd.map(lambda x: (x,1)).take(3))

"""flatMap算子"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(rdd.flatMap(lambda x: x.split(" ")) .take(9))

"""filter算子"""
rdd = spark.sparkContext.parallelize(range(10), 2)
rdd.filter(lambda x: x&1 == 0).collect()

"""reduceByKey算子"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(rdd.flatMap(lambda words: words.split(" ")).map(lambda x: (x,1)) \
        .reduceByKey(lambda x,y: x+y).collect())

"""mapValues算子"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(rdd.flatMap(lambda words: words.split(" ")).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y) \
        .mapValues(lambda x: x+1).collect())

"""groupby算子"""
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
# 使用 groupBy 进行分组, 根据第一个元素（键）进行分组
grouped_rdd = rdd.groupBy(lambda x: x[0])
print(f'rdd的内容:\n{grouped_rdd.collect()}') # 值是一个可迭代对象，可以通过list函数显示或for循环
print(f'rdd的内容:{grouped_rdd.mapValues(lambda x: list(x)).collect()}')
for key, values in grouped_rdd.collect():
    print(f"Key: {key}, Values: {list(values)}")

"""groupByKey算子"""
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
print(f'rdd的内容:\n{rdd.groupByKey().collect()}') # 值是一个可迭代对象，可以通过list函数显示
print(f'rdd的内容:\n{rdd.groupByKey().mapValues(lambda value: list(value)).collect()}')

"""sort算子"""
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
print(rdd.sortBy(lambda x: x[0], ascending=False).collect()) # 按键进行排序
print(rdd.sortBy(lambda x: x[1], ascending=False).collect()) # 按值进行排序

"""sortByKey算子"""
data = [("cat", 1), ("Dog", 2), ("cat", 3), ("dog", 1), ("Cat", 2), ("elephant", 10)]
rdd = spark.sparkContext.parallelize(data)
print(rdd.sortByKey(ascending=True, keyfunc=lambda x: x.lower()).collect())

"""join算子"""
rdd1 = spark.sparkContext.parallelize([("1001", "张三"), ("1002", "lisi"), ("1003", "wangwu")])
rdd2 = spark.sparkContext.parallelize([("1001", "销售部"), ("1002", "科技部")])
print(f"连接后的rdd的内容为{rdd1.join(rdd2).collect()}") # 使用 join 进行连接

"""glom算子"""
rdd = spark.sparkContext.parallelize(range(1, 8), 2)  # 2个分区
print(f'rdd经过glom后的内容为:{rdd.glom().collect()}')

"""行动操作"""
rdd = spark.sparkContext.parallelize(range(1, 8), 2)
print(f'rdd中的记录数为:{rdd.count()}')
print(f'rdd中的最大数为:{rdd.max()}')
print(f'rdd中的最小数为:{rdd.min()}')
print(f'rdd中的合计为:{rdd.reduce(lambda x,y: x+y)}')
print(f'rdd中的前5条记录为:{rdd.take(5)}')
print(f'rdd中的所有记录为:{rdd.collect()}')

"""RDD持久化"""
rdd = spark.sparkContext.parallelize(range(1, 8), 2)
rdd.cache() # 调用这个方法时，会自动调用persist(MEMORY_ONLY)
print(f'rdd中的记录数为:{rdd.count()}')
rdd.unpersist() # 不再需要一个RDD时，可以使用unpersist()释放该RDD