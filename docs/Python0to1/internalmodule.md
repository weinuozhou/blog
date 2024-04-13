# 内建模块

Python之所以自称batteries included，就是因为内置了许多非常有用的模块，无需额外安装和配置，即可直接使用

## `os`模块

`os`就是operating system的缩写，顾名思义，`os`模块提供的就是各种 Python 程序与操作系统进行交互的接口

> 不要使用`from os import *`来导入`os`模块；否则`os.open()`将会覆盖内置函数`open()`，从而造成预料之外的错误

### 常用功能

#### `os.name`

该属性宽泛地指明了当前 Python 运行所在的环境，实际上是导入的操作系统相关模块的名称。这个名称也决定了模块中哪些功能是可用的，哪些是没有相应实现的

* `posix`是Portable Operating System Interface of UNIX(可移植操作系统接口)的缩写
* `nt`全称应为Microsoft Windows NT
* `java`则是 Java 虚拟机环境下的返回值

<center><img alt="name" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402152101035.png" ></center>

#### `os.environ`

`os.environ`属性可以返回环境相关的信息，主要是各类环境变量。返回值是一个映射（类似字典类型），具体的值为第一次导入os模块时的快照；其中的各个键值对，键是环境变量名，值则是环境变量对应的值。在第一次导入os模块之后，除非直接修改os.environ的值，否则该属性的值不再发生变化

<center><img alt="environ" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402152103593.png"/></center>

#### `os.listdir()`

列出目录下的全部路径(及文件)。该函数存在一个参数，用以指定要列出子目录的=路径，默认为`·`，即当前路径

函数返回值是一个列表，其中各元素均为字符串，分别是各路径名和文件名

<center><img alt="listdir" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402152106842.png"/></center>

#### `os.mkdir()`和`os.makedirs()`

用处是新建一个路径。需要传入一个*类路径参数*用以指定新建路径的位置和名称，如果指定路径已存在，则会抛出`FileExistsError`异常

* `mkdir()`只能在已有的路径下新建一级路径，否则（即新建多级路径）会抛出`FileNotFoundError`异常
* `makedirs()`可以用于创建多级路径

<center><img alt="mkdir" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402171036841.png"/></center>

#### `os.chdir()`

`os.chdir()`的用处实际上是切换当前工作路径为指定路径。其中“指定路径”需要作为参数传入函数`os.chdir()`，该参数既可以是*文本或字节型字符串*，也可以是一个*文件描述符*，还可以是一个*广义的类路径(path-like)对象*

<center><img alt="chdir" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402171041059.png"/></center>

### `os.path`模块

其实这个模块是`os`模块根据系统类型从另一个模块导入的，并非直接由os模块实现

* 比如`os.name`值为nt，则在os模块中执行`import ntpath as path`
* 如果`os.name`值为posix，则执行`import posixpath as path`。

使用该模块要注意一个很重要的特性：`os.path`中的函数基本上是纯粹的字符串操作。换句话说，传入该模块函数的参数甚至不需要是一个有效路径，该模块也不会试图访问这个路径，而仅仅是按照“路径”的通用格式对字符串进行处理

#### `os.path.join()`

这将会根据你当前的操作系统（Windows、Linux、Mac等）使用适当的路径分隔符来合并给定的路径参数，生成一个有效的路径。在Windows中，路径分隔符为反斜杠（\），而在大多数其他操作系统中，路径分隔符为斜杠（/）。因此，`os.path.join('目录1', '目录2', '文件名')` 在不同操作系统下的效果会是这样：

* 在Windows系统下：`目录1\目录2\文件名`
* 在类Unix系统下（如Linux、Mac）：`目录1/目录2/文件名`

```python
import os

path = os.path.join('目录1', '目录2', '文件名')
```

#### `os.path.basename()`

`os.path.basename()`函数用于获取路径中的文件名部分

<center>
    <img alt="basename" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402171053655.png"/>
</center>

#### `os.path.dirname()`

`os.path.dirname()`函数用于获取路径中的目录部分

<center><img alt="dirname" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402171055677.png"/></center>

#### `os.path.exists()`

`os.path.exists()` 函数用于检查指定路径是否存在。如果路径存在，则返回 `True`，否则返回 `False`
<cemter><img alt="exists" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402171106734.png"/></center>

#### `os.path.isfile()` 和 `os.path.isdir()`

这两个函数分别判断传入路径是否是文件或路径，注意，此处会核验路径的有效性，如果是无效路径将会持续返回`False`

## `sys`模块

* sys 模块是与 Python 解释器交互的一个**接口**
* 该模块提供对解释器使用或维护的一些**变量**的访问和获取
* 它提供了许多函数和变量来处理 Python 运行时环境的不同部分

### 常用功能

#### `sys.argv`

* 实现从程序的外部向程序传递参数
* 返回的是一个列表, 第一个元素是*程序文件名*, 第二个元素是程*序外部传入的参数*

```python
import sys

print(f"The list of command line arguments:\n{sys.argv}")
```

<center>
    <img alt='202403031906567' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031906567.png'>
</center>

#### `sys.platform`

返回操作系统平台名称

<center>
    <img alt='202403031908958' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031908958.png'>
</center>

#### `sys.stdin`

Python 的**标准输入通道**.通过改变这个属性为其他的类文件（file-like）对象，可以实现输入的重定向，也就是说可以用其他内容替换标准输入的内容

```python
import sys

with open('./test.txt', 'r', encoding='utf-8') as f:
    sys.stdin = f
    try:
        while True:
            line = input()
            if not line:
                break
            print(f"Read from file: {line.strip()}")
    except EOFError as e:
        print("End of File reached")
    finally:
        sys.stdin = sys.__stdin__  # 恢复原始的标准输入
```

<center>
    <img alt='202403032046963' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403032046963.png'>
</center>

#### `sys.stdout`

sys.stdout则是代表**标准输出**的属性, 通过将这个属性的值修改为某个文件对象，可以将本来要打印到屏幕上的内容写入文件

```python
import sys

# 以附加模式打开文件，若不存在则新建
with open("count_log.txt", 'a', encoding='utf-8') as f:
    sys.stdout = f
    for i in range(10):
        print(f"count = {i}",)
```

<center>
    <img alt='202403032126775' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403032126775.png'>
</center>

## `time`模块

该模块提供各种与时间相关的功能

常用的方法:

* `time()` 当前时间（新纪元1970年1月1日到访问时的秒数，也叫时间戳）
* `localtime([secs])` 将时间戳转换为表示当地时间的元组
* `mktime(tuple)` 将时间元组转换为时间戳
* `sleep(sesc)` 休眠secs秒
* `strptime(string[, format])` 将字符串转换为时间元组
* `strftime(format[, t])` 将时间元组转换为字符串

```python
import time

print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
tup1 = time.localtime(1611331200)
str1 = time.strftime("%Y-%m-%d %H:%M:%S", tup1)
time.strptime(str1, "%Y-%m-%d %H:%M:%S")
```

<center><img alt="time" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402062106556.png"></center>

## `datetime`模块

datetime模块是Python中用于处理日期和时间的模块。它提供了各种类和函数，使得处理日期和时间变得简单而灵活

### 获取当前日期和时间

```python
from datetime import datetime

current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second
```

### 构造指定日期和时间

要指定某个日期和时间，我们直接用参数构造一个datetime

```python
from datetime import datetime

def create_date(year, month, day, hour, minute, second):
    return datetime(year, month, day, hour, minute, second)
```

### datetime转换为timestamp

在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为*epoch time*，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为*timestamp*

<img alt="timestamp" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402071521180.png"/>

把一个datetime类型转换为timestamp只需要简单调用`timestamp()`方法

> 注意Python的timestamp是一个*浮点数*，整数位表示秒

### timestamp转换为datetime

要把timestamp转换为datetime，使用datetime提供的`fromtimestamp()`方法

<center><img alt="fromtimestamp" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402071524555.png"/></center>

### str转换为datetime

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过`datetime.strptime()`实现，需要一个日期和时间的格式化字符串

<center><img alt="strftime" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402071529551.png"/></center>

### datetime转换为str

如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过`strftime()`实现的，同样需要一个日期和时间的格式化字符串

<center>
    <img alt="strftime" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402071531523.png"/>
</center>

|代码|含义|取值|
|:---:|:---:|:---:|
|`%a`|星期的缩写名称|Sun, Mon, …, Sat (en_US);|
|`%A`|星期的全称|Sunday, Monday, …, Saturday (en_US);|
|`%w`|工作日为十进制数，其中 0 代表星期天，6 代表星期六| 0, 1, …, 6|
|`%d`|日期的天数|01, 02, …, 31|
|`%b`|月份的缩写|Jan, Feb, …, Dec (en_US)|
|`%B`|月份的全称| January, February, …, December (en_US)|
|`%m`|以10进制数字展示月份| 01, 02, …, 12|
|`%y`|不含世纪的年份，以零填充的十进制数表示| 00, 01, …, 99|
|`%Y`|含世纪的年份|0001, 0002, …, 2013, 2014, …, 9998, 9999|
|`%H`|小时（24 小时制时钟）为零填充的十进制数| 00, 01, …, 23|
|`%I`|小时（12 小时制时钟）为零填充的十进制数| 01, 02, …, 12|
|`%p`|AM或者PM| AM, PM (en_US)|
|`%M`|分钟数| 00, 01, …, 59|
|`%S`|秒数|00, 01, …, 59|
|`%%`|%字符|%|

## `collections`模块

`collections` 模块是 Python 标准库中提供的一个模块，包含了一些额外的数据结构，比内置数据结构（如列表、元组、字典等）更加灵活和强大

### `namedtuple`

* 一个工厂函数，用来创建具有命名字段的元组子类
* `namedtuple`是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
* `namedtuple`可以很方便的定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 输出: 1 2
```

### `deque`

* 一个双向队列，支持在队列两端的快速插入和删除操作
* 为了高效实现插入和删除操作的双向列表，适合用于队列和栈
* deque除了实现list的append()和pop()外，还支持`appendleft()`和`popleft()`，这样就可以非常高效地往头部添加或删除元素

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # 在左侧插入元素
dq.append(4)      # 在右侧插入元素
print(dq)
# Output: deque([0, 1, 2, 3, 4])
```

### `defaultdict`

使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用`defaultdict`

```python
from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
print(d['b'])  # 输出: 0
```

### `OrderedDict`

一个有序字典，记住了元素的插入顺序

`OrderedDict`可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key:

```python
from collections import OrderedDict

class FIFODict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        if len(self) >= self.capacity:
            oldest_key = next(iter(self))  # 获取最早添加的键
            del self[oldest_key]            # 删除最早添加的键
        super().__setitem__(key, value)
```

### `Counter`

* 用于计数，可以统计可迭代对象中元素出现的次数
* Counter实际上也是dict的一个子类，上面的结果可以看出每个字符出现的次数

```python
from collections import Counter

data = [1, 2, 3, 1, 2, 1, 3, 4, 5, 4, 4]
counter = Counter(data)
print(counter)
# Output: Counter({1: 3, 2: 2, 3: 2, 4: 3, 5: 1})
```

## `argparse`模块

`argparse` 是 `Python` 标准库中用于解析命令行参数的模块，它提供了一个简单而灵活的方式来处理命令行参数，并生成帮助信息

### 创建 ArgumentParser 对象

`argparse.ArgumentParser` 是用于创建解析命令行参数的类，它有一些参数用于配置解析器的行为。以下是一些常用参数及其含义：

1. **prog**：程序的名称，默认是 `sys.argv[0]` 的基本文件名部分，用于在帮助信息中引用程序的名称。
2. **usage**：在生成帮助信息时显示的用法字符串，如果不指定，将自动生成。
3. **description**：在帮助信息的位置参数之前显示的程序描述。
4. **epilog**：在帮助信息的其他信息之后显示的文本。
5. **prefix_chars**：用于指定可选参数前缀的字符集，默认是 `'-'`。
6. **formatter_class**：用于指定帮助输出格式的类，默认是 `argparse.HelpFormatter`。
7. **add_help**：是否添加 `-h` 和 `--help` 选项以显示帮助信息，默认是 `True`。
8. **argument_default**：用于指定参数的默认值，默认是 `None`。
9. **parents**：一个 `ArgumentParser` 对象的列表，子解析器将从这些对象中继承参数。
10. **conflict_handler**：用于解决参数冲突的策略，可以是 `'error'`、`'resolve'`、`'ignore'` 中的一个，默认是 `'error'`。
11. **prefix_chars**：用于指定可选参数的前缀字符，默认是 `'-'`。
12. **fromfile_prefix_chars**：用于指定参数值从文件中读取的前缀字符，默认是 `None`，表示禁用从文件中读取参数值。
13. **argument_default**：指定参数的默认值，默认是 `None`。
14. **allow_abbrev**：指定是否允许缩写参数，默认是 `True`。

```python
import argparse

parser = argparse.ArgumentParser(
        prog='backup', # 程序名
        description='Backup MySQL database.', # 描述
        epilog='Copyright(r), 2023' # 说明信息
    )
```

### 添加命令行参数

`parser.add_argument` 是用于向 `ArgumentParser` 对象添加命令行参数的方法，它也有一些参数用于配置参数的行为。以下是一些常用参数及其含义：

1. **name or flags**：参数的名称或标志，可以是位置参数或可选参数的名称，也可以是选项的标志（例如 `-f` 或 `--foo`）。位置参数使用名称，可选参数使用标志。
2. **action**：参数的动作，指定参数应该如何处理。常见的动作包括：
   * `'store'`：保存参数值（默认动作）
   * `'store_const'`：保存指定的常量值
   * `'store_true'`：如果指定了参数，则将其设置为 `True`
   * `'store_false'`：如果指定了参数，则将其设置为 `False`
   * `'append'`：将参数值追加到列表中
   * `'append_const'`：将指定的常量值追加到列表中
   * `'count'`：计算参数出现的次数，并将其存储为整数
   * `'help'`：显示帮助信息并退出
3. **type**：参数的类型，用于将参数值转换为指定的类型。常见的类型包括 `int`、`float`、`str` 等。
4. **choices**：参数值的可选值列表，指定参数值只能取列表中的值。
5. **default**：参数的默认值，如果未提供参数，则使用此值。
6. **required**：指定参数是否为必需的，如果设置为 `True`，则必须在命令行中提供该参数。
7. **help**：参数的帮助信息，用于生成帮助文档。
8. **metavar**：参数的名称在帮助信息中显示的名称。
9. **nargs**：指定参数应该获取的命令行参数的数量，可以是以下值之一：
   * `N`：获取 N 个参数
   * `'?'`：0 或 1 个参数
   * `'*'`：0 或多个参数
   * `'+'`：1 或多个参数
10. **const**：`'store_const'` 动作的常量值。
11. **dest**：参数的名称，用于存储参数值的属性名称，默认是参数的名称或第一个标志的名称。

#### 添加位置参数

```python
parser.add_argument('name', help='Name of the user')
```

#### 添加关键字参数

```python
parser.add_argument('--age', help='Age of the user')
```

#### 设置参数的类型

```python
parser.add_argument('--age', type=int, help='Age of the user')
```

#### 设置参数的默认值

```python
parser.add_argument('--age', type=int, default=18, help='Age of the user')
```

#### 允许输入简写的参数

```python
parser.add_argument('-u', '--user', required=True)
```

#### 设置参数的可选择性

```python
parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')
```

### 解析参数

```python
args = parser.parse_args()
```

我们不必捕获异常，`parse_args()`非常方便的一点在于，如果参数有问题，则它打印出错误信息后，结束进程；如果参数是-h，则它打印帮助信息后，结束进程。只有当参数全部有效时，才会返回一个NameSpace对象，获取对应的参数就把参数名当作属性获取，非常方便

### 实例分析

假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：

* `host`参数：表示MySQL主机名或IP，不输入则默认为localhost；
* `port`参数：表示MySQL的端口号，int类型，不输入则默认为3306；
* `user`参数：表示登录MySQL的用户名，必须输入；
* `password`参数：表示登录MySQL的口令，必须输入；
* `gz`参数：表示是否压缩备份文件，不输入则默认为False；
* `outfile`参数：表示备份文件保存在哪，必须输入

其中，outfile是位置参数，而其他则是类似--user root这样的关键字参数

```python
import argparse

parser = argparse.ArgumentParser(
  prog='backup', # 程序名
  description='Backup MySQL database.', # 描述
  epilog='Copyright(r), 2023' # 说明信息
)
# 定义位置参数:
parser.add_argument('outfile')
# 定义关键字参数:
parser.add_argument('--host', default='localhost')
# 此参数必须为int类型:
parser.add_argument('--port', default='3306', type=int)
# 允许用户输入简写的-u:
parser.add_argument('-u', '--user', required=True)
parser.add_argument('-p', '--password', required=True)
parser.add_argument('--database', required=True)
# gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')


# 解析参数:
args = parser.parse_args()

# 打印参数:
print('parsed args:')
print(f'outfile = {args.outfile}')
print(f'host = {args.host}')
print(f'port = {args.port}')
print(f'user = {args.user}')
print(f'password = {args.password}')
print(f'database = {args.database}')
print(f'gzcompress = {args.gzcompress}')
```

## `itertools`模块

`itertools` 是 Python 标准库中的一个模块，提供了用于创建迭代器的工具函数。这些函数可以用于快速、高效地处理和操作迭代器和可迭代对象

### `count(start=0, step=1)`

这个函数返回一个**无限迭代器**，从 `start` 开始，步长为 `step`。如果不指定参数，默认从0开始，步长为1

<center><img alt='202403031722177' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031722177.png'></center>

### `cycle(iterable)`

**无限地重复**迭代一个可迭代对象

<center><img alt='202403031724239' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031724239.png'></center>

### `repeat(elem, n=None)`

重复一个元素 n 次，或者无限地重复，默认*无限重复*

<center><img alt='202403031727611' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031727611.png'></center>

### `accumulate(iterable, func=operator.add)`

返回产生对指定可迭代对象进行*累积操作*后的**迭代器**

* `iterable`：要进行累积操作的可迭代对象。
* `func`（可选）：指定用于执行累积操作的函数。如果未提供，则默认执行求和操作

<center><img alt='202403031733888' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031733888.png'></center>

### `chain(*iterables)`

将多个可迭代对象连接起来，形成一个单一的迭代器

<center><img alt='202403031734038' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031734038.png'></center>

### `takewhile(predicate, iterable)`

用于创建一个迭代器，该迭代器在给定的条件为真时从可迭代对象中返回元素

* `predicate`：一个函数，用于定义条件。该函数接受一个参数，表示可迭代对象的每个元素，返回一个布尔值，当返回值为真时，takewhile 函数会继续返回元素，当返回值为假时，停止返回元素
* `iterable`：要从中取元素的可迭代对象

<center>
<img alt='202403031741961' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031741961.png'>
</center>

### `zip_longest(*iterables, fillvalue=None)`

类似于 `zip()`，但是当迭代器长度不同时，使用 fillvalue 进行填充

* `*iterables`：要进行配对的多个可迭代对象
* `fillvalue`（可选）：指定用于填充短可迭代对象的值，默认为 None

<center><img alt='202403031743258' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031743258.png'></center>

### `product(*iterables)`

`itertools.product()`: 计算多个可迭代对象的**笛卡尔积**

<dl style="background-color: #FFCDD2">
    <dt style="font-style: normal">笛卡尔积</dt>
    <dd>用于组合两个或多个集合的所有可能组合</dd>
</dl>

<center>
    <img alt='202403031836697' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031836697.png'>
</center>

### `permutations(iterable, c=None)`

用于计算**指定可迭代对象的所有排列**,它返回一个*迭代器*，产生可迭代对象的所有可能的 r 元组排列

* `iterable`：要生成排列的可迭代对象
* `r`（可选）：指定要生成的排列的长度。如果未指定，或者为 None，则会生成与可迭代对象长度相同的所有可能排列

<center>
    <img alt='202403031845991' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403031845991.png'>
</center>
