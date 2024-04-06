# 面向对象编程基础

面向对象编程（Object-Oriented Programming，简称OOP）是一种程序设计的方法论，其中程序被组织成对象的集合，这些对象可以相互交互，通过定义对象的属性（数据）和方法（函数）来描述问题的解决方案。

面向对象的思想有三大要素，通常被称为面向对象编程的三大特征，分别是**封装**、**继承**和**多态**。这些特征帮助程序员组织和设计代码，使得代码更加灵活、可维护和可扩展。

1. **封装（Encapsulation）**
   * 封装是将对象的状态（数据）和行为（方法）包装到一个单一的单元（类）中，对外部隐藏对象的具体实现细节
   * 封装通过使用访问修饰符（如私有、公有）来控制对对象内部成员的访问，从而实现对数据的保护
2. **继承（Inheritance）**
   * 继承是一种机制，通过它一个类（子类）可以继承另一个类（父类）的属性和方法
   * 继承提供了代码重用的机制，可以在不重新编写已有代码的情况下扩展或修改类的功能
   * 子类可以拥有父类的属性和方法，并且可以添加自己特有的属性和方法
3. **多态（Polymorphism）**
   * 多态允许不同的类对象对相同的方法名做出相应，提高了代码的灵活性
   * 多态有两种形式：编译时多态（静态多态）和运行时多态（动态多态）
   * 编译时多态是通过函数重载和运算符重载实现的，发生在编译阶
   * 运行时多态是通过方法重写（覆盖）实现的，发生在运行时

## 类与对象

### 类（Class）

* 类是一种抽象的模板，用于定义对象的属性和方法
* 类可以看作是一种用户定义的数据类型，它封装了数据（属性）和行为（方法）
* 类的定义描述了对象的特征和行为，但它本身并不占有内存空间，只有类的实例化（对象的创建）才会在内存中分配空间

在Python中，定义类是通过`class`关键字

```python
class student(object):
    pass
```

### 对象（Object）

* 对象是类的实例，是类的具体实体
* 对象是内存中的实际存在，包含了类定义的属性和方法
* 通过实例化（创建对象）可以访问类中定义的属性和方法，并且不同的对象可以拥有相同的属性和方法，但它们的具体值可能不同

定义好了`Student`类，就可以根据`Student`类创建出`Student`的实例，创建实例是通过类名+()实现的

```python
xiaoming = student()
```

### `__init__` 方法

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去

!> 特殊方法`__init__`前后分别有两个下划线

 ```python
class Student(object):
     def __init__(self, name, score):
         self.name = name
         self.score = score
 ```

### 数据封装

在上面的`Student`类中，每个实例就拥有各自的`name`和`score`这些数据,我们可以通过自定义函数来获取它们的值

```python
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score
```

### 访问限制

在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，在Python中，实例的变量名如果以`__`开头，就变成了一个私有变量（ `private` ），只有内部可以访问，外部不能访问

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
```

> [!TIP]
> 有些时候，你会看到以一个下划线开头的实例变量名，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，*虽然我可以被访问，但是，请把我视为私有变量，不要随意访问*

### 继承和多态

当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类

我们已经编写了一个名为`Animal`的class，有一个`run()`方法可以直接打印

```python
class Animal(object):
    def run(self):
        print('Animal is running...')
```

当我们需要编写`Dog`和`Cat`类时，就可以直接从`Animal`类继承

```python
class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

继承有什么好处

* 最大的好处是子类**获得了父类的全部功能**
* 继承的第二个好处需要我们对代码做一点改进
* 多态

#### 鸭子类型

鸭子类型（Duck Typing）是一种动态类型的概念，其核心思想是关注对象的行为而不是其类型。鸭子类型的名字来源于一句格言：“如果看起来像、叫声像、走起路来像鸭子，那么它就是鸭子。”这意味着在鸭子类型中，对象的适用性不是基于其继承层次结构或实现特定接口，而是基于对象的方法和属性

```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Duck:
    def sound(self):
        return "Quack!"

def make_sound(animal):
    return animal.sound()

# 使用鸭子类型
dog = Dog()
cat = Cat()
duck = Duck()

print(make_sound(dog))  # 输出 "Woof!"
print(make_sound(cat))  # 输出 "Meow!"
print(make_sound(duck))  # 输出 "Quack!"
```

在这个例子中，`make_sound` 函数接受一个动物对象作为参数，调用其 `sound` 方法来获取动物的叫声。尽管 `Dog`、`Cat` 和 `Duck` 类并没有共同的基类或接口，它们仍然可以被传递给 `make_sound` 函数，因为它们都具有相同的 `sound` 方法

### 实例属性和类属性

* **实例属性**:这些属性属于类的实例，每个实例都有自己的一组实例属性
* **类属性**:这些属性属于类本身，对所有实例共享

```python
def student(object):
    teacher = 'wang' # 类属性，所有实例共享该变量
    def __init__(self, age, name):
        self.age = age # 实例属性
        self.name = name # 实例属性
```

### 实例方法、类方法、静态方法

* 实例方法是最常见的方法类型，它是在类中定义的普通方法，可以通过类的实例调用。实例方法的第一个参数通常被命名为 `self`，它指向调用该方法的实例本身。通过 `self`，实例方法可以**访问和操作实例的属性**
* 类方法是使用 `@classmethod` 装饰器定义的方法，它使用类而不是实例作为第一个参数。通常，类方法的第一个参数被命名为 `cls`，它指向类本身。类方法可以访问和修改类级别的属性，但**不能直接访问实例属性**
* `staticmethod` 是另一种方法类型，它与实例方法和类方法不同。`staticmethod` 是一个装饰器，用于定义不依赖于实例或类的方法。这意味着，`staticmethod` 不会接受任何类似 `self` 或 `cls` 的特殊参数，它在定义时与类没有直接的关联

```python
def student(object):
    teacher = 'wang' # 类属性，所有实例共享该变量

    def __init__(self, age, name):
        self.age = age # 实例属性
        self.name = name # 实例属性

    # 实例方法
    def get_name(self):
        return self.name
        
    @classmethod
    def get_teacher(cls):
        return cls.teacher

    @staticmethod
        def add(x, y):
    return x + y
```

## 面向对象高级编程

### 使用 `__slots__`

当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性

但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加`name`和`age`属性

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

### 使用@property

* `@property` 装饰器用于将一个方法转换为只读属性。这样的属性可以像访问普通属性一样，而不需要调用方法
* `@<property_name>.setter` 装饰器用于设置属性的值。它配合 `@property` 使用，允许定义一个可写的属性

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
       if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

!> 只定义 `getter` 方法，不定义 `setter` 方法就是一个只读属性

### 特殊变量和方法

类中有一些特殊的变量和方法，它们以**双下划线开头和结尾**，被称为“魔术方法”或“特殊方法”。这些方法和变量提供了一种方式，使得类能够与Python的特定功能交互，例如迭代、比较、字符串表示等

#### `__init__` 方法

**类的构造方法，用于初始化对象**, 创建对象时会自动调用 `__init__` 方法

#### `__str__` 和 `__repr__` 方法

* 交互模式下，直接输入对象,调用的是 `__repr__` 方法
  * `__str__` 是一个对象的非正式的、易于阅读的字符串描述，当类str实例化时会被调用，以及会被内置函数 `format()` 和 `print()` 调用
* `print` 对象的时候，直接调用如果有 `__str__` 方法，则直接调用 `__str__` 方法，如果没有则调用 `__repr__` 方法，如果两个方法都没有，则正常打印类的内存地址信息
  *  `__repr__` 是一个对象的官方字符串描述，会被内置函数 `repr()` 方法调用，它的描述必须是信息丰富和明确的。也就是说 `__str__` 返回的结果可读性强 `__repr__` 返回的结果更加准确

![str](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061513734.png)

#### `__getattr__` 方法

`__getattr__` 方法是Python类中的一个特殊方法,如果你尝试访问一个不存在的属性，Python会调用该对象的 `__getattr__` 方法来处理这个情况

```python
class Example:
    def __init__(self):
        self.data = {'a': 1, 'b': 2}

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"'Example' object has no attribute '{name}'")
obj = Example()
print(obj.a)  # 输出: 1
# 尝试访问不存在的属性
print(obj.c)  # 触发 __getattr__，输出: AttributeError: 'Example' object has no attribute 'c'
```

#### `__call__` 方法

`__call__` 方法是Python中的一个特殊方法，用于使对象实例可以像函数一样被调用

```python
class CallableObject:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Object {self.name} is called with args: {args} and kwargs: {kwargs}")
obj = CallableObject("example")
# 调用实例，触发 __call__ 方法
obj(1, 2, key="value")
```

#### 特殊属性

* `__class__`: 对象所属的类
* `__doc__`: 类或对象的文档字符串(用户自定义的注释)
* `__name__`: 类的名称
* `__module__`: 类所在的模块名称
* `__dict__`: 包含类或对象的属性的字典
* `__bases__`: 类的基类元组

![class](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061514405.png)

### 元类编程

#### 类是如何产生的

类内部真正的创建是由*type*来创建

#### 如何使用`type`创建类

`type()`函数依次传入3个参数:

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. 绑定的方法或属性，注意以dict的形式传入

![type](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061514980.png)

#### 什么是元类

> [!NOTE]
> 什么是类?
> 
?> **创建对象的模板**

> [!NOTE]
> 什么是元类?

?> **创建类的模板**

type是Python在背后用来创建所有类的元类，我们熟知的类的始祖 object 也是由type创建的

![type](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061516761.png)

我们知道了类是元类的实例，所以在创建一个普通类时，其实会走元类的 `__new__` 方法

![new](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061518794.png)

#### `__new__` 方法的作用

在没有元类的情况下，每次创建实例，在先进入 `__init__` 之前都会先进入`__new__`

![new](https://cdn.jsdelivr.net/gh/weno861/image/img/202402061515078.png)

在有元类的情况下，每次创建类时，会都先进入元类的` __new__ `方法，如果你要对类进行定制，可以在这时做一些手脚

* 元类的`__new__`在创建类时就会进入，它可以获取到上层类的一切属性和方法，包括类名，魔法方法
* 而普通类的`__new__`在实例化时就会进入，它仅能获取到实例化时外界传入的属性

#### 使用元类的意义

使用元类，是要对类进行定制修改。使用元类来动态生成元类的实例，而99%的开发人员是不需要动态修改类的，因为这应该是框架才需要考虑的事

使用过 Django ORM 的人都知道，有了ORM，使得我们操作数据库，变得异常简单。

ORM的一个类(User)，就对应数据库中的一张表。id,name,email,password 就是字段

首先来定义`Field`类，它负责保存数据库表的字段名和字段类型

```python
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
```

在`Field`的基础上，进一步定义各种类型的`Field`，比如`StrField`，`IntegerField`等等

```python
class StrField(Field):
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("string value need")
        self._value = value
```

我们看到User 类继承自BaseModel ，这个BaseModel 里，定义了数据库操作的各种方法，譬如我们使用的save 函数，也可以放在这里面的。所以我们就可以来写一下这个BaseModel 类

```python
class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kw):
        for k, v in kw.items():
            setattr(self, k, v)
        return super().__init__()

    def save(self):
        db_columns = []
        db_values = []
        for column, value in self.fields.items():
            db_columns.append(str(column))
        db_values.append(str(getattr(self, column)))
        sql = "insert into {table} ({columns}) values({values})".format(
            table=self.db_table, columns=','.join(db_columns),
            values=','.join(db_values))
        pass
```

最后，来看看元类是如何实现的

```python
class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs)
        fields = {k: v for k, v in attrs.items() if isinstance(v, Field)}
        _meta = attrs.get("Meta", None)
        db_table = name.lower()
        if _meta is not None:
            table = getattr(_meta, "db_table", None)
            if table is not None:
                db_table = table
        attrs["db_table"] = db_table
        attrs["fields"] = fields
        return super().__new__(cls, name, bases, attrs)
```
