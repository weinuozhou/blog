# Linux IP地址与主机名

## IP地址

每一台联网的电脑都会有一个地址， 用于和其他计算机进行通讯

IP地址主要有两个版本，也就是大家熟知的ipv4和ipv6

ipv4地址的地址格式是a.b.c.d, 其中a,b,c,d均表示0-255之间的数字

可以通过`ifconfig`命令来查看本机的ip地址， 如无法使用该命令， 请安装`net-tools`

[ifconfig命令详解](https://wangchujiang.com/linux-command/c/ifconfig.html)

### 特殊的ip地址

除了标准的ip地址外， 还要几个特殊的ip地址需要了解:

* `127.0.0.1`或`localhost`: 这个ip地址代表本机
* `0.0.0.0`: 可以指代本机或者允许任意ip访问

## 主机名

* 每一台计算机除了对外联络地址(ip地址)以外， 还有一个主机名 
* 可以通过`hostname`命令去查看系统的主机名
  * [hostname命令详解](https://wangchujiang.com/linux-command/c/hostname.html)
* 可以通过`hostnamectl`去修改主机名: `hostnamectl set-hostname name`
  * [hostnamectl命令详解](https://wangchujiang.com/linux-command/c/hostnamectl.html)

## 域名解析

ip地址难以记忆， 因此我们都是通过字符化的地址去访问服务器，很少直接指定ip地址， 例如www.google.com我们称之为**域名**

* 首先查看本机的记录(/etc/hosts)
* 再联网去查看 DNS 服务器(114.114.114.114等等)



