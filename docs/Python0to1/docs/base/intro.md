# 初识Python

## Python概述

### 背景

- 使创始人为Guido van Rossum在1989年圣诞节期间, 为了打发无聊开发出来的
- Python官网:[https://www.python.org/](https://www.python.org/)

<div style="text-align: center">
  <img src="https://raw.githubusercontent.com/christinemu/biz-mining/9d8cc885bb8a9ce985b372fbfedaf66bdc3772c8//img/python/Rossum.jpg" style="width: 20%">
</div>

### 为什么选用Python?

- **简单**
  - 语法简单精练: 对于初学者来说, 比起其他编程语言, `Python`更容易上手
- **免费**
  - `Python`是免费开源的。这意味着不用花钱, 就可以共享、复制和改动它
  - 帮助`Python`形成了强壮的社区, 使`Python`更加完善, 技术发展更快
- **兼容**
  - `Python`兼容众多平台（Windows、Mac、Linux）, 所以开发者不会遇到使用其他语言时常会遇到的困扰
  - `Python`能够以多种方式轻易地与其他语言的组件“粘接”在一起, 被称为**胶水语言**
- **面向对象**
  - `Python`既支持面向过程, 也支持面向对象编程
- **丰富的库**
  - `Python`标准库庞大, 可以帮助你处理各种工作

<center><img src='https://raw.githubusercontent.com/christinemu/biz-mining/9d8cc885bb8a9ce985b372fbfedaf66bdc3772c8//img/python/pythonSimple.jpg' style="width: 50%"></center>

### Python的应用领域

<center><img src='https://raw.githubusercontent.com/christinemu/biz-mining/9d8cc885bb8a9ce985b372fbfedaf66bdc3772c8//img/python/where-is-python-used.gif' width=40%> </center>

#### 数据科学领域

<center><img src='https://raw.githubusercontent.com/christinemu/biz-mining/9d8cc885bb8a9ce985b372fbfedaf66bdc3772c8//img/python/programming_languages_used.jpg' width=60%></center>

#### 财务会计

<center><img src='https://raw.githubusercontent.com/christinemu/biz-mining/9d8cc885bb8a9ce985b372fbfedaf66bdc3772c8//img/python/pythonAccounting.png' width=60%></center>

### 安装Python解释器

想要开始Python编程之旅, 首先得在自己使用的计算机上安装Python解释器环境, 下面将以安装官方的Python解释器为例, 讲解如何在不同的操作系统上安装Python环境。官方的Python解释器是用C语言实现的, 也是使用最为广泛的Python解释器, 通常称之为CPython。除此之外, Python解释器还有Java语言实现的Jython、C#语言实现的IronPython以及PyPy、Brython、Pyston等版本, 有兴趣的读者可以自行了解。

- 下载地址(傻瓜式安装即可)[https://www.python.org/downloads/](https://www.python.org/downloads/)

## 包（package）管理工具

pip 是 Python 包管理工具, 该工具提供了对Python 包的查找、下载、安装、卸载的功能

### `pip`升级

要是你觉得自己的pip版本有点低, 想要升级一下的话, 在命令行中输入以下命令:

```bash
pip install --upgrade pip
# 等价于以下命令
pip install -U pip
```

### **安装某个版本的包**

如果打算用pip来安装第三方的包, 用的是以下的命令行

```bash
pip install package-name
```

### **指定国内源来安装**

默认的官方安装源是[https://pypi.org/simple]

- 国内镜像

  - [清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/](https://pypi.tuna.tsinghua.edu.cn/simple/)
  - [阿里云 http://mirrors.aliyun.com/pypi/simple/](http://mirrors.aliyun.com/pypi/simple/)
  - [豆瓣(douban) https://pypi.doubanio.com/simple](https://pypi.doubanio.com/simple)

- 更改方法

  - `pip install 安装的包的名称 -i https://pypi.tuna.tsinghua.edu.cn/simple/`
  - 建立`pip.ini`文件, 方法是新建**文本文档**, 将下述内容拷贝到该文档, 然后将该文档**另存为**`pip.ini`
  - 将`pip.ini`文件拷贝到安装的`Python`的*根目录*下, 以加快包的下载速度

  ```text
  [global]
  timeout = 6000
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
  [install]
  use-mirrors = true
  mirrors = http://pypi.tuna.tsinghua.edu.cn
  trusted-host = pypi.tuna.tsinghua.edu.cn
  ```

### 批量安装软件包

我们一般在看到别人的项目时, 都会包含一个 `requirements.txt`文件, 里面包含了一些 `Python` 项目当中需要用到的第三方库

要生成这种txt文件, 需要这么来做

```bash
pip freeze > requirements.txt 
```

而如果我们需要来批量安装第三方库, 在命令行中输入以下这个命令:

```bash
pip install -r requirements.txt
```

## 运行Python程序

### python交互式命令

*启动Python解释器*: 打开终端或命令提示符, 并键入`python`, 然后按Enter键。这将启动Python解释器, 你将看到一个提示符 (`>>>`) 表示你可以输入Python代码

虽然交互式命令行在**学习、测试和快速尝试代码**时非常有用, 但也有一些缺点: 

1. **不便于长期保存**: 交互式命令行通常不是一个持久性环境, 你输入的代码不会保存。如果你有一个较大的项目或需要多次运行相同的代码, 最好将其保存在脚本文件中
2. **难以维护大型代码**:  对于大型项目而言, 交互式命令行并不是一个理想的环境。编辑和组织大量代码更容易在文本编辑器或集成开发环境（IDE）中完成
3. **难以版本控制**:  交互式命令行中的输入不容易被版本控制系统（如Git）跟踪。对于团队协作或长期项目, 使用文本文件进行版本控制更为合适
4. **无法实现模块化**:  在交互式命令行中, 很难将代码模块化为函数或类, 这可能使代码更难理解和维护。
5. **缺乏自动完成和语法高亮**:  与一些高级IDE相比, 交互式命令行通常缺少自动完成和语法高亮等功能, 这些功能有助于提高代码的编写效率和可读性
6. **不适合图形界面开发**:  交互式命令行并不是专为图形用户界面（GUI）开发而设计的。GUI开发通常需要使用特定的工具和库, 而不仅仅是在命令行中输入代码

### 编写Python源代码

可以用文本编辑工具（推荐使用[Sublime](https://www.sublimetext.com/)、[Visual Studio Code](https://code.visualstudio.com/)等高级文本编辑工具）编写 `Python` 源代码并用 `py` 作为后缀名保存该文件, 代码内容如下所示。

```python
print("hello, world!")
```

### 运行程序

切换到源代码所在的目录并执行下面的命令, 看看屏幕上是否输出了"hello, world!"

```bash
python hello.py
```

### 代码中的注释

注释是编程语言的一个重要组成部分, 用于在源代码中解释代码的作用从而增强程序的可读性和可维护性, 当然也可以将源代码中不需要参与运行的代码段通过注释来去掉, 这一点在调试程序的时候经常用到。注释在随源代码进入预处理器或编译时会被移除, 不会在目标代码中保留也不会影响程序的执行结果。

1. 单行注释: 以#和空格开头的部分
2. 多行注释:三个引号开头, 三个引号结尾

```python
"""
第一个Python程序 - hello, world!
向伟大的Dennis M. Ritchie先生致敬
"""
print('hello, world!')
# print("你好, 世界！")
```

### Python开发工具

#### IDLE - 自带的集成开发工具

IDLE是安装Python环境时自带的集成开发工具, 但是由于IDLE的用户体验并不是那么好所以很少在实际开发中被采用

#### PyCharm

PyCharm是由JetBrains开发的强大Python IDE, 提供许多高级功能, 如智能代码完成、调试、版本控制集成等。有专业版和社区版可供选择。

#### Visual Studio Code (VSCode)

VSCode是一款轻量级但功能丰富的代码编辑器, 由Microsoft开发。通过插件系统, 可以扩展支持Python开发, 并提供调试、Linting等功能。

#### Jupyter Notebooks

Jupyter是一个交互式计算环境, 支持多种编程语言, 包括Python。Jupyter Notebooks允许在浏览器中创建和共享文档, 结合代码、文本和图表