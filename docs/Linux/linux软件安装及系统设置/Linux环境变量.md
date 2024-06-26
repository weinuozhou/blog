# Linux环境变量

## 环境变量的概念

Linux 的变量可分为两类：**环境变量**和**本地变量**

* 环境变量：或者称为全局变量，存在于所有的shell 中，在你登陆系统的时候就已经有了相应的系统定义的环境变量了。Linux 的环境变量具有继承性，即子 shell 会继承父 shell 的环境变量
* 本地变量：当前shell 中的变量，很显然本地变量中肯定包含环境变量。Linux 的本地变量的非环境变量不具备继承性

当你进入系统的时候，Linux 就会为你读入系统的环境变量，Linux 中有很多记载环境变量的文件，它们被系统读入是按照一定的顺序的。

1.`/etc/profile`

此文件为系统的环境变量，它为每个用户设置环境信息，当用户第一次登录时，该文件被执行。并从 `/etc/profile.d`目录的配置文件中搜集shell 的设置。这个文件，是任何用户登陆操作系统以后都会读取的文件（如果用户的 shell 是 `csh` 、`tcsh` 、`zsh` ，则不会读取此文件），用于获取系统的环境变量，只在登陆的时候读取一次。 (假设用户使用的是BASH )

2.`/etc/bashrc`

在执行完 `/etc/profile` 内容之后，如果用户的 SHELL 运行的是 bash ，那么接着就会执行此文件。另外，当每次一个新的 bash shell 被打开时，该文件被读取。每个使用 bash 的用户在登陆以后执行完 `/etc/profile` 中内容以后都会执行此文件，在新开一个 bash 的时候也会执行此文件。因此，如果你想让每个使用 bash 的用户每新开一个 bash 和每次登陆都执行某些操作，或者给他们定义一些新的环境变量，就可以在这个里面设置。

3.`~/.bash_profile`

每个用户都可使用该文件输入专用于自己使用的 shell 信息。当用户登录时，该文件仅仅执行一次，默认情况下，它设置一些环境变量，执行用户的 `.bashrc` 文件。单个用户此文件的修改只会影响到他以后的每一次登陆系统。因此，可以在这里设置单个用户的特殊的环境变量或者特殊的操作，那么它在每次登陆的时候都会去获取这些新的环境变量或者做某些特殊的操作，但是仅仅在登陆时。

4.`~/.bashrc`

该文件包含专用于单个人的 bash shell 的 bash 信息，当登录时以及每次打开一个新的 shell 时，该文件被读取。单个用户此文件的修改会影响到他以后的每一次登陆系统和每一次新开一个 bash。因此，可以在这里设置单个用户的特殊的环境变量或者特殊的操作，那么每次它新登陆系统或者新开一个 bash ，都会去获取相应的特殊的环境变量和特殊操作。

5.`~/.bash_logout`

当每次退出系统( 退出bash shell) 时, 执行该文件

## 设置环境变量

### 设置临时环境变量

```shell
export 变量名='值'
```

采用 `export` 设置的环境变量，在退出shell后就会失效，下次登录时需要重新设置。如果希望环境变量永久生效，需要在登录脚本文件中配置

### 设置永久环境变量

1. 在 `/etc/profile`文件中设置,用户登录时执行 `/etc/profile`文件中设置系统的环境变量。但是，Linux不建议在 `/etc/profile`文件中设置系统环境变量
2. 在 `/etc/profile.d`目录中增加环境变量脚本文件，这是Linux推荐的方法
3. 在 `/etc/bashrc`文件中设置环境变量, 该文件配置的环境变量将会影响全部用户使用的bash shell。但是，Linux也不建议在 `/etc/bashrc`文件中设置系统环境变量

### 用户环境变量

1. `.bash_profile（推荐首选）`当用户登录时执行，每个用户都可以使用该文件来配置专属于自己的环境变量
2. `.bashrc`当用户登录时以及每次打开新的Shell时该文件都将被读取，不推荐在里面配置用户专用的环境变量，因为每开一个Shell，该文件都会被读取一次，效率肯定受影响
3. `.bash_logout`每次退出系统（退出bash shell）时执行该文件
4. `.bash_history`保存了当前用户使用过的历史命令

## 环境变量的生效

在脚本文件中设置的环境变量不会立即生效，退出Shell后重新登录时才生效，或者用 source命令让它立即生效，例如：`source /etc/profile`

## 查看环境变量

在Shell下，用 `env` 命令查看当前用户全部的环境变量

具体可以查看:[env命令详解](https://wangchujiang.com/linux-command/c/env.html)

