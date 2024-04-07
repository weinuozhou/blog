# Linux 文件基本属性

Linux 系统是一种典型的多用户系统，不同的用户处于不同的地位，拥有不同的权限。

为了保护系统的安全性，Linux 系统对不同的用户访问同一文件（包括目录文件）的权限做了不同的规定。

在Linux中我们可以使用`ll`命令来显示一个文件的属性以及文件所属的用户和组

<div style="text-align: center;">
    <img alt="" src="https://cdn.jsdelivr.net/gh/weno861/image/202402261628927.png" width=80%>
</div>

<div style="text-align: center;">
    <img alt="" src="https://cdn.jsdelivr.net/gh/weno861/image/202402261646469.png" width=80%>
</div>

* 第 0 位确定文件类型
* 第 1-3 位确定属主（该文件的所有者）拥有该文件的权限
* 第 4-6 位确定属组（所有者的同组用户）拥有该文件的权限
* 第 7-9 位确定其他用户拥有该文件的权限

## Linux文件类型

在Linux中第一位属性用来确定文件类型。在上图中，我们看到第一个属性用`d`表示, 在Linux中代表该文件是一个*目录文件*

* `-`：**普通文件**，包括文本文件、二进制可执行文件、图像文件等。这种类型的文件包含数据，可以由用户或程序创建和编辑
* `d`: **目录文件**,用于组织和存储其他文件和目录的特殊文件。目录文件中包含了其他文件和子目录的列表
* `l`: **符号链接文件**,也称为软链接（soft link）或符号连接，它包含指向另一个文件或目录的路径
* `b`: **块设备文件**,用于随机访问的设备，例如硬盘驱动器。
* `c`: **字符设备文件**,用于按顺序访问的设备，例如键盘、鼠标
* `p`: **管道文件**,也称为FIFO（First In, First Out），用于进程间通信
* `s`: **套接字文件**,用于进程间的网络通信，例如TCP/IP套接字和Unix域套接字

## Linux文件属性

对于Linux系统的文件来说，其基本的属性有三种：**读**、**写**、**执行**。不同的用户对于文件也拥有不同的读、写和执行权限

<dl>
    <dt>读权限</dt>
    <dd>表示具有读取目录结构的权限，可以查看和阅读文件</dd>
</dl>

<dl>
    <dt>写权限</dt>
    <dd>可以新建、删除、重命名、移动目录或文件（不过写权限受父目录权限控制）</dd>
</dl>

<dl>
    <dt>执行权限</dt>
    <dd>文件拥有执行权限，才可以运行。比如二进制文件和脚本文件。目录文件要有执行权限才可以进入</dd>
</dl>

## Linux文件属主和属组

在Linux系统中，每个文件和目录都有一个属主（owner）和一个属组（group）

<dl style="background-color: #FFCDD2">
    <dt style="font-style: normal">属主</dt>
    <dd>属主是文件或目录的创建者或拥有者,属主对于该文件或目录有特殊的权限，可以控制对其进行的操作，例如读取、写入、执行等</dd>
</dl>

<dl style="background-color: #B2EBF2">
    <dt style="font-style: normal">属组</dt>
    <dd>在Linux系统中，一个用户可以同时属于多个用户组，而一个文件或目录只能属于一个属组。属组权限是指除了属主外，其他属于同一用户组的用户对文件或目录的权限>属组是文件或目录所属的用户组在Linux系统中，一个用户可以同时属于多个用户组，而一个文件或目录只能属于一个属组。属组权限是指除了属主外，其他属于同一用户组的用户对文件或目录的权限</dd>
</dl>

## 更改文件属性

### chgrp：更改文件属组

```shell
chgrp [-R] 属组名 文件名
```

`-R`：递归更改文件属组，就是在更改某个目录文件的属组时，如果加上 -R 的参数，那么该目录下的所有文件的属组都会更改

### chown：更改文件所有者

```shell
chown [–R] 所有者 文件名
chown [-R] 所有者:属组名 文件名
```

### chmod：更改文件9个属性

Linux文件属性有两种设置方法，一种是数字，一种是符号

Linux 文件的基本权限就有九个，分别是 **owner/group/others**三种身份各有自己的 **read/write/execute** 权限

各权限的分数对照表如下:

* r:4
* w:2
* x:1

每种身份(owner/group/others)各自的三个权限(r/w/x)分数是需要累加的，例如当权限为：`-rwxrwx---` 分数则是

* $\text{owner} = \text{rwx} = 4+2+1 = 7$
* $\text{group} = \text{rwx} = 4+2+1 = 7$
* $\text{others} = --- = 0+0+0 = 0$

```shell
chmod [-R] xyz 文件或目录
```

* `xyz` : rwx 属性数值的相加
* `-R` : 进行递归(recursive)的持续变更，以及连同次目录下的所有文件都会变更

#### 符号类型改变文件权限

我们就可以使用 u, g, o 来代表三种身份(user、group、others)的权限

此外， a 则代表 all，即全部的身份。读写的权限可以写成 r, w, x，也就是可以使用下表的方式来看

<table style="text-align: center">
    <tbody>
        <tr style="text-align: center">
        <td>chmod</td>
        <td>u<br>g<br>o<br>a</td>
        <td>+(加入)<br>-(除去)<br>=(设定)</td>
        <td>r<br>w<br>x</td><td>文件或目录</td></tr>
    </tbody>
</table>

如果我们需要将文件权限设置为 -rwxr-xr-- ，可以使用`chmod u=rwx,g=rx,o=r 文件名`来设定



