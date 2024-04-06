# 文件与IO

实际开发中常常会遇到对数据进行[持久化](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96)操作的场景, 而实现数据持久化最直接简单的方式就是将数据保存到文件中

在Python中实现文件的读写操作其实非常简单, 通过Python内置的`open`函数, 我们可以指定文件名、操作模式、编码信息等来获得操作文件的对象, 接下来就可以对文件进行读写操作了。这里所说的操作模式是指要打开什么样的文件（字符文件还是二进制文件）以及做什么样的操作（读、写还是追加）, 具体的如下表所示:

| 操作模式 | 具体含义                         |
| :---:|:---:|
| `'r'`    | 读取 （默认）                    |
| `'w'`    | 写入（会先截断之前的内容）       |
| `'x'`    | 写入, 如果文件已经存在会产生异常 |
| `'a'`    | 追加, 将内容写入到已有文件的末尾 |
| `'b'`    | 二进制模式                       |
| `'t'`    | 文本模式（默认）                 |
| `'+'`    | 更新（既可以读又可以写）         |

![文件读写模式](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061549746.png)

## 读写文本文件

### 读取文件

读取文本文件时, 需要在使用 `open` 函数时指定好带路径的文件名（可以使用**相对路径或绝对路径**）并将文件模式设置为'r'（如果不指定, 默认值也是'r'）, 然后通过 `encoding` 参数指定编码（如果不指定, 默认值是None, 那么在读取文件时使用的是操作系统默认的编码）, 如果不能保证保存文件时使用的编码方式与 `encoding` 参数指定的编码方式是一致的, 那么就可能因无法解码字符而导致读取失败。下面的例子演示了如何读取一个文本文件

```python
def read_file(file_path):
    with open(file_path, 'r', enconding='utf-8') as f:
        print(f.read())
```

除了使用文件对象的 `read` 方法读取文件之外, 还可以使用 `for-in` 循环逐行读取或者用 `readlines` 方法将文件按行读取到一个列表容器中

```python
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        # todo something
```

#### 流式读取大文件

比如当你使用了`read`函数, 其实 `Python` 会将文件的内容一次性的全部载入内存中, 如果文件有10个G甚至更多, 那么你的电脑就要消耗的内存非常巨大

对于这个问题, 你也许会想到使用 `readline` 去做一个生成器来逐行返回

```python
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        yield f.readline()
```

可如果这个文件内容就一行呢, 一行就 10个G, 其实你还是会一次性读取全部内容。最优雅的解决方法是, 在使用 `read` 方法时, **指定每次只读取固定大小的内容**
```python
from functools import partial

def read_file(filename, block_size = 1024 * 8):
    with open(filename, "r", encoding="utf-8") as fp:
        for chunk in iter(partial(fp.read, block_size), ""):
            yield chunk
```

如果你使用的是 Python 3.8 +, 还有一种更直观、易于理解的写法, 既不用使用偏函数, 也不用掌握 `iter` 这种另类的用法。而只要用利用**海象运算符**就可以

```python
def read_from_file(filename, block_size = 1024 * 8):
    with open(filename, "r", encoding="utf-8") as fp:
        while chunk := fp.read(block_size):
            yield chunk
```

### 写入文件

要将文本信息写入文件文件也非常简单, 在使用 `open` 函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入, 应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常

## 读写二进制文件

二进制文件是一种文件格式, 其中包含的数据以*二进制形式*表示, 而不是像文本文件那样使用字符编码表示。在二进制文件中, 数据以字节的形式存储, 每个字节可以表示0和1的组合, 而不是字符

与文本文件相比, 二进制文件通常更加紧凑和高效, 因为它们不需要进行字符编码和解码。二进制文件可用于存储各种类型的数据, 包括图像、音频、视频、执行文件（如可执行程序或库文件）以及其他二进制数据

### 读取二进制文件

```python
import pickle

def binary_read(file_path: str, file_extension: str):
    """
    :param: file_path:文件路径
    :param: file_extension:文件后缀名(ext)
    :return: None
    """
    with open(file_path + file_extension, 'rb') as b:
        # your file maybe path will be different
        stud = pickle.load(b)
        # todo something
```

### 写入二进制文件

```python
def write_binary(filename, binary_data):
    with open(filename, 'wb') as f:
        f.write(binary_data)
```

## 读写`JSON`文件

* JSON是一种**轻量级的数据交换格式**, 由字符串化的键值对构成
* JSON是JavaScript的子集, 但也是独立于编程语言的数据格式
* JSON支持的数据类型如下:

|  对象  | {}括起来的无序键值对, 键必须是字符串 |
| :---: | :---|
|  数值  | 十进制数据                           |
| 字符串 | ""括起来的字符, 必须是双引号         |
| 布尔值 | true或false                          |
|  数组  | []括起来的多个值                     |
|   空   | null                                 |

python可以使用json模块来操作json文件,json模块主要有四个比较重要的函数, 分别是：

* `dump` - 将Python对象按照JSON格式序列化到文件中
* `dumps` - 将Python对象处理成JSON格式的字符串
* `load` - 将文件中的JSON数据反序列化成对象
* `loads` - 将字符串的内容反序列化成Python对象

### 读取json文件

```python
import json

def read_json(filename):
    with open(filename, 'r'. encoding='utf-8') as f:
        data = json.load(f)
        # todo shomething
```

### 写入json文件

```python
import json

def write_to_json(filename, data):
    with open('data.json', 'a', encoding='utf-8') as f:
        f.write(json.dump(data, indent=4, ensure_ascii=False))
# json.dumps:将字符串对象转换为json对象
# indent表示缩进的字符数, ensure_ascii=False确保中文不乱码
```

## 读写csv文件

CSV（Comma-Separated Values）是一种常见的文件格式, 用于存储表格数据。CSV文件由逗号分隔的值组成, 每行表示一条记录, 而每个值则表示记录中的字段。CSV文件通常用于在不同的应用程序之间共享数据, 因为它们易于创建和解析, 并且可以用于存储简单的表格数据。

CSV文件的基本特点包括：

1. **逗号分隔的值（Comma-Separated Values）**：每个字段之间使用逗号 `,` 进行分隔, 用于区分字段。
2. **每行表示一条记录**：每行数据代表一个完整的记录或条目。
3. **文本文件**：CSV文件是文本文件, 因此可以使用文本编辑器打开和编辑。
4. **不需要特定的编码**：CSV文件通常不需要特定的字符编码, 因为它们只包含ASCII字符或UTF-8编码的字符。
5. **灵活性**：CSV文件的字段可以包含文本、数字和其他数据类型, 因此可以用于各种类型的数据。
6. **易于解析**：由于CSV文件使用简单的结构, 因此易于编写解析器来读取和处理CSV数据。
7. **支持引号**：如果字段中包含逗号或换行符等特殊字符, 可以使用双引号将字段括起来

使用 Python 来读写csv文件是非常容易的, 因为实现csv的读取和写入功能的csv模块, 是一个内置模块, 我们可以直接使用, 使用csv模块时, 需要先导入它, 即在代码一开始写入`import csv`

### CSV文件的读取

#### `reader()`函数

`reader()` 函数是csv模块内的一个函数, 当使用 `open()` 打开csv文件, 得到文件对象后, 可以把这个文件对象传入`reader()` 函数

```python
import csv

# 必须指定 newline='', 避免不必要的空行
with open('./reader_demo.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

#### `DictReader` 类

`DictReader` 类的操作类似于常规的 `reader()` , 但 `DictReader` 会将读取到的信息转换为**字典形式**

<div style="text-align: center;">     <img alt='202403201503013' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201503013.png' width=50%> </div>

### CSV文件的写入

与读取功能类似, `csv` 模块也为我们准备了两种写入方式——函数 `writer()` 与类 `DictWriter`

#### `writer()` 函数

要将内容写入 `csv` 文件, 需要先把 `open()`返回的文件对象转化为 `writer` 对象,  然后需要调用 `writer` 对象的方法`writerow(row)`, 该方法会将参数 `row` 当作一行内容写入 `csv` 文件中,  参数 `row` 代表了你想要写入 `csv` 文件的内容, 它必须是一个**可迭代对象**, 这里推荐使用列表

```python
import csv

with open('./writer_demo.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['a', 'b', 'c'])
```

#### `DictWriter` 类

`DictWriter` 的操作类似于常规的 `writer()` , 但 `DictWriter` 会将**字典**写入（映射）到csv文件的行中

<div style="text-align: center;">     <img alt='202403201525798' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201525798.png' width=500px> </div>
