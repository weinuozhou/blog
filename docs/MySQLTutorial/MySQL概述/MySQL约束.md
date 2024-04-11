# MySQL 完整性约束控制

`MySQL` 的完整性约束是一种用于确保数据库中数据的**有效性**和**一致性**的规则或条件。它们定义了对表中数据的限制和要求，以防止不符合预期的数据插入、更新或删除操作

完整性约束可以应用于列级别或表级别，以确保数据的正确性和一致性。以下是 `MySQL` 中常见的完整性约束类型: 

* **数据完整性约束**
* **字段的约束**
* **删除约束**

## 数据完整性约束

* 各种完整性约束是作为数据库关系模式定义的一部分，可通过 `CREATE TABLE`或 `ALTER TABLE` 语句来定义
* 一旦定义了完整性约束， `MySQL` 服务器会**随时检测处于更新状态的数据库内容是否符合相关的完整性约束**，从而保证数据的一致性与正确性。如此，既能有效地防止对数据库的意外破坏，又能提高完整性检测的效率，还能减轻数据库编程人员的工作负担
* 数据的完整性约束主要分为以下几类:
  * **实体完整性**
  * **参照完整性**
  * **域完整性**
  * **用户自定义完整性** 

?> 实体完整性: 实体的完整性强制表的标识符列或主键的完整性

?> 参照完整性: 在删除和输入记录时，引用完整性保持表之间已定义的关系，引用完整性确保键值在所有表中一致。这样的一致性要求不能引用不存在的值。如果一个键值更改了，那么在整个数据库中，对该键值的引用要进行一致的更改改

?> 域完整性: 限制类型（数据类型），格式（检查约束和规则），可能值范围（外键约束，检查约束，默认值定义，非空约束和规则）

?> 用户自定义完整性:用户自己定义的业务规则

!> 在 `MySQL` 数据库中**不支持检查约束**。可以在语句中对字段添加检查约束，不会报错，但该约束不起作用

## 字段的约束

设计数据库时，可以对数据库表中的一些字段设置约束条件，由数据库管理系统自动检测输入的数据是否满足约束条件，不满足约束条件的数据，数据库管理系统拒绝录入

`MySQL` 支持的常用约束条件有7种：**主键（primary key）约束**、**外键（foreign key）约束**、**非空(not NULL)约束**、**唯一性( unique )约束**、**默认值( default)约束**、**自增（auto_increment）约束**以及**检查( check)约束**

!> 检查( check)约束需要借助触发器或者MySQL复合数据类型实现

### 主键约束

* 设计数据库时，建议为所有的数据库表都定义一个主键，用于保证数据库表中记录的**唯一性**。一张表中只允许设置一个主键，当然这个主键可以是一个字段，也可以是一个字段组（不建议使用复合主键）
* 在录入数据的过程中，必须在所有主键字段中输入数据，即任何主键字段的值不允许为 `NULL`
* 设置主键后，数据库系统会自动为表中的主键字段创建一个**唯一性的索引**，以保证主键值的唯一性

?> 设置主键通常有两种方式：**表级完整性约束**和**列级完整性约束**

#### 表级完整性约束设置主键

```sql
PRIMARY KEY(字段名)
```

<div style="text-align: center;"><img alt='202403271939428' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403271939428.png' width=500px> </div>

#### 列级完整性约束设置主键

```sql
字段名 数据类型[其他约束条件] PRIMARY KEY
```

<div style="text-align: center;"><img alt='202403271941872' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403271941872.png' width=500px> </div>

### 外键约束（FOREIGN KEY）约束

外键约束用于**建立表之间的关联关系**，确保引用表中的外键值在被引用表中存在。外键约束定义了表之间的父子关系，强制要求在子表中的外键列中的值必须存在于父表的主键列中

!> 外键约束必须引用另一个表的主键，而不能引用一个表的任意一列

!> 父表和子表必须使用相同的存储引擎，且存储引擎为 `InnoDB`, 而且禁止使用临时表

外键约束的参照操作:

* `CASCADE`: 从父表删除或更新且自动删除或更新子表中匹配的行
* `SET NULL`: 从父表删除或更新行，并设置子表中的外键列为 `NULL`, 如果使用该选项，必须保证子表列没有指定 `NOT NULL`
* `RESTRICT`: 拒绝对父表的删除或更新操作, 默认值
* `NO ACTION`: 标准 SQL 关键字，在 MySQL 中与 `RESTRICT` 相同

#### 表级完整性定义外键

```sql
[constraint <外键名>] foreign key 字段名 [，字段名2，…] references <主表名> 主键列1 [，主键列2，…]
```

<div style="text-align: center;"><img alt='202403271953440' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403271953440.png' width=500px> </div>

如果表已经建好了，可以通过`alter table`命令进行添加外键

```sql
alter table table_name
    add [ constraint 外键名] foregin key [id] (index_col_name, ……)
    references table_name(index_col_name, ……)
    [ on delete {cascade| restrict |set null | no action} ]
    [ on update {cascade| restrict |set null | no action} ]  
```

#### 列级完整性定义外键

```sql
FOREIGN KEY(字段) REFERENCES 关联表(字段) 
[ on delete {cascade| restrict |set null | no action} ]
[ on update {cascade| restrict |set null | no action} ]  
```

<div style="text-align: center;"><img alt='202403272006660' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272006660.png' width=500px> </div>

### 非空约束

若设置某个字段的非空约束，直接在该字段的数据类型后加上 `NOT NULL` 关键字即可

<div style="text-align: center;"><img alt='202403272008970' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272008970.png' width=500px> </div>

### 默认约束

若设置某个字段的默认约束，直接在该字段的数据类型后加上 `DEFAULT` 关键字即可

<div style="text-align: center;"><img alt='202403272010039' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272010039.png' width=500px> </div>

### 唯一约束

若设置某个字段的唯一约束，直接在该字段的数据类型后加上 `UNIQUE` 关键字即可

?> 唯一性约束实质上是通过**唯一性索引**实现的，因此唯一性约束的字段一旦创建，那么该字段将自动创建唯一性索引。如果要删除唯一性约束，只需删除对应的唯一性索引即可

!> 与主键约束不同，一张表中可以存在多个唯一性约束，并且满足唯一性约束的字段可以取 `NULL` 值

<div style="text-align: center;"><img alt='202403272012256' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272012256.png' width=500px> </div>

### 自增约束

在具体设置 `AUTO_INCREMENT` 约束时，一个数据库表中只能有**一个字段**使用该约束，该字段的数据类型必须是**整型类型**

由于设置 `auto_increment` 约束后的字段会生成唯一的ID，所以该字段也经常会设置为主键

<div style="text-align: center;"><img alt='202403272013225' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272013225.png' width=500px> </div>

### 检查约束

检查约束是用来**检查数据表中字段值的有效性**的一个手段

例如，学生信息表中的年龄字段是没有负数的，并且数值也是有限制的，当前大学生的年龄一般在15~30岁之间

### 删除约束

在MySQL 数据库中，一个字段的所有约束都可以用 `alter table` 命令删除

## 综合实例

?> 创建一个用户注册表，包含的字段及要求如下:

1. 主键为自增 `id`
2. 用户名 `username` 唯一非空
3. 用户密码 `password` 非空
4. 用户邮箱 `email` 非空且默认值为 `caulihui@cau.edu.cn`
5. 年龄 `age` 默认值为18
6. 性别 `sex` 默认值为保密
7. 地址 `addr` 默认值为北京
8. 薪水 `salary`
9. 注册时间`regTime`
10. 照片 `face`，默认值为`default.jpg`

<div style="text-align: center;"><img alt='202403272028725' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403272028725.png' width=500px> </div>
