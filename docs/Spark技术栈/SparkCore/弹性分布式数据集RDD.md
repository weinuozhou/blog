# RDD编程

* RDD（弹性分布式数据集）是 PySpark 的基本构建块，它是容错、不可变的分布式对象集合。不可变意味着一旦创建了 RDD，就无法更改它。RDD中的每条记录都被划分为逻辑分区，可以在集群的不同节点上进行计算。
* 换句话说，RDD 是类似于 Python 中的 list 的对象集合，不同之处在于 RDD 是在分散在多个物理服务器（也称为集群中的节点）的多个进程上计算的，而 Python 集合仅在一个进程中生存和处理
* 此外，RDD 提供数据分区和分布的数据抽象，旨在在多个节点上并行运行计算，同时在 RDD 上进行转换时，我们不必担心 PySpark 默认提供的并行性

**RDD的优点**:

* **内存处理**:PySpark从磁盘加载数据并在内存中处理并将数据保留在内存中，这是PySpark和Mapreduce（I/O密集型）之间的主要区别。在转换之间，我们还可以将 RDD 缓存/保留在内存中以重用之前的计算
* **不变性**:PySpark RDD 本质上是不可变的，这意味着 RDD 一旦创建就无法修改。当我们对 RDD 应用转换时，PySpark 会创建一个新的 RDD 并维护 RDD 谱系
* **容错能力**:PySpark 在 HDFS、S3 等上的容错数据存储上运行，因此任何 RDD 操作失败，它都会自动从其他分区重新加载数据。此外，当 PySpark 应用程序在集群上运行时，PySpark 任务失败会自动恢复一定次数（根据配置）并无缝完成应用程序
* **惰性进化**:PySpark 不会在 Driver 出现/遇到时评估 RDD 转换，而是保留遇到的所有转换 (DAG)，并在看到第一个 RDD 操作时计算所有转换

## 创建RDD

RDD 主要以两种不同的方式创建:
* **使用并行化集合**
* **使用存储系统中的数据集**

### 使用集合创建RDD

```python
spark = SparkSession.builder.master('local[*]').appName("example").getOrCreate()
spark.sparkContext.parallelize(c, numSlices)
```
* c: 要转换为 RDD 的本地集合（collection）。通常是一个 Python 列表或者其他可迭代的数据结构
* numSlices (可选): 可以指定将数据切分成的分片数量。分片数量决定了 RDD 在集群中的分布方式，影响了并行度。如果未提供此参数，默认情况下 Spark 将根据集群的配置和数据大小自动选择分片数量

```python
data = [1, 2, 3, 4, 5]
num_slices = 2 # 指定分区数量
# 使用 parallelize 将本地集合转换为 RDD，并指定分区数量
rdd = spark.sparkContext.parallelize(c=data, numSlices=num_slices)
print(f'rdd中的内容:{rdd.collect()}')
```

### 使用存储系统的数据集创建RDD

```python
spark.sparkContext.textFile(path, name, minPartitions, use_unicode)
```
* path:文件的路径，可以是hdfs、本地文件或者其他hadoop支持的文件系统
* name:为RDD创建名称
* minPartitions:指定 RDD 的最小分区数量。默认情况下，Spark 将根据集群的配置和文件的大小自动选择分区数量
* use_unicode:如果设置为 False，则表示 RDD 中的字符串是以字节形式存储的。默认为 True，表示使用 Unicode 编码

!> 对于本地文件系统,需要指定文件的绝对路径，例如:file:///home/weno/blog/data/local/word.txt

```python
rdd = spark.sparkContext.textFile('file:///home/weno/blog/data/local/word1', 2)
print(f'rdd中的内容:{rdd.collect()}')
```

!> 对于hdfs文件系统，可以这样指定路径:hdfs://localhost:9000/spark/word.txt

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
print(f'rdd中的内容:{rdd.collect()}')
```

### 创建一个空的RDD

* 可以使用emptyRDD()函数
* 也可以指定空列表来创建

```python
emptyRDD = spark.sparkContext.emptyRDD()
print(emptyRDD)
# 等价于下面这种写法
emptyRDD = spark.sparkContext.parallelize([])
print(emptyRDD)
```

## RDD分区

当我们使用parallelize()、textFile()或 wholeTextFiles()方法启动 RDD 时，它会根据资源可用性自动将数据分割成分区,也可以指定分区数量，spark会自动计算分区数量，不一定会按照用户指定的的分区数量

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt')
print(f"initial partition count:{rdd.getNumPartitions()}")
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 5)
print(f"initial partition count:{rdd.getNumPartitions()}")
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 100)
print(f"initial partition count:{rdd.getNumPartitions()}")
```

<div style="text-align: center;"><img alt='202404081339439' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081339439.png' width=500px> </div>

!> 可以看到，spark会自动计算分区数量，不一定会按照用户指定的的分区数量

### 重新分区

PySpark可以使用 `repartition()` 方法是对所有节点中的数据进行混洗，从而重新分区

!> 它会对数据集进行全局洗牌操作，并将数据重新分布到指定的分区数

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 5)
print(f"initial partition count:{rdd.getNumPartitions()}")
repartition_rdd = rdd.repartition(10)
print(f"repartition count:{repartition_rdd.getNumPartitions()}")
```

也可以使用 `coalesce()` 方法对数据集进行重新分区，但是它不会进行**全局混洗**操作，而是将数据重新分布到指定的分区数

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 5)
print(f"initial partition count:{rdd.getNumPartitions()}")
repartition_rdd = rdd.coalesce(1)
print(f"repartition count:{repartition_rdd.getNumPartitions()}")
```

### 自定义分区

RDD可以通过自定义分区来控制数据在集群中的分布

```python
# 创建自定义分区类
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
```

## RDD算子

RDD算子主要包括以下两类:
* RDD 转换:转换是惰性操作，这些操作不是更新 RDD，而是返回另一个 RDD
* RDD 操作:触发计算并返回 RDD 值的操作

### 转换操作

#### map

map()转换用于应用任何复杂的操作，例如添加列、更新列等，映射转换的输出始终具有与输入相同数量的记录

```python
map(function, preservesPartitioning)
```
* function:这是 map 方法的唯一必需参数，它定义了对每个元素进行的映射操作。这个函数可以是一个命名函数、匿名函数（lambda 函数）或者其他可调用对象。
* preservesPartitioning: 默认情况下，map 操作会保留原有的分区方式。如果设置为 False，则表示新的 RDD 将使用默认的哈希分区器进行重新分区

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
rdd.map(lambda x: (x,1)).take(3)
```

#### flatMap

flatMap()转换在应用函数后将 RDD 展平并返回一个新的 RDD
```python
flatMap(function, preservesPartitioning)
```
* function:这是 flatMap 方法的唯一必需参数，它定义了对每个元素进行的映射操作。这个函数可以是一个命名函数、匿名函数（lambda 函数）或者其他可调用对象。
* preservesPartitioning: 默认情况下，map 操作会保留原有的分区方式。如果设置为 False，则表示新的 RDD 将使用默认的哈希分区器进行重新分区

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
rdd.flatMap(lambda x: x.split(" ")) .take(9)
```

#### filter

filter()用于对 RDD 进行筛选操作的转换（transformation）操作。它根据给定的条件过滤出 RDD 中符合条件的元素
```python
filter(function)
```
* 筛选函数（function）： 这是 filter 方法的必需参数，它定义了筛选条件。这个函数接收一个参数，表示 RDD 中的每个元素，然后返回一个布尔值，决定是否保留该元素。

```python
rdd = spark.sparkContext.parallelize(range(10), 2)
rdd.filter(lambda x: x&1 == 0).collect()
```

#### reduceByKey

reduceByKey()针对于键值对RDD，自动根据key分组，然后根据聚合逻辑，完成对组内数据的聚合操作
```python
reduceByKey(function, numPartitons)
```
* function:这是 reduceByKey 方法的必需参数，它定义了对相同键的值进行聚合操作的函数。这个函数接收两个参数，表示两个值，然后返回一个新的值
* numPartitions:指定分区的数量。默认情况下，reduceByKey 使用原有 RDD 的分区数量。可以通过设置 numPartitions 来调整分区数量

```python
# 统计词频
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
rdd.flatMap(lambda words: words.split(" ")).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).collect()
```

#### mapValues

mapValues()用于对键值对 RDD 进行值的映射操作的方法。它对 RDD 中的每个值应用一个函数，而键保持不变
```python
mapValues(function, preservesPartitioning)
```
* function: 这是 mapValues 方法的必需参数，它定义了对每个值进行映射操作的函数。这个函数接收一个参数，表示值，然后返回一个新的值。
* preservesPartitioning: 默认情况下，map 操作会保留原有的分区方式。如果设置为 False，则表示新的 RDD 将使用默认的哈希分区器进行重新分区

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt', 3)
rdd.flatMap(lambda words: words.split(" ")).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y) \
    .mapValues(lambda x: x+1).collect()
```

#### groupBy

groupBy()用于对 RDD 进行分组操作的方法。它根据指定的键对 RDD 中的元素进行分组，返回一个包含键值对的 RDD，其中键是分组的键，值是对应键的所有元素的迭代器
```python
groupBy(function, numPartitons)
```
* function:  这是 groupBy 方法的必需参数，它定义了如何从每个元素中提取一个键，然后根据这个键进行分组。这个函数接收一个参数，表示元素，然后返回一个用作分组键的值。
* numPartitions:指定分区的数量。默认情况下，groupBy 使用原有 RDD 的分区数量。可以通过设置 numPartitions 来调整分区数量

```python
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
# 使用 groupBy 进行分组, 根据第一个元素（键）进行分组
grouped_rdd = rdd.groupBy(lambda x: x[0])
print(f'rdd的内容:\n{grouped_rdd.collect()}') # 值是一个可迭代对象，可以通过list函数显示或for循环
print(f'rdd的内容:{grouped_rdd.mapValues(lambda x: list(x)).collect()}')
for key, values in grouped_rdd.collect():
    print(f"Key: {key}, Values: {list(values)}")
```

#### groupByKey

groupByKey()用于对键值对 RDD 进行分组操作的方法。它根据键对 RDD 中的元素进行分组，返回一个包含键值对的 RDD，其中键是分组的键，值是对应键的所有元素的可迭代器
```python
groupByKey()
```

?> 不接受参数即可

```python
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
print(f'rdd的内容:\n{rdd.groupByKey().collect()}') # 值是一个可迭代对象，可以通过list函数显示
print(f'rdd的内容:\n{rdd.groupByKey().mapValues(lambda value: list(value)).collect()}')
```

#### sortBy

sortBy()用于对 RDD 进行排序操作的方法。它可以按照指定的排序键对 RDD 中的元素进行排序，并返回一个新的 RDD
```python
sortBy(function, ascending, numPartitons)
```
* function:这是 sortBy 方法的必需参数，它定义了如何从每个元素中提取一个排序键
* ascending:指定排序的顺序，True 表示升序（默认），False 表示降序。
* numPartitions:指定用多少分区排序，若要全局排序，请指定为1

```python
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 2)]
rdd = spark.sparkContext.parallelize(data)
rdd.sortBy(lambda x: x[0], ascending=False).collect() # 按键进行排序
rdd.sortBy(lambda x: x[1], ascending=False).collect() # 按值进行排序
```

#### sortByKey

sortByKey()用于对键值对 RDD 进行按键排序的方法。它会按照键对 RDD 中的元素进行排序，并返回一个新的排序后的 RDD
```python
sortByKey(ascending, numPartitions, keyfunc)
```
* ascending（可选）： 指定排序的顺序，True 表示升序（默认），False 表示降序。
* numPartitions（可选）： 指定输出 RDD 的分区数量。默认情况下，输出 RDD 的分区数量与原始 RDD 的分区数量相同
* keyfunc（可选）： 用于提取排序键的函数。默认情况下，使用默认的排序函数。如果需要按照键的特定部分进行排序，可以提供一个自定义的函数

```python
data = [("cat", 1), ("Dog", 2), ("cat", 3), ("dog", 1), ("Cat", 2), ("elephant", 10)]
rdd = spark.sparkContext.parallelize(data)
rdd.sortByKey(ascending=True, keyfunc=lambda x: x.lower()).collect()
```

#### join

join()用于对两个键值对 RDD 进行连接操作的方法。join 将具有相同键的元素组合在一起，生成一个新的键值对 RDD
```python
join(other, numPartitions)
```
* other（必需）：要连接的另一个键值对 RDD
* numPartitions(可选):指定输出 RDD 的分区数量

```python
rdd1 = spark.sparkContext.parallelize([("1001", "张三"), ("1002", "lisi"), ("1003", "wangwu")])
rdd2 = spark.sparkContext.parallelize([("1001", "销售部"), ("1002", "科技部")])
print(f"连接后的rdd的内容为{rdd1.join(rdd2).collect()}") # 使用 join 进行连接
```

##### glom

glom()用于将每个分区的元素组合成一个列表（数组）的方法。这个方法返回一个包含列表的新的 RDD，其中每个列表对应于原始 RDD 中的一个分区

```python
rdd = spark.sparkContext.parallelize(range(1, 8), 2)  # 2个分区
print(f'rdd经过glom后的内容为:{rdd.glom().collect()}')
```

### 行动操作

* count ():返回 RDD 中的记录数
* first ():返回第一条记录
* max():返回最大记录
* min(): 返回最小记录
* reduce():将记录减少为单个，我们可以用它来计数或求和
    * 这个函数接收两个参数，表示两个值，然后返回一个新的值
* take():返回指定为参数的记录
* collect():以数组形式返回 RDD 中的所有数据。当您使用包含数百万和数十亿数据的大型 RDD 时使用此操作时要小心，因为您可能会耗尽驱动程序上的内存
* foreach():用于对 RDD 中的每个元素应用一个函数的行动（action）操作
* saveAsTextFile():使用 saveAsTestFile 操作，我们可以将 RDD 写入文本文件

```python
rdd = spark.sparkContext.parallelize(range(1, 8), 2)
print(f'rdd中的记录数为:{rdd.count()}')
print(f'rdd中的最大数为:{rdd.max()}')
print(f'rdd中的最小数为:{rdd.min()}')
print(f'rdd中的合计为:{rdd.reduce(lambda x,y: x+y)}')
print(f'rdd中的前5条记录为:{rdd.take(5)}')
print(f'rdd中的所有记录为:{rdd.collect()}')
```

## RDD持久化

RDD采用惰性求值的机制，每次遇到行为操作时，都会从头开始计算，对于迭代计算而已，代价是很大的，因此可以通过持久化(缓存)机制来避免重复计算的开销，具体方法是通过persist()方法来标记RDD持久化,persist()方法有一个持久化级别参数，具体有以下两种:
* persist(MEMORY_ONLY):RDD作为反序列化对象存储在JVM中，内存不足则按照LRU原则替换缓存
* persist(MEMORY_AND_DISK):RDD作为反序列化对象存储在JVM中,内存不足则存放在磁盘上

```python
rdd = spark.sparkContext.parallelize(range(1, 8), 2)
rdd.cache() # 调用这个方法时，会自动调用persist(MEMORY_ONLY)
print(f'rdd中的记录数为:{rdd.count()}')
rdd.unpersist() # 不再需要一个RDD时，可以使用unpersist()释放该RDD
```


