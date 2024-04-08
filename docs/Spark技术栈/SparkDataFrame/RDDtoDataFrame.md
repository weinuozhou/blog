# RDD 与 DataFrame的转换

## 将RDD转换成DataFrame

### 使用rdd.toDF()函数

* PySpark在RDD中提供了toDF()函数，可用于将RDD转换为Dataframe
* 默认情况下，toDF()函数创建列名称为 `_1` 和 `_2`
* 它可以支持传入列名参数

```python
dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
rdd = spark.sparkContext.parallelize(dept)
rdd.toDF(["dept_name","dept_id"]).show()
```

### 使用PySpark createDataFrame()函数

```python
dept = [("Finance",10),("Marketing",20),("Sales",30),("IT",40)]
rdd = spark.sparkContext.parallelize(dept)
df = spark.createDataFrame(rdd, schema=["dept_name","dept_id"])
df.printSchema()
df.show()
```

#### 将 `createDataFrame()` 与 `StructType` 模式结合使用

当您推断架构时，默认情况下，列的数据类型是从数据派生的，并将所有列的可为空设置为 true。我们可以通过使用StructType提供架构来更改此行为，我们可以在其中为每个字段/列指定列名、数据类型和可空性

```python
deptSchema = StructType([       
    StructField('dept_name', StringType(), True),
    StructField('dept_id', StringType(), True)
])
rdd = spark.sparkContext.parallelize(dept)
df = spark.createDataFrame(rdd, schema=deptSchema)
df.printSchema()
df.show()
```

## 将DataFrame转换成RDD

`df.rdd`可以将DataFrame转换成RDD

```python
data = [("James", "","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.select("gender", "salary").filter(df.gender != '') \
    .rdd.mapValues(lambda x: (x, 1)).reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1])) \
    .mapValues(lambda x: x[0]/x[1]).toDF(columns[-2:]).show()
```

