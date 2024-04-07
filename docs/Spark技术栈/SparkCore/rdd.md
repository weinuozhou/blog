

## RDD编程

* RDD（弹性分布式数据集）是 PySpark 的基本构建块，它是容错、不可变的分布式对象集合。不可变意味着一旦创建了 RDD，就无法更改它。RDD中的每条记录都被划分为逻辑分区，可以在集群的不同节点上进行计算。
* 换句话说，RDD 是类似于 Python 中的 list 的对象集合，不同之处在于 RDD 是在分散在多个物理服务器（也称为集群中的节点）的多个进程上计算的，而 Python 集合仅在一个进程中生存和处理
* 此外，RDD 提供数据分区和分布的数据抽象，旨在在多个节点上并行运行计算，同时在 RDD 上进行转换时，我们不必担心 PySpark 默认提供的并行性

**RDD的优点**:

* **内存处理**:PySpark从磁盘加载数据并在内存中处理并将数据保留在内存中，这是PySpark和Mapreduce（I/O密集型）之间的主要区别。在转换之间，我们还可以将 RDD 缓存/保留在内存中以重用之前的计算
* **不变性**:PySpark RDD 本质上是不可变的，这意味着 RDD 一旦创建就无法修改。当我们对 RDD 应用转换时，PySpark 会创建一个新的 RDD 并维护 RDD 谱系
* **容错能力**:PySpark 在 HDFS、S3 等上的容错数据存储上运行，因此任何 RDD 操作失败，它都会自动从其他分区重新加载数据。此外，当 PySpark 应用程序在集群上运行时，PySpark 任务失败会自动恢复一定次数（根据配置）并无缝完成应用程序
* **惰性进化**:PySpark 不会在 Driver 出现/遇到时评估 RDD 转换，而是保留遇到的所有转换 (DAG)，并在看到第一个 RDD 操作时计算所有转换

### 创建RDD

RDD 主要以两种不同的方式创建:
* **使用并行化集合**
* **使用存储系统中的数据集**

#### 使用集合创建RDD

```python
spark = SparkSession.builder.master('local[*]').appName("example").getOrCreate()
spark.sparkContext.parallelize(c, numSlices)
```
* c: 要转换为 RDD 的本地集合（collection）。通常是一个 Python 列表或者其他可迭代的数据结构。
* numSlices (可选): 可以指定将数据切分成的分片数量。分片数量决定了 RDD 在集群中的分布方式，影响了并行度。如果未提供此参数，默认情况下 Spark 将根据集群的配置和数据大小自动选择分片数量。

#### 使用存储系统的数据集创建RDD

