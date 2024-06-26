# 分布式数据库与MySQL的复制、集群技术

分布式数据库系统( Distributed DataBase System, DDBS)是**地理上分散而逻辑上集中**的数据库系统, 即通过计算机网络将地理上分散的各局域节点连接起来共同组成一个逻辑上统一的数据库系统

分布式数据库系统有两种: 
* 物理上分布的, 但逻辑上却是集中的
* 分布式数据库系统在物理上和逻辑上都是分布的, 也就是所谓联邦式分布数据库系统

## 分布式数据库系统

> [!TIP]
> 集中式与分布式的区别

* 传统数据库系统作为一种主机/终端式系统, 表现出明显的集中式数据库体系结构
* 集中式数据库基本特征是单点数据存取与单点数据处理
* 数据库管理系统、所有用户数据以及所有应用程序都安装和存储在同一个“中心”计算机系统当中。这个中心计算机通常是大型机, 也称为主机。用户通过终端发出存取数据请求, 由通信线路传输到主机。主机予以响应并加以相应处理, 然后再通过通信线路将处理结果返回到用户终端

### 集中式数据库

<div style="text-align: center;"><img alt='202403292056744' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292056744.png' width=500px> </div>

存在的问题:
* 通信开销巨大
* 故障影响系统
* 灵活扩展不足

### 分布式数据库

分布计算的三层含义:
* 处理分布: 数据集中, 处理分布
* 功能分布
* 数据分布: 数据物理分布在不同节点上, 但在逻辑上构成一个整体, 是一个逻辑数据库

分布计算先后经历了“处理分布”、“功能分布”和“数据分布”的演变过程。其中功能分布产生客户机/服务器结构应当遵循的基本的原则, 而数据分布就导入了分布式数据库概念

分布式数据库(Distributed Database, DDB)作为数据库技术与计算机网络技术相结合的产物

?> 在本质上是一种虚拟的数据库, 整个系统由一些松散耦合的站点构成, 系统中的数据都物理地存储在不同地理站点的不同数据库（站点）中, 而系统中每个站点上运行的数据库系统之间实现着真正意义下的相互对立性

### 分布式数据库系统

分布式数据库系统(Distributed Database Systems, DDBS)是由一组**地理上分布在网络不同节点而在逻辑上属于同一系统的数据库子系统**组成, 这些数据库子系统分散在计算机网络不同计算实体之中, 网络中每个节点都具有独立处理数据的能力, 即是站点自治的。既可以执行局部应用, 同时也可以通过网络通信系统执行全局应用

<div style="text-align: center;"><img alt='202403292059915' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292059915.png' width=500px> </div>

分布式数据库的基本特征: 
* 物理分布性
* 逻辑整体性
* 站点自治性
* 站点协作

### 分布式数据库的分层模式结构

* 六层模式结构
    * **全局外模式结构**
        * 全局外部级（全局外模式）是全局应用的用户视图, 可以看作是全局模式的—个子集。一个分布式数据库可以有多个全局外模式
    * **全局概念级（全局模式）**
        * 它定义分布式数据库中全体数据的逻辑结构, 是整个分布式数据库所有全局关系的描述。全局模式提供了分布式系统中数据的物理独立性, 而全局外模式提供了数据的逻辑独立性
    * **分片级（分片模式）**
        * 描述了数据在逻辑上是怎样进行划分的。每一个全局关系可以划分为若干互不相交的片( Fragment), 片是全局关系的逻辑划分, 在物理上位于网络的若干节点上。全局关系和片之间的映射在分片模式中定义, 这种映射通常是一对多的。一个全局关系可以对应多个片, 而一个片只能来自于一个全局关系
    * **分布级（分布模式）**
        * 定义了片的存储节点, 即定义了一个片位于哪一个节点或哪些节点
    * **局部概念模式**
        * 全局关系被逻辑划分成为一个或多个逻辑分片, 每个逻辑分片被放置在一个或多个站点, 称为逻辑分片在某站点的物理映像或分片。分配在同一站点的同一全局模式的若干片段（物理片段）构成该全局模式在该站点的一个物理映像。一个站点局部模式是该站点所有全局模式在该处物理映像的集合。全局模式与站点独立, 局部模式与站点相关
    * **局部内模式**
        * DDB中关于物理数据库的描述, 与集中式数据库内模式相似, 但描述内容不仅包含局部本站点数据存储, 也包含全局数据在本站点存储描述
* 五级映射与分布透明
    * 映射1: 全局外模式层到全局模式层之间的映射
    * 映射2: 局部模式层到分片层之间的映射
    * 映射3: 分片层到分配层之间的映射
    * 映射4: 分配层到局部模式层之间的映射
    * 映射5: 局部概念层到局部内模式层之间的映射

<div style="text-align: center;"><img alt='202403292100201' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292100201.png' width=500px> </div>

### DDB中映射和相应数据独立性

* **分片透明性**
    * 分片透明性(Fragmentation Transparency)是最高层面的分布透明性, 由位于全局概念层和分片层之间的映射2实现。当DDB具有分片透明性时, 应用程序只需要对全局关系操作, 不必考虑数据分片及其存储站点。当分片模式改变时, 只需改变映射2即可, 不会影响全局模式和应用程序, 从而完成分片透明性
* **位置透明性**
    * 位置透明性(Location Transparency)由位于分片层和分配层的映射3实现。当DDB不具有分片透明性但具有位置透明性时, 编写程序需要指明数据片段名称, 但不必指明片段存储站点。当存储站点发生改变时, 只需改变分片模式到分配模式之间映射3, 而不会影响分片模式、全局模式和应用程序
* **局部数据模型透明性**
    * 局部数据模型透明性(Local Data Transparency)也称为局部映像透明性或模型透明性, 由位于分配模式和局部模式之间的映射4实现。当DDB不具有分片透明性和位置透明性, 但具有模型透明性时, 用户编写的程序需要指明数据片段名称和片段存储站点, 但不必指明站点使用的是何种数据模型, 而模型转换和查询语言转换都由映射4完成

<div style="text-align: center;"><img alt='202403292104126' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292104126.png' width=500px> </div>

DDB的分层、映射模式结构为DDB提供了一种通用的概念结构, 这种框架具有较好的数据管理优势, 其主要表现在下述几个方面: 
* **数据分片与数据分配分离**, 形成了数据分布独立性的状态
* **数据冗余的显式控制**, 数据在不同站点分配情况在分配模式中易于理解和把握, 便于系统管理
* **局部DBMS独立性**, 也就是通常所说局部映射透明性, 这就允许人们在不考虑局部DBMS专用数据模型情况下, 研究DDB管理相关问题

### 分布式数据库管理系统

?> 分布式数据库管理系统(Distributed Database Management System, DDBMS)是一组负责管理分布式环境下逻辑集成数据存取、一致性和完备性的软件系统

由于数据上的分布DDBMS在管理机制上还必须具有计算机网络通信协议的分布管理特性 

#### DDBMS基本功能

* 接受用户请求, 并判定将其发送到何处, 或必须访问哪些计算实体才能满足要求
* 访问网络数据字典, 了解如何请求和使用其中的信息
* 如果目标数据存储与系统的多台计算机上, 对其进行必需的分布式处理
* 在用户、局部DBMS和其他计算实体的DBMS之间进行协调, 发挥接口功能
* 在异构分布式处理器环境中提供数据和进行移植的支持, 其中异构是指各个站点的软件、硬件之间存在着差别

#### DDBMS组成模块

DDBMS由**本地DBMS模块、数据连接模块、全局系统目录模块和分布式DBMS模块**四个基本模块组成
* 本地DBMS模块
    * 本地DBMS模块（L-DBMS）, 是一个标准的DBMS, 负责管理本站点数据库中数据, 具有自身的系统目录表, 其中存储的是本站点上数据的总体信息。在同构系统中, 每个站点的L-DBMS实现相同, 而在异构系统中则不相同
* 数据连接模块
    * 数据连接模块( Data Communication, DC)作为一种可以让所有站点与其他站点相互连接的软件, 包含了站点及其连接方面的信息
* 全局系统目录模块
    * 全局系统目录模块(Global System Catalog, GSC)除了具有集中式数据库的数数据目录（数据字典）内容之外, 还包含数据分布信息, 例如, 分片、复制和分配模式, 其本身可以像关系一样被分片和复制分配到各个站点。一个全复制的GSC允许站点自治(Site Autonomy), 但如果某个站点的GSC改动, 其他站点的GSC也需要相应变动
* 分布式DBMS模块
    * 分布式DBMS模块(D-DBMS)是整个系统的控制中心, 主要负责执行全局事务, 协调各个局部DBMS以完成全局应用, 保证数据库的全局一致性

#### DDBS基本性质

* 数据分布透明性质
    * 在DDBS中, 数据独立性包括数据的逻辑独立性、数据的物理独立性和数据的分布透明性, 因而具有更广泛含义
        * 数据分布透明性要求用户或应用程序不必关心数据的逻辑分片、数据物理位置分配细节以及各个站点数据库使用何种数据模型, 可以像使用集中式数据库一样对物理上分布的数据库进行数据操作
* 集中与自治相结合控制机制
    * 局部DBMS独立管理局部数据库, 具有自治功能, 同时系统也设有集中控制机制, 协调各个局部DBMS工作, 执行全局管理功能
* 适度数据冗余性质
    * 在DDBS中, 数据冗余可以作为提高系统可靠性、可用性和改善其性能的基本技术手段
    * 当一个站点出现故障时, 通过数据冗余, 系统就可以对另一个站点相同副本进行操作, 从而避免了因个别站点故障而使得整个系统出现瘫痪。同时, 系统也可通过选择距用户最近的数据副本进行操作, 减少通信代价, 改善整个系统性能
    * 由于DDBS是集中式数据库的拓广, 数据冗余也会带来各个冗余副本之间数据可能不一致的问题, 设计时需要权衡利弊, 优化选择
* 事务管理分布性质 
    * 数据分布引发事务执行和管理分布, 一个全局事务执行能够分解为在若干站片点上子事务（局部事务）的执行
    * 事务的ACID性质和事务恢复具有分布性特点

<div style="text-align: center;"><img alt='202403292110255' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292110255.png' width=500px> </div>

### 同构系统与异构系统

?> 分布式数据库可以根据各个站点的数据库管理系统是否相同划分为同构(Homogeneous)系统和异构( Heterogeneous)系统

* 同构系统
    * 同构系统中所有站点都使用相同的数据库管理系统, 相互之间彼此熟悉, 合作处理客户需求。在同构系统中, 各个站点都无法独自更改模式或数据库管理系统。为了, 保证涉及多个站点的事务顺利执行, 数据库管理系统还需要和其他站点合作以交换事务信息
    * 同构系统又可以分为两种类型
        * 同构异质系统: 各站点采用同一数据模型和同一型号DBMS
        * 同构异质系统: 各站点采用同一数据模型, 但采用不同型号DBMS
* 异构系统
    * 异构系统中不同站点有不同模式和数据库管理系统, 各个站点之间可能彼此并不熟悉, 在事务处理过程中, 它们仅仅提供有限功能。模式差别是查询处理中难以解决的问题, 而软件的差别则成为全局应用的主要障碍

## 分布式数据存储

分布式数据库系统各个站点的数据在逻辑上是一个整体, 数据的存放是分散的。对于关系数据库中的关系R, 通常使用“数据复制”和“数据分片”来存储数据库

?> 数据复制: 数据复制(Data Replication)即将关系R的若干完全相同的副本分别存储在不同的站点中

?> 数据分片: 数据分片(Data Fragmentation)即将关系R分割成几个部分, 每个部分存储在不同站点中

!> 数据复制和数据分片可以结合起来使用, 即将关系R分割成几个片之后, 每个分片再拥有几个副本, 分别存储在不同的站点之中

### 数据复制方法

数据复制有部分复制和全部复制两种方式
* 部分复制是指在某些站点存储一个副本
* 全部复制是在系统每个站点都存储一个副本

### 数据复制的问题

* *更新传播* : 存在多个副本, 一旦某个副本发生改动操作, 如何进行操作使得所有副本保持一致
* **冗余控制** : 数据复制就是数据冗余, 数据冗余可以分为完全冗余、部分冗余和非冗余分配三类
* **数据独立** : 复制独立性是指用户操作时感觉不到副本的存在, 数据就好像没有复制过一样。

### 数据分片

将给定的关系分割为若干片段, 但用户感觉不到数据分片, 用户能感觉到的仍然是一个完整的数据视图

数据分片满足的条件:
* **完备性条件**:要求必须将全局关系的所有数据都映射到分片中, 在划分片段时不允许存在这样的属性, 其属于全局关系但不属于任何一个数据分片
* **不相交条件**: 要求一个全局关系被分片后所得到的各个数据分片互不重叠, 但对垂直分片的主键除外
* **可重构条件**: 要求划分后的数据分片可以通过一定的操作重新构建全局关系。对干水平分片可以通过并操作重构全局关系, 对于垂直分片可以通过连接操作构建全局关系

#### 水平分片

水平分片是指按照一定条件把全局关系分成若干不相交的元组子集, 每个子集均为关系的一个片段, 都有一定的逻辑意义。水平分片可以通过对关系进行选择运算实现。行的方向（水平的方向）将关系分为若干不相交的元组子集, 每一个子集都有一定的逻辑意义

<div style="text-align: center;"><img alt='202403292118635' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292118635.png' width=500px> </div>

#### 垂直分片

垂直分片是指按照列的方向（垂直的方向）将关系分为若干子集, 每一个子集保留了关系的某些属性

<div style="text-align: center;"><img alt='202403292119486' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292119486.png' width=500px> </div>

#### 导出分片

导出分片是指导出水平分片, 即定义水平分片的选择条件不是本身属性的条件而是其他关系属性的条件

?> 学生年龄小于20的学生课程关系分片SC-1(Sno, Cno, GRADE)是下述查询的结果:

```SQL
SELCET Sno ,Cno ,GRADE
    FROM Student, SC
WHERE Student.Sno = SC.Sno AND Student.Sa<20;
```

#### 混合分片

混合分片就是交替使用水平分片和垂直分片, 比如先用水平分片的方式得到某一个分片再采用垂直分片的方式对这个分片进行再分片例: 先进行水平分片（分片R1和R2）, 再进行垂直分片（对R1进行垂直分片: R11, 和R12）

<div style="text-align: center;"><img alt='202403292120131' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292120131.png' width=500px> </div>

## MySQL复制技术

MySQL复制是指从一个**MySQL主服务器(master)**将数据复制到**另一台或多台MySQL从服务器(slaves)**的过程, 将主数据库的DDL和DML操作通过二进制日志传到复制服务器上, 然后在从服务器上对这些日志重新执行, 从而使得主从服务器的数据保持同步

MySQL复制技术的步骤
* 主服务器将数据的改变记录到二进制日志(binary log)中
* 从服务器将主服务器的binary log events复制到它的中继日志(relay log)中
* 从服务器重做中继日志中的事件, 将数据的改变与从服务器保持同步。

## MySQL集群技术

MySQL Cluster是一种MySQL集群的技术, 是由一组计算机构成的, 每台计算机可以存放一个或者多个节点, 其中包括**MySQL服务器、DNB Cluster的数据节点、其他管理节点**, 以及专门的数据访问程序, 这些节点组合在一起, 就可以为应用提供高性能、高可用性和可缩放性的Cluster数据管理

### MySQL Cluster访问过程

应用通常使用一定的负载均衡算法将对数据的访问分散到不同的SQL节点, SQL节点对数据节点进行数据访问并从数据节点返回数据结果, 管理节点仅仅只是对SQL节点和数据节点进行配置管理, MySQL Cluster的系统架构

<div style="text-align: center;"><img alt='202403292122676' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403292122676.png' width=500px> </div>

### MySQL Cluster节点分类

* **管理节点**: 主要用来对其他节点进行管理。
* **SQL节点**: 即MySQLd服务器, 应用不能直接访问数据节点, 只能通过SQL节点访问数据节点来返回数据。
* **数据节点**: 用来存放Cluster里面的数据