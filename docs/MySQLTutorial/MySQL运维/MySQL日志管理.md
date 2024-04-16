# MySQL日志管理 

MySQL数据库中包含多种不同类型的日志文件, 这些文件记录了MySQL数据库的**日常操作和错误信息**, 分析这些日志文件可以了解MySQL数据库的运行情况、日常操作、错误信息以及哪些地方需要进行优化

## MySQL支持的日志

### 错误日志

错误日志是MySQL数据库中最常用的一种日志。错误日志主要用来**记录MySQL服务的开启、关闭和错误信息**。本节将为读者介绍错误日志的内容

### 开启错误日志

错误日志是 MySQL 中最重要的日志之一, 它记录了当 mysqld 启动和停止时, 以及服务器在运行过程中发生任何严重错误时的相关信息。当数据库出现任何故障导致无法正常使用时, 可以首先查看此日志

该日志是**默认开启**的, 默认存放目录为 mysql 的数据目录, 默认的日志文件名为 `hostname.err` (hostname是主机名)
错误日志的存储位置可以通过 `log-error` 选项来设置。将 log-error 选项加入到my.Ini文件的\[mysqld\]组中, 形式如下: `log-error[=DIR / [filename]]`

```sql
show variables like 'log_error%'; -- 查看日志位置指令 
```

### 查看错误日志

* 错误日志中记录着**开启和关闭MySQL服务的时间**, 以及**服务运行过程中出现哪些异常**等信息。如果MySQL服务出现异常, 可以到错误日志中查找原因
* 错误日志是以**文本文件**的形式存储的, 可以直接使用普通文本工具就可以查看

### 删除错误日志

数据库管理员可以删除很长时间之前的错误日志, 以保证MySQL服务器上的硬盘空间。MySQL数据库中, 可以使用`mysqladmin`命令来开启新的错误日志。`mysqladmin`命令的语法如下:
```SQL
mysqladmin -u root -p flush-logs
```

!> 执行该命令后, 数据库系统会自动创建一个新的错误日志。旧的错误日志仍然保留着, 只是已经更名为filename.err-old

## 二进制日志

二进制日志也叫作变更日志(update log), 主要用于**记录数据库的变化情况**。通过二进制日志可以查询MySQL数据库中进行了哪些改变

二进制日志（BINLOG）记录了所有的 DDL（数据定义语言）语句和 DML（数据操纵语言）语句, 但是不包括数据查询语句。此日志对于灾难时的数据恢复起着极其重要的作用, MySQL的主从复制, 就是通过该binlog实现的

### 启动二进制日志

> 二进制日志，MySQL8.0默认已经开启，低版本的MySQL的需要通过配置文件开启，并配置MySQL日志的格式

可以使用下列命令查找查找linux系统上的mysql可执行程序所在目录
```bash
which mysql
```

查找mysql配置文件所在路径:

```bash
/usr/bin/mysql --verbose --help | grep -A 1 'Default options' # 使用上述命令查询到的mysql可执行程序的目录
```

由于作者使用的MySQL版本比较低, 因此默认情况下, 二进制日志功能是关闭的。通过my.ini的log-bin选项可以开启二进制日志。将log-bin选项加入到my.cnf(my.ini)文件的[mysqld]组中, 形式如下:
```sql
#配置开启binlog日志， 日志的文件前缀为 mysqlbin -----> 生成的文件名如 : mysqlbin.000001,mysqlbin.000002
log_bin=mysqlbin
#配置二进制日志的格式
binlog_format=STATEMENT
```

### 日志格式

* `STATEMENT`: 该日志格式在日志文件中记录的都是SQL语句（statement），每一条对数据进行修改的SQL都会记录在日志文件中，通过Mysql提供的mysqlbinlog工具，可以清晰的查看到每条语句的文本。主从复制的时候，从库（slave）会将日志解析为原文本，并在从库重新执行一次
* `ROW`: 该日志格式在日志文件中记录的是每一行的数据变更，而不是记录SQL语句。比如，执行SQL语句: `update tb_book set status='1'` , 如果是 STATEMENT 日志格式，在日志中会记录一行SQL文件； 如果是ROW，由于是对全表进行更新，也就是每一行记录都会发生变更，ROW 格式的日志中会记录每一行的数据变更
* `MIXED`: 混合了STATEMENT 和 ROW两种格式

### 查看二进制日志

使用二进制格式可以存储更多的信息, 并且可以使写入二进制日志的效率更高。打开二进制日志的命令的语法形式如下:
```sql
-- 查看MySQL是否开启了binlog日志
show variables like 'log_bin';
-- 查看binlog日志的格式
show variables like 'binlog_format';
-- 查看所有日志
show binlog events;
-- 查看最新的日志
show master status;
-- 查询指定的binlog日志
show binlog events in 'binlog.000010';
select * from mydb1.emp2;
select count(*) from mydb1.emp2;
update mydb1.emp2 set salary = 8000;
```

?> `mysqlbinlog` 命令将在**当前文件夹**下查找指定的二进制日志。因此需要在**二进制日志filename.number**所在的目录下运行该命令, 否则将会找不到指定的二进制日志文件

### 删除二进制日志

二进制日记会记录大量的信息, 如果很长时间不清理, 将会浪费很多的磁盘空间, 以下为删除二进制日志的几种方法:
* 删除所有二进制日志
    * `reset master`
    *  删除所有二进制日志后, MySQL将会重新创建新的二进制日志
* 根据编号来删除二进制日志
    * 每个二进制日志文件后面有一个六位数的编号, 如000001。使用 `purge masterlogs to`语句可以删除编号小于这个二进制日志的所有二进制日志。该语句的基本语法形式如下: `purge master logs to 'filename.number';`
* 根据创建时间来删除二进制日志
    * 使用 `purge master logs to`语句可以删除指定时间之前创建的二进制日志。该语句的基本语法形式如下:`purge master logs before  'yyyy-mm-dd hh:mm;ss'; `

### 二进制日志还原数据库

```sql
mysqlbinlog filename.number | mysql -u root -p
```

!> 使用 `mysqlbinlog` 命令来读取 `filename.Number` 中的内容, 然后使用 `mysql` 命令将这些内容还原到数据库

## 慢查询日志

### 启动慢查询日志

默认情况下, 慢查询日志功能是关闭的。在windows下, 通过**修改my.cnf文件的slow-query-log选项**可以开启慢查询日志。在\[mysqld\]组, 把`slow-query-log`的值设置为1（默认是0）, 重新启动`MySQ`L服务即可开启慢查询日志。其语法格式如下:

```bash
# 该参数用来控制慢查询日志是否开启， 可取值： 1 和 0 ， 1 代表开启， 0 代表关闭
slow_query_log=1
 # 该参数用来指定慢查询日志的文件名
slow_query_log_file=slow_query.log
# 该选项用来配置查询的时间限制， 超过这个时间将认为值慢查询， 将需要进行日志记录， 默认10s
long_query_time=10
```

!> DIR参数指定慢查询日志的存储路径

### 查看慢查询日志

执行时间**超过指定时间的查询语句**会被记录到慢查询日志中。如果用户希望查询哪些查询语句的执行效率低, 可以从慢查询日志中获得想要的信息。慢查询日志也是以**文本文件**的形式存储的。可以使用普通的文本文件查看工具来查看

### 删除慢查询日志

慢查询日志的删除方法可以使用 `mysqladmin` 命令来删除, 也可以使用手工方式来删除。 `mysqladmin` 命令的语法如下:
```SQL
slow_query_log_file[=DIR\[filename]]
```

!> 执行该命令后, 命令行会提示输入密码。输入正确密码后, 将执行删除操作。新的慢查询日志会**直接覆盖旧的查询日志**, 不需要再手动删除了

## 通用查询日志

### 启动通用查询日志

默认情况下, 通用查询日志功能是关闭的。在windows下, 通过修改my.cnf文件的log选项可以开启通用查询日志。在\[mysqld\]组, 把`general-log`的值设置为1（默认是0）, 重新启动MySQL服务即可开启查询日志, `general_log_file`表示日志的路径, 形式如下:

```bash
#该选项用来开启查询日志 ， 可选值 ： 0 或者 1 ； 0 代表关闭， 1 代表开启 
general_log=1

#设置日志的文件名 ， 如果没有指定， 默认的文件名为 host_name.log 
general_log_file=file_name
```

### 查看通用查询日志

用户的**所有操作**都会记录到通用查询日志中。如果希望了解某个用户最近的操作, 可以查看通用查询日志, 通用查询日志是以**文本文件**的形式存储的

```sql
-- 查看MySQL是否开启了查询日志
show variables like 'general_log';
#该选项用来开启查询日志 ， 可选值 ： 0 或者 1 ； 0 代表关闭， 1 代表开启 
-- 开启查询日志
set global general_log=1;
```

### 删除通用查询日志

MySQL数据库中, 可使用`mysqladmin`命令来开启新的通用查询日志。新的通用查询日志会直接覆盖旧的查询日志, 不需要再手动删除了。`mysqladmin`命令的语法如下:

```sql
mysqladmin –u root –p flush-logs
```

!> 除了上述方法以外, 可以手工删除通用查询日志。删除之后需要重新启动MySQL服务, 重启之后就会生成新的通用查询日志










