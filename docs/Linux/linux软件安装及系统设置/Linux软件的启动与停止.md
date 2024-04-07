# 软件的启动与停止

Linux 系统很多软件均支持使用`systemctl`命令来控制启动、停止和开机自动启动等等

```shell
systemctl start | stop | status | enable | disable 服务名
```

系统内置的服务例如有:

* NetworkManager: 主网络服务
* network: 副网络服务
* firewalld: 防火墙服务
* sshd、ssh: 远程登录服务

[systemctl命令详解](https://wangchujiang.com/linux-command/c/systemctl.html)