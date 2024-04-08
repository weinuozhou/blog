from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]") .appName('SparkByExamples.com').getOrCreate()

"""
Spark会自动计算分区数, 不一定会按照给定的分区数进行分区
"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt')
print(f"initial partition count:{rdd.getNumPartitions()}")
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 5)
print(f"initial partition count:{rdd.getNumPartitions()}")
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 100)
print(f"initial partition count:{rdd.getNumPartitions()}")
"""
重新分区
"""
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 5)
print(f"initial partition count:{rdd.getNumPartitions()}")
repartition_rdd = rdd.repartition(10)
print(f"repartition count:{repartition_rdd.getNumPartitions()}")
"""
自定义分区
"""
class CustomPartitioner(object):
    def __init__(self, num_partitions):
        self.num_partitions = num_partitions

    def __call__(self, key):
        # 返回分区索引
        return hash(key) % self.num_partitions

data = [("apple", 1), ("banana", 2), ("orange", 3), ("grape", 4), ("melon", 5)]
rdd = spark.sparkContext.parallelize(data)
# 使用自定义分区器对RDD进行分区
num_partitions = 3
partitioned_rdd = rdd.partitionBy(num_partitions, CustomPartitioner(num_partitions))
partitioned_data = partitioned_rdd.glom().collect()
for i, partition in enumerate(partitioned_data):
    print("Partition {}: {}".format(i, partition))
