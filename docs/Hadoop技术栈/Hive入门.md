# Hive数据仓库入门

随着大数据时代的全面到来，传统数据仓库面临的挑战主要包括以下几个方面。

1. *无法满足快速增长的海量数据存储需求*。目前企业数据增长速度非常快，动辄几十 TB 的数据，已经大大超出了 Oracle/DB2 等传统数据仓库的处理能力。这是因为传统数据仓库大都基于关系数据库，关系数据库横向扩展性较差，纵向扩展性有限。
2. *无法有效处理不同类型的数据*。传统数据仓库通常只能存储和处理结构化数据，但是，随着企业业务的发展，企业中部署的系统越来越多，数据源的数据格式越来越丰富，很显然，传统数据仓库无法处理如此众多的数据类型。
3. *计算和处理能力不足*。由于传统数据仓库建立在关系数据库基础之上，因此，会存在一个很大的痛点，即计算和处理能力不足，当数据量达到 TB 量级后，传统数据仓库基本无法获得好的性能。

## Hadoop和Hive

### Hadoop是什么

* Hadoop是一个由Apache基金会所开发出来的分布式系统基础架构，是利用集群对大量数据进行分布式存储和处理的框架
* 主要解决海量数据的存储和分析处理

### Hadoop核心设计

* HDFS为海量数据提供了存储
* MapReduce为海量数据提供了计算

### Hadoop组成

1. **Hadoop Distributed File System (HDFS):** HDFS是Hadoop的分布式文件系统，用于存储大规模数据集。它将数据分割成小块，并分布存储在集群中的多个节点上，提供高容错性和可靠性。

   * **NameNode**

     * **定义：** NameNode是HDFS的主服务器，负责管理文件系统的命名空间和存储块信息。

     * **功能：**
       * 负责维护文件系统的命名空间树，记录文件和目录的层次结构。
       * 存储文件元数据，包括文件的名称、权限、大小、时间戳等信息。
       * 记录每个文件被分成的数据块的位置信息，但不存储实际的数据。

     * **单点故障：** NameNode是HDFS的单点故障，其失效会导致整个文件系统不可用。为了提高可用性，可以使用Secondary NameNode来定期合并和检查日志，以协助恢复

   * **DataNode**

     * **定义：** DataNode是HDFS的工作节点，负责存储实际的数据块。

     * **功能：**
       * 负责存储和检索数据块，执行对数据块的读取和写入操作。
       * 定期向NameNode报告它所存储的数据块的信息，包括块的ID、大小和存储位置。
       * 处理客户端的读写请求，并与其他DataNode协同工作以确保数据的可靠性和冗余备份。

     * **数据冗余：** HDFS通过数据冗余（通常是三个副本）来确保数据的可靠性。如果某个DataNode失效，HDFS可以从其他副本中恢复数据。

     * **动态添加：** HDFS支持动态添加DataNode，使得集群能够适应数据量的增长。

   * **Secondary NameNode**：Secondary NameNode并不是NameNode的备份，它主要用于辅助NameNode的工作。它定期合并和压缩编辑日志，以减轻NameNode的负担，并在必要时创建新的镜像文件，以帮助快速恢复NameNode
   * **Checkpoint:** Checkpoint是HDFS的检查点目录，用于存储NameNode的镜像和编辑日志的合并文件。这有助于快速恢复文件系统的状态。

2. **MapReduce:** MapReduce是Hadoop的计算模型，用于处理和分析大规模数据。它包括两个主要阶段，即Map阶段和Reduce阶段。Map阶段负责将输入数据分割成键值对，并生成中间结果；Reduce阶段负责将中间结果汇总并生成最终输出。

3. **YARN (Yet Another Resource Negotiator):** YARN是Hadoop的资源管理器，负责集群资源的管理和任务的调度。它允许多个应用程序在同一集群上共享资源，提高了集群的利用率。

   * ResourceManager
   * NodeManager
   * ApplicationMaster
   * Container

4. **Hadoop Common:** Hadoop Common包含一组共享的工具和库，为Hadoop的其他模块提供基本支持。这包括文件系统、Shell命令、日志服务等。

## Hive概述

Hive 是一个构建在 Hadoop 之上的数据仓库工具，在 2008 年 8 月开源。Hive 在某种程度上可以看作用户编程接口，其本身并不存储和处理数据，而是依赖 HDFS 来存储数据，依赖 MapReduce（或者 Tez、Spark）来处理数据。Hive 定义了简单的类似 SQL 的查询语言——HiveQL，它与大部分 SQL 语法兼容

* Hive是一种可以用来构建数据仓库的工具
* Hive分析数据底层是MapReduce
* Hive具有类似SQL的操作语言HiveQL
* 所有Hive 处理的数据都存储在HDFS中
* **Hive的核心是将HiveQL转换成MapReduce程序，然后将程序提交到Hadoop集群执行**

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402052034989.png'></center>

### Hive的优缺点

* **优点**
  * **SQL-Like查询语言：** Hive使用类似于SQL的查询语言（HiveQL），使得对有SQL经验的用户更容易上手。这降低了学习曲线，使得可以在Hadoop上进行数据处理和分析。
  * **大规模数据处理：** Hive适用于大规模数据集的处理和分析，特别是在Hadoop集群上。它能够处理PB级别的数据，并支持并行处理。
  * **可扩展性：** Hive具有良好的可扩展性，可以在需要时轻松扩展到更大的数据规模和更多的节点。
  * **数据存储格式支持：** Hive支持多种数据存储格式，包括文本、序列文件、Avro、ORC等，使得用户可以选择最适合其需求的存储格式。
  * **集成性：** Hive可以与其他Hadoop生态系统工具（如HBase、Spark）以及数据仓库工具（如Apache Impala、Apache Drill）进行集成，形成更全面的数据处理和分析解决方案。
  * **元数据存储：** Hive使用元数据存储，可以让用户方便地管理表、分区和其他元数据信息。
* **缺点**
  * **高延迟：** Hive不适合实时数据处理，因为它通常具有较高的查询延迟，不如一些专为实时查询设计的工具（如Apache Impala）
  * **复杂性：** 尽管HiveQL类似于SQL，但它并不是标准的SQL，而且某些复杂查询可能需要用户理解Hadoop的内部工作原理，这可能使得对初学者来说较为复杂。
  * **不适合小规模数据：** Hive对于小规模数据集的处理效率可能不如传统的数据库系统，因为它在处理大规模数据时才能发挥其优势
  * **性能：** 对于一些需要实时性能的场景，Hive的性能可能不如一些专门设计为低延迟的工具，如Apache Impala或Apache Drill
  * **动态数据：** Hive对于动态数据和频繁变更的数据模式的支持相对较弱，因为它更适用于静态数据和批处理作业

## Hive组件

1. **Hive CLI（命令行界面）：**
   * **定义：** Hive CLI是Hive的命令行界面，允许用户通过命令行执行HiveQL查询和管理Hive表。
   * **作用：** 提供了交互式的方式，允许用户直接在命令行中输入HiveQL语句，并查看查询结果。
2. **HiveServer2：**
   * **定义：** HiveServer2是Hive的服务化版本，允许远程客户端通过Thrift、JDBC或ODBC协议连接到Hive。
   * **作用：** 提供了一种远程方式连接和执行Hive查询的方式，支持多种编程语言和工具。
3. **Hive Metastore：**
   * **定义：** Hive Metastore存储了Hive的元数据信息，包括数据库、表、分区、列等的定义和统计信息。
   * **作用：** 允许Hive查询引擎访问和管理元数据，使用户能够执行元数据查询和分析。
4. **Hive Query Processor：**
   * **定义：** Hive查询处理器负责解析和执行HiveQL查询语句。
   * **作用：** 将HiveQL查询转换为在Hadoop集群上运行的MapReduce作业，或者在更现代的版本中，可以使用Apache Tez、Apache Spark等执行引擎。
5. **Hive Execution Engine（执行引擎）：**
   * **定义：** Hive Execution Engine是负责执行Hive查询的组件，它可以基于不同的执行引擎，如MapReduce、Tez、Spark等。
   * **作用：** 处理和优化Hive查询，将其转化为底层执行引擎可理解的形式，以实现高效的数据处理。
6. **Hive UDFs（用户自定义函数）：**
   * **定义：** Hive支持用户自定义函数，用户可以编写自己的函数来处理数据。
   * **作用：** 提供了灵活性，用户可以通过编写自定义函数来扩展Hive的功能，以满足特定的业务需求。
7. **Hive Storage Handlers：**
   * **定义：** Hive Storage Handlers定义了如何读取和写入底层数据存储系统，如HBase、ORC、Parquet等。
   * **作用：** 允许Hive与不同的数据存储格式和存储系统进行集成，提供了对多种数据存储的支持。
8. **Hive SerDe（序列化/反序列化）：**
   * **定义：** Hive SerDe定义了数据的序列化和反序列化方式，以支持在Hive中存储和查询不同格式的数据。
   * **作用：** 允许Hive在不同的数据格式之间进行转换，包括文本、Avro、JSON等。

## Hive的系统架构

Hive 主要由以下 3 个模块组成:*用户接口模块*、*驱动模块*以及*元数据存储模块*。用户接口模块包括 CLI、Hive 网页接口（Hive Web Interface,HWI）、JDBC、ODBC、Thrift Server 等，用来实现外部应用对 Hive 的访问

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402052036326.png'></center>

## Hive的工作原理

Hive 的执行引擎可以是 MapReduce、Tez 或 Spark，这里只介绍当采用 MapReduce 作为执行引擎时 Hive 的工作原理。Hive 可以快速实现简单的 MapReduce 作业，主要通过自身组件把 HiveQL 语句转换成 MapReduce 作业来实现

## Hive数据模型

* 数据模型:用来描述数据、组织数据和对数据进行操作，是对现实世界数据特征的描述
* Hive中的数据可以在粒度上分为三类
  * Table 表
  * Partition 分区
  * Bucket 分桶

### Table 表

* Hive表与关系型数据库的表相同，Hive表是存储在HDFS中的

### Partitions 分区

Hive支持分区，这是一种将数据表分割成多个部分的技术，以便更高效地执行查询。分区表是基于表中一个或多个列的值来组织的，Hive还支持多重分区，即在分区表的基础上进一步分区。

#### 分区表的优点
1. **改进查询性能**：只需查询相关分区而不是整个表，可以显著提高查询效率。
2. **数据管理**：可以对特定分区进行管理操作，如删除旧数据等。
3. **优化存储**：根据不同的分区使用不同的存储策略，如压缩。

#### 创建分区表
创建分区表的基本语法是：
```sql
CREATE TABLE table_name (column1 datatype, column2 datatype, ...)
PARTITIONED BY (partition_column1 datatype, partition_column2 datatype, ...)
STORED AS file_format;
```
这里，`PARTITIONED BY` 关键字用来定义一个或多个分区列。

#### 示例
假设你有一个销售数据表，你可以按年份和国家进行分区：
```sql
CREATE TABLE sales (item_id int, amount double, date date)
PARTITIONED BY (year int, country string)
STORED AS PARQUET;
```
在这个例子中，`year` 和 `country` 是分区列。

#### 使用分区
在分区表中插入数据时，需要指定分区。例如：
```sql
INSERT INTO sales PARTITION (year=2023, country='USA')
VALUES (1, 100.0, '2023-01-01');
```
查询时，可以指定分区以提高性能：
```sql
SELECT * FROM sales WHERE year = 2023 AND country = 'USA';
```

#### 注意事项
- 分区策略应该基于查询模式和数据大小来选择。
- 过多的分区可能导致元数据存储的膨胀和管理上的复杂性。
- 分区表在处理大量小文件时可能不太高效。

总的来说，Hive分区表是一种强大的功能，能够提高大数据环境下的查询性能和数据管理效率。

### Bucket 分桶

在Hive中，除了分区表，还有一个重要的概念叫做“分桶表”（Bucketed Table）。分桶是一种将数据在存储时分散到多个文件（或桶）中的技术，通常用于优化查询性能和提高数据的管理效率。

#### 分桶表的优点

1. **查询优化**：通过分桶可以提高某些类型查询的性能，尤其是JOIN操作。
2. **数据抽样**：通过从特定的桶中读取数据，可以方便地对数据进行抽样。
3. **高效的数据组织**：分桶有助于更有效地组织数据，减少数据倾斜问题。

#### 创建分桶表

创建分桶表的基本语法是：

```sql
CREATE TABLE table_name (column1 datatype, column2 datatype, ...)
CLUSTERED BY (column_name) INTO num_buckets BUCKETS;
```

这里，`CLUSTERED BY` 关键字用于定义用于分桶的列，`num_buckets` 指定了桶的数量。

#### 示例

假设你有一个交易记录表，你可以根据交易ID来分桶：

```sql
CREATE TABLE transactions (transaction_id int, customer_id int, amount double, date date)
CLUSTERED BY (transaction_id) INTO 10 BUCKETS;
```

在这个例子中，表是按照 `transaction_id` 分成10个桶。

#### 使用分桶

在分桶表中插入数据时，Hive会自动根据分桶列的值将数据分配到相应的桶中。例如：

```sql
INSERT INTO transactions VALUES (1, 101, 1000.0, '2023-01-01');
```

查询时，Hive可以有效地利用桶信息来优化查询，特别是在JOIN操作中。

#### 注意事项

- 选择适当的分桶列和桶的数量是优化性能的关键。
- 分桶可能不适用于所有场景，尤其是数据分布不均匀的情况。
- 分桶表的管理比非分桶表复杂。

总的来说，Hive分桶表通过将数据分散到多个桶中，为大规模数据处理提供了优化路径，特别是对于频繁的JOIN和聚合操作。

### 内部表和外部表

在Hive中，表可以被分类为内部表（Managed Table）和外部表（External Table）。这两种类型的表在数据存储和管理上有着本质的区别。

#### 内部表（Managed Table）

- **数据存储**：内部表的数据存储在Hive控制的Hadoop文件系统（HDFS）目录中。
- **生命周期管理**：当你删除一个内部表时，Hive会删除表的元数据以及存储的数据文件。
- **适用场景**：当数据只被Hive使用或者数据的生命周期完全由Hive管理时，内部表是一个好的选择。

#### 外部表（External Table）

- **数据存储**：外部表的数据存储在Hadoop文件系统上的任意位置，这些数据可能由其他应用程序生成和管理。
- **生命周期管理**：删除外部表时，只会删除表的元数据，而不会删除数据文件。
- **适用场景**：当数据需要被Hive以外的其他应用程序或系统访问时，外部表是更好的选择。它允许数据在不同的应用程序之间共享。

#### 创建表的示例

##### 内部表

```sql
CREATE TABLE internal_table (column1 datatype, column2 datatype, ...)
STORED AS file_format;
```
在这个示例中，`internal_table` 是一个内部表。

##### 外部表

```sql
CREATE EXTERNAL TABLE external_table (column1 datatype, column2 datatype, ...)
STORED AS file_format
LOCATION 'hdfs_path_to_data';
```

在这个示例中，`external_table` 是一个外部表，数据存储在指定的HDFS路径上。

#### 关键区别

1. **数据的物理存储**：内部表的数据由Hive管理，外部表的数据可以位于Hive管理范围之外。
2. **生命周期**：内部表的数据随着表的删除而被删除，而外部表的数据即使表被删除也仍然保留。
3. **数据共享**：外部表更适合于数据需要在不同应用程序间共享的场景。

选择内部表还是外部表取决于具体的数据管理需求和使用场景。例如，对于临时分析或者完全由Hive管理的数据，内部表可能是更好的选择。而对于需要跨多个平台共享的稳定数据集，外部表可能更合适。

### 视图

* 视图是一种虚拟表，是一个逻辑的概念
* 视图建立在已有表的基础上
* 视图可以简化复杂的查询