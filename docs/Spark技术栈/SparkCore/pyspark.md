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

### PySpark Shell

现在打开命令提示符并键入 pyspark 命令来运行 PySpark shell

```bash
cd /usr/local/spark/bin && ./pyspark
```

<div style="text-align: center;"><img alt='202404081411523' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081411523.png' width=500px> </div>

PySpark shell 还创建一个Spark 上下文 Web UI(作业、阶段、任务、存储、环境、执行器和 SQL)来监视 Spark 应用程序的状态、Spark 集群的资源消耗和 Spark 配置，默认情况下，它可以从 http://localhost:4040/ 访问

<div style="text-align: center;"><img alt='202404081416499' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081416499.png' width=500px> </div>

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


### PySpark Shell 中的 SparkSession

默认 PySpark shell 提供 spark 对象, 这是 SparkSession 类的一个实例。我们可以在shell中需要的地方直接使用这个对象

<div style="text-align: center;"><img alt='202404081500937' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081500937.png' width=500px> </div>

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

### 配置SparkSession对象

可以使用`config()`方法来配置SparkSession对象

```python
spark = SparkSession.builder \
      .master("local[*]") \
      .appName("SparkByExamples.com") \
      .config("spark.some.config.option", "config-value") \
      .getOrCreate()
```

### 创建一个启用Hive的SparkSession

```python
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .config("spark.sql.warehouse.dir", "<path>/spark-warehouse") \
      .enableHiveSupport() \
      .getOrCreate()
```

### SparkSession的常用方法

* `version`:返回您的应用程序运行时的 Spark 版本，可能是您的集群配置的 Spark 版本
* `createDataFrame()`:这会从集合或RDD创建一个 DataFrame
* `getActiveSession()`:返回活动的 Spark 会话
* `read()`:返回类的实例DataFrameReader，用于将记录从 csv、parquet、 avro 和更多文件格式读取到 DataFrame 中
* `readStream()`:返回类的实例 DataStreamReader ，用于读取流数据。可用于将流数据读取到 DataFrame 中
* `sparkContext()`:返回SparkContext
* `sql()`: 执行上述 SQL 后返回一个 DataFrame
* `sqlContext()`: 返回SQLContext
* `stop()`: 停止当前的SparkContext
* `table()`: 返回表或视图的 DataFrame
* `udf()`: 创建一个PySpark UDF 以在 DataFrame 、 Dataset 和 SQL上使用它

#### version

```python
spark = SparkSession.builder \
      .master("local[*]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()
print(f'当前PySpark的版本为{spark.version}')
```

#### createDataFrame()

```python
df = spark.createDataFrame([("Scala", 25000), ("Spark", 35000), ("Python", 21000)])
df.show()
```

#### spark sql

为了首先使用 SQL 功能，您需要在 PySpark 中创建一个临时视图。一旦有了临时视图，您就可以使用spark.sql()方法运行任何SQL 查询
```python
df.createOrReplaceTempView(table_name) # 创建临时视图
```

示例如下:
```python
df = spark.createDataFrame([("Scala", 25000), ("Spark", 35000), ("Python", 21000)])
df.createOrReplaceTempView("sample_table")
spark.sql("SELECT * FROM sample_table").show()
```

#### 停止SparkSession

建议在完成 Spark 作业后结束 Spark 会话，以便 JVM 关闭并释放资源

```python
spark.getActiveSession() # 获取正在活动的SparkSession
spark.stop() # 结束Spark会话
```

## SparkContext

pyspark.SparkContext是 PySpark 功能的入口点，用于与集群通信并创建 RDD、累加器和广播变量

### PySpark Shell 中的 SparkContext

PySpark shell 默认创建并提供sc对象，它是 SparkContext 类的实例。可以在需要的地方直接使用这个对象，而不需要创建

* `sc.applicationId`: 返回SparkContext的applicationId
* `sc.version`: 运行作业的 PySpark 集群的版本
* `sc.uiWebUrl`: 返回SparkContext的Web UI的URL

### 在PySpark中创建SparkContext

从 PySpark 2.0 开始，创建 SparkSession会在内部创建 SparkContext 并公开sparkContext要使用的变量

每个SparkContext只能有一个实例处于活动状态。如果您想创建另一个SparkContext，您应该使用stop()函数停止使用现有的 SparkContext

```python
spark = SparkSession.builder.master("local[*]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()
print(spark.sparkContext)
print("Spark App Name : "+ spark.sparkContext.appName)
print("spark master: " + spark.sparkContext.master)
spark.stop() # 停止spark会话
```

当然，也可以手动创建SparkContext对象

```python
conf = SparkConf().setMaster("local[*]").setAppName('demo')
sc = SparkContext(conf=conf)
```

### 获取SparkContext的配置

```python
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

configurations = spark.sparkContext.getConf().getAll()
for item in configurations:
    print(item)
```

### SparkContext常用方法

#### textFile()

从 HDFS、本地或任何 Hadoop 支持的文件系统读取文本文件并返回 RDD

在运行以下代码之前, 先将word.txt文件上传到HDFS中

```bash
hdfs dfs -put word.txt /spark
```

```python
rdd = spark.sparkContext.textFile('hdfs://localhost:9000/spark/word.txt')
rdd.collect()
```

#### wholeTextFile

用于读取一个目录下的所有文本文件，并返回一个包含文件名和文件内容的键值对（key-value pairs）的RDD（Resilient Distributed Dataset）

```python
rdd = spark.sparkContext.wholeTextFiles("file:///home/hadoop/jupyternotebook/test")
print(f'rdd中所有内容为:\n{rdd.collect()}')
for file in rdd.collect():
    print(f"File Name:{file[0]}")
    print(f"File Content:\n{file[1]}")
```

### 停止PySpark SparkContext

可以通过调用` SparkContext.stop()`该方法来停止SparkContext

```python
spark.sparkContext.stop()
```