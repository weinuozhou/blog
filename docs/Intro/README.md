# 大数据技术概述

## 大数据技术的起源

今天我们常说的大数据技术, 其实起源于Google在2004年前后发表的三篇论文, 也就是我们经常听到的**三驾马车**
* 分布式文件系统 `GFS`: [Google File System 中文翻译版](http://blog.csdn.net/xuleicsu/archive/2005/11/10/526386.aspx)
* 大数据分布式计算框架 `MapReduce`: [MapReduce: 超大机群上的简单数据处理 中文翻译版](http://blog.csdn.net/active1001/archive/2007/07/02/1675920.aspx)
* NoSQL数据库系统 `BigTable`: [Google's BigTable 原理 中文翻译版](http://blog.csdn.net/accesine960/archive/2006/02/09/595628.aspx)

## 从搜索引擎讲起

我们知道, 搜索引擎主要就做两件事情, 一个是**网页抓取**, 一个是**索引构建**, 而在这个过程中, 有大量的数据需要存储和计算。这**三驾马车**其实就是用来解决这个问题的, 从介绍中也能看出来, 一个**文件系统**、一个**计算框架**、**一个数据库系统**

## 分布式与大数据技术

现在你听到*分布式*、*大数据*之类的词, 肯定一点儿也不陌生。但你要知道, 在2004年那会儿, 整个互联网还处于懵懂时代, Google 发布的论文实在是让业界为之一振, 大家恍然大悟, 原来还可以这么玩。因为那个时间段, 大多数公司的关注点其实还是聚焦在单机上, 在思考如何提升单机的性能, 寻找更贵更好的服务器。而 Google 的思路是**部署一个大规模的服务器集群**, 通过分布式的方式将海量数据存储在这个集群上, 然后利用集群上的所有机器进行数据计算。 这样, Google其实不需要买很多很贵的服务器, 它只要把这些普通的机器组织到一起, 就非常厉害了

## 大数据技术的开源实现

当时的天才程序员, 也是 Lucene 开源项目的创始人 Doug Cutting 正在开发开源搜索引擎 Nutch, 阅读了 Google 的论文后, 他非常兴奋, 紧接着就根据论文原理初步实现了类似 `GFS` 和 `MapReduce` 的功能

两年后的2006年, Doug Cutting将这些大数据相关的功能从Nutch中分离了出来, 然后启动了一个独立的项目专门开发维护大数据技术, 这就是后来赫赫有名的 `Hadoop` , 主要包括`Hadoop`分布式文件系统 `HDFS` 和大数据计算引擎 `MapReduce`

?> 当我们回顾软件开发的历史, 包括我们自己开发的软件(当然鄙人不才,  还无法开发软件), 你会发现, 有的软件在开发出来以后无人问津或者寥寥数人使用, 这样的软件其实在所有开发出来的软件中占大多数。而有的软件则可能会开创一个行业, 每年创造数百亿美元的价值, 创造百万计的就业岗位, 这些软件曾经是 `Windows` 、 `Linux` 、 `Java`,  而现在这个名单要加上`Hadoop`的名字

如果有时间, 你可以简单浏览下`Hadoop`的代码, 这个纯用 Java 编写的软件其实并没有什么高深的技术难点, 使用的也都是一些最基础的编程技巧, 也没有什么出奇之处, 但是它却给社会带来巨大的影响, 甚至带动一场深刻的科技革命, 推动了人工智能的发展与进步。

!> 我觉得, 我们在做软件的时候, 也可以多思考一下, 我们所开发软件的价值点在哪里？真正需要使用软件实现价值的地方在哪里？你应该关注业务、理解业务, 有价值导向, 用自己的技术为公司创造真正的价值, 进而实现自己的人生价值。而不是整天埋头在需求说明文档里, 做一个没有思考的代码机器人

## 大数据技术的兴起

`Hadoop`发布之后, Yahoo很快就用了起来。大概又过了一年到了2007年, 百度和阿里巴巴也开始使用`Hadoop`进行大数据存储与计算。

2008年, `Hadoop`正式成为Apache的顶级项目, 后来Doug Cutting本人也成为了Apache基金会的主席。自此, `Hadoop`作为软件开发领域的一颗明星冉冉升起。同年, 专门运营`Hadoop`的商业公司Cloudera成立, `Hadoop`得到进一步的商业支持

## 大数据生态系统的开发

这个时候, Yahoo的一些人觉得用 `MapReduce` 进行大数据编程太麻烦了, 于是便开发了 `Pig` , `Pig` 是一种脚本语言, 使用类SQL的语法, 开发者可以用 `Pig` 脚本描述要对大数据集上进行的操作,  `Pig` 经过编译后会生成 `MapReduce` 程序, 然后在`Hadoop`上运行。编写 `Pig` 脚本虽然比直接 `MapReduce` 编程容易, 但是依然需要学习新的脚本语法。于是Facebook又发布了 `Hive` 。 `Hive` 支持使用SQL语法来进行大数据计算, 比如说你可以写个`Select` 语句进行数据查询, 然后`Hive`会把SQL语句转化成`MapReduce`的计算程序

这样, 熟悉数据库的数据分析师和工程师便可以无门槛地使用大数据进行数据分析和处理了。`Hive`出现后极大程度地降低了`Hadoop`的使用难度, 迅速得到开发者和企业的追捧。据说, 2011年的时候, Facebook大数据平台上运行的作业90%都来源于`Hive`

随后, 众多`Hadoop`周边产品开始出现, 大数据生态体系逐渐形成, 其中包括: 专门将关系数据库中的数据导入导出到`Hadoop`平台的`Sqoop`；针对大规模日志进行分布式收集、聚合和传输的`Flume`；`MapReduce`工作流调度引擎`Oozie`等

## Yarn 的推出

在`Hadoop`早期, `MapReduce`既是一个执行引擎, 又是一个资源调度框架, 服务器集群的资源调度管理由 `MapReduce` 自己完成。但是这样不利于资源复用, 也使得 `MapReduce` 非常臃肿。于是一个新项目启动了, 将`MapReduce`执行引擎和资源调度分离开来, 这就是`Yarn`。2012年, Yarn成为一个独立的项目开始运营, 随后被各类大数据产品支持, 成为大数据平台上最主流的资源调度系统

## Spark的推出

同样是在2012年, UC伯克利AMP实验室（Algorithms、Machine和People的缩写）开发的`Spark`开始崭露头角。当时AMP实验室的马铁博士发现使用`MapReduce`进行机器学习计算的时候性能非常差, 因为机器学习算法通常需要进行很多次的迭代计算, 而`MapReduce`每执行一次Map和Reduce计算都需要重新启动一次作业, 带来大量的无谓消耗。还有一点就是`MapReduce`主要使用磁盘作为存储介质, 而2012年的时候, 内存已经突破容量和成本限制, 成为数据运行过程中主要的存储介质。`Spark`一经推出, 立即受到业界的追捧, 并逐步替代`MapReduce`在企业应用中的地位

## 批处理与流处理

一般说来, 像`MapReduce`、`Spark`这类计算框架处理的业务场景都被称作**批处理计算**, 因为它们通常针对以天为单位产生的数据进行一次计算, 然后得到需要的结果, 这中间计算需要花费的时间大概是几十分钟甚至更长的时间。因为计算的数据是非在线得到的实时数据, 而是历史数据, 所以这类计算也被称为大数据离线计算。而在大数据领域, 还有另外一类应用场景, 它们需要对实时产生的大量数据进行即时计算, 比如对于遍布城市的监控摄像头进行人脸识别和嫌犯追踪。这类计算称为**大数据流计算**, 相应地, 有`Storm`、`Flink`、`Spark Streaming`等流计算框架来满足此类大数据应用的场景。 流式计算要处理的数据是实时在线产生的数据, 所以这类计算也被称为大数据实时计算

## NoSQL与大数据技术

在典型的大数据的业务场景下, 数据业务最通用的做法是, **采用批处理的技术处理历史全量数据**, 采用流式计算处理实时新增数据。而像`Flink`这样的计算引擎, 可以同时支持流式计算和批处理计算。除了大数据批处理和流处理, `NoSQL`系统处理的主要也是大规模海量数据的存储与访问, 所以也被归为大数据技术。 `NoSQL`曾经在2011年左右非常火爆, 涌现出`HBase`、`Cassandra`等许多优秀的产品, 其中`HBase`是从`Hadoop`中分离出来的、基于`HDFS`的`NoSQL`系统

## Summary

我们回顾软件发展的历史会发现, 差不多类似功能的软件, 它们出现的时间都非常接近, 比如Linux和Windows都是在90年代初出现, Java开发中的各类MVC框架也基本都是同期出现, Android和iOS也是前脚后脚问世。2011年前后, 各种`NoSQL`数据库也是层出不群, 事物发展有自己的潮流和规律, 当你身处潮流之中的时候, 要紧紧抓住潮流的机会, 想办法脱颖而出, 即使没有成功, 也会更加洞悉时代的脉搏, 收获珍贵的知识和经验。而如果潮流已经退去, 这个时候再去往这个方向上努力, 只会收获迷茫与压抑, 对时代、对自己都没有什么帮助。但是时代的浪潮犹如海滩上的浪花, 总是一浪接着一浪, 只要你站在海边, 身处这个行业之中, 下一个浪潮很快又会到来。你需要敏感而又深刻地去观察, 略去那些浮躁的泡沫, 抓住真正潮流的机会, 奋力一搏, 不管成败, 都不会遗憾

正所谓在历史前进的逻辑中前进, 在时代发展的潮流中发展。通俗的说, 就是要在风口中飞翔。上面我讲的这些基本上都可以归类为大数据引擎或者大数据框架。而大数据处理的主要应用场景包括数据分析、数据挖掘与机器学习。数据分析主要使用`Hive`、`Spark SQL`等SQL引擎完成；数据挖掘与机器学习则有专门的机器学习框架TensorFlow、Mahout以及MLlib等, 内置了主要的机器学习和数据挖掘算法

此外, 大数据要存入分布式文件系统（HDFS）, 要有序调度`MapReduce`和`Spark`作业执行, 并能把执行结果写入到各个应用系统的数据库中, 还需要有一个大数据平台整合所有这些大数据组件和企业应用系统