# 发送请求

**网络爬虫的工作流程**:

* 获取初始的 URL，该 URL 地址是用户自己制订的初始爬取的网页。
* 爬取对应 URL 地址的网页时，获取新的 URL 地址, 将新的 URL 地址放入 URL 队列中。
* 从 URL 队列中读取新的 URL，然后依据新的 URL 爬取网页，同时从新的网页中获取新的 URL 地址，重复上述的爬取过程。
* 设置停止条件，如果没有设置停止条件时，爬虫会一直爬取下去，直到无法获取新的 URL 地 址为止。设置了停止条件后，爬虫将会在满足停止条件时停止爬取

## `urllib`

* 在 Python 2 中, 有 urllib 和 urllib2 两个库来实现请求的发送
* 在 Python 3 中, 已经不存在 urllib2 这个库了, 统一为 urllib
* 其官方文档链接为: <https://docs.python.org/3/library/urllib.html>

 urllib 库是 Python 内置的 HTTP 请求库, 也就是说不需要额外安装即可使用。它包含如下 4 个模块:

* **request**: 它是最基本的 HTTP 请求模块, 可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样, 只需要给库方法传入 URL 以及额外的参数, 就可以模拟实现这个过程了。
* **error**: 异常处理模块, 如果出现请求错误, 我们可以捕获这些异常, 然后进行重试或其他操作以保证程序不会意外终止。
* **parse**: 一个工具模块, 提供了许多 URL 处理方法, 比如拆分、解析、合并等。
* **robotparser**: 主要是用来识别网站的 robots.txt 文件, 然后判断哪些网站可以爬, 哪些网站不可以爬, 它其实用得比较少

### `urlopen`

使用 urllib 的 request 模块, 我们可以方便地实现请求的发送并得到响应

urllib.request 模块提供了最基本的构造 HTTP 请求的方法,利用它可以模拟浏览器的一个请求发起过程,同时它还带有处理授权验证、重定向、浏览器 Cookies 以及其他内容

```python
response = urllib.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
```

* 该方法返回一个HTTPResponse对象
* `response.status`:返回响应的状态码
* `response.read()`:返回响应的内容(bytes类型的数据, 需要进行解码)
* `response.getheaders()`:返回响应头
* `response.getheader('content')`:查看指定的响应头
* `response.geturl()`:获取请求的url

#### data参数

data 参数是可选的。如果要添加该参数, 需要使用 bytes 方法将**参数转化为字节流编码**格式的内容, 即 bytes 类型。如果传递了这个参数, 则它的请求方式就不再是 **GET** 方式, 而是 **POST** 方式

```python
params = {'name': 'John'} # 创建一个字典
urllib.parse.urlencode(params) # 使用urlencode将字典转换为URL编码字符串
```

#### timeout参数

timeout 参数用于设置**超时时间**, 单位为秒, 就是如果请求超出了设置的这个时间, 还没有得到响应, 就会抛出异常。如果不指定该参数, 就会使用全局默认时间

可以通过设置这个超时时间来**控制一个网页如果长时间未响应, 就跳过它的抓取**。这可以利用 try except 语句来实现

```python
import socket   

try:  
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=3)  
except urllib.error.URLError as e:  
    if isinstance(e.reason, socket.timeout):  
        print('TIME OUT')
```

### Request对象

```python
urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

* `url`:用于请求 URL, 这是必传参数
* `data`:必须传 bytes（字节流）类型的,如果它是字典, 可以先用 urllib.parse 模块里的 urlencode() 编码
* `headers`:它就是请求头, 我们可以在构造请求时通过 headers 参数直接构造, 也可以通过调用请求实例的 add_header() 方法添加
* `method`: method 是一个字符串, 用来指示请求使用的方法, 比如 GET、POST 和 PUT 等

我们可以在构造请求时通过 headers 参数直接构造, 也可以通过调用请求实例的 `add_header()` 方法添加

```python
data = bytes(urllib.parse.urlencode({'name': 'Germey'}), encoding='utf8')  
req = urllib.request.Request(url='http://httpbin.org/post', data=data, method='POST')  
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = urllib.request.urlopen(req)
```

### 代理

在做爬虫的时候, 免不了要使用代理, 如果要添加代理, 可以这样做

```python
from urllib.request import ProxyHandler, build_opener  
ProxyHandler({
    'http': 'http://127.0.0.1:7890',  
    'https': 'https://127.0.0.1:7890'
})
opener = build_opener(proxy_handler) # 创建了一个 Opener 对象 
```

* ProxyHandler 用于设置代理, 接受一个字典作为参数, 字典的键为协议类型(如 http、https), 值为代理地址
* build_opener用于创建一个自定义的 Opener 对象, 可以用于发送 HTTP 请求

### 处理异常

在网络不好的情况下, 如果出现了异常, 该怎么办呢？这时如果不处理这些异常, 程序很可能因报错而终止运行, 所以异常处理还是十分有必要的

#### URLError

URLError 类来自 urllib 库的 error 模块, 它继承自 OSError 类, 是 error 异常模块的基类, 由 request 模块产生的异常都可以通过捕获这个类来处理

```python
from utllib import error
except error.URLError as e
```

* `e.reason`:返回异常的原因

```python
try:  
    response = urllib.request.urlopen('https://example.com/index.htm')  
except urllib.error.URLError as e:  
    print(e.reason)
```

程序没有直接报错, 而是输出了Not Found, 这样通过如上操作, 我们就可以避免程序异常终止, 同时异常得到了有效处理

#### HTTPError

它是 URLError 的子类, 专门用来处理 HTTP 请求错误, 比如认证请求失败等。它有如下 3 个属性:

* code: 返回 HTTP 状态码, 比如 404 表示网页不存在, 500 表示服务器内部错误等。
* reason: 同父类一样, 用于返回错误的原因。
* headers: 返回请求头

```python
try:  
    response = urllib.request.urlopen('https://example.com/index.htm')  
except urllib.error.HTTPError as e:  
    print(e.reason, e.code, e.headers, sep='\n')
```

### 解析链接

urllib 库里还提供了 parse 模块, 它定义了处理 URL 的标准接口, 例如实现 URL 各部分的抽取、合并以及链接转换。

#### urlparse

```python
urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
```

* urlstring: 这是必填项, 即待解析的 URL。
* scheme: 它是默认的协议（比如 http 或 https 等）
* 返回值:`ParseResult(scheme, netloc, path, params, query, fragment)`

```python
result = urllib.parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')  
print(type(result), result, sep='\n')
```

#### urlunparse

有了 urlparse 方法, 相应地就有另外一个方法 urlunparse。它接受的参数是一个可迭代对象, 但是**它的长度必须是 6**, 否则会抛出参数数量不足或者过多的问题

```python
data = ['http', 'www.baidu.com', 'index.html', '', 'a=6', 'comment']  
print(urllib.parse.urlunparse(data))
```

#### urlsplit

* 这个方法和 urlparse 方法非常相似, 只不过它不再单独解析 params 这一部分, **只返回 5 个结果**
* 返回结果是 SplitResult, 它其实也是一个元组类型, 既可以用**属性获取值**, 也可以用**索引**来获取

```python
result = urllib.parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')  
print(result, result[1], sep='\n')
```

#### urlunsplit

与 urlunparse 方法类似, 它也是将链接各个部分组合成完整链接的方法, 传入的参数也是一个可迭代对象, 例如列表、元组等, 唯一的区别是**长度必须为 5**

```python
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']  
print(urllib.parse.urlunsplit(data))
```

#### urljoin

生成链接还有另一个方法, 那就是 urljoin 方法。我们可以提供一个 base_url（基础链接）作为第一个参数, 将新的链接作为第二个参数, 该方法会分析 base_url 的 scheme、netloc 和 path 这 3 个内容并对新链接缺失的部分进行补充, 最后返回结果

```python
print(urllib.parse.urljoin('http://www.baidu.com', 'FAQ.html'))    
print(urllib.parse.urljoin('http://www.baidu.com', '?category=2&comment'))  
print(urllib.parse.urljoin('www.baidu.com', '?category=2&comment'))  
print(urllib.parse.urljoin('www.baidu.com#comment', '?category=2'))
```

#### urlencode

urlencode可以将字典序列化为 GET 请求参数

```python
params = {  
    'name': 'John',  
    'age': 22  
}  
base_url = 'http://www.baidu.com?'  
url = base_url + urllib.parse.urlencode(params)  
print(url) # http://www.baidu.com?name=John&age=22
```

#### parse_qs

有了序列化, 必然就有反序列化。如果我们有一串 GET 请求参数, 利用 parse_qs 方法, 就可以将它转回字典

```python
query = 'name=%E5%BC%A0%E4%B8%89&age=22'  
print(urllib.parse.parse_qs(query))
```

#### quote

该方法可以将内容转化为 URL 编码的格式。URL 中带有中文参数时, 有时可能会导致乱码的问题, 此时用这个方法可以将中文字符转化为 URL 编码

```python
keyword = ' 壁纸 '  
url = 'https://www.baidu.com/s?wd=' + urllib.parse.quote(keyword)  
print(url)
```

#### unquote

有了 quote 方法, 当然还有 unquote 方法, 它可以进行 URL 解码

```python
print(urllib.parse.unquote('https://www.baidu.com/s?wd=%20%E5%A3%81%E7%BA%B8%20'))
```

### Robot协议

Robots 协议也称作爬虫协议、机器人协议, 它的全名叫作**网络爬虫排除标准**（Robots Exclusion Protocol）, 用来告诉爬虫和搜索引擎哪些页面可以抓取, 哪些不可以抓取。它通常是一个叫作 robots.txt 的文本文件, 一般放在网站的根目录下

#### 爬虫名称

爬虫其实是有固定名字的了, 比如百度的就叫作 BaiduSpider。下表列出了一些常见的搜索爬虫的名称及对应的网站

| 爬虫名称    | 名称      | 网站              |
| ----------- | --------- | ----------------- |
| BaiduSpider | 百度      | <www.baidu.com>     |
| Googlebot   | 谷歌      | <www.google.com>    |
| 360Spider   | 360 搜索  | <www.so.com>        |
| YodaoBot    | 有道      | <www.youdao.com>    |
| ia_archiver | Alexa     | <www.alexa.cn>      |
| Scooter     | altavista | <www.altavista.com> |

#### robotparser

该模块提供了一个类 RobotFileParser, 它可以根据某网站的 robots.txt 文件来判断一个爬取爬虫是否有权限来爬取这个网页

```python
urllib.robotparser.RobotFileParser(url='')
```

这个类常用的几个方法:

* set_url : 用来设置 robots.txt 文件的链接。如果在创建 RobotFileParser 对象时传入了链接, 那么就不需要再使用这个方法设置了。
* read: 读取 robots.txt 文件并进行分析。注意, 这个方法执行一个读取和分析操作, 如果不调用这个方法, 接下来的判断都会为 False, 所以一定记得调用这个方法。这个方法不会返回任何内容, 但是执行了读取操作。
* parse: 用来解析 robots.txt 文件, 传入的参数是 robots.txt 某些行的内容, 它会按照 robots.txt 的语法规则来分析这些内容。
* can_fetch: 该方法传入两个参数, 第一个是 User-agent, 第二个是要抓取的 URL。返回的内容是该搜索引擎是否可以抓取这个 URL, 返回结果是 True 或 False。
* mtime: 返回的是上次抓取和分析 robots.txt 的时间, 这对于长时间分析和抓取的搜索爬虫是很有必要的, 你可能需要定期检查来抓取最新的 robots.txt。
* modified: 它同样对长时间分析和抓取的搜索爬虫很有帮助, 将当前时间设置为上次抓取和分析 robots.txt 的时间。

```python
from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d')) # False
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections")) #False
```

## urllib3库

urllib3 是一个功能强大、用户友好的Python HTTP 客户端。Python 生态系统的大部分已经使用 urllib3

urllib3的官方文档:<https://urllib3.readthedocs.io/en/stable/reference/index.html>

### Pool Manager

允许任意请求, 同时透明地为您跟踪必要的连接池

```python
import urllib3
urllib3.PoolManager(num_pools=10 , headers = None , **connection_pool_kw)
```

* num_pools ( int ):在丢弃最近最少使用的池之前要缓存的连接池数量。
* headers ( Mapping [ str , str ] | None ):所有请求中包含的标头, 除非显式给出其他标头。
* \*\*connection_pool_kw ( Any ):附加参数用于创建新 urllib3.connectionpool.ConnectionPool实例。

### request

```python
urllib3.request(method, url, *, body=None, fields=None, headers=None, preload_content=True, decode_content=True, redirect=True, retries=None, timeout=3, json=None)
```

* 一种方便的顶级请求方法。它使用模块全局PoolManager实例
* `method`:请求的方法, 必填参数
* `url`: 请求的网址, 必填参数

#### Response对象

```python
urllib3.response.HTTPResponse(body='', headers=None, status=0, version=0, reason=None, preload_content=True, decode_content=True, original_response=None, pool=None, connection=None, msg=None, retries=None, enforce_content_length=True, request_method=None, request_url=None, auto_close=True)
```

* response.status:获取响应状态码
* response.headers:获取响应头
* response.data:获取请求的响应体

#### fields参数

fileds参数用于构造URL请求或POST请求的表单

```python
http = urllib3.PoolManager()
r = http.request('GET', 'https://httpbin.org/get', fields={'name': 'jack', 'country':'中国',  'age': '23'})
print(f'请求的响应状态码为{r.status}')
print(f"请求的响应体为:\n{r.data.decode('utf-8')}")
```

#### retries参数

retries参数用于重复请求的次数, 默认为3次

```python
http = urllib3.PoolManager()
r1 = http.request('GET', 'https://httpbin.org/get')
r2 = http.request('GET', 'https://httpbin.org/get', retries=5)
r3 = http.request('GET', 'https://httpbin.org/get', retries=False)
print(f'r1的重复请求次数为:{r1.retries.total}') # 3
print(f'r2的重复请求次数为:{r2.retries.total}') # 5
print(f'r3的重复请求次数为:{r3.retries.total}') # False
```

#### headers参数

headers参数用于模拟浏览器请求参数

```python
http = urllib3.PoolManager()
headers = {
    'User_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
r = http.request('POST', 'https://httpbin.org/post', fields={'name': 'python', 'age': '23'}, headers=headers)
print(f'请求的响应状态码为{r.status}')
print(f"请求的响应体为:\n{r.data.decode('utf-8')}")
```

## requests库

urllib固然强大,但确实有不方便的地方,比如处理网页验证和 Cookies 时,需要写 Opener 和 Handler 来处理。

为了更加方便地实现这些操作就有了更为强大的库 `requests`

```python
try: 
    import requests
except ImportError:
    os.system("pip install requests -i https://pypi.douban.com/simple")
```

### get请求

HTTP 中最常见的请求之一就是 GET 请求, 下面首先来详细了解一下利用 requests 构建 GET 请求的方法

```python
import requests
r = requests.get(url=url, headers=headers, params=None, timeout=None)
```

* 该方法返回一个`response`对象
* `r.status_code`:返回响应的状态码
* `r.headers`:响应的请求头
* `r.text`:响应的文本
* `r.content`:响应内容(字节流、二进制)
* `r.encoding`:response对象的编码方式
* `r.url`:获取请求网址

#### 基本请求(不带参数)

```python
r = requests.get(url='https://httpbin.org/get')
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

#### 设置`url`的参数

例如,我们想要访问`https://www.baidu.com/s?wd=Python&pn=20`,

我们可以直接设置`url=https://www.baidu.com/s?wd=Python&pn=20`

```python
r = requests.get(url='https://httpbin.org/get?wd=python&pn=20')
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

除了上述直接设置`url`外, 更推荐的做法是使用`params`参数来实现

```python
data = {
    'wd':'python',
    'pn':20
}
r = requests.get(url='https://httpbin.org/get', params=data)
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

#### 设置请求头

* 有些网站会通过请求头来识别网络爬虫行为, 从而达到一定的反爬机制
* 请求头`headers`是用来模拟浏览器的行为
* `requests`可以通过设置`headers`来设置请求头

```python
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
r = requests.get(url='https://httpbin.org/get', headers=headers)
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

请求头可以通过抓包获取, 也可以第三方库`fake_useragent`来生成随机请求头

```python
from fake_useragent import UserAgent # pip install fake_useragent
headers = {
    'User_Agent': UserAgent().random
}
r = requests.get(url='https://httpbin.org/get', headers=headers)
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

#### 设置网络超时提示

可以通过`timeout`来设置网络超时,单位是s

```python
r = requests.get(url='https://httpbin.org/get', timeout=3)# 设置网络超时提示
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

### `post`请求

```python
r = requests.post(url, data, headers, timeout)
```

* `data`:post请求要发送的数据,数据类型为字典或文件对象
* `post`请求与`get`请求类似, 这里不再赘述

```python
r = requests.post(url='https://httpbin.org/post', data={'name': 'john', 'age': 24})
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

### 高级用法

#### `cookies`设置

###### 获取`cookies`

```python
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
r = requests.get(url='https://www.zhihu.com/', headers=headers, timeout=5)
print(f'cookies信息为\n{r.cookies}')
```

###### 维持登录状态

```python
cookies='your_cookies'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
     key, value = cookie.split('=', 1)
     jar.set(key, value)
r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
print(f'响应状态码为{r.status_code}')
```

#### 会话维持

在`requests`中, 直接利用`get()`或者`post()`请求可以模拟网页的请求, 但是这是不同的会话,也就是用浏览器打开了两个不同的页面,

为了维持同一个会话, 可以通过`Session`对象来实现

`Session`对象的作用:

* 自动处理`cookies`,即下次请求会自动带上上一次请求的`cookies`
* 自动处理多次请求产生的`cookies`

```python
# 创建Session对象
session = requests.Session()
r1 = session.get('http://httpbin.org/cookies/set/number/123456789')
r2 = session.get('http://httpbin.org/cookies')
print(r1.text, r2.text, sep='\n')
```

#### SSL证书验证

当发送`https`请求时,网页会检查`SSL`证书,可以使用`verify`参数来确定是否检查该证书

```python
r = requests.get(url='https://httpbin.org/get', verify=False)
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

#### 代理设置

对于某些网站, 在测试时请求几次, 能正常获取内容, 当大规模爬取时, 网站可能会**弹出验证码**、**或者跳转到登录认证页面**、更有甚者**被封禁客户端的ip**

为了防止这种情况,可以通过**设置代理**来解决这个问题, 也就是通过`proxies`这个参数

* 支持http代理和SOCKS协议的代理
* 下列为无效的代理, 只是为了演示怎么使用

```python
proxies = {
    "http":'http://10.32.12.56:3291', 
    "https":'http://10.10.1.12:1080'
}
r = requests.get(url,proxies=proxies)
```

#### Request对象

我们可以将请求表示为数据结构, 其中各个参数都可以通过一个 Request 对象来表示。这在 requests 里同样可以做到, 这个数据结构就叫 Prepared Request

```python
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent': 
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = requests.Session()
req = requests.Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(f'响应状态码为{r.status_code}')
print(f'响应内容为\n{r.text}')
```

### 封装成函数

```python
def send_request(url, headers=None, cookies=None):
    try:
        resp = requests.get(url, headers=headers, cookies=cookies, timeout=10, verify=False)
        if resp.status_code == 200:
            return resp.text
        else:
            print("服务器未响应")
            return None
    except requests.exceptions.RequestException as e:
        print("请求网页失败", e)
```