# Spark

Apache Spark是一个用于大规模数据处理的开源统一分析引擎。Spark 被设计为快速、灵活且易于使用，使其成为处理大规模数据集的流行选择。Spark 对分布式集群上数十亿和数万亿数据的运行速度比传统应用程序快 100 倍。 

Spark可以运行在**单节点机器或多节点机器(集群)**上。它的创建是为了通过进行内存处理来解决MapReduce的局限性。Spark通过使用内存缓存来重用数据，以加速在同一数据集上重复调用函数的机器学习算法。这降低了延迟，使Spark 比 MapReduce 快数倍，特别是在进行机器学习和交互式分析时

## 集群管理器的类型

在为初学者编写 Spark with Python (PySpark) 教程时，Spark 支持以下集群管理器：

* Standalone:Spark 附带的一个简单的集群管理器，可以轻松设置集群。
* Apache Mesos:Mesons 是一个集群管理器，还可以运行 Hadoop MapReduce 和 PySpark 应用程序。
* Hadoop YARN:Hadoop 2 中的资源管理器。这主要用作集群管理器。
* Kubernetes:一个用于自动化部署、扩展和管理容器化应用程序的开源系统。
* local——这并不是真正的集群管理器，我们使用“local”来master()在笔记本电脑/计算机上运行 Spark。

## PySpark

* PySpark 是一种通用的内存分布式处理引擎，可让您以分布式方式高效地处理数据。
* 在 PySpark 上运行的应用程序比传统系统快 100 倍。
* 使用 PySpark 进行数据摄取管道将给您带来巨大的好处。
* 使用 PySpark，我们可以处理来自 Hadoop HDFS、AWS S3 和许多文件系统的数据。
* PySpark 还用于使用 Streaming 和 Kafka 处理实时数据。
* 使用 PySpark 流式传输，您还可以从文件系统流式传输文件，也可以从套接字流式传输。
* PySpark 本身具有机器学习和图形库

### PySpark的架构

Apache Spark 在主从架构中工作，其中主设备称为“Driver”，从设备称为“Workers”。当您运行 Spark 应用程序时，Spark Driver会创建一个上下文作为应用程序的入口点，所有操作（转换和操作）都在工作节点上执行，资源由 Cluster Manager 管理

<div style="text-align: center;"><img alt='202404072155607' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072155607.png' width=500px> </div>

### PySpark模块

* PySpark RDD (pyspark.RDD)
* PySpark DataFrame 和 SQL (pyspark.sql)
* PySpark 流式处理 (pyspark.streaming)
* PySpark MLib（pyspark.ml、pyspark.mllib）
* PySpark GraphFrames (GraphFrames)
* PySpark 资源 (pyspark.resource) 这是 PySpark 3.0 中的新增功能

## PySpark的基本使用

## PySpark SparkSession

```python
from pyspark.sql import SparkSession
```
自 Spark 2.0 起，SparkSession 已成为 PySpark 与 RDD 和 DataFrame 配合使用的入口点。SparkSession 是我们在 2.0 版本之前使用的所有不同上下文（SQLContext 和 HiveContext 等）的组合类。创建 SparkSession 实例将是使用 RDD、DataFrame 和 Dataset 进行编程时编写的第一个语句,它是底层 PySpark 功能的入口点，以便以编程方式创建 PySpark RDD、DataFrame。它的对象spark默认在 pyspark-shell 中可用，并且可以使用 SparkSession 以编程方式创建。

虽然 SparkContext 在 2.0 之前曾经是一个入口点，但并没有完全被 SparkSession 取代，但是 SparkContext 的许多功能在 Spark 2.0 及更高版本中仍然可用并使用

SparkSession 还包括不同上下文中可用的所有 API：

* SparkContext,
* SQLContext,
* StreamingContext,
* HiveContext.

### 创建SparkSession

```python
from pyspark.sql import SparkSession

SparkSession.builder.master("local[1]") .appName('SparkByExamples.com').getOrCreate()
```
* `master()`:集群管理器的类型，单机上使用local\[*\]即可，代表使用所有cpu核心
* `appName()`:应用程序的唯一名字
* `getOrCreate()`:如果存在则返回一个SparkSession对象，如果不存在则创建一个Sparkession对象

### 创建另一个SparkSession

你可以使用`newSession`方法来创建一个新的SparkSession对象，它会使用当前的appName和集群管理器

```python
spark2 = SparkSession.newSession
```

### 获取已经存在的SparkSession对象

```python
spark3 = SparkSession.builder.getOrCreate()
```

