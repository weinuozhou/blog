# Hadoop的发展与YARN

## Hadoop的优化与发展

### Hadoop的局限与不足

Hadoop 1.0 的核心组件（仅指 MapReduce 和 HDFS，不包括 Hadoop 生态系统内的 Pig、Hive、HBase 等其他组件）主要存在以下不足:

* __抽象层次低__。功能实现需要手工编写代码来完成，有时只是为了实现一个简单的功能，也需要编写大量的代码。
* __表达能力有限__。MapReduce 把复杂分布式编程工作高度抽象为两个函数，即 Map 和 Reduce，在降低开发人员程序开发复杂度的同时，却也带来了表达能力有限的问题，实际生产环境中的一些应用是无法用简单的 Map 和 Reduce 来完成的。
* __开发者自己管理作业之间的依赖关系__。一个作业（Job）只包含 Map 和 Reduce 两个阶段，通常的实际应用问题需要大量的作业进行协作才能顺利解决，这些作业之间往往存在复杂的依赖关系，但是 MapReduce 框架本身并没有提供相关的机制对这些依赖关系进行有效管理，只能由开发者自己管理。
* __难以看到程序整体逻辑__。用户的处理逻辑都隐藏在代码细节中，没有更高层次的抽象机制对程序整体逻辑进行设计，这就给代码理解和后期维护带来了障碍。
* __执行迭代操作效率低__。对于一些大型的机器学习、数据挖掘任务，往往需要多轮迭代才能得到结果。采用 MapReduce 实现这些算法时，每次迭代都是一次执行 Map、Reduce 任务的过程，这个过程的数据来自分布式文件系统 HDFS，本次迭代的处理结果也被存放到 HDFS 中，继续用于下一次迭代过程。反复读写 HDFS 中的数据，大大降低了迭代操作的效率。
* __资源浪费__。在 MapReduce 框架设计中，Reduce 任务需要等待所有 Map 任务都完成后才可以开始，造成了不必要的资源浪费。
* __实时性差__。只适用于离线批数据处理，无法支持交互式数据处理、实时数据处理

### Hadoop的改进

<center><img src='https://pica.zhimg.com/v2-c8239bb66c6765c65fe0cf95696211ec_720w.jpg?source=d16d100b'></center>


## Hadoop2.0的改进

### HDFS HA

对于分布式文件系统 HDFS 而言，__名称节点（NameNode）是系统的核心节点__，存储了各类元数据信息，并负责管理文件系统的命名空间和客户端对文件的访问。但是，在 HDFS 1.0 中，只存在一个名称节点，一旦这个唯一的名称节点发生故障，就会导致整个集群变得不可用，这就是常说的「单点故障问题」。虽然 HDFS 1.0 中存在一个第二名称节点（Secondary NameNode），但是第二名称节点并不是名称节点的备用节点，它与名称节点有着不同的职责。第二名称节点的主要功能是周期性地从名称节点获取命名空间镜像文件（FsImage）和修改日志（EditLog），进行合并后发送给名称节点，替换掉原来的 FsImage，以防止日志文件 EditLog 过大，导致名称节点失败恢复时消耗过多时间。合并后的命名空间镜像文件 FsImage 在第二名称节点中也保存一份，当名称节点失效的时候，可以使用第二名称节点中的 FsImage 进行恢复。

HDFS 2.0 采用了高可用（High Availability,HA）架构。在一个典型的 HA 集群中，一般设置两个名称节点，其中一个名称节点处于「活跃」（Active）状态，另一个处于「待命」（Standby）状态

### HDFS联邦

* HDFS采用单名称节点的设计，不仅会带来单点故障问题，还会存在可扩展性、系统整体性能和隔离性等问
* 在系统整体性能方面，整个 HDFS 的性能会受限于单个名称节点的吞吐量
* 在隔离性方面，单个名称节点难以提供不同程序之间的隔离性，一个程序可能会影响其他程序的运行（比如一个程序消耗过多资源导致其他程序无法顺利运行）
* _在 HDFS 联邦中，设计了多个相互独立的名称节点，使得 HDFS 的命名服务能够横向扩展，这些名称节点分别进行各自命名空间和块的管理，相互之间是联邦关系，不需要彼此协调_

## 资源管理调度器YARN

### MapRecude1.0的缺陷

<center><img src='https://pica.zhimg.com/v2-17b44308b74270ca8cfea1acf60fc24a_720w.jpg?source=d16d100b'></center>

MapReduce 1.0 采用 `Master/Slave` 架构设计，包括一个 `JobTracker` 和若干个 `TaskTracker`，前者负责作业的调度和资源的管理，后者负责执行 `JobTracker` 指派的具体任务。这种架构设计具有一些很难克服的缺陷:

* **存在单点故障**：MapReduce 1.0 由 `JobTracker` 负责所有 MapReduce 作业的调度，而系统中只有一个 `JobTracker` ，因此会存在单点故障问题，即这个唯一的 `JobTracker` 出现故障就会导致系统不可用。
* `JobTracker` 导致**任务过重**:  `JobTracker` 既要负责作业的调度和失败恢复，又要负责资源管理分配。 `JobTracker` 执行过多的任务，需要消耗大量的资源
* **容易出现内存溢出**: 在 `TaskTracker` 端，资源的分配并不考虑 CPU、内存的实际使用情况，而只是根据 `MapReduce` 任务的个数来分配资源。当两个具有较大内存消耗的任务被分配到同一个 `TaskTracker` 上时，很容易发生内存溢出的情况。
* **资源划分不合理**: 资源（CPU、内存）被强制等量划分成多个「槽」（Slot），槽又被进一步划分为 Map 槽和 Reduce 槽两种，分别供 Map 任务和 Reduce 任务使用，彼此之间不能使用分配给对方的槽。也就是说，当 Map 任务已经用完 Map 槽时，即使系统中还有大量剩余的 Reduce 槽，也不能拿来运行 Map 任务，反之亦然。这就意味着，当系统中只存在单一 Map 任务或 Reduce 任务时，会造成资源的浪费

### YARN 的架构

#### 主从架构

YARN，主从架构，有2个角色
* 主（Master）角色：`ResourceManager`
    * 整个集群的资源调度者， 负责协调调度各个程序所需的资源
* 从（Slave） 角色：`NodeManager`
    * 单个服务器的资源调度者，负责调度单个服务器上的资源提供给应用程序使用

<div style="text-align: center;"><img alt='202404211910105' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211910105.png' width=500px> </div>

#### 辅助架构

YARN 还可以搭配2个辅助角色使得YARN集群运行更加稳定
* **代理服务器**(ProxyServer)：Web Application Proxy Web应用程序代理
* **历史服务器**(JobHistoryServer)： 应用程序历史信息记录服务

##### Web应用代理(Web Application Proxy)

代理服务器，即Web应用代理是 YARN 的一部分。默认情况下，它将作为资源管理器(RM)的一部分运行，但是可以配置为在独立模式下运行。使用代理的原因是为了减少通过 YARN 进行基于网络的攻击的可能性

对外提供WEB 站点会有安全性问题， 而代理服务器的功能就是最大限度保障对WEB UI的访问是安全的。 比如：
* 警告用户正在访问一个不受信任的站点
* 剥离用户访问的Cookie

!> 代理服务器默认集成在了ResourceManager中

##### JobHistoryServer历史服务器

历史服务器的功能很简单： 记录历史运行的程序的信息以及产生的日志并提供WEB UI站点供用户使用浏览器查看

<div style="text-align: center;"><img alt='202404211915982' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211915982.png' width=500px> </div>

### YARN的设计思路

* 基本思路就是「放权」，**即不让 `JobTracker` 这一个组件承担过多的功能**，对原 `JobTracker` 三大功能（资源管理、任务调度和任务监控）进行拆分，分别交给不同的新组件去处理
* 重新设计后得到的 YARN 包括 `ResourceManager`、`ApplicationMaster` 和 `NodeManager`，其中，**由 ResourceManager 负责资源管理，由 ApplicationMaster 负责任务调度和监控，由 NodeManager 负责执行原 TaskTracker 的任务**

<center><img src='https://pic1.zhimg.com/v2-88cc513265b8179c35493a7a482af814_720w.jpg?source=d16d100b'></center>

### YARN的工作流程

在 YARN 框架中执行一个 MapReduce 程序时，从提交到完成需要经历如下 8 个步骤：

1. **用户编写客户端应用程序**，向 `YARN` 提交应用程序，提交的内容包括 `ApplicationMaster` 程序、启动 `ApplicationMaster` 的命令、用户程序等。
2. **YARN 中的 ResourceManager 负责接收和处理来自客户端的请求**。接到客户端应用程序请求后，`ResourceManager` 里面的调度器会为应用程序分配一个容器。同时，`ResourceManager` 的应用程序管理器会与该容器所在的 `NodeManager` 通信，为该应用程序在该容器中启动一个 `ApplicationMaster`
3. **ApplicationMaster 被创建后会首先向 ResourceManager 注册，从而使得用户可以通过 ResourceManager 来直接查看应用程序的运行状态**。接下来的步骤（4-7）是具体的应用程序执行步骤。
4. **ApplicationMaster 采用轮询的方式通过 RPC 协议向 ResourceManager 申请资源**。
5. `ResourceManager `以「容器」的形式向提出申请的 `ApplicationMaster` 分配资源，一旦` ApplicationMaster `申请到资源，就会与该容器所在的 `NodeManager` 进行通信，要求它启动任务。
6. 当 `ApplicationMaster `要求容器启动任务时，它会为任务设置好运行环境（包括环境变量、JAR 包、二进制程序等），然后将任务启动命令写到一个脚本中，最后通过在容器中运行该脚本来启动任务。
7. 各个任务通过某个 RPC 协议向` ApplicationMaster` 汇报自己的状态和进度，让` ApplicationMaster` 可以随时掌握各个任务的运行状态，从而可以在任务失败时重新启动任务。
8. 应用程序运行完成后，`ApplicationMaster` 向 `ResourceManager` 的应用程序管理器注销并关闭自己。若 `ApplicationMaster `因故失败，`ResourceManager` 中的应用程序管理器会监测到失败的情形，然后将其重新启动，直到所有的任务执行完毕。

<center><img src='https://picx.zhimg.com/v2-6f7204657bb82697644768162f8575f1_720w.jpg?source=d16d100b'></center>

### YARN的发展目标

YARN 的提出，并非仅为了解决 MapReduce 1.0 框架中存在的缺陷，实际上，YARN 有着更加宏伟的发展构想，**即发展成为集群中统一的资源管理调度框架，在一个集群中为上层的各种计算框架提供统一的资源管理调度服务**

YARN 的目标就是实现**一个集群多个框架**，即在一个集群上部署一个统一的资源调度管理框架 YARN，在 YARN 之上可以部署各种计算框架，比如 MapReduce、Tez、HBase、Storm、Giraph、Spark、OpenMPI 等，由 YARN 为这些计算框架提供统一的资源调度管理服务，并且能够根据各种计算框架的负载需求，调整各自占用的资源，实现集群资源共享和资源弹性收缩

<center><img src='https://pic1.zhimg.com/v2-03f59564202e6808f9aa2979b6df6d30_720w.jpg?source=d16d100b'></center>

