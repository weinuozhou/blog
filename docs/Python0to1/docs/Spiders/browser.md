# 数据抓包

在你的浏览器里面,输入百度网址:https://www.baidu.com ,一回车看到一个网页如下:

<div style="text-align: center;">     <img alt='202403201308672' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201308672.png' width=500px> </div>

网页看起来似乎平平无奇,然而,你右键点击查看网页源代码, 是这个样子的

<div style="text-align: center;">     <img alt='202403201310752' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201310752.png' width=500px> </div>

* 这还仅仅是网页源代码的$\frac{1}{100}$,我们就是要在**这些网页源代码中获取我们所需要的数据**
* 在互联网上, 网站都是**托管在服务器上**的, 服务器24小时运行着, 时时刻刻等待着请求, 我们的爬虫, 首先会模拟请求就好像你在浏览器输入网址, 然后回车那样, 爬虫可以用到一些 Http 库向指定的服务器偷偷摸摸的发起请求, 这个时候爬虫可以假装自己是浏览器(添加一些header信息)大多数的服务器呢, 傻不拉的以为是浏览器发送请求, 就直接返回数据给爬虫了
* 当然了, 有一些网站比较精明, 所以他们会建立一些**反爬虫机制**, 当然我们也可以采取一些手段(例如Ajax请求、浏览器自动化)获取数据
* 不同情况下, 服务器返回给我们的数据格式不一样, 主要有**HTML**, **JSON**, **二进制数据**,根据不同的情况, 我们可以使用不同的方式对他们进行处理
* 获取到数据之后, 我们就要考虑保存数据, 保存数据也有很多种方式, 存储在**数据库**、**硬盘**、**远程服务器**等等

## 爬虫工作基本原理

1. 获取初始的 URL, 该 URL 地址是用户自己制订的初始爬取的网页。
2. 爬取对应 URL 地址的网页时, 获取新的 URL 地址, 将新的 URL 地址放入 URL 队列中。
3. 从 URL 队列中读取新的 URL, 然后依据新的 URL 爬取网页, 同时从新的网页中获取新的 URL 地址, 重复上述的爬取过程。
4. 设置停止条件, 如果没有设置停止条件时, 爬虫会一直爬取下去, 直到无法获取新的URL地址为止。设置了停止条件后, 爬虫将会在满足停止条件时停止爬取

## 浏览器抓包

### 请求网址

在你的浏览器里面,输入百度网址:<https://www.baidu.com> ,一回车看到一个网页,在输入框中输入Python回车之后,右键打开检查点击network刷新页面后可以看到以下页面:

<div style="text-align: center;">     <img alt='202403201418925' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403201418925.png' width=500px> </div>

* 可以看到有很多请求, 点开类型为document、响应状态(status)为200的请求, 可以看到我们的请求网址为:
<https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=Python&fenlei=256&rsv_pq=0xcab360b10000424d&rsv_t=14c5c2%2F0PNi9fEscZ4ENV7JpGqUBEL0SKvwPfZvV9qKGl0om8uT7LDWRL%2BS%2F&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=Python&rsp=5&inputT=1516&rsv_sug4=1517&rsv_sug=1>
* ? 后面的内容是请求参数, 这些参数以键值对的形式实现, 比如这里的wd=Python就是告诉浏览器我们要访问与Python相关的内容
* 我们可以尝试着访问:<https://www.baidu.com/s?wd=Python> ,同样可以访问到与Python相关的内容

### 请求头

点击Type为document的请求, 点击headers即可查看请求头

常用的请求头信息:

* `Accept`:请求报头域, 它说明了客户端可接受哪些类型的信息
* `Accept-Language`:指定客户端可接受的语言类型
* `Accept-Encoding`:指定客户端可接受的内容编码格式
* `Host`:指定请求资源的主机ip和端口号
* `Cookies`:这是网站为了辨别用户进行会话跟踪而存储在用户本地的数据, 主要用于维持当前会话状态,保存登录信息等
* `Referer`:标识请求是从哪个页面发过来的
* `User-Agent`:识别用户使用的操作系统及版本、浏览器及版本等信息, 在爬虫时尽量加上该参数伪装成浏览器, 否则很可能被识别出为爬虫

有了**请求头和请求网址**就可以进行一些简单的爬虫操作了

### Cookies

Cookies 指某些网站为了**辨别用户身份**、**进行会话跟踪**而存储在用户本地终端上的数据

#### 会话维持技术

当客户端第一次请求服务器时, 服务器会返回一个响应头中带有 Set-Cookie 字段的响应给客户端, 用来标记是哪一个用户, 客户端浏览器会把 Cookies 保存起来。当浏览器下一次再请求该网站时, 浏览器会把此 Cookies 放到请求头一起提交给服务器, Cookies **携带了会话 ID 信息**, 服务器检查该 Cookies 即可找到对应的会话是什么, 然后再判断会话来以此来辨认用户状态。

在成功登录某个网站时, 服务器会告诉客户端设置哪些 Cookies 信息, 在后续访问页面时客户端会把 Cookies 发送给服务器, 服务器再找到对应的会话加以判断。如果会话中的某些设置登录状态的变量是有效的, 那就证明用户处于登录状态, 此时返回登录之后才可以查看的网页内容, 浏览器再进行解析便可以看到了

Cookies属性主要有以下几个:

* `Name`: 即该 Cookie 的名称。Cookie 一旦创建, 名称便不可更改
* `Value`: 即该 Cookie 的值。如果值为 Unicode 字符, 需要为字符编码。如果值为二进制数据, 则需要使用 BASE64 编码。
* `Max Age`: 即该 Cookie 失效的时间, 单位秒, 也常和 Expires 一起使用, 通过它可以计算出其有效时间。Max Age 如果为正数, 则该 Cookie 在 Max Age 秒之后失效。如果为负数, 则关闭浏览器时 Cookie 即失效, 浏览器也不会以任何形式保存该 Cookie。
* `Path`: 即该 Cookie 的使用路径。如果设置为 /path/, 则只有路径为 /path/ 的页面可以访问该 Cookie。如果设置为 /, 则本域名下的所有页面都可以访问该 Cookie。
* `Domain`: 即可以访问该 Cookie 的域名。例如如果设置为 .zhihu.com, 则所有以 zhihu.com, 结尾的域名都可以访问该 Cookie。
* `Size`: 即此 Cookie 的大小。
* `Http`: 即 Cookie 的 httponly 属性。若此属性为 true, 则只有在 HTTP Headers 中会带有此 Cookie 的信息, 而不能通过 document.cookie 来访问此 Cookie。
* `Secure`: 即该 Cookie 是否仅被使用安全协议传输。安全协议。安全协议有 HTTPS, SSL 等, 在网络上传输数据之前先将数据加密。默认为 false。

#### 会话Cookies和持久Cookies

从表面意思来说, 会话 Cookie 就是把 Cookie 放在浏览器内存里, 浏览器在关闭之后该 Cookie 即失效；持久 Cookie 则会保存到客户端的硬盘中, 下次还可以继续使用, 用于长久保持用户登录状态。

其实严格来说, 没有会话 Cookie 和持久 Cookie 之 分, 只是由 Cookie 的 **Max Age 或 Expires 字段决定了过期的时间**。

因此, 一些持久化登录的网站其实就是把 Cookie 的有效时间和会话有效期设置得比较长, 下次我们再访问页面时仍然携带之前的 Cookie, 就可以直接保持登录状态。