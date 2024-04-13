# PySpark 读写 csv 文件

## PySpark将CSV文件读入DataFrame

在PySpark中，可以使用`read.csv()`方法将CSV文件读入DataFrame

```python
spark.read.csv(path, header, inferSchema, sep, nullValue, mode)
```

- `path`: CSV文件的路径, 可以是本地文件系统或者hdfs文件系统
- `header`: 是否包含表头，默认为`True`  
- `inferSchema`: 是否自动推断数据类型，默认为`False`
- `sep`: CSV文件的分隔符，默认为`,`       
- `nullValue`: 用于表示空值的字符串。默认为空字符串    
- `mode`: 确定如何处理解析错误的参数，默认为`"PERMISSIVE"`, 将错误的记录放入一个单独的列

```python
df = spark.read.csv('../data/spark/iris.csv', header=True, inferSchema=True, sep=',', nullValue='', mode='PERMISSIVE')
df.printSchema()
```

运行结果如下:

```bash
root
 |-- sepal_length: double (nullable = true)
 |-- sepal_width: double (nullable = true)
 |-- petal_length: double (nullable = true)
 |-- petal_width: double (nullable = true)
 |-- class: string (nullable = true)
```

## 将 PySpark DataFrame 写入 CSV 文件

在PySpark中，可以使用`write.csv()`方法将DataFrame写入CSV文件
    

```python
df.write.csv(path, header, mode, sep, quote, escape, nullValue, nanValue, dateFormat, compression, escapeQuotes)
```

* `path` ：CSV 文件的输出路径
* `mode` ：确定如何处理现有文件或目录的参数。可选值包括 "append"（追加到现有文件）、"overwrite"（覆盖现有文件）和 "ignore"（如果文件已存在，则忽略写入操作）
* `sep` ：用于分隔字段的字符串。默认为逗号
* `quote` ：用于引用字段的字符串。默认为双引号
* `escape` ：用于转义字段的字符串。默认为反斜杠
* `nullValue` ：用于表示空值的字符串。默认为空字符串

```python
data = [("James", "","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.write.csv("data/spark/output.csv", mode="ignore", header=True)
```

!> 注意: 最终实际上会生成多个文件，而不是一个单独的文件。这是因为 `PySpark` 在分布式环境中运行，数据被分成多个分区并行处理。每个分区生成一个独立的 CSV 文件。生成的文件数取决于数据的分区数和集群的配置

!> 如果希望生成一个单独的文件而不是多个文件，可以在写入 CSV 文件之前使用 `coalesce(1)` 函数将数据合并到一个分区中，然后再调用 `write.csv` 函数

```python
data = [("James", "","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.coalesce(1).write.csv("data/spark/output.csv", mode="ignore", header=True)
```

