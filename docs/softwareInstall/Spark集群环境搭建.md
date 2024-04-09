# Spark 开发环境搭建

## Local模式搭建

### 安装Spark

* 官方下载地址：[http://spark.apache.org/downloads.html](http://spark.apache.org/downloads.html) ，选择 Spark 版本和对应的 Hadoop 版本后再下载
* 也可以选择从百度网盘进行下载:[Spark环境安装](https://pan.baidu.com/s/1JPyOjpfmWTydlmrNU8hI0Q?pwd=l4sj)

下载好之后解压安装包:
```bash
sudo tar -zxvf spark-3.2.0-bin-hadoop3.2.tgz -C /usr/local
sudo mv spark* spark # 重命名
```

### 配置环境变量

```bash
vim ~/.bashrc
```

添加环境变量:
```bash
export SPARK_HOME=/usr/local/spark
export  PATH=${SPARK_HOME}/bin:$PATH
```
使得配置的环境变量立即生效:
```bash
source ~/.bashrc
```

### 启动Local模式

Local 模式是最简单的一种运行方式，它采用单节点多线程方式运行，不用部署，开箱即用，适合日常测试开发

```bash
/usr/local/spark/bin/pyspark --master local[*]
```

* local：只启动一个工作线程
* local[k]：启动 k 个工作线程
* local[*]：启动跟 cpu 数目相同的工作线程数

<div style="text-align: center;"><img alt='202404081920691' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081920691.png' width=500px> </div>

## 集群环境搭建
## 集群环境搭建

### 集群规划

这里搭建一个 3 节点的 Spark 集群，其中两台主机上均部署 Worker 服务

<div style="text-align: center;"><img alt='202404081924344' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404081924344.png' width=500px> </div>

### 前置条件

搭建 Spark 集群前，需要保证 JDK 环境、Scala 环境和 Hadoop 集群已经搭建，相关步骤可以参阅:[Hadoop 集群环境搭建](/Hadoop技术栈/Hadoop/Hadoop的简介与安装)

### 安装Spark

* 官方下载地址：[http://spark.apache.org/downloads.html](http://spark.apache.org/downloads.html) ，选择 Spark 版本和对应的 Hadoop 版本后再下载
* 也可以选择从百度网盘进行下载:[Spark环境安装](https://pan.baidu.com/s/1JPyOjpfmWTydlmrNU8hI0Q?pwd=l4sj)

下载好之后解压安装包:
```bash
sudo tar -zxvf spark-3.2.0-bin-hadoop3.2.tgz -C /usr/local
sudo mv spark* spark # 重命名
```

### 配置环境变量

```bash
vim ~/.bashrc
```

添加环境变量:
```bash
export SPARK_HOME=/usr/local/spark
export  PATH=${SPARK_HOME}/bin:$PATH
```
使得配置的环境变量立即生效:
```bash
source ~/.bashrc
```

### 集群配置

进入 `${SPARK_HOME}/conf` 目录，拷贝配置样本进行修改

#### 修改 `spark-env.sh`

```bash
sudo cp spark-env.sh.template spark-env.sh
```

```bash
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_162
export SPARK_WORKER_CORES=8
export SPARK_HOME=/usr/local/spark
export SCALA_HOME=/usr/local/scala
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$SCALA_HOME/bin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$YARN_HOME/etc/hadoop
export SPARK_MASTER_IP=192.168.23.128 # 修改成你自己的 master ip
export SPARK_LOCAL_DIRS=/usr/local/spark
export SPARK_DRIVER_MEMORY=1G
export SPARK_LIBARY_PATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$HADOOP_HOME/lib/native
```
#### slaves

```bash
cp workers.template slaves
```

配置所有 Woker 节点的位置

```bash
Node1
Node2
```

#### 分发节点

将 Spark 的安装包分发到其他服务器，分发后建议在这两台服务器上也配置一下 Spark 的环境变量

```bash
scp -r /usr/local/spark weno@node1:/usr/local
scp -r /usr/local/spark weno@node2:/usr/local
```

### 启动集群

#### 启动Hadoop集群

```bash
# 启动dfs服务
start-dfs.sh
# 启动yarn服务
start-yarn.sh
```

#### 启动Spark集群

进入 Master 的  `${SPARK_HOME}/sbin` 目录下，执行下面命令启动集群。执行命令后，会在 Master 上启动 Maser 服务，会在 slaves 配置文件中配置的所有节点上启动 Worker 服务

```bash
/usr/local/spark/sbin/start-all.sh
```

### 查看服务

查看 Spark 的 Web-UI 页面，端口为 8081。此时可以看到 Master 上的 Master 节点处于 ALIVE 状态，并有 2 个可用的 Worker 节点

<div style="text-align: center;"><img alt='202404082016613' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082016613.png' width=500px> </div>





