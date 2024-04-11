# MySQL数据库备份与还原

为了保证数据的安全,需要**定期对数据进行备份**。备份的方式有很多种,效果也不一样。如果数据库中的数据出现了错误,就需要使用备份好的数据进行数据还原,这样可以将损失降至最低

?> MySQL数据库备份的方法多种多样（例如完全备份、增量备份等）,无论使用哪一种方法,都要求**备份期间的数据库必须处于数据一致状态**,即数据备份期间,尽量不要对数据进行更新操作

## 备份与还原概述

数据库备份是指通过导出数据或者拷贝表文件的方式来制作数据库的副本

数据库的恢复（也称为数据库的还原）是将数据库从某一种错误状态（如硬件故障、操作失误、数据丢失、数据不一致等状态）恢复到某一已知的正确状态

MySQL数据库中具体实现备份数据库的方法很多,可分为以下几种:
* **完全备份**
    * 完全备份就是将**数据库中的数据及所有对象全部备份**。完全备份最简单也最快速的方式就是复制数据库文件,在复制时对MySQL数据库会有些要求。只要服务器不在进行更新,就可以复制所有文件（\*.frm、\*.MYD、\*.MYI文件）。对InnoDB表,可以进行在线备份,不需要对表进行锁定
* **表备份**
    * 表备份就是仅将**一张或多张表**中的数据进行备份,可以使用select into …outfile 或backup table语句,只提取数据库中的数据,而不备份表的结构和定义
* **增量备份**
    * 增量备份就是在某次完全备份的基础上,**只备份其后数据的变化**。可用于定期备份和自动恢复。增量备份使用mysqlbinlog处理二进制日志文件。通过增量备份,当出现操作系统崩溃或电源故障,InnoDB自己可以完成所有数据恢复的工作

## 通过文件备份和还原

由于MySQL服务器中的数据文件是基于磁盘的文本文件,所以最简单、最直接的备份操作就是**把数据库文件直接复制出来**

!> 由于MySQL服务器的数据文件在服务运行期间,总是处于打开和使用状态,因此文本文件副本备份不一定总是有效。为了解决该问题,在复制数据库文件时,需要先停止MySQL数据库服务器

虽然停止MySQL数据库服务器,可以解决复制数据库文件实现数据备份的问题,但是这种方法不是最好的备份方法。这是因为实际情况下,MySQL数据库服务器不允许被停止,**同时该方式对InnoDB储存引擎的表不适合,只适合MyISAM引擎**

## 通过命令mysqldump备份还原

MySQL提供了许多免费的客户端实用程序,且存放于MySQL安装目录下的bin子目录中。这些客户端实用程序可以连接到MySQL服务器进行数据库的访问,或者对MySQL执行不同的管理任务。其中, `mysqldump` 程序和 `mysqlimport` 程序就分别是两个常用的用于实现MySQL数据库备份和恢复的实用工具

### 使用mysqldump程序备份数据

可以使用客户端实用程序mysqldump来实现mysql数据库的备份,它除了可以与前面使用SQL语句备份表数据一样导出备份的表数据文件之外,还可以在**导出的文件中包含数据库中表结构的SQL语句**

* **备份表**
```SQL
mysqldump [options] database [tables] > filename
```
* **备份数据库**
```SQL
mysqldump[ options ]—databases [options] db1 [db2 db3 ...] > filename
```
* **备份整个数据库系统**
```SQL
mysqldump[options] - -all-databases[options] > filename ; 
```

### 使用mysqlimport程序恢复数据

```SQL
mysqlimport[options] database textfile... ; 
```

## 表的导入和导出

### 导出表

```SQL
SELECT *
INTO OUTFILE 'file_name'
[CHARACTER SET charset_name]
[export_options]
FROM table_name
WHERE condition;
```

* 导出备份语句的作用是将表中select语句选中的所有数据行写入到一个文件中,file_name指定数据备份文件的名称
* 导出语句中使用关键字outfile时,可以在export_options中加入以下两个自选的子句,它们的作用是决定数据行在备份文件中存放的格式
* 在fields子句中有三个亚子句,如果指定了fields子句,则这三个亚子句中至少要求指定一个

### 导入表

```SQL
LOAD DATA [LOW_PRIORITY | CONCURRENT] [LOCAL] INFILE 'file_name.txt'
[REPLACE | IGNORE]
INTO TABLE tbl_name
[FIELDS
    [TERMINATED BY 'string']
    [[OPTIONALLY] ENCLOSED BY 'char']
    [ESCAPED BY 'char']
]
```

- `[LOW_PRIORITY | CONCURRENT]`:可选项,指定数据加载的优先级或并发方式。
  - `LOW_PRIORITY`:表示在其他读取操作完成后再加载数据。
  - `CONCURRENT`:表示允许在加载数据时进行并发读取操作。
- `[LOCAL]`:可选项,指定使用客户端本地文件。
- `'file_name.txt'`:要导入的文件名及路径。
- `[REPLACE | IGNORE]`:可选项,指定导入数据时的处理方式。
  - `REPLACE`:表示如果导入的数据与表中已有的数据重复,则替换表中的数据。
  - `IGNORE`:表示如果导入的数据与表中已有的数据重复,则忽略导入的数据。
- `INTO TABLE tbl_name`:指定要导入数据的表名。
- `[FIELDS ...]`:可选项,用于定义字段和列的分隔符、引号和转义字符。
  - `[TERMINATED BY 'string']`:指定字段之间的分隔符。
  - `[[OPTIONALLY] ENCLOSED BY 'char']`:指定字段值的引号字符,`OPTIONALLY` 表示该引号字符是可选的。
  - `[ESCAPED BY 'char']`:指定用于转义字符的字符。





