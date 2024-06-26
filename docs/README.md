# 前言

本书是一本**对人类用户极其友善**的大数据入门工具书, 从零开始学习大数据相关知识, 主要分享所学的计算机知识, 力求构建**大数据体系知识框架**

!> 本书主要是在参考官方文档, 并结合作者学习使用经验基础上整理总结写成的, 为了记录一路走来学习的计算机专业知识，方便之后复习与查看

* 所有 SQL 语句例子, 是基于 `MySQL-5.7.19` 运行的
* 所有 Python 语句例子, 都是基于 `Python-3.9.7` 或 `Python-3.8.10` 运行的

## 目录

### 大数据技术概述

* [大数据技术概述](/Intro/)
* [推荐系统概述](/Intro/recomendationSystem)

### 大数据相关软件安装

* [大数据软件安装包](/softwareInstall/)
* [zookeeper集群环境搭建](/softwareInstall/zookeeper集群环境搭建)
* [Hadoop集群环境搭建](/softwareInstall/Hadoop集群环境安装)
* [Spark集群环境搭建](/softwareInstall/Spark集群环境搭建)

### MySQL 基础

* **`MySQL` 概述**
    * [数据库概述](/MySQLTutorial/)
    * [信息与数据模型](/MySQLTutorial/MySQL概述/信息与数据模型)
    * [关系代数及关系数据库理论](/MySQLTutorial/MySQL概述/关系代数及关系数据库理论)
    * [MySQL概述](/MySQLTutorial/MySQL概述/MySQL概述)
    * [MySQL安装](/MySQLTutorial/MySQL概述/MySQL安装)
    * [MySQL数据类型](/MySQLTutorial/MySQL概述/MySQL数据类型)
    * [MySQL函数](/MySQLTutorial/MySQL概述/MySQL函数)
    * [MySQL约束](/MySQLTutorial/MySQL概述/MySQL约束)
* **`SQL` 语句**
    * [DDL语句](/MySQLTutorial/SQL语句/DDL语句)
    * [DML语句](/MySQLTutorial/SQL语句/DML语句)
    * [DQL语句](/MySQLTutorial/SQL语句/DQL语句)
    * [DCL语句](/MySQLTutorial/SQL语句/DCL语句)
* **`MySQL` 进阶**
    * [MySQL 存储引擎与字符集](/MySQLTutorial/MySQL进阶/MySQL存储引擎与字符集)
    * [MySQL视图](/MySQLTutorial/MySQL进阶/MySQL视图)
    * [MySQL事务与并发控制](/MySQLTutorial/MySQL进阶/MySQL事务与并发控制)
    * [MySQL索引](/MySQLTutorial/MySQL进阶/MySQL索引)
    * [MySQL存储过程与函数](/MySQLTutorial/MySQL进阶/MySQL存储过程与函数)
    * [MySQL触发器与事件调度器](/MySQLTutorial/MySQL进阶/MySQL触发器与事件调度器)
* **`MySQL` 运维**
    * [MySQL优化](/MySQLTutorial/MySQL运维/MySQL的优化)
    * [MySQL日志管理](/MySQLTutorial/MySQL运维/MySQL日志管理)
    * [MySQL数据库备份与还原](/MySQLTutorial/MySQL运维/MySQL数据库备份与还原)
    * [分布式数据库与MySQL的复制、集群技术](/MySQLTutorial/MySQL运维/分布式数据库与MySQL的复制、集群技术)
    * [Python连接MySQL数据库](/MySQLTutorial/MySQL运维/Python连接MySQL)

### Python 基础

* **`Python` 基础**
    * [Python入门](/Python0to1/)
    * [数据结构](/Python0to1/DataStructure)
    * [函数式编程](/Python0to1/function)
    * [面向对象编程](/Python0to1/oop)
    * [文件与IO](/Python0to1/FileIO.md)
    * [异常处理](/Python0to1/Exceptions)
    * [正则表达式](/Python0to1/regex)
    * [内置模块](/Python0to1/internalmodule)

### 数据分析

* [Pandas--数据探索](/Analysis/)
* [Pandas--数据结构](/Analysis/数据结构)
* [Pandas--数据清洗与集成](/Analysis/数据清洗与集成)
* [Numpy](/Analysis/numpy)
* [PandasCheatSheet](/Analysis/PandasCheat)

### 数据可视化

* [Matplotlib](/Viewer/matplotlib)
* [Pyecharts](/Viewer/pyecharts)
* [Seaborn](/Viewer/seaborn)

### Python 爬虫

* [爬虫基础](/Spiders/)
* [web前端知识](/Spiders/web)
* [网络通讯](/Spiders/webConnect)
* [发送请求](/Spiders/request)
* [解析数据](/Spiders/parsel)
* [Ajax数据请求](/Spiders/AjaxSpider)
* [Selenium的使用](/Spiders/selenium)
* [Splash的使用](/Spiders/splash)
* [数据存储](/Spiders/saveData)
* [Scrapy框架](/Spiders/scrapy)

### 机器学习

* [机器学习与数据挖掘基础](/machinelearning/)
* [机器学习算法--回归基础](machinelearning/regression)
* [分类技术--决策树](machinelearning/decisionTree)

### Linux 基础

* [Linux操作系统简介](/Linux/)
* **`Linux` 命令基础**
    * [Linux文件与目录管理](/Linux/linux命令基础/Linux文件与目录管理)
    * [Linux文件权限与归属](/Linux/linux命令基础/Linux文件基本属性)
    * [Linux用户与用户组](/Linux/linux命令基础/Linux用户与用户组)
    * [Linux磁盘管理](/Linux/linux命令基础/Linux磁盘管理)
    * [Linux进程管理](/Linux/linux命令基础/Linux进程管理)
* **`Linux` 软件安装及系统设置**
    * [Linux软件安装](/Linux/linux软件安装及系统设置/Linux软件安装)
    * [Linux环境变量](/Linux/linux软件安装及系统设置/Linux环境变量)
    * [Linux软件的启动与停止](/Linux/linux软件安装及系统设置/Linux软件的启动与停止)
    * [Linux日期与时区](/Linux/linux软件安装及系统设置/Linux日期和时区)
    * [Linux网络请求和下载](/Linux/linux软件安装及系统设置/Linux网络请求和下载)
    * [Linux IP地址与主机名](/Linux/linux软件安装及系统设置/LinuxIP地址与主机名)

### 非关系型数据库--NoSQL

* [NoSQL简介](/NoSQL/)
* [Redis](/NoSQL/redis)
* [MongoDB](/NoSQL/mongodb)

### 大数据核心组件--Hadoop

* **`Hadoop` 技术栈**
    * **`Hadoop` 基础**
        * [Hadoop的简介](/Hadoop技术栈/Hadoop/)
        * [集群资源管理器--Yarn](/Hadoop技术栈/Hadoop/探讨Hadoop)
    * **`HDFS`**
        * [分布式文件存储系统--HDFS](/Hadoop技术栈/HDFS/hdfs简介)
        * [HDFS编程实践](/Hadoop技术栈/HDFS/hdfs编程实践)
    * **`HBase`**
        * [HBase简介](/Hadoop技术栈/HBase/hbase)
        * [HBase编程实践](/Hadoop技术栈/HBase/hbase编程实践)
    * **`MapReduce`**
        * [分布式计算框架--MapReduce](/Hadoop技术栈/MapReduce/MapReduce简介)

### 数据仓库应用--Hive

* **`Hive` 技术栈**
    * [数据仓库基础](/Hive技术栈/)
    * [OLAP与多维数据模型](/Hive技术栈/OLAP与多维数据模型)
    * [数据仓库架构](/Hive技术栈/数据仓库架构)
    * [Hive简介](/Hive技术栈/Hive入门)

### 基于内存的分布式计算框架--Spark

* **`Spark` 技术栈**
    * **`SparkCore`**
        * [Spark简介](/Spark技术栈/)
        * [Spark部署模式与作业提交](/Spark技术栈/SparkCore/spark部署模式与提交运行)
        * [PySpark基本使用](/Spark技术栈/SparkCore/PySpark的基本使用)
        * [弹性分布式数据集RDD](/Spark技术栈/SparkCore/弹性分布式数据集RDD)
        * [Spark共享变量](/Spark技术栈/SparkCore/Spark共享变量)
    * **`SparkSQL`**
        * [SparkSQL简介](/Spark技术栈/SparkSQL/SparkSQL简介)
        * [定义DataFrame的模式](/Spark技术栈/SparkSQL/定义DataFrame的模式)
        * [创建DataFrame](/Spark技术栈/SparkSQL/创建DataFrame)
        * [RDD与DataFrame的转换](/Spark技术栈/SparkSQL/RDD与DataFrame的转换)
        * [DataFrame常用函数](/Spark技术栈/SparkSQL/DataFrame常用函数)
        * [日期与时间函数](/Spark技术栈/SparkSQL/日期与时间函数)
    * **`SparkDataSource`**
        * [PySpark读写csv文件](/Spark技术栈/SparkDataSource/PySpark读写csv文件)
        * [PySpark读写json文件](/Spark技术栈/SparkDataSource/PySpark读写json文件)
        * [PySpark读写parquet文件](/Spark技术栈/SparkDataSource/PySpark读写Parquet文件)
        * [PySpark读写ORC文件](/Spark技术栈/SparkDataSource/PySpark读写ORC文件)
        * [PySpark读写Parquet文件](/Spark技术栈/SparkDataSource/PySpark读写Parquet文件)
        * [PySpark读写MySQL数据库](/Spark技术栈/SparkDataSource/PySpark读写MySQL数据库)
        * [PySpark读写Hive数据库](/Spark技术栈/SparkDataSource/PySpark读写Hive数据库)

## 关于作者

* github主页: [https://github.com/weinuozhou](https://github.com/weinuozhou/blog)
* 知乎主页: [https://www.zhihu.com/people/pai-da-xiao-xing-xing-7](https://www.zhihu.com/people/pai-da-xiao-xing-xing-7)

## 鼓励作者

如果本书对你有所帮助, 想鼓励一下作者, 记得给本项目加一颗星星 `star` , 并分享给你的朋友们喔!

> [!TIP]
> 当然如果可以的话, 您的赞赏就是对作者最大的支持！！

<div style="text-align: center; border-collapse: collapse; border: 1px solid #ccc;">
<table>
    <thead>
        <tr>
            <th style="background-color: #f2f2f2; padding: 10px;">微信</th>
            <th style="background-color: #f2f2f2; padding: 10px;">支付宝</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="background-color: #f2f2f2; padding: 10px; text-align:center">
              <img alt='wechat' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404012044090.png' width=50% >
            </td>
            <td style="background-color: #f2f2f2; padding: 10px; text-align:center">
                <img alt='pay' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404012044946.png' width=50%>
            </td>
        </tr>
    </tbody>
</table>
</div>
