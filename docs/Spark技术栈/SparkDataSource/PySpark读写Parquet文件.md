# PySpark 读写 Parquet 文件

## Parquet 文件简介

`Apache Parquet` 文件是一种列式存储格式，适用于 `Hadoop` 生态系统中的任何项目，无论选择何种数据处理框架、数据模型或编程语言

### 优点

* 在查询列式存储时，它会非常快速地跳过不相关的数据，从而**加快查询执行速度**。因此，与面向行的数据库相比，聚合查询消耗的时间更少
* 它能够支持**高级嵌套**数据结构
* 支持**高效的压缩选项**和编码方案

## Pyspark 将 DataFrame 写入 Parquet 文件

```python
df.write.parquet(path, mode, partitionBy, compression)
```

* `path`: 指定输出文件的路径。可以是本地文件系统路径或分布式文件系统路径（如 HDFS）
* `mode`: 指定写入模式，可以是 "append"（追加）、"overwrite"（覆盖）、"ignore"（忽略）或 "error"（报错）。默认值为 "error"
* `partitionBy`: 按照指定的列对数据进行分区，并将每个分区写入独立的 Parquet 文件。可以是单个列名的字符串，或是列名列表。默认值为 None，表示不进行分区
* `compression`: 指定压缩格式，可以是 "uncompressed"（不压缩）、"snappy"、"gzip" 或 "lzo"。默认值为 "snappy"

```python
data =[("James ","","Smith","36636","M",3000),
              ("Michael ","Rose","","40288","M",4000),
              ("Robert ","","Williams","42114","M",4000),
              ("Maria ","Anne","Jones","39192","F",4000),
              ("Jen","Mary","Brown","","F",-1)]
columns=["firstname","middlename","lastname","dob","gender","salary"]
df=spark.createDataFrame(data,columns)
df.write.parquet("data/spark/output.parquet", partitionBy=["gender"])
```
    
## Pyspark 从 Parquet 文件读取 DataFrame

```python
df = spark.read.parquet(path, inferSchema)
```

* `path`: 指定要读取的 Parquet 文件路径或目录路径。可以是单个文件的路径，也可以是包含多个 Parquet 文件的目录路径
* `inferSchema`: 指定是否自动推断模式。默认为 False。当设置为 True 时，Spark 将读取文件的一部分数据来推断模式

```python
df = spark.read.parquet("data/spark/output.parquet/gender=F")
df.show()
```

```bash
+---------+----------+--------+-----+------+
|firstname|middlename|lastname|  dob|salary|
+---------+----------+--------+-----+------+
|   Maria |      Anne|   Jones|39192|  4000|
|      Jen|      Mary|   Brown|     |    -1|
+---------+----------+--------+-----+------+
```