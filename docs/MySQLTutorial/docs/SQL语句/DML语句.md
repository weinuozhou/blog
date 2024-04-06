# DML语句

DML（Data Manipulation Language）是用于操作数据库中数据的一类SQL语句。它主要包括插入（INSERT）、更新（UPDATE）和删除（DELETE）等操作。这些语句允许用户对数据库中的数据进行增删改，从而实现对数据的操作和管理。DML语句通常用于与数据库中的表进行交互，以实现对数据的操作和管理

## 插入数据

```sql
INSERT INTO 表名 (字段1, 字段2... 字段n) VALUES (值1， 值2... 值n), ...(值1， 值2... 值n); -- 手动插入数据
INSERT INTO 表名 (字段1,字段2 ...) SELECT value1, value2, ... FROM other_table [WHERE condition]; -- 从其他表导入数据
```

> 不指定字段名时，默认给所有字段赋值

* 插入数据时，字段顺序与值顺序保持一致
* 字符串和日期数据应包含引号

<div style="text-align: center;"><img alt='202403231818765' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231818765.png' width=600px> </div>

## 更新数据

```sql
UPDATE 表名 SET 字段1=值1，字段2=值2,... [where 条件]
```

<div style="text-align: center;"><img alt='202403231825958' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231825958.png' width=500px> </div>

## 删除数据

```sql
DELETE FROM 表名 [where 条件]
```

* 若没有where条件，则会删除整张表的所有数据

<div style="text-align: center;"><img alt='202403231827427' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403231827427.png' width=500px> </div>
