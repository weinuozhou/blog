# 解析响应

`requests`库模拟浏览器请求网页可以获取网页的源代码,但网页源代码通常较为复杂，可以通过**正则表达式**、**xpath**、**BeatifulSoup**、**CSS选择器**来获取节点

## 正则表达式

* 正则表达式是处理字符串强大的工具，对于**字符串的检索、替换和匹配验证**较为容易
* 正则表达式测试工具:[https://tool.oschina.net/regex](https://tool.oschina.net/regex)

* **正则表达式常用的匹配规则**

|模式|描述|
| :---: | :---|
|  \w   | 匹配字母、数字及下划线(有些可以匹配中文) |
|  \W   | 匹配不是字母、数字及下划线的字符         |
|  \s   | 匹配任意空白字符                         |
|  \S   | 匹配任意非空白字符,等价于[\t\n\r\f]      |
|  \d   | 匹配任意数字,等价于[0-9]                 |
|  \D   | 匹配任意非数字的字符                     |
|  \A   | 匹配字符串的开头                         |
|  \b   | 匹配单词的边界                           |
|  \Z   | 匹配字符串的结尾                         |
|  \n   | 匹配一个换行符                           |
|  \t   | 匹配一个制表符                           |
|   ^   | 匹配一行字符串的开头                     |
|   $   | 匹配一行字符串的结尾                     |
|   .   | 匹配任意字符(不包括换行符)               |
|  \*   | 匹配0次或多次                            |
|  \+   | 匹配一次或多次                           |
|   ?   | 匹配0次或1次(非贪婪模式)                 |
| [...] | 匹配一组字符                             |
|  {n}  | 匹配n次                                  |
| {n,m} | 匹配n-m次(贪婪模式)                      |
| a\|b  | 匹配a或者b                               |
|  ()   | 匹配括号内的表达式, 表示一个组           |

* **正则表达式修饰符**

|修饰符|含义|
| :----: | :----|
|  re.I  | 匹配对大小写不敏感                |
|  re.L  | 做本地化识别匹配                  |
|  re.M  | 多行匹配,影响^和$                 |
|  re.S  | 使.可以匹配包括换行在内的所有字符 |
|  re.U  | 根据Unicode**字符集解析字符**     |

### `match()`方法

```python
match(pattern,string,flags=0)
```

`match`方法会从**字符串开始的位置**匹配正则表达式, 匹配到则返回`match`对象否则返回None

* `group`:按组输出匹配到的内容
* `span`:可以输出匹配的范围,在原字符串中的位置

```python
content = "hello 123 45678 This is a  Regex demo"
result = re.match('^hello.*demo$',content)
print(f'匹配到的正则表达式对象的数据类型为"{type(result)}')
print(f'匹配到的正则表达式对象为"{result}')
print(f'输出匹配到的内容为:{result.group()}')
print(f'匹配到的字符串在原字符串的位置为:{result.span()}')
"""
匹配到的正则表达式对象的数据类型为"<class 're.Match'>
匹配到的正则表达式对象为"<re.Match object; span=(0, 37), match='hello 123 45678 This is a  Regex demo'>
输出匹配到的内容为:hello 123 45678 This is a  Regex demo
匹配到的字符串在原字符串的位置为:(0, 37)
"""
```

### `search（）`方法

```python
search(pattern,string,flags=0)
```

* `match`方法是通过**字符串的开头**开始匹配的, 一旦开头不匹配, 整个匹配就失败了
* `search`方法会**扫描整个字符串**匹配正则表达式, 匹配到则返回**第一个相应的匹配对象**,否则返回None
* `group`:按组输出匹配到的内容
* `span`:可以输出匹配的范围,在原字符串中的位置

```python
content = "hello 123 45678 This is a  Regex 123 45678 hello world"
result = re.search('\d+\s\d+',content)
print(f'匹配到的正则表达式对象的数据类型为"{type(result)}')
print(f'匹配到的正则表达式对象为"{result}')
print(f'输出匹配到的内容为:{result.group()}')
print(f'匹配到的字符串在原字符串的位置为:{result.span()}')
"""
匹配到的正则表达式对象的数据类型为"<class 're.Match'>
匹配到的正则表达式对象为"<re.Match object; span=(6, 15), match='123 45678'>
输出匹配到的内容为:123 45678
匹配到的字符串在原字符串的位置为:(6, 15)
"""
```

### `findall()`方法

```python
import re
re.findall(pattern,string,flags=0)
```

* `findall`方法返回匹配到正则表达式的字符串的所有内容

```python
content = "hello 123 45678 This is a  Regex 123 45678 hello world"
result = re.findall('\d+\s\d+',content)
print(f'匹配到的正则表达式对象的数据类型为"{type(result)}')
print(f'匹配到的正则表达式对象为"{result}')
"""
匹配到的正则表达式对象的数据类型为"<class 'list'>
匹配到的正则表达式对象为"['123 45678', '123 45678']
"""
```

### `compile()`方法

该方法可以将正则表达式的样式编译成一个**正则表达式对象**, 便于使用`match`、`search`和`findall`进行匹配

```python
pattern = r'(.*?):(.*)' # 正则表达式样式
prog = re.compile(pattern) # prog是一个正则表达式对象, 可以使用search、match、findall等方法进行匹配
```

```python
content = 'name:grey age:22'
pattern = r'(.*):(\d+)' 
prog = re.compile(pattern)
result = re.findall(prog,content)
print(f'匹配到的正则表达式对象的数据类型为"{type(result)}')
print(f'匹配到的正则表达式对象为"{result}')
"""
匹配到的正则表达式对象的数据类型为"<class 'list'>
匹配到的正则表达式对象为"[('name:grey age', '22')]
"""
```

## `xpath`定位

`xpath`, 即xml路径语言,可以适用于HTML文档的搜索,它还提供了超过 100 个内建函数,它的优势如下:

* 选择功能强大, 提供非常简洁明了的路径选择表达式
* 内置函数多, 可以用于字符串、数值、时间的匹配以及节点、序列的处理等
  * 具体详情更多Xpath的用法可以参考:<https://www.w3.org/TR/xpath/>
  * 关于Python lxml库的用法, 可以参考:<http://lxml.de/>

### `xpath`常用规则

|  表达式  | 含义                       |
| :------: | :------------------------- |
| nodename | 选取此节点的所有子节点     |
|    /     | 从当前节点选取子节点       |
|    //    | 从当前节点选取所有子孙节点 |
|    .     | 选取当前节点               |
|    ..    | 选取当前节点的父节点       |
|    *     | 通配符                     |
|    @     | 选取属性                   |
| contains | 包含部分文本或者属性       |

```python
//title[@lang='eng'] 
```

这就是一个 XPath 规则, 它代表选择所有名称为 title, 同时属性 lang 的值为 eng 的节点

### `python`实现

```python
import requests
from lxml import etree
response = requests.get(url,headers)
etree.HTML(response.text)
```

```python
with open('./data/test.html', 'r', encoding='utf-8') as f:
    html = f.read()
print(f'测试的网页源代码为:\n{html}') # 接下来所有的xpath分析都以此展开
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>
        <ul id='items'>
             <li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
             <li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>
             <li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>
             <li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>
         </ul>
    </div>
</body>
</html>
```

#### 查找节点

```python
html.xpath('//标签名/text()') # 获取文本
html.xpath('//标签名/@属性名') # 获取属性值
```

```python
e = etree.HTML(html) # 初始化HTML
e.xpath('//a/text()') # 获取a节点下文本
e.xpath('//li/@class') # 获取li节点的class属性值
e.xpath('//ul/@id') # 获取ul标签的id属性值
"""
['第一个li节点', '第二个li节点', '第三个li节点', '第四个li节点']
['aa1', 'aa2', 'aa3', 'aa4']
['items']
"""
```

#### 属性定位

```python
html.xpath('//标签名[@属性="属性值"]')
```

* 常见的是通过属性class、id、name来确定节点(id属性全局只有一个, 因此只能查找到一个节点, 而class属性通常有很多个)

```python
e.xpath('//ul[@id="items"]/li/a/text()')
e.xpath('//li[@class="aa1"]/a/text()')
"""
['第一个li节点', '第二个li节点', '第三个li节点', '第四个li节点']
['第一个li节点']
"""
```

#### 模糊查询

```python
html.xpath('//标签名[contains(@属性,"属性值")]') # 匹配是否包含
```

```python
e.xpath('//li[contains(@class,"aa")]/a/text()')
"""
['第一个li节点', '第二个li节点', '第三个li节点', '第四个li节点']
"""
```

#### 按序选择

有时候, 我们在选择的时候某些属性可能同时匹配多个节点, 但我们只想要其中的某个节点, 如第二个节点或者最后一个节点, 这时可以利用中括号引入索引的方法获取特定次序的节点: 

```python
e.xpath('//li[contains(@class,"aa")]/a/text()') #获取所有li节点下a节点的内容
e.xpath('//li[1][contains(@class,"aa")]/a/text()') #获取第一个
e.xpath('//li[last()][contains(@class,"aa")]/a/text()') #获取最后一个
e.xpath('//li[position()>2 and position()<4][contains(@class,"aa")]/a/text()') #获取第三个
e.xpath('//li[last()-2][contains(@class,"aa")]/a/text()') #获取倒数第三个
"""
['第一个li节点', '第二个li节点', '第三个li节点', '第四个li节点']
['第一个li节点']
['第四个li节点']
['第三个li节点']
['第二个li节点']
"""
```

## Beatiful Soup

BeautifulSoup 提供一些简单的、Python 式的函数用来处理导航、搜索、修改分析树等功能。

* 它是一个工具箱, 通过解析文档为用户提供需要抓取的数据, 因为简单, 所以不需要多少代码就可以写出一个完整的应用程序。
* BeautifulSoup 自动将输入文档转换为 Unicode 编码, 输出文档转换为 utf-8 编码。
* BeautifulSoup 已成为和 lxml、html5lib 一样出色的 Python 解释器, 为用户灵活地提供不同的解析策略或强劲的速度

Beautiful Soup 在解析时实际上依赖解析器, 它除了支持 Python 标准库中的 HTML 解析器外, 还支持一些第三方解析器（比如 lxml）

|解析器|使用方法|优势|劣势|
| :---: | :---: | :---: | :---:|
|  Python 标准库   | BeautifulSoup(markup, "html.parser") |     Python 的内置标准库、执行速度适中 、文档容错能力强      | Python 2.7.3 or 3.2.2前的版本中文容错能力差 |
| LXML HTML 解析器 |    BeautifulSoup(markup, "lxml")     |                   速度快、文档容错能力强                    |              需要安装 C 语言库              |
| LXML XML 解析器  |     BeautifulSoup(markup, "xml")     |                速度快、唯一支持 XML 的解析器                |              需要安装 C 语言库              |
|     html5lib     |  BeautifulSoup(markup, "html5lib")   | 最好的容错性、以浏览器的方式解析文档、生成 HTML5 格式的文档 |           速度慢、不依赖外部扩展            |

lxml 解析器有解析 HTML 和 XML 的功能, 而且**速度快, 容错能力强**, 所以推荐使用它。

### 基本使用

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml') # 需要传入html对象
print(soup.prettify()) # 解析的字符串以标准的缩进格式输出
```

```python
with open('./data/test.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
```

```html
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="utf-8"/>
  <title>
   Title
  </title>
 </head>
 <body>
  <div>
   <ul id="items">
    <li class="aa1" name="item">
     <a href="link1.html">
      第一个li节点
     </a>
    </li>
    <li class="aa2" name="item">
     <a href="link2.html">
      第二个li节点
     </a>
    </li>
    <li class="aa3" name="item">
     <a href="link3.html">
      第三个li节点
     </a>
    </li>
    <li class="aa4" name="item">
     <a href="link4.html">
      第四个li节点
     </a>
    </li>
   </ul>
  </div>
 </body>
</html>
*/
```

#### 节点选择器

直接调用节点的名称就可以选择节点元素, 再调用 string 属性就可以得到节点内的文本了, 这种选择方式速度非常快。

```python
print(f'html文档的标题的数据类型为{type(soup.title)}')
print(f'html文档的标题为{soup.title.string}')
print(f'html文档的li标签为{soup.li}') # 可以看到只会获取第一个li节点
"""
html文档的标题的数据类型为<class 'bs4.element.Tag'>
html文档的标题为Title
html文档的li标签为<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
"""
```

#### 提取信息

##### 提取名称

可以利用 name 属性获取节点的名称。

```python
print(f'html文档的ul的名称为{soup.ul.name}') # html文档的ul的名称为ul
```

##### 获取属性

每个节点可能有多个属性, 比如 id 和 class 等, 选择这个节点元素后, 可以调用 attrs 获取所有属性

attrs 的返回结果是字典形式, 它把选择的节点的**所有属性和属性值**组合成一个字典。

```python
print(f'html文档的ul的属性为{soup.ul.attrs}') # html文档的ul的属性为{'id': 'items'}
```

##### 获取内容

可以利用 string 属性获取节点元素包含的文本内容

```python
print(f'html文档的第一个li标签的内容为:{soup.li.string}') # html文档的第一个li标签的内容为:第一个li节点
```

#### 嵌套选择

比如, 我们获取了 ul 节点元素, 我们可以继续调用 ul 来选取其内部的 li 节点元素, 它同样可以继续调用节点进行下一步的选择。

```python
print(f'html文档的第一个li标签的内容为:{soup.ul.li.string}')
print(f'html文档的第一个li标签的属性为:{soup.ul.li.attrs}')
"""
html文档的第一个li标签的内容为:第一个li节点
html文档的第一个li标签的属性为:{'class': ['aa1'], 'name': 'item'}
"""
```

#### 关联选择

在做选择的时候, 有时候不能做到一步就选到想要的节点元素, 需要先选中某一个节点元素, 然后以它为基准再选择它的子节点、父节点、兄弟节点

##### 子节点和子孙节点

* `contents`:获取该节点的所有内容(子节点和子孙节点),返回一个直接子节点的列表
* `children`: 返回一个包含子节点的生成器
* `descendants`:返回一个包含子孙节点的生成器

```python
print(f'html文档的ul标签的所有子节点和子孙节点为:\n{soup.ul.contents}') # 列表中每个元素都是ul标签的直接子节点
"""
html文档的ul标签的所有子节点和子孙节点为:
['\n', <li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>, '\n', <li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>, '\n', <li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>, '\n', <li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>, '\n']
"""
```

##### 父节点和祖先节点

* `parent`:返回一个包含父节点的生成器
* `parents`:返回一个包含祖先节点的生成器

```python
print(f'html文档的a标签的所有父节点为:{soup.a.parent}') 
for parent in soup.a.parent:
    print(child)
 # html文档的a标签的所有父节点为:<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
```

##### 兄弟节点

* `next_siblings`:获取同级节点的后面节点
* `previous_siblings`:获取同级节点的前面节点

```python
print(f'html文档的第一个li标签后面的内容为:')
for li in soup.li.next_siblings:
    print(li)
"""
html文档的第一个li标签后面的内容为:
<li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>
<li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>
<li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>
"""
```

#### 方法选择器

前面所讲的选择方法都是通过属性来选择的, 这种方法非常快, 但是如果进行比较复杂的选择的话, 它就比较烦琐, 不够灵活了。幸好, Beautiful Soup 还为我们提供了一些查询方法, 比如 find_all 和 find 等, 调用它们, 然后传入相应的参数, 就可以灵活查询了

##### find_all

```python
find_all(name , attrs , recursive , text , **kwargs)
```

* `name`:通过节点来查找
* `attrs`:通过属性来查找
* `text`:用来匹配节点的文本, 传入的形式可以是字符串, 可以是正则表达式对象
  * 返回一个列表

###### name参数

```python
print(f"html文档的所有li标签的内容为:\n{soup.find_all(name='li')}")
"""
html文档的所有li标签的内容为:
[<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>, <li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>, <li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>, <li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>]
"""
```

###### attrs参数

```python
print(f"html文档的ul标签的内容为:\n{soup.find_all(attrs={'id': 'items'})}")
"""
html文档的ul标签的内容为:
[<ul id="items">
<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
<li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>
<li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>
<li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>
</ul>]
"""
```

###### text参数

```python
print(f"html文档的li标签的内容为:\n{soup.find_all(text=re.compile('节点'))}")
"""
html文档的li标签的内容为:
['第一个li节点', '第二个li节点', '第三个li节点', '第四个li节点']
"""
```

##### find

除了 find_all 方法, 还有 find 方法, 只不过 find 方法返回的是单个元素, 也就是第一个匹配的元素, 而 find_all 返回的是所有匹配的元素组成的列表

```python
print(f"html文档的第一个li标签的内容为:\n{soup.find(name='li')}")
"""
html文档的第一个li标签的内容为:
<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
"""
```

#### CSS选择器

使用 CSS 选择器, 只需要调用 select 方法, 传入相应的 CSS 选择器即可

如果不熟悉CSS选择器的话, 可以参考 <http://www.w3school.com.cn/cssref/css_selectors.asp> 了解。

```python
print(f"html文档的所有li标签的内容为:\n{soup.select('ul li')}")
"""
html文档的所有li标签的内容为:
[<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>, <li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>, <li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>, <li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>]
"""
```

### Beatiful Soup 总结

* 推荐使用 LXML 解析库, 必要时使用 html.parser。
* 节点选择筛选功能弱但是速度快。
* 建议使用 find、find_all 方法查询匹配单个结果或者多个结果。
* 如果对 CSS 选择器熟悉的话可以使用 select 选择法。
* 有关CSS选择器的用法下面将详细讲述

## `CSS`选择器定位

* 如果你比较喜欢用CSS选择器, 那么`pyquery`是一个更适合你的解析库
* 具体详情可以参考[pyquery官方文档](http://pyquery.readthedocs.io)

### 初始化`pyquery`

初始化`pyquery`时, 需要传入HTML文本来初始化一个`pyqery`对象, 它的初始化方式有很多种: 

* 传入字符串
* 传入url
* 传入文件名

#### 字符串初始化

```python
# 初始化pyquery
doc = pq(requests.get('https://www.baidu.com').text)
doc('div') # 选择所有的div节点
# [<div#wrapper>, <div#head>, <div.head_wrapper>, <div.s_form>, <div.s_form_wrapper>, <div#lg>, <div#u1>, <div#ftCon>, <div#ftConw>]
```

#### `url`初始化

```python
doc = pq(url='https://www.baidu.com') # 初始化pyquery
doc('div')
# [<div#wrapper>, <div#head>, <div.head_wrapper>, <div.s_form>, <div.s_form_wrapper>, <div#lg>, <div#u1>, <div#ftCon>, <div#ftConw>]
```

#### 本地文件初始化

```python
doc = pq(filename='./data/test.html', encoding='utf-8') # 初始化pyquery
doc('li')
# [<li.aa1>, <li.aa2>, <li.aa3>, <li.aa4>]
```

### 基本`CSS`选择器

* 选取的节点仍然是`pyquery`类型的, 需要进一步提取文本或者属性
* 提取文本:`text()`方法
* 提取属性:`attr()`方法(只会获取到第一个值, 需要遍历)

#### 通过节点进行选择

```python
print(f"所有li标签的内容为:{doc('a').text()}")
# 所有li标签的内容为:第一个li节点 第二个li节点 第三个li节点 第四个li节点
```

```python
items = doc('li')
for i, item in enumerate(items.items()):
    print(f"第{i+1}个li节点的class属性值为{item.attr('class')}") # 找到所有的li节点的class值
"""
第1个li节点的class属性值为aa1
第2个li节点的class属性值为aa2
第3个li节点的class属性值为aa3
第4个li节点的class属性值为aa4
"""
```

#### 通过class选择器来选择

```python
doc('.class属性值')
```

```python
print(f"class=aa1的节点为:{doc('.aa1')}")# 找到所有class=name的节点
print(f"class=aa1的节点的内容为:{doc('.aa1').text()}")
"""
class=aa1的节点为:<li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
class=aa1的节点的内容为:第一个li节点
"""
```

#### 通过id选择器来选择

```python
doc('#id属性值')
```

```python
print(f"id=items的节点为:\n{doc('#items')}")
"""
id=items的节点为:
<ul id="items">
             <li class="aa1" name="item"><a href="link1.html">第一个li节点</a></li>
             <li class="aa2" name="item"><a href="link2.html">第二个li节点</a></li>
             <li class="aa3" name="item"><a href="link3.html">第三个li节点</a></li>
             <li class="aa4" name="item"><a href="link4.html">第四个li节点</a></li>
         </ul>
"""
```

#### 多层选择器

```python
doc('标签名 .class属性值') # 获取某个标签下class=属性值的节点
```

```python
print(f"id=items的节点下的li节点的内容为:{doc('#items li').text()}")# 选取所有id=items的节点, 在其内部节点选取li节点的内容
print(f"class=aa1的节点下的a节点的内容为:{doc('.aa1 a').text()}") # 选取class=aa1的节点, 在其内部节点选择a节点的内容
"""
id=items的节点下的li节点的内容为:第一个li节点 第二个li节点 第三个li节点 第四个li节点
class=aa1的节点下的a节点的内容为:第一个li节点
"""
```

### 伪类选择器

* 伪类是指在HTML中, 同一个标签, 根据器不同的状态, 有不同的显示样式
* 我们主要应用伪类选择器来选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点等等

```python
doc('标签名:first-child') # 选择第一个节点
doc('标签名:last-child') # 选择最后一个节点
doc('标签名:nth-child(2)') # 选择第二个节点,里面的参数可以更改
doc('标签名:gt(2)') # 选择第三个节点之后的节点
doc('标签名:nth-child(2n)') # 选择偶数节点
doc('标签名:contains(text)') # 选择包含某一文本的节点
```

```python
print(f"第一个li标签的内容为:{doc('li:first-child').text()}")
print(f"最后一个li标签的内容为:{doc('li:last-child').text()}")
print(f"第二个li标签的内容为:{doc('li:nth-child(2)').text()}")
print(f"第二个li标签之后的内容为:{doc('li:gt(1)').text()}")
print(f"偶数个li标签之后的内容为:{doc('li:nth-child(2n)').text()}")
print(f"奇数个li标签之后的内容为:{doc('li:nth-child(2n+1)').text()}")
print(f"包含节点这两个字的内容为:{doc('li:contains(节点)').text()}")
"""
第一个li标签的内容为:第一个li节点
最后一个li标签的内容为:第四个li节点
第二个li标签的内容为:第二个li节点
第二个li标签之后的内容为:第三个li节点 第四个li节点
偶数个li标签之后的内容为:第二个li节点 第四个li节点
奇数个li标签之后的内容为:第一个li节点 第三个li节点
包含节点这两个字的内容为:第一个li节点 第二个li节点 第三个li节点 第四个li节点
"""
```

### 子节点

* 查找子节点时可以使用`find`方法:查找所有的子孙节点
* 也可以使用`children`方法:只查找所有的子节点

```python
items = doc('div')
items.find('a').text()
# '第一个li节点 第二个li节点 第三个li节点 第四个li节点'
```

### 父节点

`parent`方法可以获取某个节点的父节点

```python
items = doc('a')
items.parent('li').attr('class')
# 'aa1'
```