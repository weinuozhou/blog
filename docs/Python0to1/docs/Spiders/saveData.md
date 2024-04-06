# 存储数据

## 文件存储

文件存储形式多种多样，比如可以保存成 TXT 纯文本形式，也可以保存为 JSON 格式、CSV 格式等，本节就来了解一下文本文件的存储方式

### txt、HTML文件存储

* 将数据保存到 TXT 文本的操作非常简单，而且 TXT 文本几乎兼容任何平台，但是这有个缺点，那就是**不利于检索**
* 将数据保存到 HTML 文本的操作同样简单， 便于调试解析响应

```python
open(file, mode， encoding, newline, errors)
```

* `file`：需要打开的文件路径
* `mode`(可选): 打开文件的模式，如只读、追加、写入等
  * r：表示文件只能读取
  * w：表示文件只能写入
  * a：表示打开文件，在原有内容的基础上追加内容，在末尾写入
  * w+:表示可以对文件进行读写双重操作
  * b: 表示以二进制的形式读写文件
* `encoding`(可选): 指定文件的字符编码，如 utf-8、gbk 等
* `newline`: 控制换行行为, 默认为None
* `errors`: 解码错误处理方案, 默认为None

### CSV文件存储

csv是"Comma-Separated Values（逗号分割的值）"的首字母缩写，它其实和txt文件一样，都是纯文本文件。但csv文件可以显示为电子表格的样式，所以我们也可以把csv文件视为一种简化版的电子表格

使用Python来读写csv文件是非常容易的，因为实现csv的读取和写入功能的csv模块，是一个内置模块，我们可以直接使用, 使用csv模块时，需要先导入它，即在代码一开始写入`import csv`

#### CSV文件的读取

##### `reader()`函数

reader()函数是csv模块内的一个函数，当使用open()打开csv文件，得到文件对象后，可以把这个文件对象传入reader()函数

```python
import csv

# 必须指定 newline='', 避免不必要的空行
with open('./reader_demo.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

##### `DictReader` 类

DictReader 类的操作类似于常规的 reader() ，但 DictReader 会将读取到的信息转换为**字典形式**

<div style="text-align: center;">     <img alt='202403201503013' src='https://cdn.jsdelivr.net/gh/weno861/image/202403201503013.png' width=600px> </div>

#### CSV文件的写入

与读取功能类似，csv模块也为我们准备了两种写入方式——函数writer()与类DictWriter

##### writer()函数

要将内容写入csv文件，需要先把open()返回的文件对象转化为writer对象， 然后需要调用writer对象的方法writerow(row)，该方法会将参数row当作一行内容写入csv文件中， 参数row代表了你想要写入csv文件的内容，它必须是一个**可迭代对象**，这里推荐使用列表

```python
import csv

with open('./writer_demo.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])
```

##### DictWriter类

DictWriter的操作类似于常规的writer()，但DictWriter会将**字典**写入（映射）到csv文件的行中

<div style="text-align: center;">     <img alt='202403201525798' src='https://cdn.jsdelivr.net/gh/weno861/image/202403201525798.png' width=500px> </div>

### json文件存储

* JSON是一种**轻量级的数据交换格式**，由字符串化的键值对构成
* JSON是JavaScript的子集，但也是独立于编程语言的数据格式
* JSON支持的数据类型如下:

|  对象  | {}括起来的无序键值对，键必须是字符串 |
| :----: | :----------------------------------- |
|  数值  | 十进制数据                           |
| 字符串 | ""括起来的字符，必须是双引号         |
| 布尔值 | true或false                          |
|  数组  | []括起来的多个值                     |
|   空   | null                                 |

python可以使用json模块来操作json文件,json模块主要有四个比较重要的函数，分别是：

* `dump` - 将Python对象按照JSON格式序列化到文件中
* `dumps` - 将Python对象处理成JSON格式的字符串
* `load` - 将文件中的JSON数据反序列化成对象
* `loads` - 将字符串的内容反序列化成Python对象

#### 写入json文件

```python
import json

def write_to_json(filename, data):
  with open('data.json', 'a', encoding='utf-8') as f:
      f.write(json.dump(data, indent=4, ensure_ascii=False))
# json.dumps:将字符串对象转换为json对象
# indent表示缩进的字符数，ensure_ascii=False确保中文不乱码
```

### `Excel` 文件存储

`openpyxl`的安装

```bash
pip install openpyxl
```

`openpyxl`的基本用法

```python
import openpyxl
wb = openpyxl.Workbook() # 创建一个工作表
ws = wb.active # 将工作表作为工作目录
ws.append(data) # 插入数据
ws.save('test.xlsx') # 保存文件
```

## 数据库存储

大部分程序都需要保存数据，所以不可避免要使用数据库。用来操作数据库的数据库管理系统（DBMS）有很多选择，对于不同类型的程序，不同的使用场景，都会有不同的选择

### `MySQL`数据库存储

想要操作`MySQL` 数据库，必须要先安装 `Python` 操作 `MySQL` 的驱动。在Python中，目前存在以下的`MySQL`驱动

* `MySQL-python`:只支持 Python2
* `mysqlclient`: 是 MySQL-python 的另外一个分支，支持Python3并修复了一些 bug , 是目前执行效率最高的驱动， 但是安装时容易因为环境问题出错
* `pymysql`: 纯 Python 实现的驱动，执行效率不如`mysqlclient`，但是可以与 Python 代码无缝衔接
* `mysql-connector-python`：MySQL 官方推出的纯 Python 连接 MySQ L的驱动，执行效率不如 pymysql

本文主要介绍 `PyMySQL` 这个驱动

#### 安装

```bash
pip install PyMySQL
```

#### 创建数据库连接

```python
import pymysql

connection = pymysql.connect(host='localhost',
                             port=3306, 
                             user='root',
                             password='root',
                             database='demo', 
                             autocommit=True,
                             charset='utf8')
```

| 参数               | 描述                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| host               | 数据库服务器地址，默认 localhost                                                                                                                                                                                                                                                                                                                                                     |
| user               | 用户名，默认为当前程序运行用户                                                                                                                                                                                                                                                                                                                                                       |
| password           | 登录密码，默认为空字符串                                                                                                                                                                                                                                                                                                                                                             |
| database           | 默认操作的数据库                                                                                                                                                                                                                                                                                                                                                                     |
| port               | 数据库端口，默认为 3306                                                                                                                                                                                                                                                                                                                                                              |
| bind_address       | 当客户端有多个网络接口时，指定连接到主机的接口。参数可以是主机名或IP地址。                                                                                                                                                                                                                                                                                                           |
| unix_socket        | unix 套接字地址，区别于 host 连接                                                                                                                                                                                                                                                                                                                                                    |
| read_timeout       | 读取数据超时时间，单位秒，默认无限制                                                                                                                                                                                                                                                                                                                                                 |
| write_timeout      | 写入数据超时时间，单位秒，默认无限制                                                                                                                                                                                                                                                                                                                                                 |
| charset            | 数据库编码                                                                                                                                                                                                                                                                                                                                                                           |
| sql_mode           | 指定默认的 SQL_MODE                                                                                                                                                                                                                                                                                                                                                                  |
| read_default_file  | Specifies my.cnf file to read these parameters from under the [client] section.                                                                                                                                                                                                                                                                                                      |
| conv               | Conversion dictionary to use instead of the default one. This is used to provide custom marshalling and unmarshaling of types.                                                                                                                                                                                                                                                       |
| use_unicode        | Whether or not to default to unicode strings. This option defaults to true for Py3k.                                                                                                                                                                                                                                                                                                 |
| client_flag        | Custom flags to send to MySQL. Find potential values in constants.CLIENT.                                                                                                                                                                                                                                                                                                            |
| cursorclass        | 设置默认的游标类型                                                                                                                                                                                                                                                                                                                                                                   |
| init_command       | 当连接建立完成之后执行的初始化 SQL 语句                                                                                                                                                                                                                                                                                                                                              |
| connect_timeout    | 连接超时时间，默认 10，最小 1，最大 31536000                                                                                                                                                                                                                                                                                                                                         |
| ssl                | A dict of arguments similar to mysql_ssl_set()’s parameters. For now the capath and cipher arguments are not supported.                                                                                                                                                                                                                                                              |
| read_default_group | Group to read from in the configuration file.                                                                                                                                                                                                                                                                                                                                        |
| compress           | Not supported                                                                                                                                                                                                                                                                                                                                                                        |
| named_pipe         | Not supported                                                                                                                                                                                                                                                                                                                                                                        |
| autocommit         | 是否自动提交，默认不自动提交，参数值为 None 表示以服务器为准                                                                                                                                                                                                                                                                                                                         |
| local_infile       | Boolean to enable the use of LOAD DATA LOCAL command. (default: False)                                                                                                                                                                                                                                                                                                               |
| max_allowed_packet | 发送给服务器的最大数据量，默认为 16MB                                                                                                                                                                                                                                                                                                                                                |
| defer_connect      | 是否惰性连接，默认为立即连接                                                                                                                                                                                                                                                                                                                                                         |
| auth_plugin_map    | A dict of plugin names to a class that processes that plugin. The class will take the Connection object as the argument to the constructor. The class needs an authenticate method taking an authentication packet as an argument. For the dialog plugin, a prompt(echo, prompt) method can be used (if no authenticate method) for returning a string from the user. (experimental) |
| server_public_key  | SHA256 authenticaiton plugin public key value. (default: None)                                                                                                                                                                                                                                                                                                                       |
| db                 | 参数 database 的别名                                                                                                                                                                                                                                                                                                                                                                 |
| passwd             | 参数 password 的别名                                                                                                                                                                                                                                                                                                                                                                 |
| binary_prefix      | Add _binary prefix on bytes and bytearray. (default: False)                                                                                                                                                                                                                                                                                                                          |

#### 执行 `SQL` 语句

```python
try:
    with connection.cursor() as cursor:
        cursor.execute(sql, args)

finally:
    connection.close()
```

#### 查询数据

```python
def select_data(cursor, sql):
    cursor.execute(sql)
    # result = cursor.fetchall()
    # 不建议用fetchall读取所有数据，如果数据量很大，占用的开销非常高
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
```

### `MongoDB`数据库存储



### `Redis`数据库存储

## 图片、音频、视频存储

* 图片、音频、视频都是以**二进制**的形式存储的
* 图片、音频、视频的存储方式：
```python
with open('filename', 'wb') as f:
    f.write(requests.get(url).content)
```



