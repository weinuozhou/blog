# MySQL的优化

应用的的开发过程中，由于初期数据量小，开发人员写 SQL 语句时更重视功能上的实现，但是当应用系统正式上线后，随着生产数据量的急剧增长，很多 SQL 语句开始逐渐显露出性能问题，对生产的影响也越来越大，此时这些有问题的 SQL 语句就成为整个系统性能的瓶颈，因此我们必须要对它们进行优化

MySQL的优化方式有很多，大致我们可以从以下几点来优化MySQL
* 从**设计**上优化
* 从**查询**上优化
* 从**索引**上优化
* 从**存储**上优化

## 查看SQL执行频率

MySQL 客户端连接成功后，通过 `show [session|global] status` 命令可以查看服务器状态信息。通过查看状态信息可以查看对当前数据库的主要操作类型

```sql
--下面的命令显示了当前 session 中所有统计参数的值
show session status like 'Com_______';  -- 查看当前会话统计结果
show global  status  like 'Com_______';  -- 查看自数据库上次启动至今统计结果
show status like 'Innodb_rows_%';       -- 查看针对Innodb引擎的统计结果
```

<div style="text-align: center;"><img alt='202404112010750' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112010750.png' width=500px> </div>

各个参数的含义如下:

<div style="text-align: center;"><img alt='202404112011399' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112011399.png' width=500px> </div>

## 定位低效率执行SQL 


可以通过以下两种方式定位执行效率较低的 SQL 语句:
* **慢查询日志**: 通过慢查询日志定位那些执行效率较低的 SQL 语句
* `show processlist`: 该命令查看当前MySQL在进行的线程，包括线程的状态、是否锁表等，可以实时地查看 SQL 的执行情况，同时对一些锁表操作进行优化

### 慢查询日志  

```sql
show variables like '%slow_query_log%';  -- 查看慢日志配置信息 
set global slow_query_log=1;  -- 开启慢日志查询 
show variables like 'long_query_time%';  -- 查看慢日志记录SQL的最低阈值时间 
set global long_query_time=4; -- 修改慢日志记录SQL的最低阈值时间 
```

<div style="text-align: center;"><img alt='202404112014404' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112014404.png' width=500px> </div>

### show processlist 

```sql
show processlist;  -- 查看当前MySQL正在进行的线程 
```

* id: 用户登录mysql时，系统分配的"connection_id"，可以使用函数connection_id()查看
* user: 显示当前用户。如果不是root，这个命令就只显示用户权限范围的sql语句
* host: 显示这个语句是从哪个ip的哪个端口上发的，可以用来跟踪出现问题语句的用户
* db: 显示这个进程目前连接的是哪个数据库
* command: 显示当前连接的执行的命令，一般取值为休眠（sleep），查询（query），连接（connect）等
* time: 显示这个状态持续的时间，单位是秒
* state: 显示使用当前连接的sql语句的状态，很重要的列。state描述的是语句执行中的某一个状态。一个sql语句，以查询为例，可能需要经过copying to tmp table、sorting result、sending data等状态才可以完成
* info: 显示这个sql语句，是判断问题语句的一个重要依据

<div style="text-align: center;"><img alt='202404112017068' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112017068.png' width=500px> </div>

## explain分析执行计划

通过以上步骤查询到效率低的 SQL 语句后，可以通过 `EXPLAIN` 命令获取 MySQL 如何执行 SELECT 语句的信息，包括在 `SELECT` 语句执行过程中表如何连接和连接的顺序

<div style="text-align: center;"><img alt='202404112019837' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112019837.png' width=500px> </div>

各个参数含义如下:

<div style="text-align: center;"><img alt='202404112020341' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112020341.png' width=500px> </div>

## `show profile` 分析SQL

Mysql从5.0.37版本开始增加了对 `show profiles` 和 `show profile` 语句的支持。`show profiles` 能够在做SQL优化时帮助我们了解时间都耗费到哪里去

```sql
select @@have_profiling; 
set profiling=1; -- 开启profiling 开关； 
```

先随机执行以下 sql 语句， 再执行 `show profiles`观察SQL语句的耗时

```sql
show databases;
use test;
show tables;
select * from user;
show profiles;
```

<div style="text-align: center;"><img alt='202404112024722' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112024722.png' width=500px> </div>

通过`show  profile for  query  query_id` 语句可以查看到该SQL执行过程中每个线程的状态和消耗的时间:

```sql
show profile for query 6;
```

<div style="text-align: center;"><img alt='202404112026424' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112026424.png' width=500px> </div>

在获取到最消耗时间的线程状态后，MySQL支持进一步选择all、cpu、block io 、context switch、page faults等明细类型类查看MySQL在使用什么资源上耗费了过高的时间。例如，选择查看CPU的耗费时间:

```sql
show profile cpu for query 6;
```

<div style="text-align: center;"><img alt='202404112027377' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112027377.png' width=500px> </div>

## 使用索引优化

索引是数据库优化最常用也是最重要的手段之一, 通过索引通常可以帮助用户解决大多数的MySQL的性能优化问题

```sql
create table `tb_seller` (
    `sellerid` varchar (100),
    `name` varchar (100),
    `nickname` varchar (50),
    `password` varchar (60),
    `status` varchar (1),
    `address` varchar (100),
    `createtime` datetime,
    primary key(`sellerid`)
); 
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('alibaba','阿里巴巴','阿里小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('baidu','百度科技有限公司','百度小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('huawei','华为科技有限公司','华为小店','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('itcast','传智播客教育科技有限公司','传智播客','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('itheima','黑马程序员','黑马程序员','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('luoji','罗技科技有限公司','罗技小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('oppo','OPPO科技有限公司','OPPO官方旗舰店','e10adc3949ba59abbe56e057f20f883e','0','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('ourpalm','掌趣科技股份有限公司','掌趣小店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('qiandu','千度科技','千度小店','e10adc3949ba59abbe56e057f20f883e','2','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('sina','新浪科技有限公司','新浪官方旗舰店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('xiaomi','小米科技','小米官方旗舰店','e10adc3949ba59abbe56e057f20f883e','1','西安市','2088-01-01 12:00:00');
insert into `tb_seller` (`sellerid`, `name`, `nickname`, `password`, `status`, `address`, `createtime`) values('yijia','宜家家居','宜家家居旗舰店','e10adc3949ba59abbe56e057f20f883e','1','北京市','2088-01-01 12:00:00');
-- 创建组合索引 
create index idx_seller_name_sta_addr on tb_seller(name, status, address);
```

### 全值匹配

```sql
explain select * from tb_seller where name='小米科技' and status='1' and address='北京市';
```

<div style="text-align: center;"><img alt='202404112034231' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404112034231.png' width=500px> </div>

### 最左前缀法则

> 如果索引了多列, 要遵守最左前缀法则, 最左前缀法则指的是查询从索引的最左列开始, 并且不跳过索引中的列, 否则索引会失效

```sql
-- 最左前缀法则
-- 如果索引了多列，要遵守最左前缀法则。指的是查询从索引的最左前列开始，并且不跳过索引中的列。
explain select * from tb_seller where name='小米科技'; -- 403
explain select * from tb_seller where name='小米科技' and status='1'; -- 410
explain select * from tb_seller where  status='1' and name='小米科技'; -- 410
-- 违法最左前缀法则, 索引失效：
explain select * from tb_seller where status='1'; -- nulll
-- 如果符合最左法则，但是出现跳跃某一列，只有最左列索引生效：
explain select * from tb_seller where name='小米科技'  and address='北京市'; -- 403
```

### 其他匹配原则

```sql
-- 1. 范围查询右边的列，不能使用索引 
-- 根据前面的两个字段name ， status 查询是走索引的， 但是最后一个条件address 没有用到索引。
explain select * from tb_seller where name='小米科技' and status >'1' and address='北京市'; 
-- 2. 不要在索引列上进行运算操作， 索引将失效 
explain select * from tb_seller where substring(name,3,2)='科技'
-- 3. 字符串不加单引号，造成索引失效
explain select * from tb_seller where name='小米科技' and status = 1 ;
-- 4、尽量使用覆盖索引，避免select *
-- 需要从原表及磁盘上读取数据
explain select * from tb_seller where name='小米科技'  and address='北京市';  -- 效率低
-- 从索引树中就可以查询到所有数据
explain select name from tb_seller where name='小米科技'  and address='北京市';  -- 效率高
explain select name,status,address from tb_seller where name='小米科技' and address='北京市';  -- 效率高
-- 5. 如果查询列，超出索引列，也会降低性能
explain select name,status,address,password from tb_seller where name='小米科技'  and address='北京市';  -- 效率低
-- 6. 用or分割开的条件， 那么涉及的索引都不会被用到
explain select * from tb_seller where name='黑马程序员' or createtime = '2088-01-01 12:00:00'; 
explain select * from tb_seller where name='黑马程序员' or address = '西安市';  
explain select * from tb_seller where name='黑马程序员' or status = '1';   
-- 7. 以%开头的Like模糊查询，索引失效
explain select * from tb_seller where name like '科技%'; -- 用索引
explain select * from tb_seller where name like '%科技'; -- 不用索引
explain select * from tb_seller where name like '%科技%';-- 不用索引
-- 弥补不足,不用*，使用索引列
explain select name from tb_seller where name like '%科技%';
```

## SQL优化

### 优化insert语句

```sql
create table `tb_user` (
  `id` int(11) not null auto_increment,
  `username` varchar(45) not null,
  `password` varchar(96) not null,
  `name` varchar(45) not null,
  `birthday` datetime default null,
  `sex` char(1) default null,
  `email` varchar(45) default null,
  `phone` varchar(45) default null,
  `qq` varchar(32) default null,
  `status` varchar(32) not null comment '用户状态',
  `create_time` datetime not null,
  `update_time` datetime default null,
  primary key (`id`),
  unique key `unique_user_username` (`username`)
);
```

#### 一次性插入多行数据

```sql
-- 如果需要同时对一张表插入很多行数据时，应该尽量使用多个值表的insert语句，这种方式将大大的缩减客户端与数据库之间的连接、关闭等消耗。使得效率比分开执行的单个insert语句快
-- 原始方式为：
insert into tb_test values(1,'Tom');
insert into tb_test values(2,'Cat');
insert into tb_test values(3,'Jerry');
-- 优化后的方案为 ： 
insert into tb_test values(1,'Tom'),(2,'Cat')，(3,'Jerry');
```

#### 在事务中进行数据插入

```sql
-- 在事务中进行数据插入。
begin;
insert into tb_test values(1,'Tom');
insert into tb_test values(2,'Cat');
insert into tb_test values(3,'Jerry');
commit;
```

#### 数据有序插入

```sql
-- 数据有序插入
insert into tb_test values(4,'Tim');
insert into tb_test values(1,'Tom');
insert into tb_test values(3,'Jerry');
insert into tb_test values(5,'Rose');
insert into tb_test values(2,'Cat');
-- 优化后
insert into tb_test values(1,'Tom');
insert into tb_test values(2,'Cat');
insert into tb_test values(3,'Jerry');
insert into tb_test values(4,'Tim');
insert into tb_test values(5,'Rose');
```

### 优化order by语句

```sql
CREATE TABLE `emp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `age` int(3) NOT NULL,
  `salary` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
 
insert into `emp` (`id`, `name`, `age`, `salary`) values('1','Tom','25','2300');
insert into `emp` (`id`, `name`, `age`, `salary`) values('2','Jerry','30','3500');
insert into `emp` (`id`, `name`, `age`, `salary`) values('3','Luci','25','2800');
insert into `emp` (`id`, `name`, `age`, `salary`) values('4','Jay','36','3500');
insert into `emp` (`id`, `name`, `age`, `salary`) values('5','Tom2','21','2200');
insert into `emp` (`id`, `name`, `age`, `salary`) values('6','Jerry2','31','3300');
insert into `emp` (`id`, `name`, `age`, `salary`) values('7','Luci2','26','2700');
insert into `emp` (`id`, `name`, `age`, `salary`) values('8','Jay2','33','3500');
insert into `emp` (`id`, `name`, `age`, `salary`) values('9','Tom3','23','2400');
insert into `emp` (`id`, `name`, `age`, `salary`) values('10','Jerry3','32','3100');
insert into `emp` (`id`, `name`, `age`, `salary`) values('11','Luci3','26','2900');
insert into `emp` (`id`, `name`, `age`, `salary`) values('12','Jay3','37','4500');
 -- 创建联合索引
create index idx_emp_age_salary on emp(age,salary);
```
排序方式主要有两种:
* 第一种是通过对返回数据进行排序，也就是通常说的 filesort 排序，所有不是通过索引直接返回排序结果的排序都叫 FileSort 排序
    * 两次扫描算法: MySQL4.1 之前，使用该方式排序。首先根据条件取出排序字段和行指针信息，然后在排序区 sort buffer 中排序，如果sort buffer不够，则在临时表 temporary table 中存储排序结果。完成排序之后，再根据行指针回表读取记录，该操作可能会导致大量随机I/O操作
    * 一次扫描算法: 一次性取出满足条件的所有字段，然后在排序区 sort  buffer 中排序后直接输出结果集。排序时内存开销较大，但是排序效率比两次扫描算法要高
    * MySQL 通过比较系统变量max_length_for_sort_data 的大小和Query语句取出的字段总大小， 来判定是否那种排序算法，如果max_length_for_sort_data 更大，那么使用第二种优化之后的算法；否则使用第一种
    * 可以适当提高 sort_buffer_size  和 max_length_for_sort_data  系统变量，来增大排序区的大小，提高排序的效率
* 第二种通过有序索引顺序扫描直接返回有序数据，这种情况即为 using index，不需要额外排序，操作效率高

### 优化子查询

使用子查询可以一次性的完成很多逻辑上需要多个步骤才能完成的SQL操作，同时也可以避免事务或者表锁死，并且写起来也很容易。但是，有些情况下，子查询是可以被更高效的连接（JOIN）替代

```sql
-- 优化前
explain select * from user where uid in (select uid from user_role ); 
-- 优化后
explain select * from user u , user_role ur where u.uid = ur.uid;
```

!> 连接(Join)查询之所以更有效率一些 ，是因为MySQL不需要在内存中创建临时表来完成这个逻辑上需要两个步骤的查询工作

