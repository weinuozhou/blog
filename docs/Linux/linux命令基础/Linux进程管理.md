# 进程管理

使用进程管理工具，我们可以查询程序当前的运行状态，或终止一个进程

## 查询进程

* **ps命令**用于报告当前系统的进程状态。可以搭配kill指令随时中断、删除不必要的程序。ps命令是最基本同时也是非常强大的进程查看命令，使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等，总之大部分信息都是可以通过执行该命令得到的
  * [ps命令详解](https://wangchujiang.com/linux-command/c/ps.html)
* **top命令**可以实时动态地查看系统的整体运行情况，是一个综合了多方信息监测系统性能和运行信息的实用工具。通过top命令所提供的互动式界面，用热键可以管理
    * [top命令详解](https://wangchujiang.com/linux-command/c/top.html)

### 例子

* 查询正在运行的进程信息: `ps -ef`
* 查询归属于用户test的进程: `ps -ef | grep test`
* 查询进程ID（适合只记得部分进程字段）: `pgrep -l 进程名`
* 显示进程信息，并实时更新: `top`

## 终止进程

[kill命令详解](https://wangchujiang.com/linux-command/c/kill.html)

* 杀死指定PID的进程 (PID为Process ID): `kill PID`
* 杀死job工作 (job为job number): `kill %job`

