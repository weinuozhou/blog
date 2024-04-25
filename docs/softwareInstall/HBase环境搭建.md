# HBase 环境搭建

## 安装前置条件说明

* HBase 需要依赖 JDK 环境，同时 HBase 2.0+ 以上版本不再支持 JDK 1.7 ，需要安装 JDK 1.8+ 

## Standalone 模式

1. 从[百度网盘](https://pan.baidu.com/s/1sUkgmwlRuLGLmyo1mTrpqg?pwd=d5bp)下载所需要版本的二进制安装包，并进行解压：

```bash
sudo tar -zvxf hbase-2.2.2-bin.tar.gz -C /usr/local
```

将解压的文件名hbase-2.2.2改为hbase

```bash
cd /usr/local
sudo mv hbase-2.2.2/ hbase/
```

2. 配置环境变量

```bash
sudo vim /etc/profile
```

添加如下内容

```bash
export HBASE_HOME=/usr/local/hbase
export PATH=$PATH:$HBASE_HOME/bin
```

生效环境变量

```bash
source /etc/profile
```

### 进行HBase相关配置

修改安装目录下的 `conf/hbase-env.sh`,指定 JDK 的安装路径:

```bash
# The java implementation to use.  Java 1.8+ required.
export JAVA_HOME=/usr/jdk/jvm
```

修改安装目录下的 `conf/hbase-site.xml`，增加如下配置:

```xml
<configuration>
 <property>
    <name>hbase.rootdir</name>
    <value>file:///usr/local/hbase/rootdir</value>
  </property>
  <property>
    <name>hbase.master.info.port</name>
    <value>60010</value>
  </property>
</configuration>
```

### 启动HBase

由于已经将 HBase 的 bin 目录配置到环境变量，直接使用以下命令启动:

```bash
start-hbase.sh
```


