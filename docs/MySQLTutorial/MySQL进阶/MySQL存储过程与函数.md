# MySQL 存储过程与函数

存储过程和存储函数是在数据库中**定义一些被用户定义的SQL语句集合**，这可以避免开发人员重复地编写相同的 `SQL` 语句。一个存储程序是可以被存储在服务器中的一套 `SQL` 语句。存储过程可以被程序，触发器或另一个存储过程调用

## 存储过程与函数简介

存储过程（stored procedure）是一组为了完成特定功能的**SQL语句集**，经编译后存储在数据库中，用户通过指定存储过程的名字并给定参数（如果该存储过程带有参数）来调用执行它

一个存储过程是一个**可编程的函数**，它在数据库中创建并保存。数据库中的存储过程可以看作是对编程中面向对象方法的模拟。它允许控制数据的访问方式

> [!TIP]
> 存储过程的优点

* 增强了SQL语言的**功能和灵活性**
* 存储过程被创建后，**可以在程序中被多次调用**，而不必重新编写该存储过程的SQL语句
* 能实现**较快的执行速度**
* 能过减少网络流量
* 可被作为一种安全机制来充分利用

### 存储过程和函数区别

* 一般来说，存储过程实现的功能要复杂一点，而函数的实现的功能针对性比较强
* 对于存储过程来说可以**返回参数**，如记录集，而函数只能**返回值或者表对象**。函数只能返回一个变量；而存储过程可以返回多个。存储过程声明时**不需要返回类型**，而函数声明时需要描述返回类型，且函数体中必须包含一个有效的 `return` 语句
* 存储过程，**可以使用非确定函数**，不允许在用户定义函数主体中内置非确定函数
* 存储过程一般是作为一个独立的部分来执行（ `execute` 语句执行），而函数可以作为查询语句的一个部分来调用（`select`调用）。 `SQL` 语句中不可用存储过程，而可以使用函数

## 存储过程与函数操作

### `delimiter` 命令

用 `MySQL delimiter` 来改变默认的结束标志

`delimiter` 格式语法为: `delimiter $$`

?> $$是用户定义的结束符，通常使用一些特殊的符号。当使用 `delimiter` 命令时，应该避免使用反斜杠\字符，因为那是 `MySQL` 转移字符

### 创建和使用存储过程

创建存储过程的语法格式:
```sql
delimiter 自定义结束符号
create procedure sp_name([ in ,out ,inout ] 参数名 数据类形...)
begin
  sql语句
end 自定义的结束符合
delimiter ;                                                                    
```

* `sp_name` 参数是存储过程的名称
* 可以用 `begin…end` 来标志 `SQL` 代码的开始和结束

调用存储过程的语法格式：
```sql
call sp_name([parameter[，…]]) 
```

### 创建和使用函数

创建函数语法格式:
```sql
create function sp_name ([func_parameter[，..]])                                                                      
    returns type                                                                      
    [characteristic ..] routine_body
```

* `sp_name` 参数是存储函数的名称
* `func_parameter` 表示存储函数的参数列表
* `returns type` 指定返回值的类型
* `characteristic` 参数指定存储函数的特性

调用函数的语法格式:
```sql
select sp_name([func_parameter[，…]])
```

## 查看存储过程或函数

### 查看存储过程或函数的状态

```sql
show {procedure | function} status 
[like 'pattern']; 
```

* `procedure` 该关键字表示查询存储过程
* `function` 表示查询自定义函数
* `like 'pattern'`该参数用来匹配存储过程或自定义函数的名称

### 查看存储过程或函数的具体信息

```sql
show create { procedure | function} sp_name; 
```

* `procedure` 表示查询存储过程
* `function` 表示查询自定义函数

### 查看所有的存储过程

```sql
select * from information_schema.routines [where routine_name = '名称']; 
```

!> 创建存储过程或自定义函数成功后，这些信息会存储在information_schema数据库下的routines表中，用户可以通过执行select语句查询该表中的所有记录或单条记录的信息

## 删除存储过程或函数

```sql
drop procedure | function [if exists] name; 
```

## 变量

### 申明局部变量

用户可以使用 `declare` 关键字来定义变量，然后可以为变量赋值。 `declare` 语句申明局部的变量只适用于`begin…end`程序段中。 `declare` 语法格式:
```sql
declare var_name1 [,var_name2] . . . type [ default value ]
```

* `var_name1` , `var_name2` 参数是声明的变量的名称, 这里可以定义多个变量
* `type` 参数用来指明变量的类型
* `defalut value` 字句将变量默认值设置为 `value`

### 赋值变量

用 `set` 语句给变量赋值,`set`语句格式为:
```sql
set var_name = exper[,var_name = exper]
```

* `var_name` 参数是变量的名称
* `expr` 参数是赋值的表达式

当然，还可以使用 `select` 语句给变量赋值, 语句格式为:
```sql
select col_name[,. . . ] into var_name[, . . .] table_expr
```

* `col_name` 是列名
* `var_name` 是要赋值的变量名称
* `table_var` 是 `select` 语句中的 `from` 字句以及后面的部分

## 游标的使用

使用 `MySQL` 作为数据库的话，程序员肯定要写很多存储过程，function等。其中，游标肯定是少不了的。我们可以认为游标就是一个 `cursor` ，就是一个标识，**用来标识数据取到什么地方**了。你也可以把它理解成数组中的下标

### 声明游标


```sql
declare cursorname cursor for select_statement
```

* `cursorname` 是游标的名称
* `select_statement` 是一个 `select` 语句

### 打开游标

```sql
open cursor_name
```

!> 在程序中，一个游标可以打开多次，由于其他的用户或程序本身已经更新了表，所以每次打开结果可能不同

### 读取数据

游标打开后，就可以使用 `fetch… into`语句从中读取数据

```sql
fetch cursor_name into var_name [， var_name] …
```

* `var_name` 是存放数据的变量名
* `fetch` 语句是将游标指向的一行数据赋给一些变量，子句中变量的数目必须等于声明游标时 `select` 子句中列的数目

### 关闭游标     

游标使用完以后，要及时关闭。关闭游标使用close语句
```sql
close cursorname
```













