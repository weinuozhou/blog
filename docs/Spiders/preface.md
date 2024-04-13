# 导论

## 数据的概述

* 数据是对**客观事件记录**的符号, 客观事物的性质、状态以及相关关系等进行记载
  的物理符号或这些物理符号的组合。
* 数据是重要的生产要素, 是企业核心竞争力的关键要素, 是国家重要战略资源

### 数据的类型

数据的类型主要包括**结构化数据**、**半结构化数据**和**非结构化数据**

* **结构化数据**:结构化数据是具有标准化格式的数据, 可供软件和人类高效访问。它通常以表格形式呈现, 其中行和列清楚地定义数据属性
  * EXCEL文件、CSV文件
  * 关系型数据库
* **半结构化数据**:有一定结构与一致性约束,但是结构变化很大, 本质上不存在关系的数据
  * HTML
  * XML
  * 电子邮件
* **非结构化数据**:是指数据结构不规则或不完整, 没有预定义的数据模型
  * 文本文件
  * 图片
  * 音频
  * 视频

#### XML

**可扩展标记语言** (XML): 允许您以可共享的方式定义和存储数据。XML 支持计算机系统（如网站、数据库和第三方应用程序）之间的信息交换。预定义的规则*简化了在任何网络上以 XML 文件的形式传输数据*的过程, 接收者可以使用这些规则准确高效地读取数据

关于XML的详细介绍可以参考: <https://aws.amazon.com/cn/what-is/xml/>

您可以使用标记符号（在 XML 中称为标签）来定义数据。例如, 为了表示书店的数据, 您可以创建\<book>、\<title> 和 \<author> 等标签。一本书的 XML 文档的内容如下: 

```XML
<book>
<title> Learning Amazon Web Services </title>
<author> Mark Wilkins </author>
</book>
```

#### json

* JSON是一种**轻量级的数据交换格式**, 由字符串化的键值对构成
* JSON是JavaScript的子集, 但也是**独立于编程语言**的数据格式
* JSON支持的数据类型如下:

| 对象  | {}括起来的无序键值对, 键必须是字符串 |
|:---:|:---|
| 数值  | 十进制数据               |
| 字符串 | ""括起来的字符, 必须是双引号     |
| 布尔值 | true或false          |
| 数组  | []括起来的多个值           |
|  空  | null                |

```json
{
    "name":"John",
    "age":25,
    "phoneNumber":
    [
        {
          "type":"home",
          "number":"123 456-789"
         },
         {
          "type":"fax",
          "number":"123456 -789"
         }
     ]
}
```

#### 文本数据

文本数据即字符型数据, 不能参与算术运算的字符, 在计算机中一般保存在文本文件中, 文本文件常见格式包括**ASCII, MIME, TXT**

**ASCII**:美国信息交换标准代码是基于拉丁字母的一套电脑编码系统, 主要用于显示现代英语和其他西欧语言。它是最通用的信息交换标准。

**MIME**:

* 多用途互联网邮件扩展类型。是描述消息内容类型的标准, 是设定某种扩展名的文件用一种应用程序来打开的方式类型, 当该扩展名文件被访问的时候, 浏览器会自动使用指定应用程序来打开
* MIME类型由两部分组成, 第一部分是**文件的类型**, **第二部分是文件的子类型**, 两部分之间用斜杠分隔
* 在HTTP协议中, Content-Type 是一个 HTTP 头部字段, 用于指定 HTTP 请求或响应中发送的实体的 MIME 类型。可以通过在 HTTP 请求或响应头中添加 Content-Type 字段来指定 MIME 类型
* 常见的MIME类型有: 

<div style="text-align: center;">
  <img alt='202403201212345' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201212345.png' height=400px>
</div>

#### 图片数据

图片数据是指由图形、图像等构成的平面媒体。图片格式主要分两种: 点阵图（BMP、JPG）和矢量图（SWF、Photoshop生成的PSD）

* **点阵图**:是使用像素阵列(Pixel-array/Dot-matrix点阵)来表示的图像。由像素点组成的, 每个像素点都有自己的颜色值, 放大后会出现锯齿和失真。常见的点阵图格式有JPG、PNG、GIF等。点阵图适合用于需要高清晰度的照片、插图等

<div style="text-align: center;">
  <img alt='202403201103534' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201103534.png' height=400px>
</div>

* **矢量图**:就是使用直线和曲线来描述的图形, 构成这些图形的元素是一些点、线、矩形、多边形、圆和弧线它们都是通过数学公式计算获得的, 具有编辑后不失真的特点。常见的矢量图格式有AI、EPS、SVG等。矢量图适合用于需要无限放大或缩小的设计, 如标志、图标、海报等

<div style="text-align: center;">
  <img alt='202403201059368' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201059368.webp' height=400px>
</div>

#### 音频数据

音频数据就是数字化的声音数据, 一般用音频文件保存, 格式包括CD、WAV、MP3、MID、WMA、RM

#### 视频数据

视频数据是指连续的图像序列。视频文件格式包括MPEG-4、AVI、DAT、RM、MOV、ASF、WMV、DivX等

### 数据思维

人类科学研究四种范式: 

* **实验**（科学实验）
* **理论**（模型归纳）
* **计算**（模拟仿真）
* **数据思维**: 在大数据环境下, 一切资源都将以数据为核心, 人们从数据中去发现问题, 解决问题, 在数据背后挖掘真正的价值

## 数据分析的过程

* **数据采集与预处理**: 采用各种技术手段把外部各种数据源产生的数据实时或非实时地采集、预处理并加以利用
* **数据存储与管理**: 利用计算机硬件和软件技术, 对数据进行有效的存储和应用的过程, 目的在于充分有效地发挥数据的作用
* **数据处理与分析**: 用适当的分析方法, 分析收集来的数据进行分析, 提取有用信息, 形成结论
* **数据可视化**: 将数据集中的数据以图形图像形式表示, 并利用数据分析和开发工具发现其中未知信息的处理过程

<div style="text-align: center;">     <img alt='202403201214473' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201214473.png'> </div>

### 数据采集与预处理

* **数据采集与预处理**:是对数据进行ETL操作, 通过对数据进行提取、转换、加载, 最终挖掘数据的潜在价值, 然后给用户提供解决方案或者决策参考
* 三大要点:
  * **全面性**
    * 数据量足够具有分析价值
    * 数据面足够支撑分析需求
  * **多维性**
    * 数据能满足分析需求
    * 自定义数据多种属性和类型
  * **高效性**
    * 技术执行的高效性、团队内部成员协同的高效性以及数据分析需求和目标实现的高效性

<table style="border-collapse: collapse; width: 100%; text-align: center; margin-top: 20px;">
    <tr style="background-color: #f2f2f2;">
        <th style="border: 1px solid #dddddd;text-align:center; padding: 8px;"></th>
        <th style="border: 1px solid #dddddd;text-align:center; padding: 8px;">传统的数据采集</th>
        <th style="border: 1px solid #dddddd;text-align:center; padding: 8px;">大数据采集</th>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd; text-align:center; padding: 8px;">数据源</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">来源单一, 数据量相对较少</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">来源广泛, 数据量巨大</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">数据类型</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">结构单一</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">数据类型丰富, 包括结构化、半结构化和非结构化</td>
    </tr>
    <tr>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">数据存储</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">关系数据库和并行数据仓库</td>
        <td style="border: 1px solid #dddddd;text-align:center; padding: 8px;">分布式数据库, 分布式文件系统</td>
    </tr>
  </table>

#### 数据源

* **传感器数据**:传感器是一种检测装置, 能感受到被测量的信息, 并能将感受到的信息, 按一定规律变换成为电信号或其他所需形式的信息输出, 以满足信息的传输、处理、存储、显示、记录和控制等要求

> **RFID**:一种无线通信技术, 全称为: Radio Frequency Identification, 这种通信技术依托于互联网及大数据的发展, 以无线电讯号去识别目标, 并且解读出相关数据, 不用识别系统和目标之间建立机械或者其他的接触。现如今, 许多行业都应用到了这种无线通信技术, 比如说无人售货机、智能图书柜

* **互联网数据**:互联网数据的采集通常是借助于网络爬虫来完成的
* **日志数据**:日志文件数据一般由数据源系统产生, 用于记录数据源的执行的各种操作活动
  * 系统日志采集系统做的事情就是收集日志数据提供离线和在线的实时分析使用
* **企业业务系统数据**:一些企业会使用传统的关系型数据库MySQL和Oracle等来存储业务系统数据, 除此之外, Redis和MongoDB这样的NoSQL数据库也常用于数据的存储
  * 企业可以借助于**ETL**（Extract-Transform-Load）工具, 把分散在企业不同位置的业务系统的数据, 抽取、转换、加载到企业数据仓库中, 以供后续的商务智能分析使用

#### 采集方法

##### 系统日志采集(Flume)

* **用户行为日志**: 采集系统用户使用系统过程中一系列的操作日志
* **业务变更日志**: 根据特定业务场景的需要, 采集关于某用户在某时使用某功能、对某业务进行某操作的相关信息
* **系统运行日志**: 定时采集系统服务器资源、网络及基础中间件情况
* Flume:一个**高可用**、**高可靠**, **分布式**的海量**日志采集**、聚合和传输系统,实时读取服务器本地磁盘的数据, 将数据传输到HDFS

<div style="text-align: center;">     <img alt='202403201222995' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201222995.png' width=500px> </div>

##### 分布式消息订阅(kafka)

* **消息队列**: 消息队列是一种应用间的通信方式, *消息的发送者不会将消息直接发送给特定的订阅者, 而是将发布的消息分为不同类别, 订阅者只接收感兴趣的消息*
* **消息队列中间件**: Kafka是最初由LinkedIn公司开发, 是一个**分布式**、**支持分区**的（partitioned）、复制的（replicated）**K-V**存储系统。目前归属于Apache顶级项目。它以可水平扩展和高吞吐率而被广泛使用。具有以下特性: 
  
  * **高吞吐量**: 即使是非常普通的硬件Kafka也可以支持每秒数百万的消息。
  * **高可靠性**: Kafka通过**复制**和**备份**来实现消息持久化, 因此它可以保证消息不会丢失。
  * **高容错性**: Kafka集群中有一个节点作为**主节点**, 负责处理消息的读写操作, 其他的节点作为**从节点**, 从主节点拉取消息进行处理。主节点发生故障时, 从节点中的一个节点会被选举为新的主节点, 继续提供服务。
  * **高可扩展性**: Kafka集群支持**动态扩展**, 当集群需要处理更多的消息时, 可以动态添加服务器节点, 集群会自动将分区重新分配到新的节点上, 以保证服务的可用性。
* 一个分布式的基于发布/订阅模式的消息队列（Message Queue）, 主要应用于**大数据实时处理领域**
* >发布/订阅: 消息的发布者不会将消息直接发送给特定的订阅者, 而是将发布的消息分为不同类别, 订阅者只接收感兴趣的消息

<div style="text-align: center;">     <img alt='202403201223398' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201223398.png' width=500px> </div>

##### ETL(sqoop、kettle)

ETL常用于数据仓库中的数据采集和处理环节。ETL从原系统中**抽取数据**, 并根据实际商务需求对数据进行**转换**, 并把转换结果**加载**到目标数据存储中

<div style="text-align: center;">
  <img alt='202403201223412' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201223412.png' width=500px>
</div>

##### 网络数据采集(Python脚本)

* 网络爬虫: 网络爬虫是一种按照一定规则, 自动地抓取万维网信息的程序或者脚本
* 网络爬虫的分类: 
  * **通用网络爬虫**: 根据预先定义好的规则, 对网页进行深度遍历, 并提取有价值的数据
  * **聚焦网络爬虫**: 选择性地爬行那些与预先定义好的主题相关页面的网络爬虫
  * **增量式网络爬虫**: 对已下载网页采取增量式更新和只爬行新产生的或者已经发生变化网页的爬虫
* 网络爬虫的原理: 网络爬虫通过**模拟浏览器**的行为, 向服务器发送请求, 获取网页的源代码, 并从中提取有价值的数据
* 网络爬虫的流程: 
  * 确定目标: 确定需要爬取的网页的URL
  * 发送请求: 向目标URL发送请求, 获取网页的源代码
  * 提取数据: 从网页的源代码中提取有价值的数据
  * 存储数据: 将提取的数据存储到本地文件或者数据库中
  * 循环执行: 重复以上步骤, 直到满足爬取条件
* 网络爬虫的优缺点: 
  * 优点: 可以自动获取网页数据, 提高数据获取效率
  * 缺点: 可能会对目标网站造成一定程度的访问压力, 影响网站的正常运行

<div style="text-align: center;">     <img alt='202403201228789' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201228789.png' width=500px> </div>

### 数据存储

大数据的存储和一般数据的存储有极大的差别, 需要非常**高性能、高吞吐率、大容量**的基础设备

为了能够快速、稳定地存取这些数据, 至少要依赖于**磁盘阵列**, 同时还要通过**分布式存储**的方式将不同区域、类别、级别的数据存放于不同的磁盘阵列中

* **分布式文件系统HDFS**是一个高容错性系统, 被设计成适用于批量处理, 能够提供高吞吐量的数据访问
* **分布式键值系统**用于存储关系简单的半结构化数据

#### 磁盘阵列(RAID)

**磁盘阵列(RAID)**:其实就是用多个独立的磁盘组成在一起形成一个大的磁盘系统, 从而实现比单块磁盘更好的存储性能和更高的可靠性

RAID方案常见的可以分为: 

* **RAID0**
  * 它将多块磁盘组合在一起形成一个大容量的存储。当我们要写数据的时候, 会将数据分为N份, 以独立的方式实现N块磁盘的读写, 那么这N份数据会同时并发的写到磁盘中, 因此执行性能非常的高
  * RAID0 的读写性能理论上是单块磁盘的N倍（仅限理论, 因为实际中磁盘的寻址时间也是性能占用的大头）
  * RAID0的问题是, 它并不提供**数据校验或冗余备份**, 因此一旦某块磁盘损坏了, 数据就直接丢失, 无法恢复了

    <div style="text-align:center"><img alt="RAOD0" src='https://pic3.zhimg.com/80/v2-f19764545b5aef702dcf415aeaf4f53e_720w.webp' width=500px></div>

* **RAID1**
  * 在往磁盘写数据的时候, 将同一份数据无差别的写两份到磁盘, 分别写到工作磁盘和镜像磁盘, 那么它的实际空间使用率只有50%了
  * RAID1 给数据做了一个冗余备份。任何一块磁盘损坏了, 都可以再基于另外一块磁盘去恢复数据, 数据的可靠性非常强, 但性能就没那么好了

  <div style="text-align:center"><img src='https://pic4.zhimg.com/80/v2-d96a366ea45552d769d9fd653e8122eb_720w.webp' height=400px></div>

* **RAID3**
  * 将数据按照RAID0的形式, 分成多份同时写入多块磁盘, 但是还会另外再留出一块磁盘用于写「奇偶校验码」。例如总共有N块磁盘, 那么就会让其中额度N-1块用来并发的写数据, 第N块磁盘用记录校验码数据。一旦某一块磁盘坏掉了, 就可以利用其它的N-1块磁盘去恢复数据。
  * 第N块磁盘是校验码磁盘, 因此有任何数据的写入都会要去更新这块磁盘, 导致这块磁盘的读写是最频繁的, 也就非常的容易损坏

* **RAID5**
  * RAID5模式中, 不再需要用单独的磁盘写校验码了。它把校验码信息分布到各个磁盘上。例如, 总共有N块磁盘, 那么会将要写入的数据分成N份, 并发的写入到N块磁盘中, 同时还将数据的校验码信息也写入到这N块磁盘中（数据与对应的校验码信息必须得分开存储在不同的磁盘上）。一旦某一块磁盘损坏了, 就可以用剩下的数据和对应的奇偶校验码信息去恢复损坏的数据。
  * RAID5的方式, 最少需要三块磁盘来组建磁盘阵列, 允许最多同时坏一块磁盘。如果有两块磁盘同时损坏了, 那数据就无法恢复了

    <div style="text-align:center"><img src='https://pic2.zhimg.com/80/v2-b2b9390180a9e5bf186cab19c31192d9_720w.webp'></div>

* **RAID6**
  * 为了进一步提高存储的高可用, 聪明的人们又提出了RAID6方案, 可以在有两块磁盘同时损坏的情况下, 也能保障数据可恢复
  * RAID6除了每块磁盘上都有同级数据XOR校验区以外, 还有针对每个数据块的XOR校验区, 这样的话, 相当于每个数据块有两个校验保护措施, 因此数据的冗余性更高了
  * 但是RAID6的这种设计也带来了很高的复杂度, 虽然数据冗余性好, 读取的效率也比较高, 但是写数据的性能就很差。因此RAID6在实际环境中应用的比较少

* **RAID10**
  
  * RAID10兼备了RAID1和RAID0的有优点。首先基于RAID1模式将磁盘分为2份, 当要写入数据的时候, 将所有的数据在两份磁盘上同时写入, 相当于写了双份数据, 起到了数据保障的作用。且在每一份磁盘上又会基于RAID0技术讲数据分为N份并发的读写, 这样也保障了数据的效率
  * 但也可以看出RAID10模式是有一半的磁盘空间用于存储冗余数据的, 浪费的很严重, 因此用的也不是很多

  <div style="text-align:center"><img src='https://pic3.zhimg.com/80/v2-aeb458ddba57d0e3742f6dc6a15b7756_720w.webp'></div>

#### 分布式数据库

* **分布式**:分布式（Distributed）是指系统中的组件和资源分布在多个计算机或节点上, 而不是集中在单一的地方
* **数据库**:数据库用通俗易懂的话来说就是管理数据的地方, 就像生活中一个存放货物的仓库, 我们要按一定的规则把物品整整齐齐的摆好(写数据), 这样就方便我们去检索出货(查数据)
* **分布式数据库**:分布式数据库是一种数据库系统, 其中数据存储和处理分布在**多个计算机节点**上, 而这些节点通过网络连接在一起。与传统的集中式数据库系统不同, 分布式数据库系统的设计目标是提高性能、可伸缩性、容错性和可用性
  * 横向扩展性（Scalability）:  可以通过增加节点的方式来扩展系统的容量和性能, 而不是通过提升单个节点的性能。
  * 高可用性（High Availability）:  分布式数据库设计目标之一是确保系统在某些节点发生故障时仍然能够提供服务。通过在多个节点上存储数据的副本, 系统可以在发生故障时继续运行。
  * 容错性（Fault Tolerance）:  分布式数据库需要具备容错机制, 能够处理节点故障、网络故障或其他意外情况, 以保障系统的可靠性。
  * 灵活性:  分布式数据库系统通常支持多种数据模型, 例如关系型、文档型、键值对等, 以满足不同应用场景的需求。
  * 数据一致性:  确保分布式环境下的数据一致性是一项复杂的任务。分布式数据库系统采用不同的一致性协议和机制, 如CAP定理（Consistency, Availability, Partition Tolerance）中的不同权衡。  

### 数据清洗

* **数据清洗**:是指将大量原始数据中的“脏”数据“洗掉”, 是发现并纠正数据文件中可识别的错误的最后一道程序, 包括检查数据一致性、处理无效值和缺失值等
* **数据质量**: 是指在业务环境下, 数据符合数据消费者的使用目的, 能满足业务场景具体需求的程度。主要指标包括准确性、完整性、简洁性、适用性

#### 数据清洗的任务

检查数据一致性, 过滤或修改哪些不符合要求的数据, 主要包括不完整的数据、错误的数据、重复的数据

<div style="text-align: center;">     <img alt='202403201234215' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201234215.png' width=600px> </div>

##### 一致性检查

根据每个变量的**合理取值范围**和**相互关系**, 检查数据命名是否规范, 是否有冲突, 数据内容是否合乎要求, 记录是否有拼写错误, 发现超出正常范围、逻辑上不合理或者相互矛盾的数据

##### 不完整的数据

不完整的数也叫作**缺失数据**(缺失值), 是指在该数据中的一应该有的信息缺失

##### 错误的数据

错误的数据是指在数据库中出现了错误的数据值, 错误值包括**输入错误**和**错误数据**

##### 重复的数据

重复的数据也叫作**相似重复记录**或**冗余的数据**

#### 数据清洗的流程

1. **预处理**:查看数据的元数据及数据特征。看元数据, 包括字段解释、数据来源、代码表等一切描述数据的信息；抽取一部分数据, 使用人工查看方式, 对数据本身有一个直观的了解
2. **格式与内容清洗**:错误数据包含格式内容问题数据和逻辑问题数据两类
3. **缺失值处理**
    * 将存在遗漏信息属性值的对象(元组、记录)删除
    * 将数据缺失的内容分别写入不同数据库文件并要求客户或厂商重新提交新数据, 要求在规定的时间内补全, 补全后才继续写入数据仓库中
    * 有时也可以用一定的值去填充空值, 从而使信息表完备化
4. **逻辑错误清洗**:逻辑错误清洗是指通过简单的逻辑推理来发现数据中存在的问题数据, 从而防止分析结果走偏

<table style="border-collapse: collapse; width: 100%; text-align:center">
    <tr>
      <th style="border: 1px solid #dddddd; text-align: center; padding: 8px; background-color: #f2f2f2;">步骤</th>
      <th colspan="2" style="border: 1px solid #dddddd; text-align: center; padding: 8px; background-color: #f2f2f2;">具体内容</th>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px; background-color: #f2f2f2;">预处理</td>
      <td colspan="2" style="border: 1px solid #dddddd; text-align: center; padding: 8px; background-color: #f2f2f2;">选择数据处理工具；查看数据的元数据及数据特征；多余数据清洗；关联性验证</th>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">格式与内容清洗</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">格式内容问题</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">时间、日期、数值、全半角等显示格式不一致；
内容中有不该存在的字符；数据内容与该字段应有内容不符</td>
    </tr>
    <tr>
      <td rowspan="4"style="border: 1px solid #dddddd; vertical-align: middle; text-align: center; padding: 8px;">缺失值处理方法</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">确定缺失值范围</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">区分重要性高低, 缺失率高低</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">去除不需要的字段</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">整例删除、变量删除、成对删除</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">填充缺失值的内容</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">以业务知识和经验来填充;以同一字段指标的计算结果(均值、中位数、众数等)填充;以不同指标的计算结果填充</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">重新获取数据</td>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">将数据过滤出来, 按缺失的内容分别写入不同数据库文件并要求客户或厂商重新提交新数据, 要求在规定的时间内补全, 补全后才继续写入数据仓库中</td>
    </tr>
    <tr>
      <td style="border: 1px solid #dddddd; text-align: center; padding: 8px;">逻辑错误清洗</td>
      <td colspan="2" style="border: 1px solid #dddddd; text-align: center; padding: 8px;">去重处理；矛盾内容处理；离群值(异常值)处理</td>
    </tr>
  </table>

## 编码体系

网页编码: 是指网页中字符的编码方式

* **ASCII**: 一个英文字母（不分大小写）占一个字节的空间
* **中文字符编码**:主要有gb2312、gbk以及gb18030
* **unicode**: 容纳世界上所有语言字符和符号的集合
* **utf-8**（8-bit unicode Transformation Format）是一种针对unicode字符集的可
变长度字符编码方式

Python 3中的字符串默认的编码为unicode, 因此, gbk、gb2312等字符编码与utf-8编码之间都必须通过unicode编码才能互相转换。即在python中, 使用`encode()`将unicode编码为utf-8、gbk等, 而使用`decode()`将utf-8、gbk等字符编码解码为unicode

<div style="text-align: center;">     <img alt='202403201239764' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201239764.png' width=500px> </div>
