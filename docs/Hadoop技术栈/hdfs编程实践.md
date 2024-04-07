Hadoop的安装与配置可以参考[Hadoop的安装](/Hadoop技术栈/Hadoop的简介与安装)


# 利用Shell命令与HDFS进行交互

1. **hadoop fs**:
   - 这是Hadoop的通用文件系统Shell命令。
   - 可以用于访问不仅仅是HDFS，还包括其他支持Hadoop文件系统API的文件系统，例如本地文件系统、S3等
   - 该命令的语法为：`hadoop fs <args>`，其中 `<args>` 是具体的文件系统命令和参数
2. **hadoop dfs**:
   - 这是Hadoop早期版本（1.x系列）中使用的文件系统Shell命令
   - 主要用于对HDFS进行文件和目录的操作
   - 随着Hadoop的发展，`hadoop dfs` 已经逐渐被 `hdfs dfs` 命令所取代
3. **hdfs dfs**:
   - 这是Hadoop较新版本（2.x系列及之后）中使用的文件系统Shell命令
   - 是用于在HDFS上执行文件和目录操作的推荐命令
   - 语法与 `hadoop fs` 类似，但专注于HDFS

> 在实际使用中，推荐使用 `hdfs dfs` 命令，因为它是当前版本Hadoop中的标准命令，同时支持HDFS以及其他Hadoop支持的文件系统

## 启动`Hadoop`

```shell
cd /usr/local/hadoop
./sbin/start-dfs.sh  # 启动hadoop
```

我们可以在终端输入如下命令，查看hdfs总共支持了哪些命令:
```shell
hdfs dfs
```
<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312154103.png'></center>

在终端输入如下命令，可以查看具体某个命令的作用以及如何使用:

```shell
hdfs dfs -help put
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312157988.png'></center>

## `Hadoop`命令详解

### `appendToFile`

可以使用hdfs dfs -appendToFile命令来将数据追加到文件的末尾。这个命令的一般语法如下:

```shell
hdfs dfs -appendToFile <local-source> <hdfs-destination>
```

- `<local-source>`：本地文件的路径，表示要追加到HDFS文件的数据源
- `<hdfs-destination>`：HDFS文件的路径，表示数据将要追加到的目标文件

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312208228.png'></center>

### `cat`

`hadoop fs -cat`命令用于显示HDFS上文件的内容。这个命令与Unix/Linux中的`cat`命令相似，但它是专门用于Hadoop分布式文件系统（HDFS）的

```shell
hadoop fs -cat [-ignoreCrc] <hdfs-file-path>
```

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312214697.png'></center>

```shell
hdfs dfs -cat hdfs://nn1.example.com/file1
hdfs dfs -cat /user/hadoop/file4
```

### `count`

hadoop fs -count命令用于统计HDFS文件或目录的大小、文件数目以及目录数目。基本的语法如下:

```shell
hadoop fs -count [-q] [-h] <hdfs-path>
```

- `<hdfs-path>` 是要统计的HDFS文件或目录的路径。
- `-q` 选项用于安静模式，只输出统计结果，不显示额外信息。
- `-h` 选项用于以人类可读的格式显示文件大小

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312233494.png'></center>

输出结果解读:
* 目录数量
* 文件数量
* 文件所占的字节大小

### `df`

Hadoop的文件系统是Hadoop分布式文件系统（HDFS），而不是普通的本地文件系统，因此磁盘空间的概念和管理方式也不同

如果你想要查看Hadoop集群中各个节点的磁盘空间使用情况，可以使用`df`命令

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202401312238138.png'></center>

### `ls`

列出与指定文件模式匹配的内容。如果未指定路径，则将列出 /user/\<currentUser> 的内容。对于目录，将返回其直接子目录的列表（除非指定了 -d 选项）

* `-C`: 只展示文件和目录的路径
* `-d`: 目录以纯文件地形式展示
* `-h`: 以人类可读的方式格式化文件大小而不是字节数
* `-R`: 递归列出目录内容
* `-t`: 以最近修改时间降序排序
* `-S`: 以文件大小降序排序

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402011949868.png'></center>

### `mkdir`

在指定位置创建目录

* `-p`: 创建目录时目录存在也不报错

> 值得注意的是, 递归创建不需要指定-p参数也可以

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402011958122.png'></center>

### `get`

将符合文件模式 \<src> 的文件复制到本地, \<src> 将被保留。复制多个文件时, \<src>必须是一个目录

* `-f`: 覆盖已存在的目标文件
* `-p`: 保留访问和修改时间、所有权和模式、修改时间、所有权和模式

<cenetr><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402012003071.png'></center>

### `put`

将本地文件系统的数据加载到`hdfs`中

* `-f`: 覆盖加载，数据存在也不报错
* `-l`: 允许数据节点惰性持久化到磁盘，强制将复制因子设置为1
* `-d`: 跳过临时文件的创建
* `-p`: 保留访问和修改时间、所有权和模式、修改时间、所有权和模式

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402012009821.png'></center>


### `rm`

删除指定路径的文件或者文件夹

* `-f`: 如果文件不存在，则不显示诊断信息或修改退出状态以反映错误
* `-r`: 递归删除目录

其余的shell命令可以查看[hadoop官方文档](https://apache.github.io/hadoop/hadoop-project-dist/hadoop-common/FileSystemShell.html)

## 利用Web界面管理HDFS

HDFS的web访问地址是`https://localhost:9870`

<center><img src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402021004250.png'></center>

点击 `Utilities -> Browse the file system`即可管理HDFS目录及文件

!> 使用hdfs的web界面进行创建目录时发生如下错误:Permission denied: user=dr.who, access=WRITE, inode="/user":weno:supergroup:drwxr-xr-x.如何解决?

其实是这样的，/代表文件的所有者是hdfs, 权限为755, 也就是只有hdfs才能对这个文件进行sudo的操作,可以使用HDFS的命令行接口修改相应目录的权限

```shell
hdfs dfs -chmod 777 /
```

