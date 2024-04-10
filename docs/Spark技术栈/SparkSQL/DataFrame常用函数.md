# DataFrame对列、行的类、操作和函数

## 选择列

下面的演示统一使用如下DataFrame:
```python
data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data = data, schema = columns)
df.show()
```

### 选择单列和多列

```python
df.select("firstname", "lastname").show()
df.select(df.firstname, df.lastname).show()
```

### 使用col函数

```python
from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()
```

### 从列表中选择所有列

```python
df.select(*columns).show() 
df.select([col for col in df.columns]).show()
df.select("*").show()
```

### 按索引选择列

```python
df.select(df.columns[:2]).show()
```

## Row类

### 创建Row对象

```python
from pyspark.sql import Row
row = Row(name="Alice", age=11)
print(row.name, row.age) 
```

### 在 RDD 上使用 Row 类

```python
data = [Row(name="James,,Smith", lang=["Java","Scala","C++"], state="CA"), 
    Row(name="Michael,Rose,", lang=["Spark","Java","C++"], state="NJ"),
    Row(name="Robert,,Williams", lang=["CSharp","VB"], state="NV")]
rdd = spark.sparkContext.parallelize(data)
rdd.toDF().show()
```

### 在 DataFrame 上使用 Row 类

```python
data = [Row(name="James,,Smith",lang=["Java","Scala","C++"],state="CA"), 
    Row(name="Michael,Rose,",lang=["Spark","Java","C++"],state="NJ"),
    Row(name="Robert,,Williams",lang=["CSharp","VB"],state="NV")]
spark.createDataFrame(data).show()
```

### 使用 Row 类创建嵌套结构

```python
data = [Row(name="James", prop=Row(hair="black",eye="blue")),
      Row(name="Ann", prop=Row(hair="grey",eye="black"))]
spark.createDataFrame(data).show()
```

## PySpark 列运算符

```python
data = [(100,2,1),(200,3,4),(300,4,4)]
df = spark.createDataFrame(data).toDF("col1", "col2", "col3")
df.select(df.col1 + df.col2).show()
df.select(df.col1 - df.col2).show() 
df.select(df.col1 * df.col2).show()
df.select(df.col1 / df.col2).show()
df.select(df.col1 % df.col2).show()
```

## PySpark列函数

本小节的所有演示均使用以下DataFrame:
```python
data = [("James","Bond","100",None),
      ("Ann","Varsa","200",'F'),
      ("Tom Cruise","XXX","400",''),
      ("Tom Brand",None,"400",'M')] 
columns = ["fname","lname","id","gender"]
df = spark.createDataFrame(data,columns)
```

### alias() – 设置名称

```python
df.select(df.fname.alias("first_name"),
          df.lname.alias("last_name")
   ).show()
```

### asc() 和 desc()

按升序或降序对 DataFrame 列进行排序

```python
df.sort(df.fname.asc()).show()
df.sort(df.fname.desc()).show()
```

### contains()

用于检查 DataFrame 列值是否包含此函数中指定的值

```python
df.filter(df.fname.contains("Cruise")).show()
```

### startswith() 和endswith()

这两个函数是检查DataFrame 列的值是否分别以字符串开头和结尾

```python
df.filter(df.fname.startswith("T")).show()
df.filter(df.fname.endswith("Cruise")).show()
```

### isin()

检查列表中是否存在值

```python
li = ["100","200"]
df.select(df.fname, df.lname, df.id) \
  .filter(df.id.isin(li)) \
  .show()
```
### withColumn函数

withColumn()是 DataFrame 的转换函数，用于更改值、转换现有列的数据类型、创建新列等等

这里统一使用以下DataFrame作为数据源:
```python
data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
```

#### 更改数据类型

```python
df.withColumn("salary", col("salary").cast("Integer")).printSchema()
```

#### 更新现有列的值

```python
df.withColumn("salary", col("salary")*100).show()
``` 

#### 从现有列创建列

```python
df.withColumn("CopiedColumn",col("salary")* -1).show()
```

#### 使用 withColumn() 添加新列

```python
df.withColumn("Country", lit("USA")) \
  .withColumn("anotherColumn",lit("anotherValue")) \
  .show()
```

#### 重命名列名

```python
df.withColumnRenamed("gender","sex").show()
```

### orderBy()函数

orderBy()对一列或多列进行排序的功能。默认情况下，它按升序排序

```python
simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]
columns= ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data = simpleData, schema = columns)
df.orderBy(df.age.asc(), df.salary.desc()).show()
```

### sort函数

sort()对一列或多列进行排序。 sort()采用布尔参数表示升序或降序。要为不同的列指定不同的排序顺序，可以使用该参数作为列表

```python
df.sort("age", "salary", ascending=[True, False]).show()
```

### filter函数

这一小节使用的DataFrame如下:
```python
data = [
    (("James","","Smith"),["Java","Scala","C++"],"OH","M"),
    (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
    (("Julia","","Williams"),["CSharp","VB"],"OH","F"),
    (("Maria","Anne","Jones"),["CSharp","VB"],"NY","M"),
    (("Jen","Mary","Brown"),["CSharp","VB"],"NY","M"),
    (("Mike","Mary","Williams"),["Python","VB"],"OH","M")
 ]
        
schema = StructType([
     StructField('name', StructType([
        StructField('firstname', StringType(), True),
        StructField('middlename', StringType(), True),
        StructField('lastname', StringType(), True)
     ])),
     StructField('languages', ArrayType(StringType()), True),
     StructField('state', StringType(), True),
     StructField('gender', StringType(), True)
 ])
df = spark.createDataFrame(data, schema)
df.show()
```

#### 带有列条件

```python
df.filter(df.state == "OH").show()
```

#### 具有多个条件的过滤器

```python
df.filter((df.state == "OH") & (df.gender  == "M")).show() 
```

#### 根据列表值进行过滤

* 想要过滤不在列表中的元素，请使用isin()函数
* 值得注意的是并没有isnotin()函数，但可以使用 not 运算符 (~) 执行相同的操作

```python
li = ["OH","CA","DE"]
df.filter(df.state.isin(li)).show() # df.filter(~df.state.isin(li)).show()
```

#### 基于开始、结束、包含的过滤

```python
df.filter(df.state.startswith("N")).show()
df.filter(df.state.endswith("H")).show()
df.filter(df.state.contains("Y")).show()
```

#### 模糊匹配

* like：模糊匹配
* rlike:使用正则表达式

```python
df.filter(df.state.like('N%')).show()
```

### groupBy()函数

PySpark的groupBy()函数用于将相同的数据收集到 DataFrame 上的组中，并对分组的数据执行聚合函数
* count()– 使用groupBy() count()返回每个组的行数。
* mean()– 返回每组值的平均值。
* max()– 返回每组的最大值。
* min()– 返回每组的最小值。
* sum()– 返回每组值的总计。
* avg()– 返回每组值的平均值。
* agg()– 使用agg()函数，我们可以一次计算多个聚合

这一小节使用的DataFrame如下: 
```python
simpleData = [("James","Sales","NY",90000,34,10000),
    ("Michael","Sales","NY",86000,56,20000),
    ("Robert","Sales","CA",81000,30,23000),
    ("Maria","Finance","CA",90000,24,23000),
    ("Raman","Finance","CA",99000,40,24000),
    ("Scott","Finance","NY",83000,36,19000),
    ("Jen","Finance","NY",79000,53,15000),
    ("Jeff","Marketing","CA",80000,25,18000),
    ("Kumar","Marketing","NY",91000,50,21000)
  ]

schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=simpleData, schema = schema)
df.groupBy("department").sum("salary").show(truncate=False)
```

#### agg聚合函数

```python
from pyspark.sql.functions import *
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"),
         mean("salary").alias("mean_salary"),
         sum("bonus").alias("sum_bonus"),
         max("bonus").alias("max_bonus") 
     ) \
    .show(truncate=False)
```

#### 对聚合函数使用过滤器

与 SQL“HAVING”子句类似，在 PySpark DataFrame 上，我们可以使用where()或filter()函数来过滤聚合数据行

```python
df.groupBy("department") \
    .agg(sum("salary").alias("sum_salary"),
      avg("salary").alias("avg_salary"),
      sum("bonus").alias("sum_bonus"),
      max("bonus").alias("max_bonus"))\
    .where(col("sum_bonus") >= 50000)\
    .show(truncate=False)
```

## 创建视图使用 SQL 语句

* `createOrReplaceTempView()` 创建一个临时视图，生命周期取决于当前SparkSession
* `createOrReplaceGlobalTempView()` 创建一个全局视图，生命周期取决于SparkSession本身
  
```python
data = [("James", "","Smith","36636","M",60000),
        ("Michael","Rose","","40288","M",70000),
        ("Robert","","Williams","42114","",400000),
        ("Maria","Anne","Jones","39192","F",500000),
        ("Jen","Mary","Brown","","F",0)]

columns = ["first_name","middle_name","last_name","dob","gender","salary"]
df = spark.createDataFrame(data = data, schema = columns)
df.createOrReplaceTempView("employee")
spark.sql("select gender, avg(salary) as avg_salary from employee where gender!='' group by gender ").show()
```