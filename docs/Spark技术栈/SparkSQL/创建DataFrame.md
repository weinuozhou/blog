# 创建DataFrame

DataFrame 是组织成命名列的分布式数据集合。它在概念上相当于关系数据库中的表或 R/Python 中的DataFrame，但在幕后具有更丰富的优化。 DataFrame 可以从多种来源构建，例如结构化数据文件、Hive 中的表、外部数据库或现有 RDD

可以使用`createDataFrame`方法创建DataFrame

```python
spark.createDataFrame(data, schema, samplingRatio=1.0, verifySchema=True)
```
* `data`: 必需的参数，用于指定输入数据。可以是多种类型的数据，例如列表、元组、字典、Pandas DataFrame、RDD等
* `schema`: 可选参数，用于指定DataFrame的模式（schema）。它可以是一个pyspark.sql.types.StructType对象，定义了DataFrame中每列的名称和数据类型。如果不提供模式，则Spark会尝试从数据中推断模式
* `samplingRatio`: 可选参数，用于指定用于推断模式的抽样比率。默认值为1.0，表示对所有数据进行推断。如果数据集很大，可以降低抽样比率以提高性能
* `verifySchema`: 可选参数，用于指定是否验证数据与模式是否一致。默认值为True，表示进行验证。设置为False可以提高性能，但可能导致数据与模式不匹配的错误

## 使用Schema（StructType）创建空DataFrame

```python
schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
  ])
emptyRDD = spark.sparkContext.emptyRDD() # 创建空RDD
df = spark.createDataFrame(emptyRDD, schema)
df.printSchema()
```

## 将空 RDD 转换为 DataFrame

```python
schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
  ])
emptyRDD = spark.sparkContext.emptyRDD()
df = emptyRDD.toDF(schema)
df.printSchema()
```

## 使用列表创建空 DataFrame

```python
schema = StructType([
  StructField('firstname', StringType(), True),
  StructField('middlename', StringType(), True),
  StructField('lastname', StringType(), True)
  ])
df = spark.createDataFrame([], schema)
df.printSchema()
```

## 创建空 DataFrame（无列）

```python
df = spark.createDataFrame([], StructType([]))
df.printSchema()
```

## 将DataFrmae转换成Pandas DataFrame

toPandas() 结果会将 PySpark DataFrame 中的所有记录收集到驱动程序，并且应该仅对一小部分数据进行操作。在较大的数据集上运行会导致内存错误并使应用程序崩溃。要处理更大的数据集，可以尝试增加驱动程序上的内存

```python
data = [("James", "","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
pysparkDF = spark.createDataFrame(data = data, schema = columns)
pandasDF = pysparkDF.toPandas()
```