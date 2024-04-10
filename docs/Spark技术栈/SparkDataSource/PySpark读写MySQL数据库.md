# PySpark 读写 MySQL 数据库

PySpark 要想连接 MySQL 数据库，需要下载 MySQL 驱动程序，并将其添加到 PySpark 的依赖中
```bash
scp -r ./lib/mysql-connector-java-5.1.19-bin.jar weno@master:/usr/local/spark/jars/
```

## 读取 MySQL 数据

可以使用 `read.jdbc()`来读取数据库的数据

```python
spark.read.jdbc(url="jdbc:mysql://hostname:port/database_name", table="tbname", properties, columns, predicates, numPartitions)
```

* `url`：数据库的连接 URL，用于指定数据库类型、位置、端口和数据库名称等信息。例如，`jdbc:mysql://localhost:3306/mydb` 表示连接到本地 MySQL 数据库的 URL
* `table`：数据库中的表名
* `properties`: 包含连接属性的字典，用于指定 JDBC 连接的配置选项。常见的属性包括 user、password、driver等。例如，`properties={"user": "root", "password": "root", "driver": "com.mysql.jdbc.Driver"}`
* `column`: 要选择的列或表达式列表，用于指定要加载的特定列。默认为 *，表示加载所有列
* `predicates`: 用于指定过滤条件，用于过滤掉不需要的数据。例如，`predicates="id > 10"` 表示只加载 id 大于 10 的数据, 也可以使用多个条件: `predicates=["age > 30", "gender = 'Male'"]`
* `numPartitions`: 用于指定读取数据的分区数，默认为 1

```python
url = "jdbc:mysql://127.0.0.1:3306/experiment"
prop = {
    "user": "root",
    "password": "686521",
    "driver": "com.mysql.jdbc.Driver"
}
df = spark.read.jdbc(url, table="student", properties=prop)
df.show()
df.printSchema()
```

## 写入 MySQL 数据

可以使用 `write.jdbc()`来将数据写入 MySQL 数据库
    
```python
df.write.jdbc(url="jdbc:mysql://hostname:port/database_name", table="tbname", mode="overwrite", properties, batchsize)
```

* `url`：数据库的连接 URL，用于指定数据库类型、位置、端口和数据库名称等信息。例如，`jdbc:mysql://localhost:3306/mydb` 表示连接到本地 MySQL 数据库的 URL
* `table`：数据库中的表名
* `properties`: 包含连接属性的字典，用于指定 JDBC 连接的配置选项。常见的属性包括 user、password、driver等。例如，`properties={"user": "root", "password": "root", "driver": "com.mysql.jdbc.Driver"}`
* `mode`: 用于指定写入模式，默认为 `append`，表示追加写入数据。还可以设置为 `overwrite`，表示覆盖写入数据
* `batchsize`: 批量写入的行数。默认为 1000 行。可以根据数据大小和性能需求进行调整

```python
columns = ["sno", "sname", "ssex", "sbirth", "sclass", "zno", "age"]
data = [["211360", "张金生", "男", "2001-09-12", "安全2104", "1102", 23], ]
df = spark.createDataFrame(data, columns)
df.write.jdbc(url, table="student", mode="append", properties=prop)
```
