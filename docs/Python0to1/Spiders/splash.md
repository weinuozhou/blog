# `Splash`

Lua脚本语法可以参考: [http://www.runoob.com/lua/lua-basic-syntax.html](https://www.runoob.com/lua/lua-basic-syntax.html)

Splash是一个**javascript渲染服务**。它是一个带有HTTP API的轻量级Web浏览器，splash的主要功能:
* 并行处理多个网页
* 获取HTML源代码或截取屏幕截图
* 关闭图像或使用Adblock Plus规则使渲染更快
* 在页面上下文中执行自定义JavaScript
* 可通过Lua脚本来控制页面的渲染过程
* 在 Splash-Jupyter 笔记本中开发 Splash Lua脚本
* 以HAR格式获取详细的渲染信息

## `Splash`的安装

`splash` 的安装必须基于**docker容器**。所以首先需要安装 `docker` 容器

docker官方网址: [https://www.docker.com/get-started](https://www.docker.com/get-started)

安装好 `docker` 之后, 执行命令 `docker pull scrapinghub/splash`, 它会自动拉取镜像

接下来执行命令 `docker run -p 8050:8050 scrapinghub/splash`, 它会运行splash服务

谷歌浏览器中输入 `https://localhost:8050` 有如下界面说明安装成功

<div style="text-align: center;"><img alt='202404052012595' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404052012595.png' width=500px> </div>

假如你的Lua脚本编辑区域无法显示(**可以通过打开F12开发者工具的console选项查看渲染失败原因**)，可能的原因是无法加载网页静态资源,这里可以下载[Watt Toolkit](https://steampp.net/)开启加速服务即可


## `Splash`的基本使用

上面有个输入框(输入需要渲染的网址)，默认是[http://google.com](http://www.google.com)

我们可以换成想要渲染的网页如:[https://www.baidu.com](https:/www.baidu.com), 然后点击Render me按钮开始渲染，页面返回结果包括渲染截图、HAR加载统计数据、网页源代码

从HAR中可以看到，Splash执行了整个页面的渲染过程，包括CSS、JavaScript的加载等，通过返回结果可以看到它分别对应搜索框下面的脚本文件中return部分的三个返回值，html、png、har：

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
```
这个脚本是使用Lua语言写的，它首先使用 `go()` 方法加载页面， `wait()` 方法等待加载时间，然后返回源码、截图和HAR信息

现在我们修改下它的原脚本，访问[www.baidu.com](https://www.baidu.com) ,通过 `javascript` 脚本，让它返回title，然后执行：

```lua
function main(splash, args)
  splash:go("http://www.baidu.com")
  splash:wait(0.5)
  local title = splash:evaljs("document.title") -- 执行javascript脚本
  return {title = title} -- 返回值可以是字典、也可以是字符串
end
```

<div style="text-align: center;"><img alt='202404052023228' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404052023228.png' width=500px> </div>

在前面的例子中，main()方法的第一个参数是 `splash` ，这个对象它类似于 `selenium` 中的 `WebDriver` 对象，可以调用它的属性和方法来控制加载规程，下面介绍一些常用的属性：

### `splash`对象属性

#### args

该属性可以获取加载时配置的参数，例如url等等

```lua
function main(splash, args)
  splash:go("http://www.baidu.com")
  local url = args.url
  return {url = url}
end
```

#### resource_timeout

设置网络请求的默认超时，以秒为单位，如设置为0或 `nil` 则表示不检测网络超时: `splash.resource_timeout=nil`

#### splash.images_enabled

* 启用或禁用图片加载，默认情况下是加载的：`splash.images_enabled=true`
* 禁用该属性后，可以节省网络流量并提供网页加载速度，但是禁用可能会影响javascript渲染

```lua
function main(splash, args)
  splash.images_enabled=False
  splash:go("http://www.jd.com")
  return {png = splash:png()}
end
```

#### splash.scroll_position

这个属性主要用来控制页面上下、左右滚动

```lua
function main(splash, args)
  assert(splash:go(args.url))
  splash.scroll_position = {x=0, y=400}
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png(),
    har = splash:har(),
  }
end
```

### `splash`对象方法

#### go()

该方法用于请求某个链接，可以模拟get、post请求，同时支持传入请求头等

```lua
ok, reason = splash:go(url,baseurl=nil,http_method="GET",body=nil,formdata=nil)
-- url:请求的url
-- baseurl:资源加载的相对路径
-- http_method:请求的方法
-- 该方法的返回值是结果ok和原因reason
```

#### set_user_agent()

该方法可以用于设置网页的请求头

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
  return {
    html = splash:html()
  }
end
```

#### html()

该方法用于获取网页源代码,它是非常简单实用的方法

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html()
  }
end
```

#### png()

该方法可以获取png格式的网页截图

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    png = splash:png()
  }
end
```

#### har()

该方法可以获取网页加载的过程描述

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    har = splash:har()
  }
end
```

#### get_cookies()

该方法可以获取当前页面的Cookies

```lua
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    cookies = splash:get_cookies()
  }
end
```

#### evaljs()

该方法可以执行javascript代码并返回最后一条javascript语句的返回结果

```lua  
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    splash:evaljs("document.title")
  }
end
```

#### select() & send_text()

`select()`方法用于选择符合条件的第一个节点，如果有多个符合条件，只会返回第一个，其参数是CSS选择器

`send_text()`方法可以对指定的节点进行填写文本操作

```lua
function main(splash)
  splash:go("https://www.baidu.com/")
  input = splash:select("#kw")
  input:send_text('Splash')
  splash:wait(3)
  return splash:png()
end
```

#### mouse_click()

该方法可以模拟鼠标点击操作

```lua
function main(splash,args)
    splash:go("https://www.baidu.com")
    input = splash:select('#kw')
    input:send_text("python")
    splash:select("#su"):mouse_click()
    splash:wait(5)
    return splash:png()
end 
```

## `splash`的API调用

前面主要说明了一些Lua脚本的使用语法，但是这些脚本是在splash页面中测试运行的，如何才能和python程序结合使用并抓取javascript渲染过的页面呢?

`splash` 内置了一些接口,我们只需要调用这些接口即可使用

### render.html

此接口主要用于获取javascript渲染的页面的HTML代码，接口地址就是: [http://localhost:8050/render.html](http://localhost:8050/render.html)

具体的用法可以参考: [https://splash.readthedocs.io/en/stable/api.html#render-html](https://splash.readthedocs.io/en/stable/api.html#render-html)

```python
import requests
# 获取渲染后的淘宝网页并设置等待时间为0.5s和网络请求等待时间为10s
url = 'http://localhost:8050/render.html?url=http://www.taobao.com&wait=0.5&timeout=10'
html = requests.get(url).text
```

### render.png

此接口可以用来获取网页截图，可以通过width、weight来控制宽高等，它返回是png格式的图片二进制数据

```python
url = 'http://localhost:8050/render.png?url=http://www.taobao.com&wait=5&timeout=10&width=1000&height=800'
res = requests.get(url)
with open('taobao.png','wb') as f:
    f.write(res.content)
```

### render.har

此接口可以获取网页加载的HAR数据，它返回一个json格式的数据，其中包含页面加载过程中的HAR数据

```python
url = 'http://localhost:8050/render.har?url=http://www.taobao.com&wait=0.5&timeout=10'
har = requests.get(url).text
```

### render.json

此接口包含了前面接口的所有功能，返回结果是json格式的，可以传入html、png、har等参数

```python
url = 'http://localhost:8050/render.json?url=http://www.taobao.com&wait=0.5&timeout=10&html=1&png=1&har=1'
data = requests.get(url).content.decode('utf-8')
```

### execute

* render.html、render.png对于一般的javascript渲染页面是可以解决问题的，但是要实现一些交互式操作，就必须依赖execute接口
* 此接口可以用于实现与Lua脚本的对接

```python
from urllib.parse import quote
lua = '''
function main(splash, args)
  assert(splash:go('http://www.baidu.com'))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
    png = splash:png()
  }
end
'''
url = 'http://localhost:8050/execute?lua_source='+ quote(lua)
res = requests.get(url)
```










