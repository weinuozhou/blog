## Hadoop简介

* Hadoop是Apache软件基金会旗下的一个开源分布式计算平台，为用户提供了系统底层细节透明的分布式基础架构
* Hadoop是**基于Java语言**开发的，具有很好的跨平台特性，并且可以部署在廉价的计算机集群中
* Hadoop的核心是**分布式文件系统HDFS**和**分布式计算框架MapReduce**
* Hadoop被公认为行业大数据标准开源软件，在分布式环境下提供了海量数据的处理能力
* 几乎所有主流厂商都围绕Hadoop提供开发工具、开源软件、商业化工具和技术服务，如谷歌、雅虎、微软、思科、淘宝等，都支持Hadoop

## Hadoop的特性

Hadoop是一个能够对大量数据进行分布式处理的软件框架，并且是以一种可靠、高效、可伸缩的方式进行处理的，它具有以下几个方面的特性:

* 高可靠性
* 高效性
* 高可扩展性
* 高容错性
* 成本低
* 运行在Linux平台上
* 支持多种编程语言

<center><img src=https://picx.zhimg.com/v2-07d55413850c1404a647a8dd3efae257_720w.jpg?source=d16d100b'></center>


## Hadoop的版本演变

<center><img src='https://pica.zhimg.com/v2-a1023e7a34224bfc7027198dd6475930_720w.jpg?source=d16d100b'></center>

## Hadoop项目结构

<center><img src='https://pic1.zhimg.com/v2-a9b6c7cfa810bcf3a8e7efbd734a3449_720w.jpg?source=d16d100b'></center>

### Hadoop组件说明

<center><img src='https://picx.zhimg.com/v2-58e02fac2887225a1cac39fb04f25d54_720w.jpg?source=d16d100b'></center>

## Hadoop的安装与使用

### Hadoop单机模式

默认情况下，Hadoop被配置成以非分布式模式运行的一个独立Java进程

下面的实例将已解压的 conf 目录拷贝作为输入，查找并显示匹配给定正则表达式的条目,输出写入到指定的output目录

```bash
mkdir input
cp conf/*.xml input
bin/hadoop jar hadoop-*-examples.jar grep input output 'dfs[a-z.]+'
cat output/*
```

### Hadoop伪分布式安装

* Hadoop 可以在单节点上以伪分布式的方式运行，Hadoop 进程以分离的 Java 进程来运行，节点既作为 *NameNode* 也作为 *DataNode*，同时，读取的是 HDFS 中的文件
* Hadoop 的配置文件位于 /usr/local/hadoop/etc/hadoop/ 中，伪分布式需要修改2个配置文件 `core-site.xml` 和 `hdfs-site.xml`
* Hadoop的配置文件是 xml 格式，每个配置以声明 property 的 name 和 value 的方式来实现

#### 安装`java`

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

#### 安装SSH、配置SSH无密码登陆

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

#### 安装 Hadoop

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

### Hadoop集群安装

当Hadoop采用分布式模式部署和运行时，存储采用分布式文件系统HDFS，而且，HDFS的名称节点和数据节点位于不同机器上。这时，数据就可以分布到多个节点上，不同数据节点上的数据计算可以并行执行，这时的MapReduce分布式计算能力才能真正发挥作用

集群模式主要用于生产环境部署，需要多台主机，并且这些主机之间可以相互访问。以三台主机为例，以下是集群规划:

|局域网ip地址|各节点名称|运行角色
|---|---|---|
|192.168.159.136|Master|NameNode、ResourceManager、SecondaryNamenode|
|192.168.159.135|Node1|DataNode 、NodeManager|
|192.168.159.137|Node2|DataNode 、NodeManager|

#### 网络配置

假设集群所用的三个节点（机器）都位于同一个局域网内。如果三个节点使用的是虚拟机安装的Linux系统，那么三者都需要更改网络连接方式为“桥接网卡”模式，才能实现多个节点互连

网络配置完成以后，可以查看一下机器的IP地址，可以使用ifconfig命令查看。本教程在同一个局域网内部的两台机器的IP地址分别是192.168.159.135、192.168.159.136、192.168.159.137

#### 修改主机名

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

#### SSH无密码登录节点

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

#### 配置PATH变量

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

#### 配置集群/分布式环境

在配置集群/分布式模式时，需要修改/usr/local/hadoop/etc/hadoop目录下的配置文件，这里仅设置正常启动所必须的设置项，包括workers 、core-site.xml、hdfs-site.xml、mapred-site.xml、yarn-site.xml共5个文件

1. 修改文件workers

在进行分布式配置时，可以保留localhost，让Master节点同时充当名称节点和数据节点，或者也可以删掉localhost这行，让Master节点仅作为名称节点使用

```bash
cd /usr/local/hadoop/etc/hadoop
sudo vim workers
```

将workers文件中原来的localhost删除，只添加如下内容:

```text
Node1
Node2
```

2. 修改文件core-site.xml

请把core-site.xml文件修改为如下内容:

```xml
<configuration>
        <property>
                <name>fs.defaultFS</name>
                <value>hdfs://Master:9000</value>
        </property>
        <property>
                <name>hadoop.tmp.dir</name>
                <value>file:/usr/local/hadoop/tmp</value>
                <description>Abase for other temporary directories.</description>
        </property>
</configuration>
```

3. 修改文件hdfs-site.xml

对于Hadoop的分布式文件系统HDFS而言，一般都是采用冗余存储，冗余因子通常为3，也就是说，一份数据保存三份副本。但是，本教程只有两个Node节点作为数据节点，即集群中只有2个数据节点，数据只能保存一份，所以 ，dfs.replication的值还是设置为 2

```xml
<configuration>
        <property>
                <name>dfs.namenode.secondary.http-address</name>
                <value>Master:50090</value>
        </property>
        <property>
                <name>dfs.replication</name>
                <value>2</value>
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

4. 修改文件mapred-site.xml

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
                <name>yarn.resourcemanager.hostname</name>
                <value>Master</value>
        </property>
        <property>
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
</configuration>
```

#### 分发节点

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

首次启动Hadoop集群时，需要先在Master节点执行名称节点的格式化（只需要执行这一次，后面再启动Hadoop时，不要再次格式化名称节点）

```bash
hdfs namenode -format
```

现在就可以启动Hadoop了，启动需要在Master节点上进行，执行如下命令:

```bash
start-dfs.sh
start-yarn.sh
mr-jobhistory-daemon.sh start historyserver
```

在Master节点上可以看到NameNode、ResourceManager、SecondrryNameNode和JobHistoryServer进程:

<cenetr><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301842805.png'></center>

在Node节点可以看到DataNode和NodeManager进程

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401301843081.png'></center>