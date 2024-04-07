# 用户与用户组

Linux系统是一个多用户多任务的分时操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统

* 配置多个用户
* 配置多个用户组
* 用户可以加入到多个用户组

Linux 关于权限的管控有两个级别:
* **针对用户的权限控制**
* **针对用户组的权限控制**

## 用户组管理

* 创建用户组:[groupadd命令详解](https://wangchujiang.com/linux-command/c/groupadd.html)
* 删除用户组:[groupdel命令详解](https://wangchujiang.com/linux-command/c/groupdel.html)

## 用户管理

* 创建用户: [useradd命令详解](https://wangchujiang.com/linux-command/c/useradd.html)
* 删除用户: [userdel命令详解](https://wangchujiang.com/linux-command/c/userdel.html)
* 查看用户所属的组: [id命令详解](https://wangchujiang.com/linux-command/c/id.html)
* 修改用户所属的组: [usermod命令详解](https://wangchujiang.com/linux-command/c/usermod.html)
* 查看所有已知用户: `getent passwd`
* 查看所有已知用户组: `getent group`



