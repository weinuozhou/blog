# Ajax数据爬取

Ajax: 全称为 Asynchronous JavaScript and XML , 即异步的 JavaScript XML 它不是一门编程语言, 而是利用 JavaScript 在保证**页面不被刷新**、**页面链接不改变**的情况下与**服务器交换数据并更新部分网页**的技术。对于传统的网页, 如果想更新其内容, 那么必须要刷新整个页面, 但有了 Ajax , 便可以在页面不被全部刷新的情况下更新其内容 在这个过程中, 页面实际上是在后台与服务器进行了数据交互, 获取到数据之后, 再利用 JavaScript改变网页, 这样网页内容就会更新了。

## 实例引入

- 我们以CSDN为例子, 点击Python, 我们向下拉取页面, 数据会不断的更新有新的内容, 这就是Ajax。
- 我们注意到页面其实并没有整个刷新, 也就意味着页面的链接没有变化, 但是网页中却多了新内容, 也就是后面刷出来的新微博, 这就是通过Ajax获取新数据呈现的过程

```python
url = 'https://blog.csdn.net/nav/python'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}

response = requests.get(url,headers=headers)
print(response.text)
```

## Ajax分析方法

我们以前面的头条网站为例, 知道刷新的内容由Ajax加载, 而且也没的URL没有变化, 那么应该到哪里去看这些Ajax请求呢？

1. 右键点击检查并点击NetWork
2. 点击Fetch/XHR
3. 向下滑动, 会有一条条XHR数据更新, 这样我们就可以捕获到所有的 Ajax 请求了

<div style="text-align: center;"><img alt='202403212105109' src='https://cdn.jsdelivr.net/gh/weno861/image/img/202403212105109.png' width=500px> </div>