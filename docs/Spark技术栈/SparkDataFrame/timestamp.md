# 日期和时间函数

DataFrame 和 SQL 查询支持 PySpark **日期**和**时间戳函数**

?> 大多数这些函数接受日期类型、时间戳类型或字符串输入。如果使用字符串，则它应该采用可以转换为日期的默认格式

* DateType默认格式是yyyy-MM-dd 
* TimestampType默认格式是yyyy-MM-dd HH:mm:ss.SSSS
* 如果输入是无法转换为日期或时间戳的字符串，则返回null
* 日期和时间函数顾名思义，这里不再详细解释

```python
from pyspark.sql.functions import *
```

## 日期函数

|日期函数|说明|
| :---: | :--|
|`current_date()`|以日期列形式返回当前日期|
|`date_format(dateExpr,format)` | 将日期/时间戳/字符串转换为第二个参数给出的日期格式指定的格式的字符串值|
|`to_date(column, fmt)`|转换为日期类型|
|`add_months(Column, numMonths)`|增加numMonths个月|
|`data_add(column, days)`|增加days天|
|`datadiff(end, start)`|计算两个日期差|
|`months_between(end, start)`|计算月数差，如果两个输入的日期相同或均为各自月份的最后一天，则返回整数。否则，将假设每月 31 天来计算差异。|
|`next_day(column, dayOfWeek)`|返回下一个星期的日期|
|`year(column)`|返回年|
|`month(clolumn)`|返回月份|
|`dayofweek(column)`|返回星期几|
|`dayofmonth(column)`|返回给定日期在这个月是第几天|
|`dayofyear(column)`|返回给定日期是今年的第几天|
|`weekofyear(column)`|返回给定日期是今年的第几周|
|`last_day(column)`|返回给定日期的月份的最后一天|

```python
data = [["1","2020-02-01 11:01:19.06"],["2","2019-03-01 12:01:19.406"],["3","2021-03-01 12:01:19.406"]]
df = spark.createDataFrame(data, ["id","input"])
# to_date函数
df.select(col("input"), 
    to_date(col("input")).alias("to_date") 
  ).show(truncate=False)
# year、month函数
df.select(col("input"), 
     year(col("input")).alias("year"), 
     month(col("input")).alias("month"), 
  ).show(truncate=False)
# weekofyear()、dayofweek()、 dayofmonth()、dayofyear()函数
df.select(col("input"),
     weekofyear(col("input")).alias("weekofyear"),
     dayofweek(col("input")).alias("dayofweek"), 
     dayofmonth(col("input")).alias("dayofmonth"), 
     dayofyear(col("input")).alias("dayofyear"), 
  ).show(truncate=False)
```

## 时间戳函数

|函数|说明|
|:---:|:---|
|`current_timestamp()`|返回当前时间戳|
| `hour(column)`|返回给定时间的小时|
| `minute(column)`|返回给定时间的分钟|
| `second(column)`| 返回给定时间的秒|
| `to_timestamp(column, fmt)`|以给定的形式转换时间戳|


```python
data = [["1","2020-02-01 11:01:19.06"],["2","2019-03-01 12:01:19.406"],["3","2021-03-01 12:01:19.406"]]
df = spark.createDataFrame(data, ["id","input"])
df.select(col("input"), 
    hour(col("input")).alias("hour"), 
    minute(col("input")).alias("minute"),
    second(col("input")).alias("second") 
  ).show(truncate=False)
```



