# MySQL 概述

<div style="text-align: center;"><img alt='202403262018063' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403262018063.png' width=500px> </div>

## MySQL 简介

<div style="text-align: center;"><img alt='202403311806695' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311806695.png' width=500px> </div>

### 概述

- MySQL以其**开源**、**免费**、**体积小**、**便于安装**，而且功能强大等特点，成为了全球最受欢迎的数据库管理系统之一。
- MySQL是一款单进程多线程、支持多用户、基于客户机/服务器( Client/Server，C/S)的关系数据库管理系统。
- 开源软件

### 优势

- 成本低：开放源代码，社区版本可以免费使用。
- 性能良：执行速度快，功能强大。
- 操作简单：安装方便快捷，有多个图形客户端管理工具（MySQL Workbench/Navicat、MySQLFront, SQLyog等客户端）和一些集成开发环境。
- 兼容性好：安装于多种操作系统，跨平台性好，不存在32位和64位机的兼容，无法安装的问题。

## MySQL体系

### 组成

连接池组件、管理服务和工作组件、SQL接口组件、查询分析组件、优化器组件、缓存组件、插件式存储引擎以及物理文件

<div style="text-align: center;"><img alt='202403262019242' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403262019242.png' width=500px> </div>

### MySQL 的工作流程

<div style="text-align: center;"><img alt='202403262021724' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403262021724.png' width=500px> </div>

1. 操作系统用户**启动MySQL服务**
2. MySQL服务启动期间，首先将MySQL配置文件中的**参数信息读入MySQL服务器**内存
3. 根据MySQL配置文件的参数信息或者编译MySQL时参数的默认值生成一个MySQL服务实例进程
4. MySQL服务实例进程派生出**多个线程**为多个MySQL客户机提供服务
5. 数据库用户访问MySQL服务器的数据时，首先需要选择一台登录主机，然后在该登录主机上开启MySQL客户机，输入正确的账户名、密码，建立一条MySQL客户机与MySQL服务器之间的**通信链路**
6. 接着数据库用户就可以在MySQL客户机上**书写MySQL命令或SQL语句**，这些MySQL命令或SQL语句沿着该通信链路传送给MySQL服务实例，这个过程称为MySQL客户机向MySQL服务器发送请求
7. MySQL服务实例负责解析这些MySQL命令或SQL语句，并选择一种执行计划运行这些MySQL命令或SQL语句，然后将执行结果沿着通信链路返回给MySQL客户机，这个过程称为MySQL服务器向MySQL客户机返回响应
8. 数据库用户关闭MySQL客户机，通信链路被断开，该客户机对应的MySQL会话结束

### MySQL系统组成

- MySQL数据库服务
  - MySQL服务器、MySQL实例和MySQL数据库
- MySQL客户程序和工具程序
  - 负责与服务器进行通信
  - 主要有：mysql，mysqladmin，mysqlcheck、isamchk、muisamchk，mysqldump和mysqlhotcopy
- 服务器的语言: sql
  - SQL是结构化查询语言(Structured Query Language，SQL)的英文缩写
  - 它是一种专门用来与数据库通信的语言，即数据库管理系统就是通过SQL语言管理数据库中的数据

#### 服务器的语言分类

SQL：结构化查询语言（Structured Query Language），是关系型数据库的标准语言，它的特点是：简单、灵活、功能强大。它具体包含以下 5个部分：

- 数据查询语言（DQL）：就是用来搜索数据库里面的数据，也称为“数据检索语句”，以从表中获得数据，确定数据怎样5在应用程序出。保留字 SELECT 是 DQL（也是所有 SQL）用得最多的动词，其他 DQL 常用的保留字有 WHERE，ORDER BY，GROUP BY 和 HAVING
- 数据操作语言（DML）：对数据表里的数据进行添加，修改，删除。其语句包括动词 INSERT，UPDATE 和 DELETE。它们分别用于添加，修改和删除表中的 行。也称为动作查询语言
- 数据定义语言（DDL）：创建删除修改数据库(表，列，索引等...)其语句包括动词 CREATE 和 DROP。在数据库中创建新表或删除表（CREATE TABLE 或 DROP TABLE）；为表加入索引等
- 事务控制语言（TCL）：它的语句能确保被 DML 语句影响的表的所有行及时得以更新。TCL 语句包括 BEGIN TRANSACTION，COMMIT 和 ROLLBACK
- 数据控制语言（DCL）：它的语句通过 GRANT（授予权限）或 REVOKE（撤销权限）获得许可，确定单个用户和 用户组对数据库对象的操作权限

### MySQL服务器和端口号

1. MySQL服务器
    - 一个安装有MySQL服务的主机系统，该主机系统还应该包括操作系统、CPU、内存及硬盘等软硬件资源
    - 同一台MySQL服务器同时运行多个MySQL服务实例时，使用端口号区分这些MySQL服务实例
2. 端口号
    - 服务器上运行的网络程序一般都是通过端口号来识别的，一台主机上端口号可以有65536个之多

## MySQL 通用语法及其分类

* SQL 通用语法:
  * SQL 可以单行或者多行书写, 以分号进行结尾；
  * SQL 语句可以使用空格或者缩进以增强语句的可读性
  * MySQL 数据库的 SQL 语句不区分大小写,  关键字建议使用大写
  * 单行注释: --注释内容,  多行注释: /\*注释内容\*/
* SQL 语句的分类

| 分类 | 全称                       | 描述                                                    |
| ---- | -------------------------- | ------------------------------------------------------- |
| DDL  | Data Definition Language   | 数据定义语言, 用来定义数据库对象(数据库、表、字段)      |
| DML  | Data Manipulation Language | 数据操作语言, 用于对数据库中的数据进行增删改            |
| DQL  | Data Query Language        | 数据查询语言,  用于查询数据库中表的记录                 |
| DCL  | Data Control Language      | 数据控制语言,  用来创建数据库用户, 控制数据库的访问权限 |