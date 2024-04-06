# MySQL 视图

## 视图概述

视图( view )为数据查询提供了一条捷径, 视图是一个**虚拟表**，其内容由查询定义，即视图中的数据并不像表、索引那样需要占用存储空间，视图中保存的仅仅是一条 `select` 语句，其数据源来自于数据库表，或者其他视图

视图是存储在数据库中的**查询的SQL语句**，使用它主要出于两种原因:
* 安全原因，视图可以隐藏一些数据
* 可使复杂的查询易于理解和使用

> [!NOTE]
> 视图可以使用户的操作更方便，并且可以保障数据库系统安全性

<div style="text-align: center;"><img alt='202403281822159' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403281822159.png' width=500px> </div>

> [!TIP]
> **视图的优势**
> 1. 增强数据安全性
    > * 同一个数据库表可以创建不同的视图，为不同的用户分配不同的视图，这样就可以实现不同的用户只能查询或修改与之对应的数据，继而增强了数据的安全访问控制
> 2. 提高灵活性，操作变简单
    > * 使用视图可以简化数据查询操作，对于经常使用，但结构复杂的select语句，建议将其封装为一个视图
> 3. 提高数据的逻辑独立性
    > * 使应用程序和数据库表结构在一定程度上逻辑分离

## 视图的工作机制

* 当调用视图的时候，才会**执行视图中的SQL**，进行取数据操作
* 视图的内容没有存储，而是在视图被引用的时候才派生出数据
* 这样**不会占用空间**，由于是即时引用，视图的内容总是与真实表的内容是一致的

## 视图的定义与管理

### 创建视图

创建视图需要具有 `create view` 的权限，同时应该具有查询涉及的列的 `select` 权限

```sql
CREATE [OR REPLACE] 
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}] 
    [DEFINER = {user | CURRENT_USER}] 
    [SQL SECURITY {DEFINER | INVOKER}] 
    VIEW view_name [(column_list)]
AS
    select_statement;
```

1. `CREATE VIEW`：这是创建视图的关键字
2. `OR REPLACE`（可选）：如果指定了OR REPLACE，则如果同名视图已经存在，它将被替换。否则，将创建一个新视图
3. `ALGORITHM`（可选）：指定视图的算法。可选值包括UNDEFINED（默认值）、MERGE和TEMPTABLE。它们决定了MySQL优化器在查询视图时的处理方式
4. `DEFINER`（可选）：指定视图的创建者。可以是特定的用户（例如，'user'@'host'）或CURRENT_USER。如果未指定该选项，默认创建者将是当前用户
5. `SQL SECURITY`（可选）：指定视图的SQL安全性。可选值为DEFINER和INVOKER。如果设置为DEFINER，则视图将使用定义者的权限执行查询。如果设置为INVOKER，则视图将使用执行者的权限执行查询
6. `view_name`：要创建的视图的名称
7. ·（可选）：指定视图中包含的列名列表。这是可选的，如果未指定，则将使用查询结果的列名
8. `select_statement`：定义视图的查询语句。它可以是一个复杂的SELECT语句，可以包含JOIN、WHERE和其他查询子句

> [!TIP]
> * select语句不能包含 from 子句中的子查询
> * select语句不能引用系统或用户变量
> * 在定义中不能引用 temporary 表，不能创建temporary视图
> * 不能将触发程序与视图关联在一起

?> 创建一个视图，返回年龄大于19岁的学生信息

<div style="text-align: center;"><img alt='202403281929949' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403281929949.png' width=500px> </div>


### 删除视图

删除视图时，只能删除视图的定义，不会删除数据

```sql
drop view [if exsists] view_name                                              
```

### 查看视图定义

查看视图是指查看数据库中已经存在的视图的定义。查看视图必须要有 `show view` 的权限

查看视图的几种方法:
1. `desc 视图名称`
2. `show table status like '视图名'`
3. `show create view '视图名'`
4. `select * from information_schema.views where table_name ='视图名'`

### 修改视图定义

修改视图是指修改数据库中已经存在表的定义。当基本表的某些字段发生改变时，可以通过修改视图来保持视图和基本表之间的一致

```sql
create or replace  [algorithm = {undefined | merge | temptable}]
    view 视图名[ { 属性清单 } ]
    as select 语句
    [ with [ cascaded | local ] check option];
```

## 更新视图数据

对视图的更新其实就是**对表的更新**，更新视图是指通过视图来插入（insert）、更新（update）和删除（delete）表中的数据。因为视图是一个虚拟表，其中没有数据

检查视图分为 **local检查视图**与 **cascade检查视图**

* `with_check_option` 的值为1时表示 `local`（`local`视图），通过检查视图对表进行更新操作时，只有满足了视图检查条件的更新语句才能够顺利执行
* `with_check_option`值为2时表示 `cascade`（级联视图，在视图的基础上再次创建另一个视图），通过级联视图对表进行更新操作时，只有满足所有针对该视图的所有视图的检查条件的更新语句才能够顺利执行

### 视图无法更新的情况

1. 视图中包含 `sum()`，`count()`等聚合函数的
2. 视图中包含 `union`、`union all`、`distinct`、`group by`、`having`等关键字的
3. 常量视图，比如：`create view view_now as select now()`
4. 视图中包含**子查询**
5. 由不可更新的视图导出的视图
6. 创建视图时 `algorithm` 为 `temptable` 类型
7. 视图对应的表上存在没有默认值的列，而且该列没有包含在视图里
8. `with [cascaded|local] check option`也将决定视图是否可以更新
    * `local` 参数表示更新视图时要满足该视图本身定义的条件即可
    * `cascaded` 参数表示更新视图时要满足所有相关视图和表的条件，默认值

## 对视图的进一步说明

视图是在原有的表或者视图的基础上**重新定义的虚拟表**，这可以从原有的表上选取对用户有用的信息。那些对用户没有用，或者用户没有权限了解的信息，都可以直接屏蔽掉

视图的作用:

* **使操作简单化**
    * 视图需要达到的目的就是所见即所需。也就是说，从视图看到的信息就是所需要了解的信息。视图可以简化对数据的操作
* **增加数据的安全性**
    * 通过视图，用户只能查询和修改指定的数据。数据库授权命令可以限制用户的操作权限，但不能限制到特定行和列上。这样可以保证敏感信息不会被没有权限的人看到，可以保证一些机密信息的安全
* **提高表的逻辑独立性**
    * 视图可以屏蔽原有表结构变化带来的影响

