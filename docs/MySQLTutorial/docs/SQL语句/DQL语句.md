# DQL 语句

DQL（Data Query Language）是用于在数据库中查询数据的语言。它主要包含SELECT语句，用于从数据库表中检索数据。DQL通常被用于执行**数据查询**操作，以获取所需的数据结果集

为了下面演示方便，我们现在创建以下四个表:

1. 专业表（specialty）

```sql
create table specialty(
    zno int primary key,
    zname char(10) not null
);
```

<div style="text-align: center;"><img alt='202403261624800' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261624800.png' width=500px> </div>

2. 课程表（course）

```sql
create table course(
    cno int primary key,
    cname char(10) unique,
    ccredit int,
    cdept varchar(20)
);
```

<div style="text-align: center;"><img alt='202403261625792' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261625792.png' width=500px> </div>

3. 学生表（student）

```sql
create table student(
    sno int primary key,
    ssex char(2) default '男',
    sname char(10) not null unique,
    sclass char(20),
    sbirth date,
    CONSTRAINT student_ibfk_1 FOREIGN KEY (zno) REFERENCES specialty (zno) 
    ON DELETE SET NULL ON UPDATE CASCADE
);
```

<div style="text-align: center;"><img alt='202403261625802' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261625802.png' width=500px> </div>

4. 选修表（sc）

```sql
create table sc(
    sno int,
    cno int,
    grade int check (grade between 0 and 100),
    primary key(sno,cno),
    CONSTRAINT `sc_ibfk_1` FOREIGN KEY (sno) REFERENCES student (sno)
    ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT `sc_ibfk_2` FOREIGN KEY (cno) REFERENCES course (cno)
    ON DELETE CASCADE ON UPDATE CASCADE
);
```

<div style="text-align: center;"><img alt='202403261626957' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261626957.png' width=500px> </div>

## 基础查询

```sql
SELECT 字段列表 from 表名列表
where 条件列表
GROUP BY 分组字段列表
HAVING 分组后条件列表
ORDER BY 排序字段列表
LIMIT 分页参数
```

### 查询多个字段与设置别名

```sql
select 字段1，字段2... from 表名
select * from 表名 -- 查询所有字段
select 字段1 as 别名1, ... from 表名
```

<div style="text-align: center;"><img alt='202403231839412' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231839412.png' width=500px> </div>

### 条件查询

* 比较运算符条件

|  比较运算符   |                   功能                   |
| :-----------: | :--------------------------------------: |
|       >       |                   大于                   |
|      >=       |                 大于等于                 |
|       <       |                   小于                   |
|      <=       |                 小于等于                 |
|    <>或!=     |                  不等于                  |
| BETWEEN...AND |       在某个范围之间(含最大最小值)       |
|    IN(...)    |                  多选一                  |
|  LIKE 占位符  | 模糊匹配(_匹配一个字符, %匹配任意个字符) |
|    IS NULL    |                  是空值                  |
|REGEXP '匹配方式'| 匹配正则表达式|


* 逻辑运算符条件

| 逻辑运算符 | 功能 |
| ---------- | ---- |
| AND 或 &&  | 并且 |
| OR 或 \|\| | 或者 |
| NOT 或 !   | 非   |

?> 1. 查询姓名为两个字的学生信息

<div style="text-align: center;"><img alt='202403231851965' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231851965.png' width=500px> </div>

?> 2. 查询年龄在18，19，20岁之间的学生信息(注意这里的字段是出生日期)

<div style="text-align: center;"><img alt='202403231930761' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231930761.png' width=500px> </div>

### 聚合函数

* 将某一列数据作为整体，进行纵向计算
* 常见的聚合函数

| 聚合函数 |  描述  |
| :------: | :----: |
|  count   |  计数  |
|   max    | 最大值 |
|   min    | 最小值 |
|   avg    | 平均值 |
|   sum    |  求和  |

!> sql中count(*)、count(col)、count(1)区别

count(\*)是针对于**全表**的，而count(列)是针对于某一列的，如果此列值为空的话，count(列)是不会统计这一行的。也就是说count(列)会用到索引，并且会过滤掉该列为null的那行。而count(\*)是全表扫描，并且只要某一条数据有一列不为null，那就会统计到这条数据。 count(1)可以理解为表里有一列数据都为1的列。count(\*)执行时会把星号翻译成字段的具体名字，效果也是一样的，不过多了一个翻译的动作，比固定值的方式效率稍微低一些。


?> 1. 统计男同学的年龄之和

<div style="text-align: center;"><img alt='202403231947793' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231947793.png' width=500px> </div>

?> 2. 统计学生的数量

<div style="text-align: center;"><img alt='202403231948419' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231948419.png' width=500px> </div>

### 分组查询

```sql
select 字段列表 from 表名 [where 条件] group by 分组列表 [having 分组过滤条件]
```

* where 和 having的区别
  * where 是**分组之前过滤**，不满足where 条件不参与分组
  * where **不能对聚合函数**进行判断
* 分组之后，查询的字段一般是**聚合函数和分组字段**

?> 1. 统计出男同学和女同学的数量

<div style="text-align: center;"><img alt='202403231951155' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231951155.png' width=500px> </div>

?> 2. 统计出男女同学的平均年龄

<div style="text-align: center;"><img alt='202403231946779' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231946779.png' width=500px> </div>

?> 3.  查询平均年龄小于20的专业	

<div style="text-align: center;"><img alt='202403231958079' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231958079.png' width=500px> </div>

### 排序查询

```sql
select 字段列表 from 表名 order by 字段1 排序方式 字段2 排序方式
```

* ASC: 升序排序(默认)
* DESC: 降序排序

?> 1. 按照年龄进行降序排序

<div style="text-align: center;"><img alt='202403232003563' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403232003563.png' width=500px> </div>

?> 2. 查询性别为男，并且年龄在18-19岁以内名字为3个字的学生信息，按照年龄降序排序

<div style="text-align: center;"><img alt='202403232011131' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403232011131.png' width=500px> </div>

### 分页查询

```sql
select 字段列表 from 表名 limit 起始索引， 查询记录数;
```

* 起始索引从0开始， $\text{起始索引}=(\text{查询页码}-1) \times \text{展示记录数}$
* 查询第一页则起始索引可以忽略，即limit 展示记录数

?> 1. 查询第2页的客户数据，每页展示10条记录

<div style="text-align: center;"><img alt='202403232009806' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403232009806.png' width=500px> </div>

### DQL 语句的执行顺序

1. **FROM**：指定要从中检索数据的表或视图
2. **WHERE**：对 FROM 子句中指定的表进行筛选，只返回满足条件的行
3. **GROUP BY**：按照指定的列对结果进行分组
4. **HAVING**：类似于 WHERE 子句，但是用于对 GROUP BY 分组后的数据进行筛选
5. **SELECT**：选择要检索的列
6. **ORDER BY**：对结果进行排序
7. **LIMIT/OFFSET**：限制返回的行数和偏移量（如果需要）

## 多表查询

### 多表关系

mysql相互关联的表之间存在一对一，一对多（多对一），多对多的关系

* 一对一: 这种关系即多个表具有相同的主键，实际中用的并不多，因为完全可以将这种关系的合并为同一张表
* 一对多: 其中表1的主键是表2的外键（即表1的某字段作为主键，表2的相同字段字段绑定到表1的主键字段上）
* 多对多: 这种关系在实际中也很常见，比如：一个老师教很多学生的课，一个学生选了很多老师的课。那么，老师和学生之间就是多对多的关系

### 多表查询分类

* 内连接查询
  * 内连接： 相当于查询A、B交集部分的数据
  * 自连接: 当前表与自身的连接查询, 自连接必须使用表别名
* 外连接查询
  * 左外连接: 查询**左表**所有数据以及两张表交集部分
  * 右外连接: 查询**右表**所有数据以及两张表交集部分
* 子查询: 将一个查询语句嵌套在另一个查询语句中。内层查询语句的查询结果，可以作为外层查询语句提供条件。执行时是从内层查询到外层查询
* 联合查询: 将多条查询语句合并成一个查询结果集

#### 内连接

内连接查询的是两张表的交集部分，也就是A、B交集部分的数据

* 隐式内连接

```sql
SELECT 字段列表 FROM 表1, 表2 WHERE 条件;
```

* 显式内连接

```sql
SELECT 字段列表 FROM 表1 [INNER] JOIN 表2 ON 连接条件;
```

?> 1. 查询每个学生的姓名，以及关联的专业的名称(隐式内连接)

<div style="text-align: center;"><img alt='202403261655734' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261655734.png' width=500px> </div>

?> 2. 查询每个学生的姓名，以及关联的专业的名称(显式内连接)

<div style="text-align: center;"><img alt='202403261656814' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261656814.png' width=500px> </div>

#### 外连接

* 左外连接: 查询表1所有数据，以及两张表交集部分

```sql
select 字段列表 from 表1 left [outer] join 表2 on 条件;
```

* 右外连接: 查询表2所有数据，以及两张表交集部分

```sql
select 字段列表 from 表1 right [outer] join 表2 on 条件;
```

?> 1. 查询所有学生的信息以及对应的专业名称(左外连接)

<div style="text-align: center;"><img alt='202403261855792' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261855792.png' width=500px> </div>

?> 2. 查询所有的专业及对应的学生姓名(右外连接)

<div style="text-align: center;"><img alt='202403261856131' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261856131.png' width=500px> </div>

#### 自连接

```sql
select 字段列表 from 表A 别名A join 表A 别名B on 连接条件
```

!> 自连接可以是内连接也可以是外连接

#### 联合查询

对于联合查询，就是将多个查询结果合并起来，形成一个新的查询结果

```sql
select 字段列表 from 表A
UNION [ALL]
select 字段列表 from 表B
```

* 默认情况下，会去除相同行，如果需要保留重复行，使用 UNION ALL

?> 查询年龄大于18的学生信息，和名字是3个字的学生信息(联合查询)

<div style="text-align: center;"><img alt='202403261906418' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261906418.png' width=500px> </div>

#### 子查询

SQL 语句嵌套 SELECT 语句，又称嵌套查询

```sql
select 字段列表 from 表1 where columns = (select 字段 from 表2 where condition)
```

!> 子查询外部语句可以是 INSERT、UPDATE、DELETE和SELECT的任何一个

根据子查询的结果不同，可以分为:

* 标量子查询(子查询的结果为一个值)
* 列子查询(子查询的结果为一列)
* 行子查询(子查询的结果为一行)
* 表子查询(子查询的结果为一张表)

##### 标量子查询

?> 查询工商的所有学生信息

<div style="text-align: center;"><img alt='202403261918337' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261918337.png' width=500px> </div>

##### 列子查询

?> 查询工商和机电的所有学生信息

<div style="text-align: center;"><img alt='202403261919892' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261919892.png' width=500px> </div>

##### EXISTS 关键字

exists 关键字表示存在，使用 exists 关键字时，内查询语句不返回查询的记录。而是返回一个真假值

?> 如果存在机电这个专业，就查询所有的课程信息

<div style="text-align: center;"><img alt='202403261937120' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261937120.png' width=500px> </div>

##### ANY 关键字

ANY关键字表示满足其中任何一个条件。使用ANY关键字时。只要满足内查询语句返回结果中的一个，就可以通过该条件来执行外层查询语句

?> 查询比其他班级（比如，机电2104班级）某一个同学年龄小的学生的姓名和年龄

<div style="text-align: center;"><img alt='202403261941725' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261941725.png' width=500px> </div>

##### ALL关键字

ALL关键字表示满足所有的条件。使用ALL关键字时，只有满足内层查询语句返回的所有结果，才能执行外层的查询语句。 \>ALL表示大于所有的值，\<ALL表示小于所有的值

?> 查询比其他班级（比如机电2104班级）所有同学年龄都大的学生的姓名和年龄

<div style="text-align: center;"><img alt='202403261943009' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261943009.png' width=500px> </div>


