# MySQL触发器与事件调度器

MySQL数据库管理系统中关于触发器、事件调度器的操作, 主要包含**触发器和事件的创建、使用、查看和删除**。触发器是由事件来触发某个操作, 这些事件包括 `insert` 语句、 `update` 语句和 `delete` 语句。当数据库系统执行这些事件时, 就会激活触发器执行相应的操作

事件调度器(event scheduler), 可以用做**定时执行某些特定任务**（例如: 删除记录、对数据进行汇总等等）, 来取代原先只能由操作系统的计划任务来执行的工作

## 触发器

触发器是一种**特殊的存储过程**, 它在**插入, 删除或修改特定表中的数据时触发执行**, 它比数据库本身标准的功能有更精细和更复杂的数据控制能力

### 创建触发器

触发程序是与表有关的命名数据库对象, 当表上出现特定事件时, 将激活该对象。在MySQL中, 创建触发器的基本形式如下: 
```sql
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON table_name
FOR EACH ROW
trigger_body
```

* `trigger_name` : 触发器的名称, 自定义的标识符
* `{BEFORE | AFTER}`: 指定触发器的触发时机, 可以是在执行操作之前或之后触发
* `{INSERT | UPDATE | DELETE}`: 指定触发器的操作类型, 可以是插入、更新或删除操作
* `table_name` : 触发器所属的表名
* `FOR EACH ROW` : 定义触发器对每一行数据都执行
* `trigger_body` : 触发器的执行内容, 可以是一条或多条 SQL 语句

!> 触发程序与命名为 `table_name` 的表相关。 `tbl_name` 必须引用永久性表。不能将触发程序与temporary表或视图关联起来

?> 创建触发器名为 my_trigger, 在每次向表 my_table 插入数据之前触发。触发器的执行内容是将插入的数据行的 column2 字段设置为插入的数据行的 column1 字段的两倍

```sql
CREATE TRIGGER my_trigger
BEFORE INSERT
ON my_table
FOR EACH ROW
BEGIN
  -- 执行的 SQL 语句
  SET NEW.column2 = NEW.column1 * 2;
END;
```

### 查看触发器

* 可以通过执行以下命令执行命令查看触发器的状态、语法等信息, 但是因为不能查看指定的触发器, 所以每次否返回所有的触发器信息, 使用起来不是很方便

```sql
show triggers 
```

* 另一种方法是查询系统表`information_schema.triggers`表, 这个方式可以查询指定触发器的指定信息, 操作起来明显方便得多

### 删除触发器

```sql
drop trigger [schema_name.]trigger_name触发程序
```

!> 数据库（schema_name）是可选的。如果省略了schema, 将从当前数据库中删除触发程序

### 对触发器的进一步说明

!> 触发器不能调用将数据返回客户端的存储过程, 也不能使用采用call语句的动态sql

* 触发器不能使用以显式或隐式方式开始或结束事务的语句, 如 `start transaction`、 `commit` 或 `rollback` 。 需要注意以下两点
    * MySQL触发器针对行来操作, 当处理大数据集的时候可能效率很低
    * 触发器不能保证原子性, 例如在 `myisam` 中, 当一个更新触发器在更新一个表后, 触发对另外一个表的更新, 若触发器失败, 不会回滚第一个表的更新

## 事件

* 事件调度器有时也可称为临时触发器(temporal triggers), 它可以用做**定时执行某些特定任务**（例如: 删除记录、对数据进行汇总等等）, 来取代原先只能由操作系统的计划任务来执行的工作
* 因为事件调度器是**基于特定时间周期**触发来执行某些任务, 而触发器(triggers)是基于某个表所产生的事件触发的, 区别也就在这里

### 创建事件

```sql
CREATE EVENT event_name
  ON SCHEDULE schedule
  [ON COMPLETION [NOT] PRESERVE]
  [ENABLE | DISABLE]
  DO event_body
```

* `event_name`: 事件的名称, 自定义的标识符
* `ON SCHEDULE schedule`: 定义事件的执行计划, 包括执行时间和重复规则
    * `AT timestamp`: 指定事件的具体执行时间, 例如 'YYYY-MM-DD HH:MM:SS' 格式的时间戳
    * `EVERY interval`: 指定事件的重复间隔, 例如 '1 HOUR'、'1 DAY' 或者 '1 WEEK' 等
    * `STARTS timestamp`: 指定事件的开始执行时间, 例如 'YYYY-MM-DD HH:MM:SS' 格式的时间戳
    * `ENDS timestamp`: 指定事件的结束执行时间, 例如 'YYYY-MM-DD HH:MM:SS' 格式的时间戳
* `[ON COMPLETION [NOT] PRESERVE]`: 定义事件的完成后的处理方式
    * `NOT PRESERVE`: 事件完成后将自动删除
    * `PRESERVE`: 事件完成后保留不删除
* `[ENABLE | DISABLE]`: 定义事件的启用状态
    * `ENABLE` : 启用事件, 使其可以执行
    * `DISABLE` : 禁用事件, 暂停其执行
* `DO event_body` : 事件的执行内容, 可以是一条或多条 SQL 语句

?> 创建一个每天凌晨1点执行的事件

```sql
CREATE EVENT my_event
  ON SCHEDULE
    EVERY 1 DAY
    STARTS '2024-03-29 01:00:00'
  DO
    BEGIN
      -- 执行的 SQL 语句
      INSERT INTO my_table (column1, column2) VALUES ('value1', 'value2');
    END;
```

### 删除事件

```sql
drop event [if exists] event_name
```




