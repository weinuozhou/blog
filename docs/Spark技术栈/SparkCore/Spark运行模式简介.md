# Spark概述

## Spark简介

Spark是**基于内存计算**的大数据并行计算框架，可用于构建大型的、低延迟的数据分析应用程序

Spark 具有如下 4 个主要特点:

* **运行速度快**: Spark 使用先进的有向无环图（Directed Acyclic Graph,DAG）执行引擎，以支持循环数据流与内存计算，基于内存的执行速度可比 Hadoop MapReduce 快上百倍，基于磁盘的执行速度也能快十倍左右
* **容易使用**: Spark 支持使用 Scala、Java、Python 和 R 语言进行编程，简洁的 API 设计有助于用户轻松构建并行程序，并且可以通过 Spark Shell 进行交互式编程
* **通用性**: Spark 提供了完整而强大的技术栈，包括 SQL 查询、流式计算、机器学习和图算法组件，这些组件可以无缝整合在同一个应用中，足以应对复杂的计算
* **运行模式多样**: Spark 可运行于独立的集群模式中，或者运行于 Hadoop 中，也可运行于 Amazon EC2 等云环境中，并且可以访问 HDFS、Cassandra、HBase、Hive 等多种数据源

## Spark与Hadoop的对比

回顾 Hadoop 的工作流程，可以发现 Hadoop 存在以下缺点:

* **表达能力有限**: 计算都必须要转化成 Map 和 Reduce 两个操作，但这并不适合所有的情况，难以描述复杂的数据处理过程。
* **磁盘 IO 开销大**: 每次执行时都需要从磁盘读取数据，并且在计算完成后需要将中间结果写入磁盘中，IO 开销较大。
* **延迟高**: 一次计算可能需要分解成一系列按顺序执行的 MapReduce 任务，任务之间的衔接由于涉及 IO 开销，会产生较高延迟。而且，在前一个任务执行完成之前，其他任务无法开始，因此难以胜任复杂、多阶段的计算任务

Spark 在借鉴 Hadoop MapReduce 优点的同时，很好地解决了 MapReduce 所面临的问题。相比于 MapReduce，Spark 主要具有如下优点:

* Spark 的计算模式也属于 MapReduce，但不局限于 Map 和 Reduce 操作，还提供了多种数据集操作类型，编程模型比 MapReduce 更灵活
* Spark 提供了内存计算，中间结果直接放到内存中，带来了更高的迭代运算效率
* Spark 基于 DAG 的任务调度执行机制，要优于 MapReduce 的迭代执行机制

尽管 Spark 相对 Hadoop 具有较大优势，但 **Spark 并不能完全替代 Hadoop**，其主要用于替代 Hadoop 中的 MapReduce 计算模型

## Spark运行架构

### 基本概念

* RDD：是分布式内存的一个抽象概念，提供了一种高度受限的共享内存模型
* DAG：反映 RDD 之间的依赖关系
* Executor：是运行在工作节点（Worker Node）上的一个进程，负责运行任务，并为应用程序存储数据
* 应用：用户编写的 Spark 应用程序
* 任务：运行在 Executor 上的工作单元
* 作业：一个作业（Job）包含多个 RDD 及作用于相应 RDD 上的各种操作
* 阶段：是作业的基本调度单位，一个作业会分为多组任务（Task），每组任务被称为「阶段」（Stage），或者也被称为「任务集」

### 架构设计

Spark 的运行架构包括**集群管理器**（Cluster Manager）、**运行作业任务的工作节点**（Worker Node）、**每个应用的任务控制节点**（Driver）和**每个工作节点上负责具体任务的执行进程**（Executor）。其中，集群管理器可以是 Spark 自带的资源管理器，也可以是 YARN 或 Mesos 等资源管理框架

Spark 所采用的 Executor 有两个优点：

* 利用多线程来执行具体的任务（Hadoop MapReduce 采用的是进程模型），减少任务的启动开销
* Executor 中有一个 BlockManager 存储模块，会将内存和磁盘共同作为存储设备，当需要多轮迭代计算时，可以将中间结果存储到这个存储模块里，下次需要时就可以直接读该存储模块里的数据，而不需要读写到 HDFS 等文件系统里，因而有效减少了 IO 开销

<div style="text-align: center;"><img alt='202404072139940' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072139940.png' width=500px> </div>

在 Spark 中，一个应用（Application）由一个任务控制节点（Driver）和若干个作业（Job）构成，一个作业由多个阶段（Stage）构成，一个阶段由多个任务（Task）组成。当执行一个应用时，任务控制节点会向集群管理器（Cluster Manager）申请资源，启动 Executor，并向 Executor 发送应用程序代码和文件，然后在 Executor 上执行任务，运行结束后执行结果会返回给任务控制节点，或者写到 HDFS 或者其他数据库中

<div style="text-align: center;"><img alt='202404072140373' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072140373.png' width=500px> </div>

### Spark运行流程

1. 当一个 Spark 应用被提交时，首先需要为这个应用构建起基本的运行环境，即由任务控制节点（Driver）创建一个 SparkContext，由 SparkContext 负责和资源管理器—Cluster Manager 的通信，以及进行资源的申请、任务的分配和监控等。SparkContext 会向资源管理器注册并申请运行 Executor 的资源
2. 资源管理器为 Executor 分配资源，并启动 Executor 进程，Executor 运行情况将随着「心跳」发送到资源管理器上
3. SparkContext 根据 RDD 的依赖关系构建 DAG，并将 DAG 提交给 DAG 调度器（DAGScheduler）进行解析，将 DAG 分解成多个「阶段」（每个阶段都是一个任务集），并且计算出各个阶段之间的依赖关系，然后把一个个「任务集」提交给底层的任务调度器（TaskScheduler）进行处理；Executor 向 SparkContext 申请任务，任务调度器将任务分发给 Executor 运行，同时 SparkContext 将应用程序代码发放给 Executor
4. 任务在 Executor 上运行，把执行结果反馈给任务调度器，然后反馈给 DAG 调度器，运行完毕后写入数据并释放所有资源

<div style="text-align: center;"><img alt='202404072140367' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072140367.png' width=500px> </div>

总体而言，Spark 运行架构具有以下特点:

* 每个应用都有自己专属的 Executor 进程，并且该进程在应用运行期间一直驻留。Executor 进程以多线程的方式运行任务，减少了多进程任务频繁的启动开销，使得任务执行变得非常高效和可靠
* Spark 运行过程与资源管理器无关，只要能够获取 Executor 进程并保持通信即可
* 任务采用了**数据本地性**和推测执行等优化机制。数据本地性是尽量将计算移到数据所在的节点上进行，即「计算向数据靠拢」，因为移动计算比移动数据所占的网络资源要少得多。而且，Spark 采用了延时调度机制，可以在更大程度上实现执行过程优化。比如拥有数据的节点当前正被其他的任务占用，那么在这种情况下是否需要将数据移动到其他的空闲节点上呢？答案是不一定。因为如果经过预测发现当前节点结束当前任务的时间要比移动数据的时间还要少，那么调度就会等待，直到当前节点可用

## RDD的设计与运行原理

### RDD的设计背景

* 许多迭代式算法（比如机器学习、图算法等）和交互式数据挖掘工具，共同之处是，不同计算阶段之间会重用中间结果
* 目前的MapReduce框架都是把中间结果写入到HDFS中，带来了大量的**数据复制**、**磁盘IO**和**序列化开销**
* RDD就是为了满足这种需求而出现的，它提供了一个抽象的数据架构，我们不必担心底层数据的分布式特性，只需将具体的应用逻辑表达为一系列转换处理，不同RDD之间的转换操作**形成依赖关系**，可以实现管道化，避免中间数据存储

### RDD的概念

* 一个RDD就是一个**分布式对象集合**，本质上是一个只读的分区记录集合，每个RDD可分成多个分区，每个分区就是一个数据集片段，并且一个RDD的不同分区可以被保存到集群中不同的节点上，从而可以在集群中的不同节点上进行并行计算
* RDD提供了一种**高度受限的共享内存模型**，即RDD是只读的记录分区的集合，不能直接修改，只能基于稳定的物理存储中的数据集创建RDD，或者通过在其他RDD上执行确定的转换操作（如map、join和group by）而创建得到新的RDD

RDD典型的执行过程如下：

* RDD读入外部数据源进行创建
* RDD经过一系列的转换（Transformation）操作，每一次都会产生不同的RDD，供给下一个转换操作使用
* 最后一个RDD经过“动作”操作进行转换，并输出到外部数据源

!> 这一系列处理称为一个Lineage（血缘关系），即DAG拓扑排序的结果

?> 优点：惰性调用、管道化、避免同步等待、不需要保存中间结果、每次操作变得简单

<div style="text-align: center;"><img alt='202404072143630' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072143630.png' width=500px> </div>

### RDD 特性

Spark采用RDD以后能够实现高效计算的原因主要在于：

* **高效的容错性**
    * 现有容错机制：数据复制或者记录日志
    * RDD：**血缘关系**、重新计算丢失分区、无需回滚系统、重算过程在不同节点之间并行、只记录粗粒度的操作
* **中间结果持久化到内存**，数据在内存中的多个RDD操作之间进行传递，避免了不必要的读写磁盘开销
* **存放的数据可以是Java对象**，避免了不必要的对象序列化和反序列化

### RDD 之间的依赖关系

DAG 调度器根据 RDD 之间的依赖关系，把 DAG 划分成若干个阶段。RDD 中的依赖关系分为窄依赖（Narrow Dependency）与宽依赖（Wide Dependency），二者的主要区别在于**是否包含 Shuffle 操作**

* 窄依赖表现为一个父RDD的分区对应于一个子RDD的分区或多个父RDD的分区对应于一个子RDD的分区
* 宽依赖则表现为存在一个父RDD的一个分区对应一个子RDD的多个分区

<div style="text-align: center;"><img alt='202404072144202' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072144202.png' width=500px> </div>

### 阶段的划分

* Spark 根据 DAG 图中的RDD 依赖关系，把一个作业分成多个阶段。阶段划分的依据是窄依赖和宽依赖。对于宽依赖和窄依赖而言，窄依赖**对于作业的优化很有利**，宽依赖无法优化
* 逻辑上，每个RDD 操作都是一个fork/join（一种用于并行执行任务的框架），把计算 fork 到每个RDD 分区，完成计算后对各个分区得到的结果进行join 操作，然后fork/join下一个RDD 操作
* 窄依赖可以实现“流水线”优化，宽依赖无法实现“流水线”优化

<div style="text-align: center;"><img alt='202404072145291' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072145291.png' width=500px> </div>

### RDD运行过程

通过上述对RDD概念、依赖关系和Stage划分的介绍，结合之前介绍的Spark运行基本流程，再总结一下RDD在Spark架构中的运行过程：

1. 创建RDD对象
2. SparkContext负责计算RDD之间的依赖关系，构建DAG
3. DAGScheduler负责把DAG图分解成多个Stage，每个Stage中包含了多个Task，每个Task会被TaskScheduler分发给各个WorkerNode上的Executor去执行

## Spark的部署和应用方式

### Spark三种部署方式

Spark支持三种不同类型的部署方式，包括：

* Standalone（类似于MapReduce1.0，slot为资源分配单位）
* Spark on Mesos（和Spark有血缘关系，更好支持Mesos）
* Spark on YARN

<div style="text-align: center;"><img alt='202404072146772' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072146772.png' width=500px> </div>


### Hadoop和Spark的统一部署

* 由于Hadoop生态系统中的一些组件所实现的功能，目前还是无法由Spark取代的，比如，Storm
* 现有的Hadoop组件开发的应用，完全转移到Spark上需要一定的成本

不同的计算框架统一运行在YARN中，可以带来如下好处：

* 计算资源按需伸缩
* 不用负载应用混搭，集群利用率高
* 共享底层存储，避免数据跨集群迁移

<div style="text-align: center;"><img alt='202404072147837' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404072147837.png' width=500px> </div>

