# MySQL 索引

索引是通过某种算法，构建出一个数据模型，用于快速找出在某个列中有一特定值的行，不使用索引，MySQL必须从第一条记录开始读完整个表，直到找出相关的行，表越大，查询数据所花费的时间就越多，如果表中查询的列有一个索引，MySQL能够快速到达一个位置去搜索数据文件，而不必查看所有数据，那么将会节省很大一部分时间

索引是一种特殊的数据库结构，其作用相当于一本书的目录，可以用来**快速查询数据库表**中的特定记录

## 索引概述

所有 `MySQL` 列类型都可以被索引，对相关列使用索引是提高 `select` 操作性能的最佳途径

索引分为
* **哈希索引**
  
<div style="text-align: center;"><img alt='202403311659376' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311659376.png' width=500px> </div>

* **B+树索引**

<div style="text-align: center;"><img alt='202403311659205' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311659205.png' width=500px> </div>

`InnoDB` 和 `MyISAM` 支持B树索引， `MyISAM` 支持哈希索引、B树索引但默认的是哈希索引

### 索引的优缺点

?> 优点

* 通过创建唯一性索引，可以**保证数据库表中每一行数据的唯一性**
* 可以大大**加快数据的检索速度**，这也是创建索引的最主要的原因
* 可以**加速表和表之间的连接**，特别是在实现数据的参考完整性方面特别有意义
* 在使用分组和排序子句进行数据检索时，同样可以**显著减少查询中分组和排序的时间**
* 通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能

?> 缺点

* 创建索引和维护索引要**耗费时间**，这种时间随着数据量的增加而增加
* 索引需要占**物理空间**，除了数据表占数据空间之外，每一个索引还要占一定的物理空间，如果要建立聚簇索引，那么需要的空间就会更大
* 当对表中的数据进行增加、删除和修改的时候，索引也要动态的维护，这样就**降低了数据的维护速度**

### 索引的分类

* **普通索引**
    * 可以创建在任何数据类型中，其值是否唯一和非空由字段本身的完整性约束条件决定
    * 建立索引以后，查询时可以通过**索引**进行查询
* **唯一性索引**
    * 使用 `UNIQUE` 参数可以设置索引为唯一性索引
    * 通过唯一性索引，可以更快速地确定某条记录。主键就是一种特殊唯一性索引
* **全文索引**
    * 使用 `FULLTEXT` 参数可以设置索引为全文索引
    * 全文索引只能创建在 `CHAR` 、 `VARCHAR` 或 `TEXT` 类型的字段上
    * 查询数据量较大的字符串类型的字段时，使用全文索引可以提高查询速度
    * 在默认情况下，全文索引的搜索执行方式不区分大小写。但索引的列使用二进制排序后，可以执行区分大小写的全文索引
* **单列索引**
    * 单列索引可以是普通索引，也可以是唯一性索引，还可以是全文索引。只要保证该索引只对应一个字段即可
* **多列索引**
    * 该索引指向创建时对应的多个字段，可以通过这几个字段进行查询。但是，只有查询条件中使用了这些字段中第一个字段时，索引才会被使用
* **空间索引**
    * 使用 `SPATIAL` 参数可以设置索引为空间索引
    * `MySQL` 中的空间数据类型包括 `GEOMETRY` 和 `POINT` 、 `LINESTRING` 和 `POLYGON` 等
    * 目前只有 `MyISAM` 存储引擎支持空间检索，而且索引的字段不能为空值

## 索引的定义与管理

### 创建索引

创建索引是指在某个表的一列或多列上建立一个索引

* 在已存在的表上创建索引: `CREATE [UNIQUE|FULLTEXT|SPATIAL] INDEX 索引名称 ON 表名 {字段名称[(长度)] [ASC|DESC]}`
* 使用 `ALTER TABLE` 语句来创建索引: `ALTER TABLE tbl_name ADD [UNIQUE|FULLTEXT|SPATIAL] INDEX`
* 创建表的时候创建索引

```sql
CREATE TABLE tbl_name(
字段名称 字段类型 [完整性约束条件],
…,
[UNIQUE|FULLTEXT|SPATIAL] INDEX|KEY [索引名称](字段名称[(长度)] [ASC|DESC])
);
```

* `INDEX` 或 `KEY` 参数用来指定字段为索引
* 索引名参数是用来指定要创建索引的名称
* 字段名称参数用来指定索引索要关联的字段的名称
* 长度参数用来指定索引的长度
* `ASC` 用来指定为升序， `DESC` 用来指定为降序

#### 创建普通索引

```sql
CREATE TABLE t_test4(
     id TINYINT UNSIGNED,
     username VARCHAR(20),
     INDEX in_id(id),
     KEY in_username(username)
     );
```

<div style="text-align: center;"><img alt='202403291653038' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291653038.png' width=500px> </div>

#### 创建唯一索引

```sql
CREATE TABLE t_test5(
     id TINYINT UNSIGNED AUTO_INCREMENT KEY,
     username VARCHAR(20) NOT NULL UNIQUE,
     card CHAR(18) NOT NULL,
     UNIQUE KEY uni_card(card)
     );   
```

<div style="text-align: center;"><img alt='202403291654508' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291654508.png' width=500px> </div>

!> 一个表可有多个唯一性索引，但只能有一个主键索引

#### 创建一个全文索引

```sql
CREATE TABLE t_test6(
     id TINYINT UNSIGNED AUTO_INCREMENT KEY,
     username VARCHAR(20) NOT NULL UNIQUE,
     userDesc VARCHAR(20) NOT NULL,
     FULLTEXT INDEX full_userDesc(userDesc)
     );
```

<div style="text-align: center;"><img alt='202403291654877' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291654877.png' width=500px> </div>

#### 创建单列索引

```sql
CREATE TABLE t_test7(
     id TINYINT UNSIGNED AUTO_INCREMENT KEY,
     t_test1 VARCHAR(20) NOT NULL,
     t_test2 VARCHAR(20) NOT NULL,
     t_test3 VARCHAR(20) NOT NULL,
     t_test4 VARCHAR(20) NOT NULL,
     INDEX in_test1(t_test1)
 );
```

<div style="text-align: center;"><img alt='202403291655994' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291655994.png' width=500px> </div>

#### 创建多列索引

```sql
CREATE TABLE t_test8(
     id TINYINT UNSIGNED AUTO_INCREMENT KEY,
     t_test1 VARCHAR(20) NOT NULL,
     t_test2 VARCHAR(20) NOT NULL,
     t_test3 VARCHAR(20) NOT NULL,
     t_test4 VARCHAR(20) NOT NULL,
     INDEX mul_t1_t2_t3(t_test1, t_test2, t_test3)
     );
```

<div style="text-align: center;"><img alt='202403291656049' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291656049.png' width=500px> </div>

#### 创建空间索引

```sql
CREATE TABLE t_test10(
     id TINYINT UNSIGNED AUTO_INCREMENT KEY,
     t_test GEOMETRY NOT NULL,
     SPATIAL INDEX spa_test(t_test)
     )ENGINE=MyISAM;
```

<div style="text-align: center;"><img alt='202403291657684' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403291657684.png' width=500px> </div>

### 查看索引

```sql
SHOW INDEX FROM table_name [FROM db_name]
```

### 删除索引

删除索引可以使用 `ALTER TABLE` 或 `DROP INDEX` 语句来实现
* `DROP INDEX index_name ON table_name;`
* `ALTER TABLE table_name DROP INDEX index_name;`

## 索引的设计原则和注意事项

!> 索引的设计原则

* **选择唯一性索引**
    * 唯一性索引的值是唯一的，可以更快速的通过该索引来确定某条记录
* **为经常需要排序、分组和联合操作的字段建立索引**
    * 经常需要 `ORDER BY`、 `GROUP BY`、`DISTINCT`和 `UNION` 等操作的字段，排序操作会浪费很多时间。如果为其建立索引，可以有效地避免排序操作
* **为常作为查询条件的字段建立索引**
* **限制索引的数目**
    * 索引的数目不是越多越好。每个索引都需要占用磁盘空间，索引越多，需要的磁盘空间就越大。修改表时，对索引的重构和更新很麻烦。越多的索引，会使更新表变得很浪费时间
* **尽量使用数据量少的索引**
    * 如果索引的值很长，那么查询的速度会受到影响
* **尽量使用前缀来索引**
    * 如果索引字段的值很长，最好使用值的前缀来索引
* **删除不再使用或者很少使用的索引**

!> 合理使用索引注意事项

* 在**经常需要搜索的列**上，可以加快搜索的速度
* 在**作为主键的列**上，强制该列的唯一性和组织表中数据的排列结构
* 在经常**用在连接的列**上，这些列主要是一些外键，可以加快连接的速度
* 在经常需要**根据范围进行搜索的列**上创建索引，因为索引已经排序，其指定的范围是连续的
* 在经常**需要排序的列**上创建索引，因为索引已经排序，这样查询可以利用索引的排序，加快排序查询时间
* 经常使用在 `WHERE` 子句中的列上创建索引，加快条件的判断速度

!> 不合理使用索引的注意事项

* 对于那些在查询中很少使用或者参考的列不应该创建索引
* 对于那些只有很少数据值的列也不应该增加索引
* 对于那些定义为 `text` 、 `image` 和 `bit` 数据类型的列不应该增加索引
    * 主要是由于列的数据量要么相当大，要么取值很少
* 当修改性能远远大于检索性能时，不应该创建索引
    * 由于修改性能和检索性能是互相矛盾的。当增加索引时，会提高检索性能，但是会降低修改性能。当减少索引时，会提高修改性能，降低检索性能。因此，当修改性能远远大于检索性能时，不应该创建索引



