# Python+MySQL

## PyMySQL 介绍与安装

想要操作`MySQL`数据库，必须要先安装`Python` 操作 `MySQL` 的驱动。在Python中，目前存在以下的`MySQL`驱动

* `MySQL-python`:只支持 Python2
* `mysqlclient`: 是 MySQL-python 的另外一个分支，支持Python3并修复了一些 bug , 是目前执行效率最高的驱动， 但是安装时容易因为环境问题出错
* `pymysql`: 纯 Python 实现的驱动，执行效率不如`mysqlclient`，但是可以与 Python 代码无缝衔接
* `mysql-connector-python`：MySQL 官方推出的纯 Python 连接 MySQ L的驱动，执行效率不如 pymysql

本文主要使用`pymysql`进行数据库的连接，在使用PyMySQL前，需要确保计算机上安装了PyMySQL

```bash
pip install pymysql
```

## PyMySQL连接MySQL数据库

### 创建连接

* MySQL 服务器启动后，提供了基于 TCP （传输控制协议）的网络服务。我们可以通过pymysql模块的connect函数连接 MySQL 服务器
* 在调用connect函数时，需要指定主机（host）、端口（port）、用户名（user）、口令（password）、数据库（database）、字符集（charset）等参数，该函数会返回一个Connection对象

```python
import pymysql

connection = pymysql.connect(
    host='localhost',    # 主机名
    user='username',     # 用户名
    password='password', # 密码
    database='database',  # 数据库名
    port=3306, # 端口
    charset='utf-8' #字符集
)
```

### 获取游标

* 连接 MySQL 服务器成功后，接下来要做的就是向数据库服务器发送 SQL 语句，MySQL 会执行接收到的 SQL 并将执行结果通过网络返回
* 要实现这项操作，需要先通过连接对象的cursor方法获取游标（Cursor）对象

```python
cur = db.cursor()
```

### 发出 SQL

通过游标对象的execute方法，我们可以向数据库发出 SQL 语句

```python
cur.execute("select version()")
```

* 如果执行 `insert` 、 `delete` 或 `update` 操作，需要根据实际情况提交或回滚事务。因为创建连接时，默认开启了事务环境，在操作完成后，需要使用连接对象的 `commit` 或 `rollback` 方法，实现事务的提交或回滚， `rollback` 方法通常会放在异常捕获代码块except中
* 如果执行 `select` 操作，需要通过游标对象抓取查询的结果，对应的方法有三个，分别是： `fetchone` 、 `fetchmany` 和 `fetchall` 
    * 其中 `fetchone` 方法会抓取到一条记录，并以元组或字典的方式返回
    *  `fetchmany` 和 `fetchall` 方法会抓取到多条记录，以嵌套元组或列表装字典的方式返回

### 关闭连接

在完成持久化操作后，请不要忘记关闭连接，释放外部资源。我们通常会在finally代码块中使用连接对象的close方法来关闭连接

```python
db.close()
```

## 常见的操作

### 连接数据库

```python
import pymysql

try:
    db = pymysql.connect(user="root", password="password",
                        host="localhost", port=3306, db='experiment',
                        autocommit=True)
    cur = db.cursor()
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败")
```

### 创建数据表

```python
def create_table(create_sql: str):
    """
    :param create_sql: the sql of the creating table:
    'CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    age INT);'
    :return:None
    """
    try:
        cur.execute(create_sql)
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("创建数据表成功")
```

### 插入数据

```python
def insert_data(insert_sql: str, data: list | tuple | dict):
    """
    :param insert_sql: th sql of the insert data:
    insert_sql = 'insert into users values (%s, %s, %s, %s)
    :param data:the data to be inserted
    :return:None
    """
    try:
        if isinstance(data, dict):
            cur.executemany(insert_sql, list(data.values()))
        else:
            cur.executemany(insert_sql, data)
    except pymysql.IntegrityError as e:
        print(f"插入数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("插入数据成功")
```

### 更新数据

```python
def update_data(update_sql: str):
    """
    :param update_sql: the sql of the update data:
    update_sql = 'update users SET name = %s, email = %s WHERE id = %s;'
    :return:None
    """
    try:
        cur.execute(update_sql)
    except pymysql.IntegrityError as e:
        print(f"更新数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("更新数据成功")
```

### 查询数据

```python
def select_data(select_sql: str):
    """
    :param select_sql: the sql of the select data:
    select_sql = 'select * from users'
    :return: None
    """
    try:
        cur.execute(select_sql)
        # result = cursor.fetchall()
        # 不建议用fetchall读取所有数据，如果数据量很大，占用的开销非常高
        row = cur.fetchone()
        while row:
            print(row)
            row = cur.fetchone()
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
```

### 删除数据

```python
def delete_data(delete_sql: str):
    """
    :param delete_sql: the sql of the delete data:
    delete_sql = 'delete from users'
    :return: None
    """
    try:
        cur.execute(delete_sql)
    except pymysql.IntegrityError as e:
        print(f"删除数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("删除数据成功")
```



