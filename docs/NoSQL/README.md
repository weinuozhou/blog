# NoSQL简介

NoSQL 数据库**没有固定的表结构**, 通常也不存在连接操作, 也没有严格遵守 ACID 约束。因此, 与关系数据库相比, NoSQL 具有**灵活的水平可扩展性**, 可以支持海量数据存储。此外, NoSQL 数据库支持 MapReduce 风格的编程, 可以较好地应用于大数据时代的各种数据管理。通常 NoSQL 数据库具有以下 3 个特点: 

* **灵活的可扩展性**: NoSQL 数据库在设计之初就是为了满足「横向扩展」的需求, 因此天生具备良好的横向（水平）扩展能力
* **灵活的数据模型**: NoSQL 数据库天生就旨在摆脱关系数据库的各种束缚条件, 摈弃了流行多年的关系数据模型, 转而采用键值、列族等非关系数据模型, 允许在一个数据元素里存储不同类型的数据
* **与云计算紧密融合**: NoSQL 数据库可以凭借自身良好的横向扩展能力, 充分利用云计算基础设施, 很好地将数据库融入云计算环境中, 构建基于 NoSQL 的云数据库服务

## web2.0的特性

* **Web 2.0 网站系统通常不要求严格的数据库事务**: 如果一个用户发布微博过程出现错误, 可以直接丢弃该信息, 而不必像关系数据库那样执行复杂的回滚操作, 这样并不会给用户造成什么损失
* **Web 2.0 并不要求严格的读写实时性**: 比如用户的微博粉丝数量增加了 10 个, 在几分钟后显示更新的粉丝数量, 用户可能也不会察觉
* **Web 2.0 通常不包含大量复杂的 SQL 查询**: Web 2.0 网站在设计时就已经尽量减少甚至避免这类操作, 通常只采用单表的主键查询, 因此关系数据库的查询优化机制在 Web 2.0 中难以有所作为

### 关系型数据库的缺陷

关系数据库已经无法满足 Web 2.0 的需求, 主要表现在以下 3 个方面: 

* **无法满足海量数据的管理需求**: 对于关系数据库来说, 在一张有 10 亿条记录数据的表里进行 SQL 查询, 效率极其低下, 甚至是不可忍受的
* **无法满足数据高并发的需求**
* **无法满足高可扩展性和高可用性的需求**

### NoSQL兴起的原因

随着 Web 2.0 的兴起和大数据时代的到来, 关系数据库已经显得越来越力不从心, 暴露出越来越多难以克服的缺陷。于是 NoSQL 数据库应运而生, 它很好地满足了 Web 2.0 的需求, 得到了市场的青睐

## NoSQL四大类型

* **键值存储数据库**（Key-Value Stores）
    * 特点:  数据以键值对的形式存储, 每个键对应唯一的值。这种模型非常简单, 适用于需要快速存储和检索数据的场景
    * 例子:  Redis、Amazon DynamoDB
* **文档型数据库**（Document Stores）
    * 特点:  数据以文档的形式存储, 文档可以是JSON、XML等格式。文档型数据库更灵活, 适用于处理复杂的数据结构
    * 例子:  MongoDB、CouchDB
* **列族型数据库**（Column-Family Stores）
    * 特点:  数据以列族（column family）的形式存储, 每个列族包含多行, 但每行不一定包含相同的列。这种模型适合读取大量列的操作
    * 例子:  Apache Cassandra、HBase
* **图形数据库**（Graph Databases）
    * 特点:  数据以图形结构的形式存储, 包含节点和边。图形数据库适用于处理复杂的关系型数据
    * 例子:  Neo4j、Amazon Neptune

## NoSQL的三大基石

NoSQL 的三大基石包括 **CAP** 、 **BASE** 和**最终一致性**

### CAP

* **一致性**（Consistency）: 所有节点在同一时间具有相同的数据视图。即, 如果一个节点对数据进行了更新, 那么所有其他节点在同一时间应该能够读取到这个更新后的值
* **可用性**（Availability）: 每个非故障的节点在有限时间内必须返回合法的响应, 即系统需要保证对于每一个请求, 系统要么能够返回正确的结果, 要么能够报告一个错误
* **分区容错性**（Partition Tolerance）: 系统在遇到网络分区（节点之间的通信被中断）的情况下仍然能够继续工作。分区容错性是分布式系统必须要具备的基本特征, 因为网络分区是不可避免的

CAP 理论告诉我们, **一个分布式系统不可能同时满足一致性、可用性和分区容忍性这 3 个特性**, 最多只能同时满足其中 2 个, 如果追求一致性, 就要牺牲可用性, 需要处理因为系统不可用而导致的写操作失败的情况；如果要追求可用性, 就要预估到可能发生数据不一致的情况, 比如系统的读操作可能不能精确地读取写操作写入的最新值

<div style="text-align: center;"><img alt='202404072113509' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072113509.png' width=500px> </div>

#### CA（一致性 + 可用性）

* 特点:  系统追求**强一致性和高可用性**, 但不考虑分区容错性。在没有网络分区的情况下, 保证所有节点的数据一致性, 并且在任何时候都能够提供正确的响应
* 例子:  传统的关系型数据库系统, 如单机版的MySQL, 往往追求CA

#### AP（可用性 + 分区容错性）

* 特点:  系统追求**高可用性和分区容错性**, 但可能在某些情况下放弃一致性。在网络分区的情况下, 系统仍然能够提供服务, 即使不同节点之间的数据不是强一致的
* 例子:  NoSQL数据库, 如Cassandra、Amazon DynamoDB, 通常追求AP

#### CP（一致性 + 分区容错性）

* 特点:  系统追求**强一致性和分区容错性**, 但可能在某些情况下牺牲可用性。在网络分区的情况下, 系统可能会拒绝一些请求以保持一致性
* 例子:  一些分布式数据库系统, 如HBase, 往往追求CP

### Base

BASE理论是与CAP理论相关的分布式系统理论, 它提供了一种对于分布式系统在面对分区容错性（Partition Tolerance）时的一致性和可用性权衡的思考方式。BASE是"Basically Available, Soft state, Eventually consistent"的缩写

* **Basically Available** (基本可用): 系统保证基本的可用性, 即系统在面对分区故障时仍能提供服务。这意味着系统可以在一些节点发生故障或无法通信的情况下继续运行
* **Soft state** (软状态): 系统允许一段时间内不同节点的数据副本之间存在不一致。在一些时刻, 系统的状态可能是不确定的, 允许出现中间状态
* **Eventually consistent** (最终一致性): 系统最终会达到一致的状态, 但不要求实时一致性。在系统进行一些更新后, 最终所有节点的数据会达到一致状态, 但这个过程可能需要一些时间

?> BASE理论相对于ACID（Atomicity、Consistency、Isolation、Durability）传统事务模型而言, 提出了一种更为宽松的一致性模型。BASE更适用于大规模分布式系统, 特别是面对网络分区、故障和延迟的情况

?> BASE并不是一个具体的算法或技术, 而是一种设计思想, 强调在分布式系统中, 由于网络不可靠和节点故障等原因, 无法做到强一致性, 因此在可用性和一致性之间做出权衡。BASE理论的灵活性允许系统在某些情况下牺牲一致性以获得更好的可用性

### 最终一致性

> * 从服务端来看, 一致性是指更新如何复制分布到整个系统, 以保证数据最终一致
> * 从客户端来看, 一致性主要指的是在高并发的数据访问操作下, 后续操作是否能够获取最新的数据

最终一致性的要求更低, **只要经过一段时间后能够访问到更新后的数据**即可

最终一致性根据更新数据后各进程访问到数据的时间和方式的不同, 又可以进行如下区分:

* **因果一致性**:如果进程 A 通知进程 B 它已更新了一个数据项, 那么进程 B 的后续访问将获得进程 A 写入的最新值。而与进程 A 无因果关系的进程 C 的访问, 仍然遵守一般的最终一致性规则
* **读己之所写一致性**:这可以视为因果一致性的一个特例。当进程 A 自己执行一个更新操作之后, 它自己总是可以访问到更新过的值, 绝不会看到旧值
* **会话一致性**:它把访问存储系统的进程放到会话（Session）的上下文中, 只要会话还存在, 系统就保证「读己之所写」一致性。如果由于某些失败情形令会话终止, 就要建立新的会话, 而且系统保证不会延续到新的会话
* **单调读一致性**:如果进程已经看到过数据对象的某个值, 那么任何后续访问都不会返回在那个值之前的值
* **单调写一致性**:系统保证来自同一个进程的写操作顺序执行。系统必须保证这种程度的一致性, 否则编程难以进行