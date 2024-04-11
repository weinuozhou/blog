# DCL 语句

DCL 指的是数据库控制语言（Data Control Language），用于控制**数据库用户访问权限**的语言。DCL 包括授权（GRANT）、回收（REVOKE）等操作，用于管理数据库用户对数据的访问权限

## 用户管理

### 查询用户

```sql
select user from mysql.user;
```

<div style="text-align: center;"><img alt='202403232132296' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403232132296.png' width=500px> </div>


### 创建用户

```sql
create user 'username'@'host' identified by 'password';
```

?> 1. 创建用户test，只能在当前主机localhost访问，密码为123456

<div style="text-align: center;"><img alt='202403261947648' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261947648.png' width=500px> </div>

?> 2. 创建用户test2，可以在任意主机访问，密码为123456

<div style="text-align: center;"><img alt='202403261950582' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261950582.png' width=500px> </div>

### 修改用户密码

```sql
ALTER USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY 'new_password';
```

?> 修改用户test的密码为root

<div style="text-align: center;"><img alt='202403261952522' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261952522.png' width=500px> </div>

### 删除用户

```sql
drop user 'username'@'host';
```

?> 删除用户test及test2

<div style="text-align: center;"><img alt='202403261953954' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261953954.png' width=500px> </div>

## 权限控制

MySQL 中定义了很多权限，主要权限有以下几种:

1. ALL: 允许用户具有所有权限
2. SELECT：允许用户查询（读取）数据库中的数据。用户可以执行SELECT语句来检索数据，但不能修改或删除数据
3. INSERT：允许用户向数据库中的表中插入新的行数据。用户可以执行INSERT语句将新数据插入到表中
4. UPDATE：允许用户修改数据库中表的现有行数据。用户可以执行UPDATE语句来更新表中的数据
5. DELETE：允许用户删除数据库中表的现有行数据。用户可以执行DELETE语句来从表中删除数据
6. CREATE：允许用户创建新的数据库或表。用户可以执行CREATE DATABASE语句来创建新的数据库，或执行CREATE TABLE语句来创建新的表
7. DROP：允许用户删除数据库或表。用户可以执行DROP DATABASE语句来删除数据库，或执行DROP TABLE语句来删除表
8. ALTER：允许用户修改数据库或表的结构。用户可以执行ALTER TABLE语句来添加、修改或删除表的列

### 查询权限

```sql
SHOW GRANTS FOR 'username'@'host';
```

<div style="text-align: center;"><img alt='202403261959134' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403261959134.png' width=500px> </div>

### 授予权限

```sql
grant privileges on databasename.tablename to 'username'@'host';
```

<div style="text-align: center;"><img alt='202403262012404' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403262012404.png' width=500px> </div>

### 撤销权限

```sql
REVOKE privileges ON databasename.tablename FROM 'username'@'host';
```

<div style="text-align: center;"><img alt='202403262014616' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403262014616.png' width=500px> </div>
