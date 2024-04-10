# PySpark StructType 和 StructField

PySpark StructType 和 StructField 类用于以编程方式指定 DataFrame 的架构并创建复杂的列，例如嵌套结构、数组和映射列。StructType 是 StructField 对象的集合，它定义列名称、列数据类型、用于指定字段是否可以为空的布尔值以及元数据

* **定义 DataFrame 模式**: StructType通常用于在创建 DataFrame 时定义模式，特别是对于具有不同数据类型字段的结构化数据
* **嵌套结构StructType**: 您可以通过嵌套在其他对象中来创建具有嵌套结构的复杂模式StructType，从而允许您表示分层或多级数据
* **强制数据结构**: 从各种来源读取数据时，指定StructType作为模式可确保数据得到正确解释和结构化。在处理半结构化或无模式数据源时很重要

```python
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
```

## StructType的两种构建方法

```python
StructType([StructField("column_name",StringType(),True),])
StructType().add("column_name", StringType(), True)
```
* 需要传入的参数:列名、数据类型和是否可以为空值

```python
schema = StructType([
    StructField("firstname", StringType(), True),
    StructField("middlename", StringType(), True),
    StructField("lastname",StringType(), True),
    StructField("id", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("salary", IntegerType(), True)
  ])
# 等价于
schema = StructType() \
        .add("firstname", StringType(), True) \
        .add("middlename", StringType(), True) \
        .add("lastname", StringType(), True) \
        .add("id", StringType(), True) \
        .add("gender", StringType(), True) \
        .add("salary", IntegerType(), True)
```

## PySpark StructType 和 StructField 与 DataFrame 结合使用

```python
data = [("James", "", "Smith", "36636", "M", 3000),
    ("Michael", "Rose", "", "40288", "M", 4000),
    ("Robert", "", "Williams", "42114", "M", 4000),
    ("Maria", "Anne", "Jones", "39192", "F", 4000),
    ("Jen", "Mary", "Brown", "", "F", -1)
  ]
schema = StructType([
    StructField("firstname",StringType(),True),
    StructField("middlename",StringType(),True),
    StructField("lastname",StringType(),True),
    StructField("id", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("salary", IntegerType(), True)
  ])
df = spark.createDataFrame(data=data,schema=schema)
df.printSchema()
df.show()
```