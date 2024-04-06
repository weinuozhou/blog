# Python中的异常处理

错误可（至少）被分为两种: *语法错误* 和 *异常*

## 语法错误

![语法错误](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061930487.png)

解析器会复现出现句法错误的代码行, 并用小箭头指向行里检测到的第一个错误。错误是由箭头上方的`token`触发的(至少是在这里检测出的)本例中, 在`print()`函数中检测到错误, 因为, 在它前面缺少冒号

## 异常处理

即使语句或表达式使用了正确的语法, 执行时仍可能触发错误。执行时检测到的错误称为*异常*

![Exception](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061934340.png)

异常处理在任何一门编程语言里都是值得关注的一个话题, 良好的异常处理可以让你的程序更加健壮, 清晰的错误信息更能帮助你快速修复问题。在Python中, 和不部分高级语言一样, 使用了`try/except/finally`语句块来处理异常, 如果你有其他编程语言的经验, 实践起来并不难

常见的异常类型如下

| 异常名称                  | 类型描述                             |
| :---:| :---:|
| BaseException             | 所有异常的基类                       |
| SystemExit                | 解释器请求退出                       |
| KeyboardInterrupt         | 用户中断执行(通常是输入^C)           |
| Exception                 | 常规错误的基类                       |
| StopIteration             | 迭代器没有更多的值                   |
| GeneratorExit             | 生成器(generator)发生异常来通知退出  |
| StandardError             | 所有的内建标准异常的基类             |
| ArithmeticError           | 所有数值计算错误的基类               |
| FloatingPointError        | 浮点计算错误                         |
| OverflowError             | 数值运算超出最大限制                 |
| ZeroDivisionError         | 除(或取模)零                         |
| AssertionError            | 断言语句失败                         |
| AttributeError            | 对象没有这个属性                     |
| EOFError                  | 没有内建输入,到达EOF                 |
| EnvironmentError          | 操作系统错误的基类                   |
| IOError                   | 输入/输出操作失败                    |
| OSError                   | 操作系统错误                         |
| WindowsError              | 系统调用失败                         |
| ImportError               | 导入模块/对象失败                    |
| LookupError               | 无效数据查询的基类                   |
| IndexError                | 序列中没有此索引(index)              |
| KeyError                  | 映射中没有这个键                     |
| MemoryError               | 内存溢出错误(对于Python)              |
| NameError                 | 未声明/初始化对象                    |
| UnboundLocalError         | 访问未初始化的本地变量               |
| ReferenceError            | 弱引用(Weak)                          |
| RuntimeError              | 一般的运行时错误                     |
| NotImplementedError       | 尚未实现的方法                       |
| SyntaxError               | Python                               |
| IndentationError          | 缩进错误                             |
| TabError                  | Tab                                  |
| SystemError               | 一般的解释器系统错误                 |
| TypeError                 | 对类型无效的操作                     |
| ValueError                | 传入无效的参数                       |
| UnicodeError              | Unicode                              |
| UnicodeDecodeError        | Unicode                              |
| UnicodeEncodeError        | Unicode                              |
| UnicodeTranslateError     | Unicode                              |
| Warning                   | 警告的基类                           |
| DeprecationWarning        | 关于被弃用的特征的警告               |
| FutureWarning             | 关于构造将来语义会有改变的警告       |
| OverflowWarning           | 旧的关于自动提升为长整型(long)的警告 |
| PendingDeprecationWarning | 关于特性将会被废弃的警告             |
| RuntimeWarning            | 可疑的运行时行为(runtime)             |
| SyntaxWarning             | 可疑的语法的警告                     |
| UserWarning               | 用户代码生成的警告                   |

Python异常类的层次关系如下:

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402061947898.png'></center>

### try-except块

`try-except` 块用于捕获可能发生异常的代码块。在 `try` 语句块中放置可能引发异常的代码, 而在 `except` 语句块中处理捕获到的异常。如果 `try` 语句块中的代码引发了异常,  `Python` 将跳过该块的剩余部分, 并尝试在 `except` 语句块中处理异常。如果没有发生异常, 则 `except` 语句块将被忽略

`try` 语句的工作原理如下: 

* 首先, 执行 `try` 子句 （ `try` 和 `except` 关键字之间的（多行）语句）
* 如果没有触发异常, 则跳过 `except` 子句,  `try` 语句执行完毕
* 如果在执行 try 子句时发生了异常, 则跳过该子句中剩下的部分。 如果异常的类型与 `except` 关键字后指定的异常相匹配, 则会执行 `except` 子句, 然后跳到 `try/except` 代码块之后继续执行。
* 如果发生的异常与 `except` 子句中指定的异常不匹配, 则它会被传递到外层的 `try` 语句中；如果没有找到处理句柄, 则它是一个未处理异常且执行将停止并输出一条错误消息

```python
try:
    # 可能引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 异常处理代码
    print("Error: Division by zero")
```

### 捕获多个异常

可以使用多个 `except` 语句块来捕获不同类型的异常, 并针对每种类型的异常执行不同的处理逻辑

```python
try:
    # 可能引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理除零异常
    print("Error: Division by zero")
except ValueError:
    # 处理值错误异常
    print("Error: Value error")
```

### 捕获所有异常

如果你想捕获所有类型的异常, 可以使用 `except` 语句块而不指定特定的异常类型

```python
try:
    # 可能引发异常的代码
    result = 10 / 0
except:
    # 处理所有异常
    print("An error occurred")
```

### finally块

如果存在 [`finally`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#finally) 子句, 则 `finally` 子句是 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 语句结束前执行的最后一项任务。不论 `try` 语句是否触发异常, 都会执行 `finally` 子句。以下内容介绍了几种比较复杂的触发异常情景: 

* 如果执行 `try` 子句期间触发了某个异常, 则某个 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 子句应处理该异常。如果该异常没有 `except` 子句处理, 在 `finally` 子句执行后会被重新触发。
* `except` 或 `else` 子句执行期间也会触发异常。 同样, 该异常会在 `finally` 子句执行之后被重新触发
* 如果 `finally` 子句中包含 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break)、[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 或 [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) 等语句, 异常将不会被重新引发
* 如果执行 `try` 语句时遇到 [`break`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#break),、[`continue`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#continue) 或 [`return`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#return) 语句, 则 `finally` 子句在执行 `break`、`continue` 或 `return` 语句之前执行
* 如果 `finally` 子句中包含 `return` 语句, 则返回值来自 `finally` 子句的某个 `return` 语句的返回值, 而不是来自 `try` 子句的 `return` 语句的返回值

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
```

### 自定义异常

还可以定义自己的异常类, 以便根据特定的业务逻辑引发和捕获异常

```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("An error occurred")
except MyCustomError as e:
    print("Custom error:", e)
```

1. `except`语句不是必须的, `finally`语句也不是必须的, 但是二者必须要有一个, 否则就没有`try`的意义了。
2. `except`语句可以有多个, Python会按`except`语句的顺序依次匹配你指定的异常, 如果异常已经处理就不会再进入后面的`except`语句。
3. `except`语句可以以元组形式同时指定多个异常, 参见实例代码。
4. `except`语句后面如果不指定异常类型, 则默认捕获所有异常, 你可以通过 `logging` 或者 `sys` 模块获取当前异常。
5. 如果要捕获异常后要重复抛出, 请使用`raise`, 后面不要带任何参数或信息
6. 不建议捕获并**抛出同一个异常**, 请考虑重构你的代码
7. 不建议在**不清楚逻辑的情况下捕获所有异常**, 有可能你隐藏了很严重的问题
8. 尽量使用**内置的异常处理语句**来替换`try/except`语句, 比如`with`语句, `getattr()`方法

## 抛出异常 raise

如果你需要自主抛出异常一个异常, 可以使用raise关键字

```python
raise NameError("bad name!")
```

`raise` 关键字后面可以指定你要抛出的异常实例, 一般来说抛出的异常越详细越好, Python在`builtins`模块内建了很多的异常类型, 通过使用 `dir()` 函数来查看异常类型

![异常类型](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061646979.png)

## 使用内置的语法范式代替try/except

Python 本身提供了很多的语法范式简化了异常的处理

* `for`语句处理了的`StopIteration`异常, 让你很流畅地写出一个循环
* `with`语句在打开文件后会自动调用`finally`并关闭文件
* `getattr()`访问一个不确定的属性

## 最佳实践

1. **精细化捕获异常**:尽可能地精细化捕获异常, 只捕获你能够处理的特定异常类型, 而不是捕获所有异常。这样可以避免隐藏潜在的错误, 同时使代码更加可读和可维护,*只处理你知道的异常, 避免捕获所有异常然后吞掉它们*
2. **避免在Except语句块中干一些没意义的事情**, 捕获异常也是需要成本的
3. **处理异常的同时提供有用的信息**:在捕获异常时, 提供有用的信息来描述发生了什么错误以及如何解决它
4. **使用 finally 块进行清理工作**:在 `try-except` 块之后使用 `finally` 块来执行清理工作, 例如释放资源或回滚操作
