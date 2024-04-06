# 函数

在Python中, 函数是一段可重复使用的代码块, 它接受输入（参数）, 执行一系列操作, 然后返回输出（结果）。函数可以用来组织代码, 提高代码的可读性和可维护性, 以及避免重复编写相同的代码片段。

Python中的函数定义使用关键字 `def`, 后跟函数的名称和参数列表。函数的基本结构如下: 

```python
def function_name(parameter1, parameter2, ...):
    # 函数体, 包含执行的代码块
    # 可以包含一些操作, 控制流语句, 返回语句等
    return result  # 返回结果（可选）
```

函数在Python中具有以下特点: 

1. **参数传递**: 函数可以接受零个或多个参数, 这些参数可以是必需的或可选的, 也可以有默认值。
2. **返回值**: 函数可以返回一个或多个值。如果没有明确指定返回值, 函数将默认返回 `None`。
3. **模块化**: 函数可以用于将代码模块化, 使代码更易于理解和维护。通过在程序中定义和调用函数, 可以使代码更具结构性。
4. **可调用性**: 函数是可调用的对象, 可以像其他对象一样传递给其他函数, 作为参数传递, 或者被存储在变量中。
5. **作用域**: 函数具有自己的作用域, 变量在函数内外是独立的。在函数内定义的变量通常称为局部变量, 而在函数外定义的变量称为全局变量。

## 内置函数

Python 解释器内置了很多函数和类型, 任何时候都能使用

![内置函数](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061458382.png)

### **abs**(x)

返回一个数的绝对值。 参数可以是整数、浮点数或任何实现了 [`__abs__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__abs__) 的对象。 如果参数是一个复数, 则返回它的模

![abs](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061458727.png)

### **all**(*iterable*)

如果 *iterable* 的所有元素均为真值（或可迭代对象为空）则返回 `True`

```python
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```

例如有多个判断条件时可以这样:

![all](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061459521.png)

### **any**(*iterable*)

如果 *iterable* 的任一元素为真值则返回 `True`。 如果可迭代对象为空, 返回 `False`

```python
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
```

### **complex**(*real=0*, *imag=0*)

返回值为 *real* + *imag*\*1j 的复数, 或将字符串或数字转换为复数。如果第一个形参是字符串, 则它被解释为一个复数, 并且函数调用时必须没有第二个形参。第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。如果省略了 *imag*, 则默认值为零, 构造函数会像 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 和 [`float`](https://docs.python.org/zh-cn/3/library/functions.html#float) 一样进行数值转换。如果两个实参都省略, 则返回 `0j`

![complex](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061459955.png)

### **dir**(*object*)

如果没有实参, 则返回当前本地作用域中的名称列表。如果有实参, 它会尝试返回该对象的有效属性列表

默认的 [`dir()`](https://docs.python.org/zh-cn/3/library/functions.html#dir) 机制对不同类型的对象行为不同, 它会试图返回最相关而不是最全的信息: 

* 如果对象是模块对象, 则列表包含模块的属性名称
* 如果对象是类型或类对象, 则列表包含它们的属性名称, 并且递归查找所有基类的属性
* 否则, 列表包含对象的属性名称, 它的类属性名称, 并且递归查找它的类的所有基类的属性

![dir](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061459555.png)

### **divmod**(*a*, *b*)

以两个（非复数）数字为参数, 在作整数除法时, 返回商和余数

* 对于整数而言, 结果与 `(a // b, a % b)` 相同
* 对于浮点数则结果为 `(q, a % b)`, 其中 *q* 通常为 `math.floor(a / b)`, 但可能比它小 1

![divmod](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061459302.png)

### **enumerate**(*iterable*, *start=0*)

返回一个枚举对象。*iterable* 必须是一个序列, 或 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator), 或其他支持迭代的对象

```python
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
```

![enumerate](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061459620.png)

### **isinstance**(*object*, *classinfo*)

如果 *object* 参数是 *classinfo* 参数的实例, 或者是其 (直接、间接或 [虚拟](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class)) 子类的实例则返回 `True`

如果 *object* 不是给定类型的对象, 则该函数总是返回 `False`

![isinstance](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061500652.png)

其他关于内置函数的详细说明请参考[python官方文档](https://docs.python.org/zh-cn/3/library/functions.html)

## 函数的参数

定义函数的时候, 我们把参数的名字和位置确定下来, 函数的接口定义就完成了。对于函数的调用者来说, 只需要知道如何传递正确的参数, 以及函数将返回什么样的值就够了, 函数内部的复杂逻辑被封装起来, 调用者无需了解

### 位置参数

位置参数是在调用函数时按照函数定义中的**参数位置**传递的参数。在函数定义中, 参数的顺序很重要, 调用函数时必须按照相同的顺序传递参数, 这样函数能够正确地识别和使用这些参数

位置参数的特点包括: 

1. **顺序敏感**: 位置参数的传递必须按照函数定义的顺序, 否则会导致参数值与参数名称不匹配, 产生错误。
2. **数量匹配**: 调用函数时必须传递与函数定义中位置参数数量相匹配的参数值, 否则也会导致错误

![power](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061500675.png)

`power(x, n)`函数有两个参数: `x`和`n`, 这两个参数都是位置参数, 调用函数时, 传入的两个值按照位置顺序依次赋给参数`x`和`n

默认参数是在函数定义时为参数指定的默认值。当调用函数时, 如果没有为该参数提供值, 将使用默认值。这使得函数在大多数情况下能够正常工作, 同时允许调用者在需要时提供定制的参数值

```python
def function_name(parameter1, parameter2=default_value):
    # 函数体
    # 可以使用 parameter1 和 parameter2
# 在这里, parameter1 是一个必需的位置参数, 而 parameter2 是一个带有默认值的参数。如果调用函数时没有提供 parameter2 的值, 将使用默认值
```

默认参数可以简化函数的调用。设置默认参数时, 有几点要注意:

!> 定义默认参数要牢记一点: 默认参数必须指向不变对象！

!> 必选参数在前, 默认参数在后

![add](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061503531.png)

### 可变参数

可变参数是允许函数接受任意数量参数的一种方式。在Python中, 有两种类型的可变参数: **位置可变参数**和**关键字可变参数**

#### **位置可变参数（args）**

位置可变参数是指在函数定义时, 允许接受可变数量的位置参数的特性。使用位置可变参数, 函数可以接受任意数量的参数, 并将它们作为**一个元组**传递给函数体, 从而实现灵活的参数传递

![args](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061503848.png)

#### 关键字可变参数（**kwargs）**

关键字可变参数允许函数接受任意数量的关键字参数。在函数定义中, 使用 `**kwargs` 表示这样的参数。这些参数将**作为一个字典**传递给函数

![kwargs](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061503485.png)

递归函数是在函数定义中调用自身的函数。通过递归, 一个问题可以被分解为更小的、类似的子问题, 从而简化解决方案。递归在一些问题上具有简洁而优雅的解决方法, 但需要小心处理, 以防止无限递归导致栈溢出

![递归函数](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061503956.png)

## 函数式编程

### 高阶函数

#### map(function, iterable)

`map()` 函数是Python内置的高阶函数之一, 用于将一个函数应用到一个或多个可迭代对象的所有元素, 生成一个新的可迭代对象

* `function`: 用于处理每个元素的函数
* `iterable`: 一个或多个可迭代对象, 可以是列表、元组等

利用`map()`函数, 把用户输入的不规范的英文名字, 变为首字母大写, 其他小写的规范名字

![map](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061504083.png)

#### reduce(function, iterable)

`reduce()` 函数是Python内置的高阶函数之一, 用于将一个二元函数累积地应用到可迭代对象的元素上, 从而返回一个单一的累积结果

* `function`: 一个二元函数, 接受两个参数并返回一个值
* `iterable`: 一个可迭代对象, 例如列表、元组等

利用`reduce()`求积

![reduce](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061504627.png)

#### filter(function, iterable)

`filter()` 函数是Python内置的高阶函数之一, 用于过滤可迭代对象中的元素, 返回符合指定条件的元素组成的迭代器

使用 `filter()` 函数过滤出列表中的偶数

![filter](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061505120.png)

利用`filter()`筛选出回数(回数是指从左向右读和从右向左读都是一样的数, 例如`12321`, `909`)

![filter](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061505116.png)

### 函数作为返回值

#### 闭包

1. **内函数定义在外函数内**: 闭包通常涉及到一个函数（内函数）, 这个内函数定义在另一个函数（外函数）内部
2. **内函数引用外函数的变量**: 内函数引用了外函数中的变量。这些变量可以是外函数的参数、局部变量, 或者外函数中定义的其他变量
3. **外函数返回内函数**: 外函数通常会返回内函数。由于内函数引用了外函数的变量, 当调用内函数时, 它仍然可以访问和操作这些变量

函数是一等公民, 这意味着你可以将函数作为其他函数的返回值。这样的函数被称为高阶函数。返回函数的函数通常用于创建可定制的、具有特定行为的函数

例如, 我们可以实现一个可变参数的求和函数:

![闭包](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061505782.png)

!> 返回函数不要引用任何循环变量, 或者后续会发生变化的变量

!> 使用闭包时, 对外层变量赋值前, 需要先使用nonlocal声明该变量不是当前函数的局部变量

### 匿名函数

匿名函数, 也称为lambda函数, 是一种在一行内定义的简单函数, 通常用于需要一个临时函数的场合。匿名函数使用`lambda`关键字来定义, 其语法格式为: `lambda arguments: expression`

以`map`函数为例, 计算$f(x)=x^2$时,除了定义一个`f(x)`的函数之外, 还可x

![lambda](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061506689.png)

### 装饰器

装饰器本质上是一个Python函数, 它可以让其他函数在不需要做任何代码变动的前提下增加额外功能, 装饰器的返回值也是一个函数对象

它经常用于有切面需求的场景, 比如: **插入日志**、**性能测试**、**事务处理**、**缓存**、**权限校验**等场景

装饰器是解决这类问题的绝佳设计, 有了装饰器, 我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用

装饰器的使用方法很固定

1. 先定义一个装饰器（帽子）
2. 再定义你的业务函数或者类（人）
3. 最后把这装饰器（帽子）扣在这个函数（人）头上

![decorator](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061506788.png)

实际上, 装饰器并不是编码必须性, 意思就是说, 你不使用装饰器完全可以, 它的出现, 应该是使我们的代码

?> 更加优雅, 代码结构更加清晰

?> 将实现特定的功能代码封装成装饰器, 提高代码复用率, 增强代码可读性

#### 普通的装饰器

首先咱来写一个最普通的装饰器, 它实现的功能是: 

* 在函数执行前, 先记录一行日志
* 在函数执行完, 再记录一行日志

![decorator](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061506721.png)

#### 带参数的函数装饰器

装饰器本身是一个函数, 做为一个函数, 如果不能传参, 那这个函数的功能就会很受限, 只能执行固定的逻辑。这意味着, 如果装饰器的逻辑代码的执行需要根据不同场景进行调整, 若不能传参的话, 我们就要写两个装饰器, 这显然是不合理的

![decorator](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061507749.png)

#### 不带参数的类装饰器

基于类装饰器的实现, 必须实现\_\_call\_\_ 和\_\_init\_\_ 两个内置函数。

* `__init__` : **接收被装饰函数**
* `__call__` : **实现装饰逻辑**

![decorator](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061507760.png)

#### 带参数的类装饰器

上面不带参数的例子, 你发现没有, 只能打印INFO 级别的日志, 正常情况下, 我们还需要打印DEBUG、WARNING 等级别的日志。这就需要给类装饰器传入参数, 给这个函数指定级别了

带参数和不带参数的类装饰器有很大的不同。

* `__init__` : 不再接收被装饰函数, 而是接收传入参数
* `__call__` : 接收被装饰函数, 实现装饰逻辑

![decorator](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061508360.png)

### 偏函数

偏函数是指通过固定一个或多个函数的参数, 从而创建一个新的函数的过程。在Python中, 可以使用 `functools` 模块的 `partial` 函数来实现偏函数。

?> 偏函数的作用是固定函数的一部分参数, 将其变为一个带有默认值的新函数。这在一些需要多次调用的函数中特别有用, 减少了重复代码

![partial](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061508747.png)
