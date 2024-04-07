# Linux 文件与目录管理

我们知道 Linux 的目录结构为树状结构，最顶级的目录为根目录 /

<dl style="background-color: aqua">
    <dt style="font-style: normal">绝对路径</dt>
    <dd>由根目录 / 写起，例如： /usr/share/doc 这个目录</dd>
</dl>

<dl style="background-color: #FFCDD2">
    <dt style="font-style: normal">相对路径</dt>
    <dd>例如由 /usr/share/doc 要到 /usr/share/man 底下时，可以写成： cd ../man 这就是相对路径的写法</dd>
</dl>

## 目录切换

[cd命令详解](https://wangchujiang.com/linux-command/c/cd.html)

### 主要用途

* 切换工作目录至`dir`。其中`dir`的表示法可以是*绝对路径*或*相对路径*
* 若参数`dir`省略，则默认为使用者的shell变量`HOME`
* 如果`dir`指定为`~`时表示为使用者的shell变量`HOME`，`.`表示当前目录，`..`表示当前目录的上一级目录
* 环境变量`CDPATH`是由冒号分割的一到多个目录，你可以将常去的目录的上一级加入到`CDPATH`以便方便访问它们；如果`dir`以`/`
  开头那么`CDPATH`不会被使用

## 文件及目录管理

文件管理不外乎文件或目录的*创建*、*删除*、*查询*、*移动*

**文件查询**是重点，用`find`来进行查询

### 创建和删除

#### 创建文件及目录

[mkdir命令详解](https://wangchujiang.com/linux-command/c/mkdir.html)

**mkdir命令**
用来创建目录。该命令创建由dirname命名的目录。如果在目录名的前面没有加任何路径名，则在当前目录下创建由dirname指定的目录；如果给出了一个已经存在的路径，将会在该目录下创建一个指定的目录。在创建目录时，应保证新建的目录与它所在目录下的文件没有重名。

* `-Z`：设置安全上下文，当使用SELinux时有效
* `-m`<目标属性>或--mode<目标属性>: 建立目录的同时设置目录的权限
* `-p`或`--parents`: 建立多级目录
* `--version`: 显示版本信息

##### 例子

* 建立多级目录/user/test，并且只有文件主有读、写和执行权限，其他人无权访问:
    * `mkdir -p -m 700 ./user/test`

#### 删除文件及目录

* 删除目录: `rmdir`
    * [rmdir命令详解](https://wangchujiang.com/linux-command/c/rmdir.html)
* 删除文件及目录: `rm`
    * [rm命令详解](https://wangchujiang.com/linux-command/c/rm.html)

##### 例子

* 删除日志
    * `rm *log` 或 `find ./ -name "*log" -exec rm {} \;`
* 查找 .html 结尾的文件并删除:
    * `find ./docs -name "*.html" -exec rm -rf {} \;`
* 删除非空目录
    * `rm -rf dir`(**使用时要非常注意目录是否正确**)

### 文件的查询与检索

* [find命令详解](https://wangchujiang.com/linux-command/c/find.html)
* [locate命令详解](https://wangchujiang.com/linux-command/c/find.html)

#### 例子

* 当前目录搜索所有文件，文件内容 包含 “140.206.111.111” 的内容
    * `find . -type f -name "*" | xargs grep "140.206.111.111"`
* 查找目标文件夹中是否有obj文件
    * `find ./ -name '*.o'`
* 在/home目录下查找以.txt结尾的文件名, 忽略大小写
    * `find /home -iname "*.txt"`
* 基于正则表达式匹配文件路径
    * `find . -regex ".*\(\.txt\|\.pdf\)$"`
* 根据文件类型进行搜索
    * `find . -type 类型参数`
        * f 普通文件
        * l 符号连接
        * d 目录
        * c 字符设备
        * b 块设备
        * s 套接字
        * p Fifo
* 根据文件时间戳进行搜索
    * `find . -type f 时间戳`
        * 访问时间 （-atime/天，-amin/分钟）：用户最近一次访问时间
        * 修改时间 （-mtime/天，-mmin/分钟）：文件最后一次修改时间
        * 变化时间 （-ctime/天，-cmin/分钟）：文件数据元（例如权限等）最后一次修改时间
* 根据文件大小进行匹配
    * `find . -type f -size 文件大小单元`
        * b —— 块（512字节）
        * c —— 字节
        * w —— 字（2字节）
        * k —— 千字节
        * M —— 兆字节
        * G —— 吉字节

### 查看文件内容

查看文件: `cat`、`head`、`tail`和`more`

* [cat命令详解](https://wangchujiang.com/linux-command/c/cat.html)
* [head命令详解](https://wangchujiang.com/linux-command/c/head.html)
* [tail命令详解](https://wangchujiang.com/linux-command/c/tail.html)
* [more命令详解](https://wangchujiang.com/linux-command/c/more.html)

#### 例子

* 显示文件内容时同时显示行号
    * `cat -n file`
* 按页显示列表内容
    * `ls -al | more`
* 查看两个文件间的差别
    * `diff file1 file2`

### 文件及目录权限修改

* 改变文件或目录的拥有者或所属群组: [chown命令详解](https://wangchujiang.com/linux-command/c/chown.html)
* 变更文件或目录的权限(rwx): [chmod命令详解](https://wangchujiang.com/linux-command/c/chmod.html)

#### 例子

* 递归子目录修改
    * `chown -R root:root /usr/source`
* 增加脚本可执行权限
    * `chmod a+x script`

### 创建链接

为文件创建链接: [ln命令详解](https://wangchujiang.com/linux-command/c/ln.html)

<dl style="background-color: aqua">
    <dt style="font-style: normal">软连接</dt>
    <dd>删除源，另一个无法使用</dd>
</dl>

<dl style="background-color: blue">
    <dt style="font-style: normal">硬链接</dt>
    <dd>删除一个，将仍能找到</dd>
</dl>

* 创建软链接(在目录/usr/liu下建立一个符号链接文件abc，使它指向目录/usr/mengqc/mub1)
    * `ln -s /usr/mengqc/mub1 /usr/liu/abc`
* 给文件创建硬链接，为 log2022.log 创建硬链接 ln2022，log2022.log 与 ln2022 的各项属性相同
    * `ln log2022.log ln2022`

### 文本搜索

[grep命令详解](https://wangchujiang.com/linux-command/c/grep.html)

#### 例子

* 多级目录中对文本递归搜索
    * `grep "class" . -R -n`
* 搜索命令行历史记录中 输入过 git 命令的记录
    * `history | grep git`
* 匹配多个模式
    * `grep -e "class" -e "vitural" file`

## 管道与重定向

* 重定向操作符 > 和 >> 可以把 stdout 从 terminal window 重定向到文件中
    * `>` : 重定向 stdout 到文件，会覆盖已有文件的内容
    * `>>` : 重定向 stdout 到文件，追加到已有文件内容上
* 管道 | 可以把前一个命令的标准输出(stdout)作为后一个命令的标准输入(stdin)





