# Spark部署模式与作业提交

Spark 所有模式均使用 `spark-submit` 命令提交作业，其格式如下:

```bash
cd /usr/local/spark/bin && spark-submit \
  --class <main-class> \        # 应用程序主入口类
  --master <master-url> \       # 集群的 Master Url
  --deploy-mode <deploy-mode> \ # 部署模式 client 或者 cluster
  --conf <key>=<value> \        # 可选配置       
  ... # other options    
  <application-jar> \           # Jar 包路径 
  [application-arguments]       #传递给主入口类的参数  
```

* `deploy-mode` 有 `cluster` 和 `client ` 两个可选参数，默认为 client
* `master-url` 的所有可选参数如下表所示

| Master URL| Meaning|
| :---: |:---|
|              `local`              | 使用一个线程本地运行 Spark                                   |
|            `local[K]`             | 使用 K 个 worker 线程本地运行 Spark                          |
|           `local[K,F]`            | 使用 K 个 worker 线程本地运行 , 第二个参数为 Task 的失败重试次数 |
|            `local[*]`             | 使用与 CPU 核心数一样的线程数在本地运行 Spark                |
|           `local[*,F]`            | 使用与 CPU 核心数一样的线程数在本地运行 Spark 第二个参数为 Task 的失败重试次数 |
|        `spark://HOST:PORT`            | 连接至指定的 standalone 集群的 master 节点。端口号默认是 7077。 |
| `spark://HOST1:PORT1,HOST2:PORT2` | 如果 standalone 集群采用 Zookeeper 实现高可用，则必须包含由 zookeeper 设置的所有 master 主机地址|
|        `mesos://HOST:PORT`        | 连接至给定的 Mesos 集群。端口默认是 5050。对于使用了 ZooKeeper 的 Mesos cluster 来说，使用 `mesos://zk://...` 来指定地址，使用 `--deploy-mode cluster` 模式来提交。 |
|              `yarn`               | 连接至一个 YARN 集群，集群由配置的 `HADOOP_CONF_DIR` 或者 `YARN_CONF_DIR` 来决定。使用 `--deploy-mode` 参数来配置 `client` 或 `cluster` 模式|

!> 需要注意的是：在集群环境下，`application-jar` 必须能被集群中所有节点都能访问，可以是 HDFS 上的路径；也可以是本地文件系统路径，如果是本地文件系统路径，则要求集群中每一个机器节点上的相同路径都存在该 Jar 包(一般使用**分发节点**的方式确保相同路径)

Spark任务的运行，运行方式可分为两大类:
* **本地运行**: Spark在本地运行模式一般在开发测试时使用，该模式通过在本地的一个JVM进程中同时运行driver和1个executor进程，实现Spark任务的本地运行
* **集群运行**: 在集群中运行时，其实现的本质都是考虑如何将Spark的Driver进程和Executor进程在集群中调度，并实现Dirver和Executor进行通信。当Driver程序运行在集群中时，被称为**cluster模式**，当Driver程序运行在集群之外时，称为**client模式**

<div style="text-align: center;"><img alt='202404081900922' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081900922.png' width=500px> </div>

## Local模式

在Local运行模式中，Driver和Executor运行在同一个节点的同一个JVM中。在Local模式下，只启动了一个Executor。根据不同的Master URL，Executor中可以启动不同的工作线程，用于执行Task

<div style="text-align: center;"><img alt='202404081901380' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081901380.png' width=500px> </div>

Local 模式下提交作业最为简单，不需要进行任何配置，提交命令如下:

```bash
# 本地模式提交应用
spark-submit \
--class org.apache.spark.examples.SparkPi \
--master local[2] \
/usr/local/spark/examples/jars/spark-examples_2.12-3.2.0.jar \
100
```

`spark-examples_2.12-3.2.0.jar` 是 Spark 提供的测试用例包，SparkPi 用于计算 Pi 值，执行结果如下:

<div style="text-align: center;"><img alt='202404081805626' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081805626.png' width=500px> </div>

## Standalone模式

Spark框架除了提供Spark应用程序的计算框架外，还提供了一套简易的资源管理器。该资源管理器由Master和Worker组成。Master负责对所有的Worker运行状态管理，如Worker中可用CPU、可用内存等信息，Master也负责Spark应用程序注册，当有新的Spark应用程序提交到Spark集群中时，Master负责对该应用程序需要的资源进行划分，通知Worker启动Driver或Executor。Worker负责在本节点上进行Driver或Executor的启动和停止，向Master发送心跳信息等

<div style="text-align: center;"><img alt='202404081902960' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081902960.png' width=500px> </div>

### 集群配置

请参考[Spark环境搭建](/softwareInstall/Spark集群环境搭建)

### 启动

使用 `start-all.sh` 代表启动 Master 和所有 Worker 服务

```bash
./sbin/start-master.sh 
```

访问 8080 端口，查看 Spark 的 Web-UI 界面,，此时应该显示有两个有效的工作节点:

<div style="text-align: center;"><img alt='202404081819668' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081819668.png' width=500px> </div>

### 提交作业

#### 使用 client 模式提交作业

Spark任务运行在Spark集群中时，在 `client` 模式下，用户执行 `spark-submit` 脚本后，会在执行的节点上直接运行用户编写的main函数。在用户编写的main函数中会执行 `SparkContext` 的初始化。在 `SparkConext` 初始化的过程中，该进程会向Spark集群的Master节点发送消息，向Spark集群注册一个Spark应用程序，Master节点收到消息后，会根据应用程序的需求，通知在Worker上启动相应的Executor，Executor启动后，会再次反向注册到Driver进程中。此时Driver即可知道所有的可用的Executor，在执行Task时，将Task提交至已经注册的Executor上, 也就是**在哪台机器上用spark-submit脚本提交application，driver就会在那台机器上启动**

<div style="text-align: center;"><img alt='202404081905217' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081905217.png' width=500px> </div>

```bash
# 以client模式提交到standalone集群 
spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://Master:7077 \
--executor-memory 2G \
--total-executor-cores 10 \
/usr/local/spark/examples/jars/spark-examples_2.12-3.5.0.jar \
100
```

#### 使用 cluster 模式提交作业

在cluster模式下，用户编写的main函数即Driver进程并不是在执行spark-submit的节点上执行的，而是在spark-submit节点上临时启动了一个进程，这个进程向Master节点发送通知，Master节点在Worker节点中启动Driver进程，运行用户编写的程序，当Driver进程在集群中运行起来以后，spark-submit节点上启动的进程会自动退出，其后续注册Application的过程，与client模式是完全相同的， 也就是说**driver会通过master进程，随机被分配给某一个worker进程来启动**

<div style="text-align: center;"><img alt='202404081906473' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081906473.png' width=500px> </div>

```bash
spark-submit \
--class org.apache.spark.examples.SparkPi \
--master spark://Master:7077 \
--deploy-mode cluster \
--supervise \  
--executor-memory 2G \
--total-executor-cores 10 \
/usr/local/spark/examples/jars/spark-examples_2.12-3.5.0.jar \
100
```

### 可选配置

关于 Master 和 Woker 节点的所有可选配置如下，可以在 `spark-env.sh` 中进行对应的配置

| Environment Variable（环境变量） | Meaning（含义）                                              |
| :------------------------------: | :----------------------------------------------------------- |
|       `SPARK_MASTER_HOST`        | master 节点地址                                              |
|       `SPARK_MASTER_PORT`        | master 节点地址端口（默认：7077）                            |
|    `SPARK_MASTER_WEBUI_PORT`     | master 的 web UI 的端口（默认：8080）                        |
|       `SPARK_MASTER_OPTS`        | 仅用于 master 的配置属性，格式是 "-Dx=y"（默认：none）,所有属性可以参考官方文档：[spark-standalone-mode](https://spark.apache.org/docs/latest/spark-standalone.html#spark-standalone-mode) |
|        `SPARK_LOCAL_DIRS`        | spark 的临时存储的目录，用于暂存 map 的输出和持久化存储 RDDs。多个目录用逗号分隔 |
|       `SPARK_WORKER_CORES`       | spark worker 节点可以使用 CPU Cores 的数量。（默认：全部可用） |
|      `SPARK_WORKER_MEMORY`       | spark worker 节点可以使用的内存数量（默认：全部的内存减去 1GB）； |
|       `SPARK_WORKER_PORT`        | spark worker 节点的端口（默认： random（随机））             |
|    `SPARK_WORKER_WEBUI_PORT`     | worker 的 web UI 的 Port（端口）（默认：8081）               |
|        `SPARK_WORKER_DIR`        | worker 运行应用程序的目录，这个目录中包含日志和暂存空间（default：SPARK_HOME/work） |
|       `SPARK_WORKER_OPTS`        | 仅用于 worker 的配置属性，格式是 "-Dx=y"（默认：none）。所有属性可以参考官方文档：[spark-standalone-mode](https://spark.apache.org/docs/latest/spark-standalone.html#spark-standalone-mode) |
|      `SPARK_DAEMON_MEMORY`       | 分配给 spark master 和 worker 守护进程的内存。（默认： 1G）  |
|     `SPARK_DAEMON_JAVA_OPTS`     | spark master 和 worker 守护进程的 JVM 选项，格式是 "-Dx=y"（默认：none） |
|        `SPARK_PUBLIC_DNS`        | spark master 和 worker 的公开 DNS 名称。（默认：none）       |

## Spark on Yarn模式

Spark 支持将作业提交到 Yarn 上运行，此时不需要启动 Master 节点，也不需要启动 Worker 节点

### 环境配置

Spark on Yarn环境搭建可以参考[Spark环境搭建](/softwareInstall/Spark集群环境搭建)

### 启动

必须要保证 Hadoop 已经启动，这里包括 YARN 和 HDFS 都需要启动，因为在计算过程中 Spark 会使用 HDFS 存储临时文件，如果 HDFS 没有启动，则会抛出异常

```bash
start-yarn.sh
start-dfs.sh
```

### 提交作业

#### 使用 client模式提交到yarn集群 

Spark Drvier 在提交作业的客户端进程中运行，Master 进程仅用于从 YARN 请求资源

```bash
spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode client \
--executor-memory 2G \
--num-executors 10 \
/usr/local/spark/examples/jars/spark-examples_2.12-3.5.0.jar \
100
```

#### 使用 cluster模式提交到yarn集群

Spark Drvier 在应用程序的 Master 进程内运行，该进程由群集上的 YARN 管理，提交作业的客户端可以在启动应用程序后关闭

```bash
spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode cluster \
--executor-memory 2G \
--num-executors 10 \
/usr/local/spark/examples/jars/spark-examples_2.12-3.5.0.jar \
100
```