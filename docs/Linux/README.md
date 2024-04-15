# linux简介

## linux概述

Linux是一个开源的操作系统(OS)。它由 Linus Torvalds 于 1991 年构思设计而成，最初这只是他的一项兴趣爱好。当时还在读大学的 Linus 想要基于 Unix 的原则和设计来创建一个免费的开源系统，从而代替 MINIX 操作系统。自此，这项兴趣爱好便逐步演变成了拥有最大用户群的操作系统。如今，它不仅是公共互联网服务器上最常用的操作系统，还是速度排名前 500 的超级电脑上使用的唯一一款操作系统

<div style="text-align: center;">
    <img alt="intro" src='https://cdn.jsdelivr.net/gh/weno861/image/img/202402202208438.png' width=40%>
</div>

## Linux 操作系统中的抽象级别和层次

Linux操作系统主要分为三层

* 最底层是**硬件系统**，包括内存和中央处理器（用于计算和从内存中读写数据），硬盘和网络接口也是硬件系统的一部分
* 硬件系统之上是**内核**，它是操作系统的核心。内核是运行在内存中的软件，它向中央处理器发送指令。内核管理硬件系统，是硬件系统和应用程序之间进行通信的接口
* 进程是指计算机中运行的所有程序，由内核统一管理，它们组成了最顶层，称为**用户空间**（user space）。（另一个更确切的术语是用户进程，无论它们是否直接和用户交互。例如，所有的Web服务器都是以用户进程的形式运行的。）

<div style="text-align: center;">
    <img alt="" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402202218404.png" width=60%>
</div>

## Linux 内核

内核负责管理以下四个方面：

* 进程：内核决定哪个进程可以使用CPU
* 内存：内核管理所有的内存，为进程分配内存，管理进程间的共享内存以及空闲内存
* 设备驱动程序：作为硬件系统（如磁盘）和进程之间的接口，内核负责操控硬件设备
* 系统调用和支持：进程通常使用系统调用和内核进行通信

## Linux 的发行版

Linux 的发行版说简单点就是将 Linux 内核与应用软件做一个打包

<div style="text-align: center;">
    <img alt="" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402220933850.png" width=80%>
</div>

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等

## Linux 系统目录结构

<div style="text-align: center;">
    <img alt="" src="https://cdn.jsdelivr.net/gh/weno861/image/img/202402261601657.png" width=60%>
</div>

* `/var`：存放经常变化的文件，例如日志文件、缓存文件等
* `/bin`：存放系统基本命令（binary）的目录，例如ls、cp等
* `/boot`：存放启动Linux时所需的核心文件，包括引导加载程序和内核映像等。
* `/dev`：存放设备文件，Linux将所有设备都视为文件，这些设备文件包括硬盘、键盘、鼠标等。
* `/etc`：存放系统的配置文件，包括网络配置、用户配置等。
* `/home`：普通用户的目录，每个用户都有一个独立的子目录存放个人文件。
* `/lib`：系统库文件存放目录，包含了程序运行所需的共享库文件
* `/mnt`：系统管理员安装临时文件系统的挂载点，通常用于挂载CD-ROM、USB等设备
* `/opt`：用于存放可选的应用程序软件包的目录，一般是第三方软件
* `/proc`：虚拟文件系统，提供关于系统内核运行时的信息，包括当前运行的进程信息等
* `/root`：超级用户（root）的 home 目录
* `/sbin`：存放系统管理命令（superuser binary），只有root用户才能执行
* `/tmp`：临时目录，任何人都可以在这里创建、读取和修改文件，但不会持久保存
* `/usr`：存放用户相关程序和文件的目录，包括用户的应用程序和文件、库文件、帮助文档等
* `/media`：linux 系统会自动识别一些设备，例如U盘、光驱等等，当识别后，Linux 会把识别的设备挂载到这个目录下


