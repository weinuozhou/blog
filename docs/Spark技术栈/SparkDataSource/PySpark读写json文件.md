# PySpark 读写 json 文件

## PySpark 将 JSON 文件 读入 DataFrame

在PySpark中，可以使用`read.json()`方法将JSON文件读入DataFrame

```python
spark.read.json(path, schema, multiLine)
```

- `path`: 指定要加载的 JSON 文件的路径。可以是本地文件系统路径或分布式文件系统（如 HDFS）的路径
- `schema`: 指定自定义的数据模式（Schema），用于解析 JSON 数据。可以通过 `pyspark.sql.types` 模块中的数据类型来定义模式。默认情况下，模式将自动从数据中推断出来
- `multiLine`: 指定是否将每个 JSON 对象视为单独的行。默认为 `False`, 表示每行包含一个完整的 JSON 对象。如果设置为 `True`, 则每行将被视为一个 JSON 对象

```python
df = spark.read.json("data/spark/yelp_academic_dataset_business.json")
df.printSchema()
```

## PySpark 将 DataFrame 写入 JSON 文件

在PySpark中，可以使用`write.json()`方法将DataFrame写入JSON文件
    
```python
df.write.json(path, mode)
```

* `path`: 定要写入的 JSON 文件的路径。可以是本地文件系统路径或分布式文件系统（如 HDFS）的路径
* `mode`: 指定写入模式。可选值包括 "overwrite"（覆盖写入，如果文件已存在则先删除）、"append"（追加写入，如果文件已存在则在末尾追加）、"ignore"（忽略写入，如果文件已存在则不进行写入）和 "error"（发生错误时抛出异常，默认值）

```python
df = spark.read.json("data/spark/output.json")
df.show()
```