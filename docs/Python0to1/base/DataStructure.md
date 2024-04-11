# 序列类型

除了字符串，Python还内置了多种类型的数据结构，如果要在程序中保存和操作数据，绝大多数时候可以利用现有的数据结构来实现，最常用的包括列表、元组、集合和字典

## 通用序列操作

大多数序列类型，包括可变类型和不可变类型都支持下表中的操作

此表按优先级升序列出了序列操作。 在表格中，*s* 和 *t* 是具有相同类型的序列，*n*, *i*, *j* 和 *k* 是整数而 *x* 是任何满足 *s* 所规定的类型和值限制的任意对象

|          运算          |结果|
| :---: | :---: |
|        `x in s`        |  如果 *s* 中的某项等于 *x* 则结果为 `True`，否则为 `False`   |
|      `x not in s`      |  如果 *s* 中的某项等于 *x* 则结果为 `False`，否则为 `True`   |
|        `s + t`         |                      *s* 与 *t* 相拼接                       |
|   `s * n` 或 `n * s`   |               相当于 *s* 与自身进行 *n* 次拼接               |
|         `s[i]`         |                  *s* 的第 *i* 项，起始为 0                   |
|        `s[i:j]`        |                   *s* 从 *i* 到 *j* 的切片                   |
|       `s[i:j:k]`       |             *s* 从 *i* 到 *j* 步长为 *k* 的切片              |
|        `len(s)`        |                          *s* 的长度                          |
|        `min(s)`        |                         *s* 的最小项                         |
|        `max(s)`        |                         *s* 的最大项                         |
| `s.index(x[, i[, j]])` | *x* 在 *s* 中首次出现项的索引号（索引号在 *i* 或其后且在 *j* 之前） |
|      `s.count(x)`      |                  *x* 在 *s* 中出现的总次数                   |

### 不可变序列类型

不可变序列类型普遍实现而可变序列类型未实现的唯一操作就是对 [`hash()`](https://docs.python.org/zh-cn/3/library/functions.html#hash) 内置函数的支持

这种支持允许不可变类型，例如 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 实例被用作 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 键，以及存储在 [`set`](https://docs.python.org/zh-cn/3/library/stdtypes.html#set) 和 [`frozenset`](https://docs.python.org/zh-cn/3/library/stdtypes.html#frozenset) 实例中

!> 尝试对包含有不可哈希值的不可变序列进行哈希运算将会导致 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)

常见的不可变序列类型有:
* 字符串（`string`）：字符串是由字符组成的不可变序列。一旦创建，字符串的内容就无法更改
* 元组（`tuple`）：元组是由多个元素组成的不可变序列。一旦创建，元组的元素和长度都不可变
* 字节串（`bytes`）：字节串是一种不可变的字节序列，常用于处理二进制数据
* 不可变集合（`frozenset`）：不可变集合是一种不可变的集合类型，其中包含不可变的唯一元素

### 可变序列类型

可变序列类型在 `Python` 中指的是序列的元素可以被修改

常见的可变序列类型有:
* 列表（`list`）：列表是由多个元素组成的可变序列。列表可以通过添加、删除或修改元素来动态改变
* 字节数组（`bytearray`）：字节数组是一种可变的字节序列，类似于字节串（bytes），但可以修改

## 使用列表

列表是可变序列，通常用于存放同类项目的集合（其中精确的相似程度将根据应用而变化）

### 创建列表

* 使用一对方括号来表示空列表: `[]`
* 使用方括号，其中的项以逗号分隔: `[a]`, `[a, b, c]`
* 使用列表推导式: `[x for x in iterable]`
* 使用类型的构造器: `list()` 或 `list(iterable)`

> 构造器将构造一个列表，其中的项与 *iterable* 中的项具有相同的的值与顺序。 *iterable* 可以是序列、支持迭代的容器或其它可迭代对象。 如果 *iterable* 已经是一个列表，将创建并返回其副本，类似于 `iterable[:]`
> 例如，`list('abc')` 返回 `['a', 'b', 'c']` 而 `list( (1, 2, 3) )` 返回 `[1, 2, 3]`。 如果没有给出参数，构造器将创建一个空列表 `[]`

### 列表常用的方法

<div style="text-align:center">
    <img src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402061444113.png" width=60%>
</div>

#### append

1. `append` 方法接受一个参数，即要添**加到列表末尾**的元素。
2. `append` 方法会**修改原始列表**，而不是创建一个新的列表。
3. 如果你想一次性添加多个元素，可以考虑使用 `extend` 方法，它接受一个可迭代对象，并将其元素逐一添加到列表中

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061445797.png'>
</div>

#### extend

1. `extend` 方法接受**一个可迭代对象**作为参数，如列表、元组、字符串等。
2. `extend` 方法会修改原始列表，而不是创建一个新的列表

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061446052.png'>
</div>

#### insert

1. 如果指定的索引超出了列表的范围，`insert` 方法会在列表的末尾添加新元素。
2. 负数索引表示从列表末尾开始计数，例如，`my_list.insert(-1, 7)` 将在列表倒数第一个位置插入元素 7
3. `insert` 方法会修改原始列表，而不是创建一个新的列表


<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061445163.png'>
</div>

#### remove

1. 如果列表中没有匹配的元素，`remove` 方法会引发 `ValueError`。因此，在调用 `remove` 之前，最好使用 `in` 运算符检查元素是否存在于列表中
2. 如果有多个相同的元素，只会**移除第一个匹配**的元素


<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061447140.png'>
</div>

#### pop

1. 如果不提供索引，`pop` 将默认移除并返回列表中的最后一个元素
2. 如果指定的索引超出了列表的范围，`pop` 方法会引发 `IndexError`


<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061447303.png'>
</div>

#### index

```python
index(value, start=0, end=len(list)) # value 是要查找的元素的值，start 和 end 是可选参数，表示查找的范围
```

1. 如果列表中没有匹配的元素，`index` 方法会引发 `ValueError`。因此，在调用 `index` 之前，最好使用 `in` 运算符检查元素是否存在于列表中
2. 可以使用 `start` 和 `end` 参数指定查找范围，其中 `start` 表示起始索引，`end` 表示结束索引（不包含在内）
3. `index` 方法只**返回第一个匹配元素的索引**。如果需要查找所有匹配元素的索引，可以使用循环结构或列表推导式

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061447842.png'>
</div>

#### count

1. 如果列表中没有匹配的元素，`count` 方法返回
2. `count` 方法只统计指定值的出现次数，不考虑值的索引

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061448782.png'>
</div>

#### sort

```python
sort(key=None, reverse=False)
```

* `key` 是可选参数，用于指定一个自定义排序函数
* `reverse` 是可选参数，如果设置为 `True`，则是降序, 默认是升序排序

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061449242.png'>
</div>

#### reverse

1. `reverse` 方法用于反转列表中的元素顺序
2. 更推荐的方法是使用切片:`[::-1]`

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061451491.png'>
</div>

#### clear

1. `clear`方法用于清空列表中所有元素

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061451720.png'>
</div>

#### len、min、max、sum

* `len`:返回列表中元素的个数

* `min`:返回列表中的最小值
* `max`:返回列表中的最大值
* `sum`：返回列表中所有元素的和（要求元素是可加的）

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061452526.png'>
</div>

## 使用元组

元组（tuple）是一种**有序**、**不可变**的数据类型。它是由一系列用逗号分隔的值组成，通常用圆括号括起来。元组与列表（list）相似，但元组的主要区别在于元组是不可变的，一旦创建后，不能修改其内容

### 创建元组

* 使用一对圆括号来表示空元组: `()`
* 使用一个后缀的逗号来表示单元组: `a,` 或 `(a,)`
* 使用以逗号分隔的多个项: `a, b, c` or `(a, b, c)`
* 使用内置的 [`tuple()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple): `tuple()` 或 `tuple(iterable)`

> *iterable* 可以是序列、支持迭代的容器或其他可迭代对象。 如果 *iterable* 已经是一个元组，会不加改变地将其返回。 例如，`tuple('abc')` 返回 `('a', 'b', 'c')` 而 `tuple( [1, 2, 3] )` 返回 `(1, 2, 3)`。 如果没有给出参数，构造器将创建一个空元组 `()`

元组实现了通用序列类型的全部操作，具体可见上文

## 使用range对象

* [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 类型相比常规 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list) 或 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 的优势在于一个 [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 对象总是占用固定数量的（较小）内存，不论其所表示的范围有多大（因为它只保存了 `start`, `stop` 和 `step` 值，并会根据需要计算具体单项或子范围的值）
* [`range`](https://docs.python.org/zh-cn/3/library/stdtypes.html#range) 类型表示不可变的数字序列，通常用于在 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中循环指定的次数

```python
range(start=0, end, step=1) # range() 函数生成的序列包含起始值，但不包含结束值。这是因为 Python 的索引和切片习惯是左闭右开的
```

* `start`：序列的起始值（可选，默认为0）。
* `stop`：序列的结束值（必须指定）。
* `step`：序列值之间的步长（可选，默认为1）

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061453254.png'>
</div>

## 使用集合

集合是一种无序、可变的数据类型，用于存储不重复的元素。Python提供了两种主要的集合类型：`set` 和 `frozenset`


<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061453792.png' width=60%>
</div>

## 使用字典

Python中的字典（Dictionary）是一种无序的数据结构，用于存储键值对。字典是由一系列键（keys）和相应的值（values）组成的，每个键与其对应的值之间用冒号分隔，而不同键值对之间用逗号分隔。字典通常用花括号 `{}` 来表示

**python字典为什么是无序的?**

> Python字典的内部实现使用哈希表(hash table)来存储键值对，这样可以快速查找和访问元素。哈希表是一种数据结构，它使用哈希函数将键映射到存储桶（buckets）中的索引，以实现快速的查找。由于哈希函数的性质，相同的键始终映射到相同的索引，从而保证了快速的查找速度。然而，哈希表并不关心元素的顺序。因此，当你遍历字典时，键值对的顺序并不是按照它们被插入的顺序来的，而是由哈希函数的结果决定的

### 字典的创建

创建字典的基本方法是使用花括号`{}`，在其中放置以逗号分隔的键值对。例如：

```python
{"name": "smith white", "age": 22, "salary": 1000}
```

此外，也可以使用`dict()`函数来创建字典。例如：

```python
dict(name="smith white", age=22, salary=1000)
dict([("name", "smith white"), ("age", 22), ("salary", 1000)])
```

**dict和{}的区别?**

> 使用 timeit 模块，可以测试出在运行效率上，{} 会比 dict() 快三倍左右。使用 dict()，会多了个调用函数的过程，而这个过程会有进出栈的操作，相对更加耗时

<div style="text-align: center;">
    <img alt='202403301337266' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301337266.png' width=500px>
</div>

### 访问字典中的值

#### 使用键进行访问

```python
person = {"name": "smith white", "age": 22, "salary": 1000}
person["name"]
```

如果尝试访问字典中不存在的键，将引发`KeyError`。为了避免这种错误，可以使用`get()`方法，当键不存在时，它将返回`None`或者指定的默认值

```python
person = {"name": "smith white", "age": 22, "salary": 1000}
person.get("work", None)
```

<div style="text-align: center;"><img alt='202403301338885' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301338885.png' width=500px> </div>

#### 使用`values`进行访问

`values` 方法返回的对象是 `dict_values` 类型的视图对象。这个视图对象提供了对字典中所有值的动态视图。你可以使用这个视图对象进行迭代、转换为列表，或者执行其他集合操作

> **注意**:两个 `dict.values()` 视图之间的相等性比较将总是返回 `False`。 这在 `dict.values()` 与其自身比较时也同样适用

```python
person.values()
for value in person.values():
    print(value)
list(person.values())
```

<div style="text-align: center;"><img alt='202403301339188' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301339188.png' width=500px> </div>

#### 自定义方法使用点式访问

创建了一个名为 `Dict` 的类，它继承自内置的 `dict` 类。通过覆盖 `__getattr__`，我们使得可以通过点式访问值，就像访问对象属性一样

```python
class Dict(dict):
    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            raise AttributeError(f"'Dict' object has no attribute '{attr}'")
    def __setattr__(self, attr, value):
        self[attr] = value
```

<div style="text-align: center;"><img alt='202403301341616' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301341616.png' width=500px> </div>

### 修改字典的值

可以直接通过键来修改字典中的值。**如果该键存在，其值将被更新；如果不存在，将添加新的键值对**。例如：

```python
  person['age'] = 21  # 修改已存在的键
  person['address'] = 'beijing'  # 添加新的键值对
```

<div style="text-align: center;"><img alt='202403301344771' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301344771.png' width=500px> </div>

### 字典的合并

#### 使用`update` 方法

字典对象内置了一个`update`方法,用于把另一个字典更新到自己身上

<div style="text-align: center;"><img alt='202403301346957' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301346957.png' width=500px> </div>

#### 使用字典解析式

Python 里对于生成列表、集合、字典，有一套非常 Pythonic 的写法。那就是列表解析式，集合解析式和字典解析式

<div style="text-align: center;"><img alt='202403301347900' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301347900.png' width=500px> </div>

#### 使用`|` 进行合并

Python 3.9.04a 版本中，新增了一个抓眼球的新操作符：`|`， PEP584 将它称之为合并操作符（Union Operator），用它可以很直观地合并多个字典

<div style="text-align: center">
    <img src="https://picx.zhimg.com/80/v2-a43fbc5a61e8a2d6408544a024ab2f27_720w.webp?source=d16d100b" width=500px>
</div>

#### 先解包再合并字典

使用`**`可以解包字典，解包完后再使用 dict 或者`{}`就可以合并

<div style="text-align: center">
    <img src="https://picx.zhimg.com/80/v2-7f0e213862af127695dec3efbeb0d989_720w.webp?source=d16d100b" width=500px>
</div>

## 字符串

### 字符编码

网页编码：是指网页中字符的编码方式

* **ASCII**：一个英文字母（不分大小写）占一个字节的空间
* **中文字符编码**:主要有gb2312、gbk以及gb18030
* **unicode**：容纳世界上所有语言字符和符号的集合
* **utf-8**（8-bit unicode Transformation Format）是一种针对unicode字符集的可变长度字符编码方式

Python 3中的字符串默认的编码为unicode，因此，gbk、gb2312等字符编码与utf-8编码之间都必须通过unicode编码才能互相转换。即在python中，使用`encode()`将unicode编码为utf-8、gbk等，而使用`decode()`将utf-8、gbk等字符编码解码为unicode

<div style="text-align: center;"><img alt='202403301352398' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301352398.png' width=500px> </div>

### 字符串格式化

#### 使用%进行字符串格式化

在Python中，采用的格式化方式和C语言是一致的，用`%`实现

| 占位符 |   替换内容   |
| :----: | :----------: |
|   %d   |     整数     |
|   %f   |    浮点数    |
|   %s   |    字符串    |
|   %x   | 十六进制整数 |

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061456870.png'>
</div>

#### 使用`format`进行字符串格式化

另一种格式化字符串的方法是使用字符串的`format()`方法，它会用传入的参数依次替换字符串内的占位符`{0}`、`{1}`

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061456304.png'>
</div>

#### 使用`f-string`进行格式化

f-string，亦称为格式化字符串常量（formatted string literals），是Python3.6新引入的一种字符串格式化方法，该方法源于[PEP 498 – Literal String Interpolation](https://python.org/dev/peps/pep-0498/)，主要目的是使格式化字符串的操作更加简便。f-string在形式上是以 `f` 或 `F` 修饰符引领的字符串（`f'xxx'` 或 `F'xxx'`），以大括号 `{}` 标明被替换的字段；f-string在本质上并不是字符串常量，而是一个在运行时运算求值的表达式

f-string在功能方面不逊于传统的[%-formatting语句](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)和[`str.format()`函数](https://docs.python.org/3/library/stdtypes.html#str.format)，同时性能又优于二者，且使用起来也更加简洁明了，因此对于Python3.6及以后的版本，推荐使用f-string进行字符串格式化

<div style="text-align: center">
    <img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061456196.png'>
</div>

### 字符串常用的方法

#### **len()**: 返回字符串的长度

```python
my_string = "Hello, World!"
length = len(my_string)
print(length)  # 输出：13
```

#### **lower() 和 upper()**: 分别用于将字符串转换为小写和大写

```python
my_string = "Hello, World!"
lower_case = my_string.lower()
upper_case = my_string.upper()
print(lower_case)  # 输出：hello, world!
print(upper_case)  # 输出：HELLO, WORLD!
```

#### **strip()**: 用于去除字符串两端的空格或指定的字符

```python
my_string = "   Hello, World!   "
stripped_string = my_string.strip()
print(stripped_string)  # 输出：Hello, World!
```

#### **replace()**: 替换字符串中指定的子串

```python
my_string = "Hello, World!"
new_string = my_string.replace("Hello", "Hi")
print(new_string)  # 输出：Hi, World!
```

#### **split()**: 将字符串分割成列表，默认以空格为分隔符

```python
my_string = "Hello, World!"
words = my_string.split()
print(words)  # 输出：['Hello,', 'World!']
```

#### **join()**: 将列表中的元素连接成一个字符串

```python
words = ['Hello,', 'World!']
my_string = ' '.join(words)
print(my_string)  # 输出：Hello, World!
```

#### **isalpha()、isdigit()、isspace()**: 分别用于检查字符串是否只包含字母、数字或空格

```python
alpha_check = "Hello".isalpha()
digit_check = "123".isdigit()
space_check = "   ".isspace()
print(alpha_check)  # 输出：True
print(digit_check)  # 输出：True
print(space_check)  # 输出：True
```

#### **capitalize() 和 title()**: 分别用于将字符串的第一个字符大写和将每个单词的第一个字符大写

```python
my_string = "hello world"
capitalized = my_string.capitalize()
title_case = my_string.title()
print(capitalized)  # 输出：Hello world
print(title_case)   # 输出：Hello World
```

#### **swapcase()**: 将字符串中的大小写互换

```python
my_string = "Hello, World!"
swapped_case = my_string.swapcase()
print(swapped_case)  # 输出：hELLO, wORLD!
```
