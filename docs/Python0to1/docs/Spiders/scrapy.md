# Scrapy框架介绍

当你写了很多爬虫，你会发现每次写爬虫程序时，都需要实现页面获取、页面解析、异常处理、保存数据等等，这里面很多工作都是乏力的重复劳动，我们可以使用 `scrapy` 爬虫框架来提供编写爬虫代码的效率

## `scrapy`的安装

可以使用python的包管理工具pip来安装scrapy
```bash
pip install scrapy
```

## `scrapy`组件

* **scrapy引擎**:控制数据处理流程,是整个框架的核心
* **调度器(Scheduler)**:从引擎接受请求并列入队列
* **下载器(Downloader)**:将网页内容返回给蜘蛛程序
* **蜘蛛程序(spider)**:解析网页并抓取特定URL
* **数据管道(Item PipeLine)**:清理、验证和存储数据
* **中间件(Middlewares)**:扩展scrapy的功能

<div style="text-align: center;"><img alt='202404061841289' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404061841289.png' width=500px> </div>

### 数据流

Scrapy 中的数据流由引擎控制，其过程如下:

* Engine 首先打开一个网站，找到处理该网站的 Spider 并向该 Spider 请求第一个要爬取的 URL
* Engine 从 Spider 中获取到第一个要爬取的 URL 并通过 Scheduler 以 Request 的形式调度
* Engine 向 Scheduler 请求下一个要爬取的 URL
* Scheduler 返回下一个要爬取的 URL 给 Engine，Engine 将 URL 通过 Downloader Middlewares 转发给 Downloader 下载
* 一旦页面下载完毕， Downloader 生成一个该页面的 Response，并将其通过 Downloader Middlewares 发送给 Engine
* Engine 从下载器中接收到 Response 并通过 Spider Middlewares 发送给 Spider 处理
* Spider 处理 Response 并返回爬取到的 Item 及新的 Request 给 Engine
* Engine 将 Spider 返回的 Item 给 Item Pipeline，将新的 Request 给 Scheduler
* 重复第二步到最后一步，直到  Scheduler 中没有更多的 Request，Engine 关闭该网站，爬取结束

通过多个组件的相互协作、不同组件完成工作的不同、组件对异步处理的支持，Scrapy 最大限度地利用了网络带宽，大大提高了数据爬取和处理的效率

### 项目结构

它是通过命令行来创建项目的，代码的编写还是需要 IDE。项目创建之后，项目文件结构如下所示：

```text
scrapy.cfg
project/
    __init__.py
    items.py
    pipelines.py
    settings.py
    middlewares.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...
```

* scrapy.cfg：它是 Scrapy 项目的配置文件，其内定义了项目的配置文件路径、部署相关信息等内容。
* items.py：它定义 Item 数据结构，所有的 Item 的定义都可以放这里。
* pipelines.py：它定义 Item Pipeline 的实现，所有的 Item Pipeline 的实现都可以放这里。
* settings.py：它定义项目的全局配置。
* middlewares.py：它定义 Spider Middlewares 和 Downloader Middlewares 的实现。
* spiders：其内包含一个个 Spider 的实现，每个 Spider 都有一个文件

## 创建项目及蜘蛛程序

在命令行中使用`scrapy`命令创建名为demo的项目
```bash
scrapy startproject demo
```
cd到demo目录下，用下面的命令创建名为`douban`的蜘蛛程序
```bash
scrapy genspider douban movie.douban.com # 后面跟着是你想要爬取的url
```
创建好的项目如下图所示:

<div style="text-align: center;"><img alt='202404061900492' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404061900492.png' width=500px> </div>

下面将对各个模块如何编写进行讲解

## Item的使用

Item是保存爬取数据的容器，它的使用方法和字典类似。不过相对于字典，Item还多了额外的保护机制，可以**避免定义字段错误**等等

### 声明item

创建Item需要继承 `scrapy.Item` 类，并且定义类型为 `scrapy.Field` 的字段，例如:
```python
import scrapy

class ScrapyItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
```

### item字段(Item Fields)

可以根据自己的需求，定义使用其他的 Field 键。 设置 Field 对象的主要目的就是在一个地方定义好所有的元数据。 一般来说，那些依赖某个字段的组件肯定使用了特定的键(key)。您必须查看组件相关的文档，查看其用了哪些元数据键(metadata key)

需要注意的是，用来声明item的 Field 对象并没有被赋值为class的属性。 不过您可以通过 Item.fields 属性进行访问

### 创建Item

```python
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()

product = Product(name='Desktop', price=1000)
print(product)
```

### 获取字段及值

```python
print(f"product的所有字段为:{product.fields}")
print(f"product的name字段的值为{product['name']}")
print(f"product的name字段的值为{product.get('name', '')}") # 使用get方法，若name为空不会报错而是输出预先设置好的值
```

### 设置字段的值

```python
product['name'] = 'chairs'
print(f"product的name字段的值为{product['name']}")
```

### 获取到所有的值

```python
print(f"product的所有字段为:{product.keys()}")
print(f"product的所有字段的值为:{product.values()}")
```

### Item的扩展

可以通过继承原始的Item来扩展item(添加更多的字段或者修改某些字段的元数据)

```python
class DiscountedProduct(Product):
    discount = scrapy.Field()

discount_product = DiscountedProduct(discount=0.8)
print(f"product的所有字段为:{discount_product.fields}")
```

## Spiders的使用

Spider类定义了如何爬取某个(或某些)网站。包括了爬取的动作(例如:是否跟进链接)以及如何从网页的内容中提取结构化数据(爬取item)

1. 以初始的URL初始化Request，并设置回调函数。 当该request下载完毕并返回时，将生成response，并作为参数传给该回调函数
2. spider中初始的request是通过调用 start_requests() 来获取的。 start_requests() 读取 start_urls 中的URL， 并以 parse 为回调函数生成 Request 
3. 在回调函数内分析返回的(网页)内容，返回 Item 对象、dict、 Request 或者一个包括三者的可迭代容器。 返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)
4. 在回调函数内，您可以使用 选择器(Selectors) (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item
5. 最后，由spider返回的item将被存到数据库(由某些 Item Pipeline 处理)或使用 Feed exports 存入到文件中

### scrapy.Spider

Spider是最简单的spider。每个其他的spider必须继承自该类。 Spider仅仅提供了 `start_requests()` 的默认实现，读取并请求spider属性中的 `start_urls`, 并根据返回的结果调用 `spider` 的 `parse` 方法

* `name`:定义spider名字的字符串(string),必选参数
* `allowed_domains`:包含了spider允许爬取的域名(domain)列表(list),可选参数
* `start_urls`:URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取
* `start_requests()`:该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request
* `parse(response)`:当response没有指定回调函数时，该方法是Scrapy处理下载的response的默认方法

`douban.py` 的具体内容如下:
```python
import scrapy

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["mobie.douban.com"]
    start_urls = ["https://mobie.douban.com"]

    def parse(self, response):
        pass
```

这里有三个属性name、allowed_domains、start_urls和一个方法parse
* **name**:这是项目的唯一名字，用于区分不同的Spider
* **allowed_domains**:允许爬取的域名，如果后续的请求不是在这个域名下，请求会被过滤
* **start_urls**:它包含SPider在启动时爬取的url列表
* **parse**:该方法负责解析返回的响应，提取数据或者进一步生成要处理的请求

#### 在单个回调函数中返回多个Request以及Item的例子

```python
class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
        'http://www.example.com/1.html',
        'http://www.example.com/2.html',
        'http://www.example.com/3.html',
    ]

    def parse(self, response):
        sel = scrapy.Selector(response) # 构造选择器
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse) # 回调函数指定为parse
```

#### start_requests函数

```python
class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']

    def start_requests(self): # 该函数用于构造Request对象
        yield scrapy.Request('http://www.example.com/1.html', self.parse)
        yield scrapy.Request('http://www.example.com/2.html', self.parse)
        yield scrapy.Request('http://www.example.com/3.html', self.parse)

    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
```

## 选择器

当抓取网页时，你做的最常见的任务是从HTML源码中提取数据。现有的一些库可以达到这个目的：

* BeautifulSoup是在程序员间非常流行的网页分析库,它基于HTML代码的结构来构造一个Python对象,对不良标记的处理也非常合理，但它有一个缺点：慢。
* lxml 是一个基于 ElementTree (不是Python标准库的一部分)的python化的XML解析库(也可以解析HTML)。

Scrapy提取数据有自己的一套机制。它们被称作选择器(seletors)，因为他们通过特定的 XPath 或者 CSS 表达式来“选择” HTML文件中的某个部分

### 直接使用

Selector 是一个可以独立使用的模块。我们可以直接利用 Selector 这个类来构建一个选择器对象，然后调用它的相关方法如 xpath()、css() 等来提取数据

```python
body = '<html><head><title>Hello World</title></head><body></body></html>'
selector = scrapy.Selector(text=body)
title = selector.xpath('//title/text()').extract_first()
print(title)
```

### scrapy shell

由于 Selector 主要是与 Scrapy 结合使用，如 Scrapy 的回调函数中的参数 response 直接调用 xpath() 或者 css() 方法来提取数据，所以在这里我们借助 Scrapy shell 来模拟 Scrapy 请求的过程，来讲解相关的提取方法

在命令行输入以下代码:
```bash
scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
```
我们就进入到 Scrapy shell 模式。这个过程其实是，Scrapy 发起了一次请求，请求的 URL 就是刚才命令行下输入的 URL，然后把一些可操作的变量传递给我们，如 request、response 等

该网页的源代码如下:
```html
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
  </div>
 </body>
</html>
```

#### xpath选择器

response 有一个属性 selector，我们调用 **response.selector** 返回的内容就相当于用 response 的 text 构造了一个 Selector 对象。通过这个 Selector 对象我们可以调用解析方法如 xpath()、css() 等，通过向方法传入 XPath 或 CSS 选择器参数就可以实现信息的提取

```bash
response.selector.xpath('//a')
[<Selector query='//a' data='<a href="image1.html">Name: My image ...'>,
 <Selector query='//a' data='<a href="image2.html">Name: My image ...'>,
 <Selector query='//a' data='<a href="image3.html">Name: My image ...'>,
 <Selector query='//a' data='<a href="image4.html">Name: My image ...'>,
 <Selector query='//a' data='<a href="image5.html">Name: My image ...'>]
 ```

#### CSS 选择器

使用 response.css() 方法可以使用 CSS 选择器来选择对应的元素

```bash
response.css('a')
[<Selector xpath='descendant-or-self::a' data='<a href="image1.html">Name: My image 1 <'>, 
<Selector xpath='descendant-or-self::a' data='<a href="image2.html">Name: My image 2 <'>, 
<Selector xpath='descendant-or-self::a' data='<a href="image3.html">Name: My image 3 <'>, 
<Selector xpath='descendant-or-self::a' data='<a href="image4.html">Name: My image 4 <'>, 
<Selector xpath='descendant-or-self::a' data='<a href="image5.html">Name: My image 5 <'>]
```

#### 正则表达式

Scrapy 的选择器还支持正则匹配

```bash
response.xpath('//a/text()').re('Name:\s(.*)')
['My image 1 ', 'My image 2 ', 'My image 3 ', 'My image 4 ', 'My image 5 ']
```

## Downloader Middleware

Downloader Middleware 即下载中间件，它是处于 Scrapy 的 Request 和 Response 之间的处理模块。

Scheduler 从队列中拿出一个 Request 发送给 Downloader 执行下载，这个过程会经过 Downloader Middleware 的处理。另外，当 Downloader 将 Request 下载完成得到 Response 返回给 Spider 时会再次经过 Downloader Middleware 处理

也就是说，Downloader Middleware 在整个架构中起作用的位置是以下两个:

* 在 Scheduler 调度出队列的 Request 发送给 Downloader 下载之前，也就是我们可以在 Request 执行下载之前对其进行修改。
* 在下载后生成的 Response 发送给 Spider 之前，也就是我们可以在生成 Resposne 被 Spider 解析之前对其进行修改。

Downloader Middleware 的功能十分强大，**修改 User-Agent、处理重定向、设置代理、失败重试、设置 Cookies** 等功能都需要借助它来实现

### 使用说明

Scrapy 其实已经提供了许多 Downloader Middleware，比如负责失败重试、自动重定向等功能的 Middleware，它们被 DOWNLOADER_MIDDLEWARES_BASE 变量所定义

```python
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}
```

这是一个字典格式，字典的键名是 Scrapy 内置的 Downloader Middleware 的名称，键值代表了调用的优先级，优先级是一个数字，数字越小代表越靠近 Scrapy 引擎，数字越大代表越靠近 Downloader。每个 Downloader Middleware 都可以定义 process_request() 和 request_response() 方法来分别处理请求和响应，对于 process_request() 方法来说，优先级数字越小越先被调用，对于 process_response() 方法来说，优先级数字越大越先被调用

### 核心方法

Scrapy 内置的 Downloader Middleware 为 Scrapy 提供了基础的功能，但在项目实战中我们往往需要单独定义 Downloader Middleware。不用担心，这个过程非常简单，我们只需要实现某几个方法即可

每个 Downloader Middleware 都定义了一个或多个方法的类，核心的方法有如下三个:
* **process_request(request, spider)**
* **process_response(request, response, spider)**
* **process_exception(request, exception, spider)**

#### process_request

Request 被 Scrapy 引擎调度给 Downloader 之前，process_request() 方法就会被调用，也就是在 Request 从队列里调度出来到 Downloader 下载执行之前，我们都可以用 process_request() 方法对 Request 进行处理。方法的返回值必须为 None、Response 对象、Request 对象之一，或者抛出 IgnoreRequest 异常。

process_request() 方法的参数有如下两个:
* request，即 Request 对象，即被处理的 Request
* spider，即 Spdier 对象，即此 Request 对应的 Spider

返回类型不同，产生的效果也不同。下面归纳一下不同的返回情况:

* 当返回是 None 时，Scrapy 将继续处理该 Request，接着执行其他 Downloader Middleware 的 process_request() 方法，一直到 Downloader 把 Request 执行后得到 Response 才结束。这个过程其实就是修改 Request 的过程，不同的 Downloader Middleware 按照设置的优先级顺序依次对 Request 进行修改，最后送至 Downloader 执行
* 当返回为 Response 对象时，更低优先级的 Downloader Middleware 的 process_request() 和 process_exception() 方法就不会被继续调用，每个 Downloader Middleware 的 process_response() 方法转而被依次调用。调用完毕之后，直接将 Response 对象发送给 Spider 来处理
* 当返回为 Request 对象时，更低优先级的 Downloader Middleware 的 process_request() 方法会停止执行。这个 Request 会重新放到调度队列里，其实它就是一个全新的 Request，等待被调度。如果被 Scheduler 调度了，那么所有的 Downloader Middleware 的 process_request() 方法会被重新按照顺序执行。
如果 IgnoreRequest 异常抛出，则所有的 Downloader Middleware 的 process_exception() 方法会依次执行。如果没有一个方法处理这个异常，那么 Request 的 errorback() 方法就会回调。如果该异常还没有被处理，那么它便会被忽略

#### process_response

Downloader 执行 Request 下载之后，会得到对应的 Response。Scrapy 引擎便会将 Response 发送给 Spider 进行解析。在发送之前，我们都可以用 process_response() 方法来对 Response 进行处理。方法的返回值必须为 Request 对象、Response 对象之一，或者抛出 IgnoreRequest 异常。

process_response() 方法的参数有如下三个:
* request，是 Request 对象，即此 Response 对应的 Request。
* response，是 Response 对象，即此被处理的 Response。
* spider，是 Spider 对象，即此 Response 对应的 Spider。

下面对不同的返回情况做一下归纳：
* 当返回为 Request 对象时，更低优先级的 Downloader Middleware 的 process_response() 方法不会继续调用。该 Request 对象会重新放到调度队列里等待被调度，它相当于一个全新的 Request。然后，该 Request 会被 process_request() 方法顺次处理。
* 当返回为 Response 对象时，更低优先级的 Downloader Middleware 的 process_response() 方法会继续调用，继续对该 Response 对象进行处理。
* 如果 IgnoreRequest 异常抛出，则 Request 的 errorback() 方法会回调。如果该异常还没有被处理，那么它便会被忽略。

#### process_exception

当 Downloader 或 process_request() 方法抛出异常时，例如抛出 IgnoreRequest 异常，process_exception() 方法就会被调用。方法的返回值必须为 None、Response 对象、Request 对象之一。

process_exception() 方法的参数有如下三个:
* request，即 Request 对象，即产生异常的 Request
* exception，即 Exception 对象，即抛出的异常
* spider，即 Spider 对象，即 Request 对应的 Spider

下面归纳一下不同的返回值:
* 当返回为 None 时，更低优先级的 Downloader Middleware 的 process_exception() 会被继续顺次调用，直到所有的方法都被调度完毕。
* 当返回为 Response 对象时，更低优先级的 Downloader Middleware 的 process_exception() 方法不再被继续调用，每个 Downloader Middleware 的 process_response() 方法转而被依次调用。
* 当返回为 Request 对象时，更低优先级的 Downloader Middleware 的 process_exception() 也不再被继续调用，该 Request 对象会重新放到调度队列里面等待被调度，它相当于一个全新的 Request。然后，该 Request 又会被 process_request() 方法顺次处理

### 设置请求头


1. 第一种方法非常简单，我们只需要在 setting.py 里面加一行 USER_AGENT 的定义即可
```python
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
```
一般推荐使用此方法来设置。但是如果想设置得更灵活，比如设置随机的 User-Agent，那就需要借助 Downloader Middleware 了

2. 在 middlewares.py 里面添加一个 RandomUserAgentMiddleware 的类
```python
import random

class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agents = ['Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1'
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
```

不过，要使之生效我们还需要再去调用这个 Downloader Middleware。在 settings.py 中，将 DOWNLOADER_MIDDLEWARES 取消注释，并设置成如下内容:
```python
DOWNLOADER_MIDDLEWARES = {'scrapydownloadertest.middlewares.RandomUserAgentMiddleware': 543}
```

## Spider Middleware

Spider Middleware 是介入到 Scrapy 的 Spider 处理机制的钩子框架

当 Downloader 生成 Response 之后，Response 会被发送给 Spider，在发送给 Spider 之前，Response 会首先经过 Spider Middleware 处理，当 Spider 处理生成 Item 和 Request 之后，Item 和 Request 还会经过 Spider Middleware 的处理。

Spider Middleware 有如下三个作用:
* 我们可以在 Downloader 生成的 Response 发送给 Spider 之前，也就是在 Response 发送给 Spider 之前对 Response 进行处理。
* 我们可以在 Spider 生成的 Request 发送给 Scheduler 之前，也就是在 Request 发送给 Scheduler 之前对 Request 进行处理。
* 我们可以在 Spider 生成的 Item 发送给 Item Pipeline 之前，也就是在 Item 发送给 Item Pipeline 之前对 Item 进行处理。

### 使用说明

Scrapy 其实已经提供了许多 Spider Middleware，它们被 SPIDER_MIDDLEWARES_BASE 这个变量所定义

```python
{
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}
```

和 Downloader Middleware 一样，Spider Middleware 首先加入到 SPIDER_MIDDLEWARES 设置中，该设置会和 Scrapy 中 SPIDER_MIDDLEWARES_BASE 定义的 Spider Middleware 合并。然后根据键值的数字优先级排序，得到一个有序列表。第一个 Middleware 是最靠近引擎的，最后一个 Middleware 是最靠近 Spider 的

### 核心方法

Scrapy 内置的 Spider Middleware 为 Scrapy 提供了基础的功能。如果我们想要扩展其功能，只需要实现某几个方法即可。

每个 Spider Middleware 都定义了以下一个或多个方法的类，核心方法有如下 4 个:
* process_spider_input(response, spider)
* process_spider_output(response, result, spider)
* process_spider_exception(response, exception, spider)
* process_start_requests(start_requests, spider)

#### process_spider_input(response, spider)

当 Response 通过 Spider Middleware 时，该方法被调用，处理该 Response。

方法的参数有两个：

* response，即 Response 对象，即被处理的 Response
* spider，即 Spider 对象，即该 response 对应的 Spider

process_spider_input() 应该返回 None 或者抛出一个异常。

* 如果其返回 None ，Scrapy 将会继续处理该 Response，调用所有其他的 Spider Middleware 直到 Spider 处理该 Response。
* 如果其抛出一个异常，Scrapy 将不会调用任何其他 Spider Middlewar e 的 process_spider_input() 方法，并调用 Request 的 errback() 方法。 errback 的输出将会以另一个方向被重新输入到中间件中，使用 process_spider_output() 方法来处理，当其抛出异常时则调用 process_spider_exception() 来处理。

#### process_spider_output(response, result, spider)

当 Spider 处理 Response 返回结果时，该方法被调用。

方法的参数有三个：

* response，即 Response 对象，即生成该输出的 Response
* result，包含 Request 或 Item 对象的可迭代对象，即 Spider 返回的结果
* spider，即 Spider 对象，即其结果对应的 Spider

process_spider_output() 必须返回包含 Request 或 Item 对象的可迭代对象

#### process_spider_exception(response, exception, spider)

当 Spider 或 Spider Middleware 的 process_spider_input() 方法抛出异常时， 该方法被调用。

方法的参数有三个：

* response，即 Response 对象，即异常被抛出时被处理的 Response
* exception，即 Exception 对象，被抛出的异常
* spider，即 Spider 对象，即抛出该异常的 Spider

process_spider_exception() 必须要么返回 None ， 要么返回一个包含 Response 或 Item 对象的可迭代对象。

* 如果其返回 None ，Scrapy 将继续处理该异常，调用其他 Spider Middleware 中的 process_spider_exception() 方法，直到所有 Spider Middleware 都被调用。
* 如果其返回一个可迭代对象，则其他 Spider Middleware 的 process_spider_output() 方法被调用， 其他的 process_spider_exception() 将不会被调用

#### process_start_requests(start_requests, spider)

该方法以 Spider 启动的 Request 为参数被调用，执行的过程类似于 process_spider_output() ，只不过其没有相关联的 Response 并且必须返回 Request。

方法的参数有两个：

* start_requests，即包含 Request 的可迭代对象，即 Start Requests
* spider，即 Spider 对象，即 Start Requests 所属的 Spider

其必须返回另一个包含 Request 对象的可迭代对象

## Item Pipeline

当 Spider 解析完 Response 之后，Item 就会传递到 Item Pipeline，被定义的 Item Pipeline 组件会顺次调用，完成一连串的处理过程，比如数据清洗、存储等。

它的主要功能有：

* 清洗 HTML 数据
* 验证爬取数据，检查爬取字段
* 查重并丢弃重复内容
* 将爬取结果储存到数据库

### 核心方法

我们可以自定义 Item Pipeline，只需要实现指定的方法就好，其中必须要实现的一个方法是：

* process_item(item, spider)

另外还有几个比较实用的方法，它们分别是：
* open_spider(spider)
* close_spider(spider)
* from_crawler(cls, crawler)

#### process_item(item, spider)

process_item() 是必须要实现的方法，被定义的 Item Pipeline 会默认调用这个方法对 Item 进行处理。比如，我们可以进行数据处理或者将数据写入到数据库等操作。它必须返回 Item 类型的值或者抛出一个 DropItem 异常。

process_item() 方法的参数有如下两个。

* item，是 Item 对象，即被处理的 Item
* spider，是 Spider 对象，即生成该 Item 的 Spider

下面对该方法的返回类型归纳如下：

* 如果返回的是 Item 对象，那么此 Item 会接着被低优先级的 Item Pipeline 的 process_item() 方法进行处理，直到所有的方法被调用完毕。
* 如果抛出的是 DropItem 异常，那么此 Item 就会被丢弃，不再进行处理

#### open_spider(self, spider)

open_spider() 方法是在Spider开启的时候被自动调用的，在这里我们可以做一些初始化操作，如开启数据库连接等。其中参数 spider 就是被开启的 Spider 对象

#### close_spider(spider)

close_spider() 方法是在 Spider 关闭的时候自动调用的，在这里我们可以做一些收尾工作，如关闭数据库连接等，其中参数 spider 就是被关闭的 Spider 对象

#### from_crawler(cls, crawler)

from_crawler() 方法是一个类方法，用 @classmethod 标识，是一种依赖注入的方式。它的参数是 crawler，通过 crawler 对象，我们可以拿到 Scrapy 的所有核心组件，如全局配置的每个信息，然后创建一个 Pipeline 实例。参数 cls 就是 Class，最后返回一个 Class 实例

### 将数据保存至EXCEL表格或MySQL数据库

在settings.py中设置:
```python
ITEM_PIPELINES = {
   "scrapyspider.pipelines.ExcelPipeline": 300, # 数字越大越先调用
   "scrapyspider.pipelines.MySQLPipeline": 200,
}
```

pipelines.py的内容如下:

```python
class ExcelPipeline:

    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        # self.ws = self.wb.create_sheet('top250')
        self.ws.append(("标题", "评分", "简介"))

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        self.ws.append((title, rank, subject))
        return item

    def close_spider(self, spider):
        self.wb.save("电影数据.xlsx")
```

```python
class MySQLPipeline:
    def __init__(self):
        self.db = pymysql.connect(user="root", password="your_password", host="localhost", 
                                    port=3306, db='experiment', autocommit=True)
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        title = item.get('title', '')
        rank = item.get('rank', '')
        subject = item.get('subject', '')
        self.cur.execute("insert into douban(title, rank, subject) values (%s, %s, %s)", (title, rank, subject))
        return item

    def close_spider(self, spider):
        self.db.close()
```

## 命令行工具

Scrapy提供了两种类型的命令。
* 一种必须在Scrapy项目中运行(针对项目(Project-specific)的命令)
    * crawl、check、list、edit、parse、genspider、bench
* 另外一种则不需要(全局命令)。全局命令在项目中运行时的表现可能会与在非项目中运行有些许差别(因为可能会使用项目的设定)
    * startproject、settings、runspider、shell、fetch、view、version
    
下面介绍一些常用的命令

### 创建项目(全局命令)

一般来说，使用 scrapy 工具的第一件事就是创建您的Scrapy项目:
```bash
scrapy startproject <project_name>
```
在 project_name 文件夹下创建一个名为 project_name 的Scrapy项目

### 创建spider(项目命令)

可以在您的项目中使用 scrapy 工具来对其进行控制和管理
```bash
scrapy genspider mydomain mydomain.com
```
这仅仅是创建spider的一种快捷方法。该方法可以使用提前定义好的模板来生成spider。您也可以自己创建spider的源码文件

### crawl(项目命令)

crawl命令可以启动spider进行爬取
```bash
scrapy crawl myspider
```
Scrapy内置了CSV、JSON、XML等文件的保存，只需要通过 -o 参数即可保存文件

```bash
scrapy crawl myspider -o spider.csv
scrapy crawl myspider -o spider.json
scrapy crawl myspider -o spider.xml
```

### list(项目命令)

列出当前项目中所有可用的spider。每行输出一个spider
```bash
scrapy list
```

### shell(全局命令)

以给定的URL(如果给出)或者空(没有给出URL)启动Scrapy shell
```bash
scrapy shell
```

### parse(项目命令)

获取给定的URL并使用相应的spider分析处理。如果您提供 --callback 选项，则使用spider的该方法处理，否则使用 parse
```bash
scrapy parse url
```

### version(全局命令)

输出Scrapy版本。配合 -v 运行时，该命令同时输出Python, Twisted以及平台的信息，方便bug提交。
```bash
scrapy version
```