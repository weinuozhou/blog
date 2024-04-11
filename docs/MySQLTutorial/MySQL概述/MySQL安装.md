# MySQL 安装

## `Windows` 安装 `MySQL`

可以参考[超级详细的mysql数据库安装指南](https://zhuanlan.zhihu.com/p/37152572)

> [!warning]
> 链接文章并非作者本人所写，不代表作者观点

## `Mac` 安装 `MySQL`

可以参考[mac下mysql的安装步骤](https://zhuanlan.zhihu.com/p/37942063)

> [!warning]
> 链接文章并非作者本人所写，不代表作者观点

## `Linux` 安装 `MySQL`

在 `Linux` 系统中, 可以使用以下命令来安装 `MySQL`

```bash
sudo apt-get install mysql-server
```

该命令将会安装 `MySQL` 服务器和客户端，并创建一个名为 `mysql` 的用户组和一个名为 `mysql` 的用户账户

### 启动 MySQL 服务

```bash
sudo service mysql start
```

### 登录MySQL

```bash
mysql -u root -p
```

其中，`-u` 选项表示要使用的用户名， `root` 为默认用户名； `-p`选项表示要求输入密码。如果您没有设置密码，则可以直接按回车键进行登录

## MySQL常用图形管理工具

如果日常的开发和维护均在类似dos窗口中进行，对于编程初学者来说，上手就略微有点困难，增加了学习成本。我们一般使用mysql图形管理工具来连接Mysql，然后在图形化界面上操作Mysql

MySQL的管理维护工具非常多，除了系统自带的命令行管理工具之外，还有许多其他的图形化管理工具

### `Navicat`

Navicat是一套快速、可靠的数据库管理工具，Navicat 是以直觉化的图形用户界面而建的，可以兼容多种数据库,支持多种操作系统

<div style="text-align: center;"><img alt='202403311910129' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311910129.png' width=50%> </div>

### `SQLyog`

SQLyog 是一个快速而简洁的图形化管理MySQL数据库的工具，它能够在任何地点有效地管理你的数据库，由业界著名的Webyog公司出品

使用SQLyog可以快速直观地让您从世界的任何角落通过网络来维护远端的MySQL数据库

<div style="text-align: center;"><img alt='202403311911465' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311911465.png' width=50%> </div>

### `DataGrip`

DataGrip，是大名鼎鼎的JetBrains公司出品的，就是那个出品 Intellij IDEA 的公司

DataGrip是一款数据库管理客户端工具，方便连接到数据库服务器，执行sql、创建表、创建索引以及导出数据等

!> 本文建议使用 DataGrip 作为管理 MySQL 数据库的图形工具

<div style="text-align: center;"><img alt='202403311911464' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403311911464.png'> </div>







