# DDL 语句

## 数据库操作

1. 查询所有数据库

  ```sql
  show databases;
  ```

2. 查询当前数据库

  ```sql
  select databse();
  ```

3. 创建数据库

  ```sql
  create database [if not exists] 数据库名 [default charset 字符集] [collate 排序规则];
  ```

4. 删除数据库

  ```sql
  drop database [if exists] 数据库名;
  ```

5. 使用(切换)数据库

  ```sql
  use 数据库名;
  ```

<div style="text-align: center;">
  <img alt='202403231029910' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231029910.png' width=500px> </div>

## 表操作

### 查询表

1. 查询当前数据库的所有表

```sql
show tables;
```

2. 查询表结构

```sql
desc 表名;
```

3. 查询指定表的建表语句

```sql
show create table 表名;
```

<div style="text-align: center;">
  <img alt='202403231035305' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231035305.png' width=500px> </div>

### 创建表

```sql
create table [if not exists] 表名(
 字段1 字段1类型 [comment 字段1注释],
  字段2 字段2类型 [comment 字段2注释],
  ...
  字段n 字段n类型 [comment 字段n注释]
)[engine=存储引擎] [default charset=字符集] [comment 表注释];
```

<div style="text-align: center;">
  <img alt='202403231040357' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231040357.png' width=500px> </div>
  
#### 数据类型

1. **整数类型**：
   - TINYINT: 1 字节整数，范围从 -128 到 127 （有符号），或者从 0 到 255 （无符号）.
   - SMALLINT: 2 字节整数，范围从 -32768 到 32767 （有符号），或者从 0 到 65535 （无符号）.
   - MEDIUMINT: 3 字节整数，范围从 -8388608 到 8388607 （有符号），或者从 0 到 16777215 （无符号）.
   - INT 或 INTEGER: 4 字节整数，范围从 -2147483648 到 2147483647 （有符号），或者从 0 到 4294967295 （无符号）.
   - BIGINT: 8 字节整数，范围从 -9223372036854775808 到 9223372036854775807 （有符号），或者从 0 到 18446744073709551615 （无符号）.
2. **小数和浮点数类型**：
   - FLOAT: 单精度浮点数.
   - DOUBLE: 双精度浮点数.
   - DECIMAL 或 DEC: 固定精度的小数类型.
3. **字符串类型**：
   - CHAR: 定长字符串.
   - VARCHAR: 变长字符串.
   - BINARY: 定长二进制字符串.
   - VARBINARY: 变长二进制字符串.
   - TINYBLOB: 不超过 255 个字符的二进制大对象.
   - TINYTEXT: 不超过 255 个字符的文本大对象.
   - BLOB: 二进制大对象.
   - TEXT: 文本大对象.
   - MEDIUMBLOB: 介于 TINYBLOB 和 BLOB 之间的二进制大对象.
   - MEDIUMTEXT: 介于 TINYTEXT 和 TEXT 之间的文本大对象.
   - LONGBLOB: 介于 BLOB 和 TINYBLOB 之间的二进制大对象.
   - LONGTEXT: 介于 TEXT 和 MEDIUMTEXT 之间的文本大对象.
   - ENUM: 枚举类型，存储字符串对象的一种.
   - SET: 集合类型，存储零个或多个字符串对象的集合.
4. **日期和时间类型**：
   - DATE: 日期值.
   - TIME: 时间值.
   - DATETIME: 日期和时间值.
   - TIMESTAMP: 时间戳，存储从1970年1月1日至今的秒数.
   - YEAR: 年份值.
5. **其他类型**：
   - BOOL 或 BOOLEAN: 布尔类型，通常用 0 表示假，1 表示真.
   - JSON: JSON 数据类型，用于存储 JSON 数据.

### 修改表

在 MySQL 中可以使用 **ALTER TABLE** 语句来改变原有表的结构，例如**增加或删减列**、**更改原有列类型**、**重新命名列或表**等

```sql
ALTER TABLE 表名 [修改选项]
--修改选项包括以下:
ADD COLUMN <列名> <类型> [comment 注释] [约束] -- 新增一列
CHANGE COLUMN <旧列名> <新列名> <新列类型> -- 修改列名和数据类型
ALTER COLUMN <列名> { SET DEFAULT <默认值> | DROP DEFAULT } -- 修改数据表
MODIFY COLUMN <列名> <类型> --修改列名或数据类型
DROP COLUMN <列名> -- 删除列
RENAME TO <新表名> -- 修改表名
CHARACTER SET <字符集名> -- 修改字符集
COLLATE <校对规则名>  -- 修改排序规则
```

#### 添加字段

```sql
ALTER TABLE 表名 ADD COLUMN <列名> <类型> [comment 注释] [约束]; -- 新增一列
```

<div style="text-align: center;">
  <img alt='202403231413165' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231413165.png' width=500px> </div>

#### 修改数据类型

```sql
ALTER TABLE 表名 CHANGE COLUMN <旧列名> <新列名> <新列类型>; -- 修改列名和数据类型
```

<div style="text-align: center;">
  <img alt='202403231421221' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231421221.png' width=500px> </div>

#### 删除字段

```sql
ALTER TABLE 表名 DROP COLUMN <列名>;
```

<div style="text-align: center;">
  <img alt='202403231423475' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231423475.png' width=500px> </div>

#### 修改表名

```sql
ALTER TABLE 表名 RENAME TO 新表名;
```

<div style="text-align: center;">
  <img alt='202403231628484' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231628484.png' width=500px> </div>

### 删除表

```sql
DROP TABLE [if exists] 表名; -- 删除表
TRUNCATE TABLE 表名; -- 清除表中的所有数据 
```

<div style="text-align: center;"><img alt='202403231632938' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231632938.png' width=500px> </div>
