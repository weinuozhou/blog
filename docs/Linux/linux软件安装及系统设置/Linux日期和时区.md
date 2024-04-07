# Linux 日期和时区

## 查看系统的时间

* `date`命令可以显示或设置系统时间与日期
* [date命令详解](https://wangchujiang.com/linux-command/c/date.html)

## 修改 Linux 的时区

通过 date 查看的日期时间有可能是不准确的， 这是因为系统默认时区可能并不是中国的东八区， 通过以下shell命令可以修改时区:

```shell
rm -f /etc/localtime 
sudo ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```
