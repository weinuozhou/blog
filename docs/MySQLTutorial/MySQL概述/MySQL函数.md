# `MySQL` 内置函数

`MySQL` 提供了许多内置函数，用于执行各种操作和计算,下面将介绍一些常用的内置函数

具体的 `MySQL` 内置函数可以参考: [MySQL官方文档](https://dev.mysql.com/doc/refman/5.7/en/built-in-function-reference.html)

## `MySQL` 字符串函数

`MySQL` 提供了许多字符串函数，用于处理和操作字符串数据

| 函数| 描述| 实例|
| :---| :---| :---|
| `ASCII(s)`| 返回字符串 `s` 的第一个字符的 `ASCII` 码|`select ascii("hello MySQL")`|
| `CHAR_LENGTH(s)`| 返回字符串 `s` 的字符数|`select char_length("hello MySQL")`|
| `REVERSE(s)`| 将字符串 `s` 的顺序反过来|`select reverse("hello MySQL")`|
| `TRIM(s)` | 去除字符串两端的空格 | `select trim("   hello MySQL   ")`|
| `REPLACE(s, old, new)` | 将字符串中的部分内容替换为新的内容| `select replace("hello MySQL", "MySQL", "world")`|
| `LEFT(s,n)`| 返回字符串 `s` 的前 `n` 个字符|`select left("hello NySQL", 2)`|
| `RIGHT(s,n)`| 返回字符串 `s` 的后 `n` 个字符|`select right("hello MySQL", 5)`|
| `LOWER(s)`| 将字符串 `s` 的所有字母变成小写字母|`select lower("hello MySQL")`|
| `UPPER(s)`| 将字符串 `s` 转换为大写|`select upper("hello MySQL")`|
|`CONCAT(s1,s2...sn)`|字符串 `s1`,`s2` 等多个字符串合并为一个字符串|`select concat("hello", "MySQL")`|

## `MySQL` 数值函数

`MySQL` 提供了许多数值函数，用于执行各种数值操作和计算

|函数|描述|实例|
|:---:|:---:|:---:|
|`ABS(x)`|返回 `x` 的绝对值|`select abs(-10)`|
|`CEIL(x)`|返回大于或等于 `x` 的最小整数|`select ceil(3.2)`|
|`FLOOR(x)`|返回小于或等于 `x` 的最大整数|`select floor(3.2)`|
|`ROUND(x,d)`|返回保留 `d` 位小数后的 `x`|`select round(3.1415926, 3)`|
|`TRUNCATE(x,d)`|返回 `x` 截断为 `d` 位小数的结果|`select truncate(3.1415926, 3)`|
|`MOD(x,y)`|返回 `x` 除以 `y` 的余数|`select mod(10, 3)`|
|`POW(x, y)`|返回 `x` 的 `y` 次方|`select pow(2, 3)`|

## `MySQL` 日期函数

|函数|描述|实例|
|:---:|:---:|:---:|
|`CURDATE()`|返回当前日期|`select curdate()`|
|`CURTIME()`|返回当前时间|`select curtime()`|
|`NOW()`|返回当前日期和时间|`select now()`|
|`YEAR(date)`|返回年份|`select year("2017-06-15")`|
|`MONTH(date)`|返回月份|`select month("2017-06-15")`|
|`DAY(date)`|返回日期|`select day("2017-06-15")`|
|`DATE_FORMAT(date,format)`|按指定格式显示日期时间|`select date_format("2011-10-03 15:08:06", "%Y/%m/%d-%H:%i:%s")`|
|`TIMESTAMPDIFF(unit, datetime_expr1, datetime_expr2)`|计算时间差|`select timestampdiff(year, '2004-01-14', '2024-3-26')`|

## `MySQL` 其他函数

|函数|描述|实例|
|:---:|:---:|:---:|
| `VERSION()`| 返回数据库的版本号| `select version()`|
| `DATABASE()`| 返回当前数据库名| `select database()`|
| `USER()`| 返回当前用户名| `select user()`|
| `PASSWORD(str)`| 返回字符串 `str` 的密码形式| `select password('123456')`|
| `MD5(str)`| 返回字符串 `str` 的 `MD5` 加密形式| `select MD5('123456')`|
| `SHA(str)`| 返回字符串 `str` 的 `SHA` 加密形式| `select SHA('123456')`|
| `INET_ATON(ip)`| 返回 `IPv4` 地址 `ip` 的整数形式| `select inet_aton('192.168.0.1')`|
| `INET_NTOA(num)`| 返回整数 `num` 的 `IPv4` 地址形式| `select inet_ntoa(3232235777)`|
