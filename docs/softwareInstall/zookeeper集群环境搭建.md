# `zookeeper` 集群搭建 

## 集群规划

通过 VMware ，我们安装了三台虚拟机，用来搭建 zookeeper 集群，虚拟机网络地址如下

| 主机名   | IP地址      |
|:---:|:---:|
|Master|192.168.23.128|
|Node1|192.168.23.129|
|Node2|192.168.23.130|

?> 在搭建 zookeeper 集群之前，我们首先要明白为什么要选择三台机器搭建，2台不可以吗？4台不可以吗？

zookeeper 集群通常是用来对用户的分布式应用程序提供协调服务的，为了保证数据的一致性，对 zookeeper 集群进行了这样三种角色划分：leader、follower、observer分别对应着总统、议员和观察者

* **总统**（leader）：负责进行投票的发起和决议，更新系统状态
* **议员**（follower）：用于接收客户端请求并向客户端返回结果以及在选举过程中参与投票
* **观察者**（observer）：也可以接收客户端连接，将写请求转发给leader节点，但是不参与投票过程，只同步leader的状态。通常对查询操作做负载

## 前置条件

由于 `zookeeper` 集群的运行需要Java运行环境，所以需要首先安装 JDK

## 下载 zookeeper

* 官网下载地址：http://mirror.bit.edu.cn/apache/zookeeper/
* 也可以通过我的百度网盘进行下载:[zookeeper安装包](https://pan.baidu.com/s/13oShWnxAmbMHdZ9r-kBUwQ?pwd=ar4g)

下载好安装包后解压:
```bash
sudo tar -zvxf apache-zookeeper-3.8.3-bin.tar.gz -C /usr/local
cd /usr/local && sudo mv apache-zookeeper-3.8.3 zookeeper
```

## 修改配置文件

进入 zookeeper 目录，复制样本配置文件 `conf/zoo_sample.cfg`

```bash
cd /usr/local/zookeeper/conf
cp zoo_sample.cfg zoo.cfg
```

然后使用vim对配置文件`zoo.cfg`进行修改:
```bash
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/usr/local/zookeeper/data
clientPort=2181
server.0=192.168.23.128:2888:3888
server.1=192.168.23.129:2888:3888
server.2=192.168.23.130:2888:3888
```

* `tickTime` ：基本事件单元，这个时间是作为Zookeeper服务器之间或客户端与服务器之间维持心跳的时间间隔，每隔tickTime时间就会发送一个心跳；最小 的session过期时间为2倍tickTime
* `dataDir` ：存储内存中数据库快照的位置，除非另有说明，否则指向数据库更新的事务日志。注意：应该谨慎的选择日志存放的位置，使用专用的日志存储设备能够大大提高系统的性能，如果将日志存储在比较繁忙的存储设备上，那么将会很大程度上影像系统性能
* `client` ：监听客户端连接的端口
* `initLimit` ：允许follower连接并同步到Leader的初始化连接时间，以tickTime为单位。当初始化连接时间超过该值，则表示连接失败
* `syncLimit` ：表示Leader与Follower之间发送消息时，请求和应答时间长度。如果follower在设置时间内不能与leader通信，那么此follower将会被丢弃
* `server.A=B:C:D`
    * A：其中 A 是一个数字，表示这个是服务器的编号
    * B：是这个服务器的 ip 地址
    * C：Zookeeper服务器之间的通信端口
    * D：Leader选举的端口

我们需要修改的有两个部分:
* 第一个是 dataDir ,在指定的位置处创建好目录
* 第二个需要新增的是 server.A=B:C:D 配置，其中 A 对应下面我们即将介绍的myid 文件。B是集群的各个IP地址，C:D 是端口配置

## 创建数据目录

创建上一步 dataDir 指定的目录
```bash
cd /usr/local/zookeeper && mkdir data
```

## 分发节点并创建myid文件

首先将zookeeper文件分发到两个Node节点:
```bash
scp -r /usr/local/zookeeper weno@Node1:/usr/local
scp -r /usr/local/zookeeper weno@Node2:/usr/local
```

在 上一步 dataDir 指定的目录下，创建 myid 文件, 然后在该文件添加上一步 server 配置的对应 A 数字

```bash
echo "0" > /usr/local/zookeeper/data/myid # Master节点
echo "1" > /usr/local/zookeeper/data/myid # Node1节点
echo "2" > /usr/local/zookeeper/data/myid # Node2节点
```

## 配置环境变量

为了能够在任意目录启动zookeeper集群，我们需要配置环境变量

!> 你也可以不配，这不是搭建集群的必要操作，只不过如果你不配置环境变量，那么每次启动zookeeper需要到安装文件的 bin 目录下去启动

首先进入到 ~/.bashrc 目录，添加相应的配置信息:
```bash
export ZK_HOME=/usr/local/zookeeper
export PATH=$PATH:$ZK_HOME/bin
```

然后通过如下命令使得环境变量生效
```bash
source ~/.bashrc
```

## 启动zookeeper服务

```bash
zkServer.sh start # 启动
zkServer.sh stop # 停止
zkServer.sh status # 查看集群节点状态
```

我们分别对集群三台机器执行启动命令。执行完毕后，分别查看集群节点状态：

<div style="text-align: center;"><img alt='202404091118670' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404091118670.png' width=500px> </div>
<div style="text-align: center;"><img alt='202404091120463' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404091120463.png' width=500px> </div>
<div style="text-align: center;"><img alt='202404091121260' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404091121260.png' width=500px> </div>

三台机器，Node1 成功的通过了选举称为了leader,而剩下的两台成为了 follower。这时候，如果你将Node1关掉，会发现剩下两台又会有一台变成了 leader节点

当然也可以自己编写脚本来启动集群并查看集群状态, 首先我们新建一个脚本文件为`zk-cluster.sh`

```bash
cd /usr/local/zookeeper/bin
touch zk-cluster.sh
```

然后我们使用vim编辑器写入以下内容:

```bash
#!/bin/bash
case $1 in
"start"){
for i in master node1 node2 # 这里需要修改为自己的主机名
do
echo  -------------------------------- $i zookeeper 启动 ---------------------------
ssh $i "/usr/local/zookeeper/bin/zkServer.sh start"
done
}
;;
"status"){
for i in master node1 node2 # 这里需要修改为自己的主机名
do
     echo -------------------------------- $i zookeeper status ---------------------------
    ssh $i "/usr/local/zookeeper/bin/zkServer.sh status"
done
}
;;
"stop"){
for i in master node1 node2 # 这里需要修改为自己的主机名
do
 echo -------------------------------- $i zookeeper 停止 ---------------------------
ssh $i "/usr/local/zookeeper/bin/zkServer.sh stop"
done
}
;;
esac
```

接着给脚本赋予可执行权限

```bash
chmod a+x zk-cluster.sh
```

最后我们就可以使用以下命令来启动、停止和查看zookeeper的状态

```bash
zk-cluster.sh start # 启动zookeeper集群
zk-cluster.sh status # 查看zookeeper集群状态
zk-cluster.sh stop # 停止zookeeper集群
```

<div style="text-align: center;"><img alt='202405201614786' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202405201614786.png' width=500px> </div>