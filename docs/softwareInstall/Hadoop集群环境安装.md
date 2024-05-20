# Hadoop的安装与使用

## Hadoop单机模式

默认情况下，Hadoop被配置成以非分布式模式运行的一个独立Java进程

下面的实例将已解压的 conf 目录拷贝作为输入，查找并显示匹配给定正则表达式的条目,输出写入到指定的output目录

```bash
mkdir input
cp conf/*.xml input
bin/hadoop jar hadoop-*-examples.jar grep input output 'dfs[a-z.]+'
cat output/*
```

## Hadoop伪分布式安装

* Hadoop 可以在单节点上以伪分布式的方式运行，Hadoop 进程以分离的 Java 进程来运行，节点既作为 *NameNode* 也作为 *DataNode*，同时，读取的是 HDFS 中的文件
* Hadoop 的配置文件位于 /usr/local/hadoop/etc/hadoop/ 中，伪分布式需要修改2个配置文件 `core-site.xml` 和 `hdfs-site.xml`
* Hadoop的配置文件是 xml 格式，每个配置以声明 property 的 name 和 value 的方式来实现

### 安装`java`

我已经把JDK1.8的安装包jdk-8u162-linux-x64.tar.gz放在了百度云盘，可以点击这里到百度云盘下载JDK1.8安装包（提取码：ziyu）。请把压缩格式的文件jdk-8u162-linux-x64.tar.gz下载到本地电脑，假设保存在“~/Downloads/”目录下

在Linux命令行界面中，执行如下Shell命令(注意当前登录的用户名)

```bash
cd /usr/lib
sudo mkdir jvm #创建/usr/lib/jvm目录用来存放JDK文件
cd ~ #进入用户的主目录
cd Downloads  #注意区分大小写字母，刚才已经通过scp把JDK安装包jdk-8u162-linux-x64.tar.gz上传到该目录下
sudo tar -zxvf ./jdk-8u162-linux-x64.tar.gz -C /usr/lib/jvm  #把JDK文件解压到/usr/lib/jvm目录下
```

JDK文件解压缩以后，可以执行如下命令到/usr/lib/jvm目录查看一下,可以看到，在/usr/lib/jvm目录下有个jdk1.8.0_162目录
```bash
cd /usr/lib/jvm
ls -lrh
```
下面继续执行如下命令，设置环境变量

```bash
cd ~
vim ~/.bashrc
```
请在这个文件的开头位置，添加如下几行内容:

```sh
export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_162
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
```

保存.bashrc文件并退出vim编辑器。然后，继续执行如下命令让.bashrc文件的配置立即生效

```bash
source ~/.bashrc
```

这时，可以使用如下命令查看是否安装成功

```bash
java -version
```

### 安装SSH、配置SSH无密码登陆

集群、单节点模式都需要用到 SSH 登陆（类似于远程登陆，你可以登录某台 Linux 主机，并且在上面运行命令），Ubuntu 默认已安装了 SSH client，此外还需要安装 SSH server：

```bash
sudo apt-get install openssh-server
```

安装后，可以使用如下命令登陆本机：

```bash
ssh localhost
```

此时会有提示(SSH首次登陆提示)，输入 yes 。然后按提示输入密码 ，这样就登陆到本机了

但这样登陆是需要每次输入密码的，我们需要配置成SSH无密码登陆比较方便。

首先退出刚才的 ssh，就回到了我们原先的终端窗口，然后利用 ssh-keygen 生成密钥，并将密钥加入到授权中

```bash
exit
cd ~/.ssh
ssh-keygen -t rsa
cat ./id_rsa.pub >> ./authorized_keys
```
此时再用 ssh localhost 命令，无需输入密码就可以直接登陆了

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301745593.png'></center>

### 安装 Hadoop

我们选择将 Hadoop 安装至 /usr/local/ 中

```bash
sudo tar -zxf ~/Downloads/hadoop-3.1.3.tar.gz -C /usr/local    # 解压到/usr/local中
cd /usr/local/
sudo mv ./hadoop-3.1.3/ ./hadoop            # 将文件夹名改为hadoop
sudo chown -R hadoop ./hadoop       # 修改文件权限(注意用户名为hadoop)
```

Hadoop 解压后即可使用。输入如下命令来检查 Hadoop 是否可用，成功则会显示 Hadoop 版本信息

```bash
cd /usr/local/hadoop
./bin/hadoop version
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301749407.png'></center>


修改配置文件 `core-site.xml`

```bash
cd /usr/local/hadoop/etc/hadoop
sudo vim core-site.xml
```

修改为以下内容:
```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

* hadoop.tmp.dir表示存放临时数据的目录，即包括NameNode的数据，也包括DataNode的数据。该路径任意指定，只要实际存在该文件夹即可
* name为fs.defaultFS的值，表示hdfs路径的逻辑名称

同样的，修改配置文件 hdfs-site.xml
```bash
sudo vim hdfs-site.xml
```

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
       <value>file:/usr/local/hadoop/tmp/dfs/data</value>
    </property>
</configuration>
```

* dfs.replication表示副本的数量，伪分布式要设置为1
* dfs.namenode.name.dir表示本地磁盘目录，是存储fsimage文件的地方
* dfs.datanode.data.dir表示本地磁盘目录，HDFS数据存放block的地方

配置完成后，执行 NameNode 的格式化:
```bash
cd /usr/local/hadoop
./bin/hdfs namenode -format
```

## 基于zookeeper实现Hadoop集群安装

当Hadoop采用分布式模式部署和运行时，存储采用分布式文件系统HDFS，而且，HDFS的名称节点和数据节点位于不同机器上。这时，数据就可以分布到多个节点上，不同数据节点上的数据计算可以并行执行，这时的MapReduce分布式计算能力才能真正发挥作用

集群模式主要用于生产环境部署，需要多台主机，并且这些主机之间可以相互访问。以三台主机为例，以下是集群规划:

|局域网ip地址|各节点名称|运行角色
|---|---|---|
|192.168.159.136|Master|NameNode、NodeManager、DataNode|
|192.168.159.135|Node1|NameNode、DataNode 、NodeManager、ResourceManager|
|192.168.159.137|Node2|DataNode 、NodeManager、ResourceManager|

### 网络配置

假设集群所用的三个节点（机器）都位于同一个局域网内。如果三个节点使用的是虚拟机安装的Linux系统，那么三者都需要更改网络连接方式为“桥接网卡”模式，才能实现多个节点互连

网络配置完成以后，可以查看一下机器的IP地址，可以使用ifconfig命令查看。本教程在同一个局域网内部的两台机器的IP地址分别是192.168.159.135、192.168.159.136、192.168.159.137

### 修改主机名

在Linux系统中打开一个终端以后，在终端窗口的标题和命令行中都可以看到主机名，就比较容易区分当前是对哪台机器进行操作

```bash
sudo vim /etc/hostname
```

修改为master(注意是区分大小写的)，然后，保存退出vim编辑器，这样就完成了主机名的修改，需要重启Linux系统才能看到主机名的变化。

然后，在Master节点中执行如下命令打开并修改master节点中的/etc/hosts文件

```bash
sudo vim /etc/hosts
```

可以在hosts文件中增加如下两条IP和主机名映射关系:

```text
192.168.159.135 Node1
192.168.159.136 Master
192.168.159.137 Node2
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301813862.png'></center>

这样就完成了master节点和Node节点的配置，然后，需要在各个节点上都执行如下命令，测试是否相互ping得通，如果ping不通，后面就无法顺利配置成功

```bash
ping Node1 -c 3
ping Node2 -c 3     
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301815327.png'></center>

### SSH无密码登录节点

必须要让master节点可以SSH无密码登录到各个node节点上。首先，生成master节点的公匙

```bash
cd ~/.ssh              # 如果没有该目录，先执行一次ssh localhost
rm ./id_rsa*           # 删除之前生成的公匙（如果已经存在）
ssh-keygen -t rsa       # 执行该命令后，遇到提示信息，一直按回车就可以
cat ./id_rsa.pub >> ./authorized_keys
```

接下来，在Master节点将上公匙传输到Node1节点：

```bash
scp ~/.ssh/id_rsa.pub weno@Node1:~/ # 注意用户名是weno
```

上面的命令中，scp是secure copy的简写，用于在 Linux下进行远程拷贝文件，类似于cp命令，不过，cp只能在本机中拷贝。执行scp时会要求输入Slave1上hadoop用户的密码，输入完成后会提示传输完毕，如下图所示:

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301819964.png'></center>

接着在Node1节点上，将SSH公匙加入授权:

```bash
mkdir ~/.ssh       # 如果不存在该文件夹需先创建，若已存在，则忽略本命令
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
rm ~/id_rsa.pub    # 用完以后就可以删掉
```

**Node2**节点重复上述过程， 这样，在Master节点上就可以无密码SSH登录到各个Node节点了，可在Master节点上执行如下命令进行检验

```bash
ssh Node1
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301821291.png'></center>

### 配置PATH变量

如果还没有配置PATH变量，那么需要在Master节点上进行配置

```bash
sudo vim ~/.bashrc
```

在该文件最上面的位置加入下面内容:
```sh
export HADOOP_HOME=/usr/local/hadoop
export PATH=${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin
```

保存后执行命令`source ~/.bashrc`，使配置生效

### 配置集群/分布式环境

在配置集群/分布式模式时，需要修改/usr/local/hadoop/etc/hadoop目录下的配置文件，这里仅设置正常启动所必须的设置项，包括workers 、core-site.xml、hdfs-site.xml、mapred-site.xml、yarn-site.xml共5个文件

1. 修改文件workers

在进行分布式配置时，可以保留localhost，让Master节点同时充当名称节点和数据节点，或者也可以删掉localhost这行，让Master节点仅作为名称节点使用

```bash
cd /usr/local/hadoop/etc/hadoop
sudo vim workers
```

将workers文件中原来的localhost删除，只添加如下内容:

```text
Master
Node1
Node2
```

2. 修改文件core-site.xml

请把core-site.xml文件修改为如下内容:

```xml
<configuration>
    <property>
        <!-- 指定 namenode 的 hdfs 协议文件系统的通信地址 -->
        <name>fs.defaultFS</name>
        <value>hdfs://master:9000</value>
    </property>
    <property>
        <!-- 指定 hadoop 集群存储临时文件的目录 -->
        <name>hadoop.tmp.dir</name>
        <value>/usr/local/hadoop/tmp</value>
    </property>
    <property>
        <!-- ZooKeeper 集群的地址 -->
        <name>ha.zookeeper.quorum</name>
        <value>master:2181,node1:2181,node2:2181</value>
    </property>
    <property>
        <!-- ZKFC 连接到 ZooKeeper 超时时长 -->
        <name>ha.zookeeper.session-timeout.ms</name>
        <value>10000</value>
    </property>
</configuration>
```

3. 修改文件hdfs-site.xml

对于Hadoop的分布式文件系统HDFS而言，一般都是采用冗余存储，冗余因子通常为3，也就是说，一份数据保存三份副本。但是，本教程只有三个Node节点作为数据节点，即集群中只有3个数据节点，所以 ，dfs.replication的值还是设置为 3

```xml
<configuration>
    <property>
        <!-- 指定 HDFS 副本的数量 -->
        <name>dfs.replication</name>
        <value>3</value>
    </property>
    <property>
        <!-- namenode 节点数据（即元数据）的存放位置，可以指定多个目录实现容错，多个目录用逗号分隔 -->
        <name>dfs.namenode.name.dir</name>
        <value>/usr/local/hadoop/namenode/data</value>
    </property>
    <property>
        <!-- datanode 节点数据（即数据块）的存放位置 -->
        <name>dfs.datanode.data.dir</name>
        <value>/usr/local/hadoop/datanode/data</value>
    </property>
    <property>
        <!-- 集群服务的逻辑名称 -->
        <name>dfs.nameservices</name>
        <value>mycluster</value>
    </property>
    <property>
        <!-- NameNode ID 列表-->
        <name>dfs.ha.namenodes.mycluster</name>
        <value>nn1,nn2</value>
    </property>
    <property>
        <!-- nn1 的 RPC 通信地址 -->
        <name>dfs.namenode.rpc-address.mycluster.nn1</name>
        <value>master:9000</value>
    </property>
    <property>
        <!-- nn2 的 RPC 通信地址 -->
        <name>dfs.namenode.rpc-address.mycluster.nn2</name>
        <value>node1:9000</value>
    </property>
    <property>
        <!-- nn1 的 http 通信地址 -->
        <name>dfs.namenode.http-address.mycluster.nn1</name>
        <value>master:9870</value>
    </property>
    <property>
        <!-- nn2 的 http 通信地址 -->
        <name>dfs.namenode.http-address.mycluster.nn2</name>
        <value>node1:9870</value>
    </property>
    <property>
        <!-- NameNode 元数据在 JournalNode 上的共享存储目录 -->
        <name>dfs.namenode.shared.edits.dir</name>
        <value>qjournal://master:8485;node1:8485;node2:8485/mycluster</value>
    </property>
    <property>
        <!-- Journal Edit Files 的存储目录 -->
        <name>dfs.journalnode.edits.dir</name>
        <value>/usr/local/hadoop/journalnode/data</value>
    </property>
    <property>
        <!-- 配置隔离机制，确保在任何给定时间只有一个 NameNode 处于活动状态 -->
        <name>dfs.ha.fencing.methods</name>
        <value>sshfence</value>
    </property>
    <property>
        <!-- 使用 sshfence 机制时需要 ssh 免密登录 -->
        <name>dfs.ha.fencing.ssh.private-key-files</name>
        <value>/home/weno/.ssh/id_rsa</value>
    </property>
    <property>
        <!-- SSH 超时时间 -->
        <name>dfs.ha.fencing.ssh.connect-timeout</name>
        <value>30000</value>
    </property>
    <property>
        <!-- 访问代理类，用于确定当前处于 Active 状态的 NameNode -->
        <name>dfs.client.failover.proxy.provider.mycluster</name>
        <value>org.apache.hadoop.hdfs.server.namenode.ha.ConfiguredFailoverProxyProvider</value>
    </property>
    <property>
        <!-- 开启故障自动转移,无法手动切换namenode -->
        <name>dfs.ha.automatic-failover.enabled</name>
        <value>true</value>
    </property>
</configuration>
```

1. 修改文件mapred-site.xml

/usr/local/hadoop/etc/hadoop目录下有一个mapred-site.xml.template，需要修改文件名称，把它重命名为mapred-site.xml

```bash
cd /usr/local/hadoop/etc/hadoop
sudo cp mapred-site.xml.template mapred-site.xml
```

然后，把mapred-site.xml文件配置成如下内容:

```xml
<configuration>
        <property>
                <name>mapreduce.framework.name</name>
                <value>yarn</value>
        </property>
        <property>
                <name>mapreduce.jobhistory.address</name>
                <value>Master:10020</value>
        </property>
        <property>
                <name>mapreduce.jobhistory.webapp.address</name>
                <value>Master:19888</value>
        </property>
        <property>
                <name>yarn.app.mapreduce.am.env</name>
                <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        </property>
        <property>
                <name>mapreduce.map.env</name>
                <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        </property>
        <property>
                <name>mapreduce.reduce.env</name>
                <value>HADOOP_MAPRED_HOME=/usr/local/hadoop</value>
        </property> 
</configuration>
```

5. 修改文件 yarn-site.xml

把yarn-site.xml文件配置成如下内容:

```xml
<configuration>
    <property>
        <!--配置 NodeManager 上运行的附属服务。需要配置成 mapreduce_shuffle 后才可以在 Yarn 上运行 MapReduce 程序。-->
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.pmem-check-enabled</name>
        <value>false</value>
    </property>
    <property>
         <name>yarn.nodemanager.vmem-check-enabled</name>
         <value>false</value>
    </property>
    <property>
        <!-- 是否启用日志聚合 (可选) -->
        <name>yarn.log-aggregation-enable</name>
        <value>true</value>
    </property>
    <property>
        <!-- 聚合日志的保存时间 (可选) -->
        <name>yarn.log-aggregation.retain-seconds</name>
        <value>86400</value>
    </property>
    <property>
        <!-- 启用 RM HA -->
        <name>yarn.resourcemanager.ha.enabled</name>
        <value>true</value>
    </property>
    <property>
        <!-- RM 集群标识 -->
        <name>yarn.resourcemanager.cluster-id</name>
        <value>my-yarn-cluster</value>
    </property>
    <property>
        <!-- RM 的逻辑 ID 列表 -->
        <name>yarn.resourcemanager.ha.rm-ids</name>
        <value>rm1,rm2</value>
    </property>
    <property>
        <!-- RM1 的服务地址 -->
        <name>yarn.resourcemanager.hostname.rm1</name>
        <value>node1</value>
    </property>
    <property>
        <!-- RM2 的服务地址 -->
        <name>yarn.resourcemanager.hostname.rm2</name>
        <value>node2</value>
    </property>
    <property>
        <!-- RM1 Web 应用程序的地址 -->
        <name>yarn.resourcemanager.webapp.address.rm1</name>
        <value>node1:8088</value>
    </property>
    <property>
        <!-- RM2 Web 应用程序的地址 -->
        <name>yarn.resourcemanager.webapp.address.rm2</name>
        <value>node2:8088</value>
    </property>
    <property>
        <!-- ZooKeeper 集群的地址 -->
        <name>yarn.resourcemanager.zk-address</name>
        <value>master:2181,node1:2181,node2:2181</value>
    </property>
    <property>
        <!-- 启用自动恢复 -->
        <name>yarn.resourcemanager.recovery.enabled</name>
        <value>true</value>
    </property>
    <property>
        <!-- 用于进行持久化存储的类 -->
        <name>yarn.resourcemanager.store.class</name>
        <value>org.apache.hadoop.yarn.server.resourcemanager.recovery.ZKRMStateStore</value>
    </property>
</configuration>
```

### 分发节点

上述5个文件全部配置完成以后，需要把Master节点上的/usr/local/hadoop文件夹复制到各个节点上

```bash
cd /usr/local
sudo rm -r ./hadoop/tmp     # 删除 Hadoop 临时文件
sudo rm -r ./hadoop/logs/*   # 删除日志文件
tar -zcf ~/hadoop.master.tar.gz ./hadoop   # 先压缩再复制
cd ~
scp ./hadoop.master.tar.gz weno@Node1:~/
scp ./hadoop.master.tar.gz weno@Node2:~/
```

然后在Node1节点上执行如下命令:

```bash
sudo rm -r /usr/local/hadoop    # 删掉旧的（如果存在）
sudo tar -zxf ~/hadoop.master.tar.gz -C /usr/local
sudo chown -R weno /usr/local/hadoop # 注意用户名是weno
```

然后在Node2节点上执行如下命令:

```bash
sudo rm -r /usr/local/hadoop    # 删掉旧的（如果存在）
sudo tar -zxf ~/hadoop.master.tar.gz -C /usr/local
sudo chown -R weno /usr/local/hadoop # 注意用户名是weno
```

### 启动集群

#### 启动ZooKeeper

分别到三台服务器上启动 ZooKeeper 服务：

```bash
zkServer.sh start
```

#### 初始化NameNode

首次启动Hadoop集群时，需要先在Master节点执行名称节点的格式化（只需要执行这一次，后面再启动Hadoop时，不要再次格式化名称节点）

```bash
hdfs namenode -format
```

执行初始化命令后，需要将 NameNode 元数据目录的内容，复制到其他未格式化的 NameNode 上。元数据存储目录就是我们在 hdfs-site.xml 中使用 dfs.namenode.name.dir 属性指定的目录。这里我们需要将其复制到 node1 上

```bash
scp -r /usr/local/hadoop/namenode/data node1:/usr/local/namenode/
```

#### 初始化HA状态

在任意一台 NameNode 上使用以下命令来初始化 ZooKeeper 中的 HA 状态

```bash
hdfs zkfc -formatZK
```

#### 启动Hadoop

现在就可以启动Hadoop了，启动需要在Master节点上进行，执行如下命令:

```bash
start-dfs.sh
start-yarn.sh
```

#### 查看集群

<div style="text-align: center;"><img alt='202405201626987' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202405201626987.png' width=500px> </div>

还可以编写脚本查看当前哪个namenode1处于active状态

```bash
#!/bin/bash
host=(master node1)
cluster=(nn1 nn2)

case $1 in
"status"){
for ((i=0;i<2;i++))
do
echo  -------------------------------- 检测 ${host[i]} 的namenode的状态 ---------------------------
ssh ${host[i]} "hdfs haadmin -getServiceState ${cluster[i]}"
done
}
;;
esac
```

<div style="text-align: center;"><img alt='202405201627740' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202405201627740.png' width=500px> </div>