# 磁盘管理

日程磁盘管理中，我们最常用的有查看当前磁盘使用情况，查看当前目录所占大小，以及打包压缩与解压缩

## 查看磁盘空间

* 显示磁盘的相关信息
  * [df命令详解](https://wangchujiang.com/linux-command/c/df.html)
* 显示每个文件和目录的磁盘使用空间
  * [du命令详解](https://wangchujiang.com/linux-command/c/du.html)

### 例子

* 查看磁盘空间利用大小
  * `df -h`
* 查看当前目录所占空间大小
  * `du -sh`

##  解压 / 压缩

[tar命令详解](https://wangchujiang.com/linux-command/c/tar.html)

### zip格式

* 压缩: `zip -r [目标文件名].zip [原文件/目录名]`
* 解压: `unzip [原文件名].zip`

### tar.gz格式

* 打包并压缩: `tar -zcvf [目标文件名].tar.gz [原文件名/目录名]`
* 解压并解包: `tar -zxvf [原文件名].tar.gz`

### jar格式

* 压缩: `jar -cvf [目标文件名].jar [原文件名/目录名]`
* 解压: `jar -xvf [原文件名].jar`

### 7z格式

* 压缩: `7z a [目标文件名].7z [原文件名/目录名]`
* 解压: `7z x [原文件名].7z`
  * 这个7z解压命令支持rar格式


