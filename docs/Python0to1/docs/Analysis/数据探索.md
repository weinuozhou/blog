# 数据探索

## 数据的定义

数据是*对象(objects)* 和 *它们属性(attributes)* 的集合

![](https://cdn.jsdelivr.net/gh/weno861/image/img/202402171358389.svg)

* 对象:属性的集合
  * 通常也被称为*记录（record）*、*点（point）*、*样本（sample）*、*实例（instance）*、*案例（case）*、*实体（entity）* 
* 属性:对象的特性（characteristic）或性质（property）
  * 通常也被称作*变量（variable）*、*字段（field）*、*维度（dimension）*、*特征（feature）*

## 属性的类型

* 属性的类型取决于该属性的数值具备下列哪些性质
  * **相异性**（distinctness）：$=$ 和 $\ne$
  *  **序**（order）：$\lt$，$\le$，$\gt$ 和 $\ge$
  *  **有意义的差**（meaningful differences）：$+$ 和 $-$
  *  **有意义的比率**（meaningful ratios）：$\times$ 和 $/$
  
| 属性类型         | 特点                 | 包含的性质                           | 示例             | 适合的统计量                       |
| ---| ---| ---| ----| ---|
| 标称（nominal）  | 仅仅是名称           | 相异性                               | 名字、班级、颜色 | 众数                               |
| 序数（ordinal）  | 具有自然排序         | 相异性、序                           | 年级、等级       | 众数、中位数                       |
| 区间（interval） | 没有绝对零点、等间隔 | 相异性、序、有意义的差               | 温度、日期、IQ   | 众数、中位数、均值、方差           |
| 比率（ratio）    | 有绝对零点           | 相异性、序、有意义的差、有意义的比率 | 距离、重量、收入 | 众数、中位数、均值、方差、几何均值 |

例如:

| ID   | 工作状况 | 教育水平 | 居住年限 | 信用状况 |
| --- | --- | --- | --- | --- |
| 1    | 就业     | 研究生   | 5        | 好       |
| 2    | 就业     | 高中     | 2        | 差       |
| 3    | 失业     | 本科生   | 1        | 差       |
| 4    | 就业     | 高中     | 10       | 好       |

* ID: 标称
* 工作状况：标称
* 教育水平：序数
* 居住年限：比率
* 信用状况：序数

## 数据获取

### 从文本文件中获取数据

数据分析的首要任务就是*读取数据*

读取不同类型的数据|格式
|:---:|:---|
读取csv,txt,json文件| `pd.read_csv()`
读取excel文件| `pd.read_excel()`
读取mysql 数据文件| `pd.read_sql()`

#### 读取`csv`文件

```python
import pandas as pd

pd.read_csv(filepath, sep='', header=None, names=list)
```

pd.read_csv的各个参数如下:

参数|说明
:---|:---
`filepath_or_buffer`|文件的路径
`sep`|分隔符的类型，默认是逗号
`header`|指定以哪一行作为列名，默认是0，可以是行号或者None
`names`|指定列名(列表)，如果`header=None`，则必须指定

#### 读取`json`文件

* 一种轻量级的数据格式，便于人的阅读和书写，也便于计算机的解析和生成
* name/value pairs的集合，即`Python`中的字典（dictionary）类型

```json
{
    "name": "John Smith",
    "studentID": "stu001",
    "age": 20,
    "class": "管理2019",
    "courses": ["管理学","经济学","数据分析"],
    "graduated": False
}
```

```python
import json
json.load(fp)
```

- `fp`：用`open()`方法打开的包含`json`格式的文本对象
- 返回一个`Python`对象

### 从数据库获取数据

接口包：`PyMySQL`

#### 连接数据库

```python
user, password, host, port, dbname = 'root', 'password', 'localhost', 3306, 'experiment'
connection = pymysql.connect(user=user, password=password, host=host,
                            port=port, db=dbname, autocommit=True)
```

#### 创建游标

```python
cursor = connection.cursor()
```

#### 创建表

```python
def create_table(create_sql: str):
    """
    :param create_sql: the sql of the creating table:
    CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    age INT);
    :return:None
    """
    try:
        cursor.execute(create_sql)
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("创建数据表成功")

create_sql = 'CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY,username VARCHAR(50),email VARCHAR(100),age INT);'
create_table(create_sql)
```

#### 插入数据

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
            cursor.executemany(insert_sql, list(data.values()))
        else:
            cursor.executemany(insert_sql, data)
    except pymysql.IntegrityError as e:
        print(f"插入数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("插入数据成功")

insert_sql = r'insert into users values(%s, %s, %s, %s)'
data = ((1, "weno", "weno@qq.com", 20), )
insert_data(insert_sql, data)
```

#### 更新数据

```python
def update_data(update_sql: str):
    """
    :param update_sql: the sql of the update data:
    update_sql = 'update users SET name = %s, email = %s WHERE id = %s;'
    :return:None
    """
    try:
        cursor.execute(update_sql)
    except pymysql.IntegrityError as e:
        print(f"更新数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("更新数据成功")

update_sql = 'update users set username="we" where 1=1'
update_data(update_sql)
```

#### 查询数据

```python
def select_data(select_sql: str):
    """
    :param select_sql: the sql of the select data:
    select_sql = 'select * from users'
    :return: None
    """
    try:
        cursor.execute(select_sql)
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")

select_sql = "select * from users"
select_data(select_sql)
```

#### 删除数据

```python
def delete_data(delete_sql: str):
    """
    :param delete_sql: the sql of the delete data:
    delete_sql = 'delete from users'
    :return: None
    """
    try:
        cursor.execute(delete_sql)
    except pymysql.IntegrityError as e:
        print(f"删除数据失败:{e}")
    except pymysql.ProgrammingError as e:
        print(f"SQL语句发生错误:{e}")
    else:
        print("删除数据成功")

delete_sql = r'delete from users'
delete_data(delete_sql)
```

#### 读取`sql`文件

```python
pd.read_sql(sql,con,index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)
```

参数|说明
:---|:---|
sql|SQL命令字符串
con|连接sql数据库的engine，一般可以用SQLalchemy或者pymysql之类的包建立
index_col| 选择某一列作为index
coerce_float|非常有用，将数字形式的字符串直接以float型读入
parse_dates|将某一列日期型字符串转换为datetime型数据，与pd.to_datetime函数功能类似。可以直接提供需要转换的列名以默认的日期形式转换，也可以用字典的格式提供列名和转换的日期格式，比如{column_name: format string}（format string："%Y:%m:%H:%M:%S"）。
columns|要选取的列。一般没啥用，因为在sql命令里面一般就指定要选择的列了
chunksize|如果提供了一个整数值，那么就会返回一generator，每次输出的行数就是提供的值的大小。

### 从互联网上获取数据

?> 爬虫
> 即网络爬虫，是一种按照一定的规则，自动的抓取互联网信息的程序或者脚本

?> 静态网页
> 纯粹HTML格式的网页，文件扩展名是.htm、.html。没有后台数据库、不可交互的网页
> 
?> 动态网页
> 基本的HTML语法规范与高级程序设计语言、数据库编程等多种技术的融合，以期实现对网站内容和风格的高效、动态和交互式的管理







