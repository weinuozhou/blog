# 动态渲染网页的爬取

* 我们了解Ajax的分析和爬取方式，这其实也是一种javascript动态渲染的页面，通过直接分析Ajax，可以直接借助requests来实现数据爬取
* 然而，javascript动态渲染的方式不止Ajax这一招，比如中国青年网(http://news.youth.cn/gn/ ) ,并不含Ajax请求，又比如淘宝这种页面，它虽然是Ajax请求的数据，但Ajax接口含有很多加密参数，很难发现其中的规律
* 因此，为了解决这些问题，我们可以用模拟浏览器运行的库，这样就不用管网页内部的javascript是如何渲染页面的了，常见的库有`selenium`、`splash`、`PyV8`、`Ghost`,`playwright`等等

## `selenium`的基本使用

`selenium`是一种自动化测试工具，利用它可以驱动浏览器执行特定的动作，如点击、下拉等操作。同时还可以获取浏览器当前呈现的网页源代码，做到**可见即可爬**

### 声明浏览器对象

* `selenium`支持很多浏览器对象，如chrome、FireFox、Edge等,另外也支持手机端浏览器和无界面浏览器
* 可以通过`close`方法来关闭浏览器对象

```python
from selenium import webdriver

browser = webdriver.Chrome() # 初始化Chrome浏览器
browser.close()  # 关闭浏览器
```

### 为浏览器对象添加相关配置

```python
from selenium import webdriver

# 为浏览器对象添加相关配置，可在一定程度上避免检测
def create_chrome(*, headless=None):
    """
    :param headless:是否设置无头浏览器(默认否)
    :return: 浏览器对象
    """
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options)
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source':'Object.defineProperty(navigator, "webdriver",{get:() => undefined})'}
                           )
    return browser
```

### 窗口操作

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window() # 最大化窗口
time.sleep(2)
browser.fullscreen_window() # 全屏
time.sleep(2)
browser.close()
```

### 请求网页

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com') # 只需要传入参数url即
time.sleep(2)
browser.close()
```

### 屏幕截图

```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()
time.sleep(2)
browser.get('https://www.baidu.com')
browser.save_screenshot('baidu.png') # 只支持png格式的图片
time.sleep(2)
browser.close()  
```

### 查找节点

当我们对浏览器进行**点击、输入**等操作时，需要找到该容器对应的节点,可以通过以下方法来查找节点:
* xpath定位
* id、class、CSS选择器

```python
from webdriver import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 查找百度网址的搜索框
input_id = browser.find_element(By.ID,'kw')
input_class = browser.find_element(By.CLASS_NAME,'s_ipt')
input_CSS = browser.find_element(By.CSS_SELECTOR,'#kw')
input_xpath = browser.find_element(By.XPATH,'//input[@id="kw"]')
print([input_id,input_class,input_CSS,input_xpath])
browser.close()
# 需要传入两个参数:查找方式By和值
# 返回值是 WebElement 类型
```

### 节点交互

#### 点击和输入

`slenium`可以模拟浏览器进行操作，比较常见的用法有点击、输入和清空文字
* 点击:`click()`
* 输入:`send_keys()`
* 清空:`clear()`

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 查找百度网址的搜索框
input_id = browser.find_element(By.ID, 'kw')
# 查找搜索按钮的节点
search = browser.find_element(By.ID, 'su')
# 在搜索框内输入python
input_id.send_keys('python')
# 点击搜索按钮
search.click()
time.sleep(1)
browser.close()
```

#### 下拉操作

`selenium`没有对应的API来模拟鼠标向下滚动的操作，但是可以通过执行js代码来实现
```python
browser.execute_script(js)
```
* 常见的js代码如下:
    * `js = "window.scrollTo(0,0)"`:滑动至顶部
    * `js = "window.scrollTo(0, document.body.scrollHeight)"`:滑动至底部
    * `js = "window.scrollTo(x, y)"`:x控制左右,y控制上下,单位为像素

##### 滑动至底部

```python
from selenium import wendriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(2)
browser.find_element(By.ID, 'kw').send_keys('python')
browser.find_element(By.ID, 'su').click()
time.sleep(2)
# 模拟鼠标滚轮，滑动至页面底部
js = "window.scrollTo(0, document.body.scrollHeight)"
browser.execute_script(js)
time.sleep(2)
browser.close()
```

##### 滑动至顶部

```python
from selenium import wendriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(2)
browser.find_element(By.ID,'kw').send_keys('python')
browser.find_element(By.ID,'su').click()
time.sleep(2)
# 模拟鼠标滚轮，滑动至页面底部
js = "window.scrollTo(0, document.body.scrollHeight)"
browser.execute_script(js)
time.sleep(2)
# 模拟鼠标滚轮，滑动至页面顶部
js = "window.scrollTo(0, 0)"
browser.execute_script(js)
time.sleep(2)
browser.close()
```

##### 滑动至目标元素可见

```python
from selenium import wendriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
time.sleep(2)
browser.find_element(By.ID, 'kw').send_keys('python')
browser.find_element(By.ID, 'su').click()
time.sleep(2)
element = browser.find_element(By.ID, 'lg')
js = "arguments[0].scrollIntoView();"
browser.execute_script(js, element)
time.sleep(2)
browser.close()
```

### 获取节点信息

#### 获取网页源代码

`page_source`属性可以获取网页的源代码

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()
```

#### 获取属性

`get_attribute()`方法可以获取节点的属性

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 查找百度网址的搜索框
input_id = browser.find_element(By.ID,'kw')
# 获取该搜索框的class属性
print(input_id.get_attribute('class'))
browser.close()
```

#### 获取文本

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 查找百度热搜
hot_questions = browser.find_elements(By.CLASS_NAME, 'title-content-title')
for question in hot_questions:
    print(question.text)
browser.close()
```

#### 获取位置、标签名和大小

* `location`属性可以获取该节点在页面中的相对位置
* `tag_name`属性可以获取标签名称
* `size`属性可以获取节点的大小(宽高)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 查找百度网址的搜索框
input_id = browser.find_element(By.ID,'kw')
print(input_id.location)
print(input_id.tag_name)
print(input_id.size)
browser.close()
```

#### 获取`cookies`

`get_cookies()`方法可以获取当前页面的所有`cookies`

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.get_cookies())
browser.close()
```

### 延时等待

在`selenium`中，`get()`方法会在**网页框架加载结束后执行**，此时获取网页源代码，可能不是浏览器完全加载的页面，所以需要延时等待一段时间，确保节点已经加载出来

#### 隐式等待

* 使用隐式等待时，如果`selenium`没有在DOM找到节点，将继续等待，超过设定等待时间后，则抛出找不到节点的异常
* 即查找节点时如果节点没有出现，则隐式等待一段时间再查找，默认等待时间是0
```python
implicitly.wait() # 参数为时间，单位为s
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.baidu.com')
# 查找百度网址的搜索框
input_id = browser.find_element(By.ID,'kw')
print(input_id)
browser.close()
```

#### 显式等待

* 隐式等待的效果可能并不是这么好，因为只规定了固定等待时间，而页面加载的时间会受网络条件的影响
* 显式等待可以指定要查找的节点，然后指定一个最长等待时间，如果规定时间内该节点加载出来了，则返回查找的节点，否则抛出超时异常

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome() # 初始化浏览器对象
wait = WebDriverWait(browser,10)# 指定最长等待时间
wait.util(EC.expected_conditions)# 传入等待条件
```

* 常见的等待条件如下

|       ecpected_conditions       | describe                                       |
| :-----------------------------: | :--------------------------------------------- |
|            title_is             | 标题是某内容                                   |
|   presence_of_element_located   | 节点加载出来，需要传入定位元组，如(By.id,'kw') |
|  visibility_of_element_located  | 节点可见,传入定位元组                          |
| presence_of_all_element_located | 所有节点加载出来                               |
|     element_to_be_clickable     | 节点可点击                                     |

* 更多的等待条件及用法可以参考:[官方文档](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()  # 初始化浏览器对象
wait = WebDriverWait(browser, 10) # 指定最长等待时间
browser.get('https://www.baidu.com')
# 显式等待查找百度网址的输入框
input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
# 显示等待查找搜索框
search = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
print(input,search)
browser.close()
```

### 前进和后退

```python
from selenium import webdriver

browser = webdriver.Chrome()
# 访问百度
browser.get('https://www.baidu.com/')
time.sleep(5)
# 访问淘宝官网
browser.get('https://www.taobao.com/')
time.sleep(5)
# 网页后退
browser.back()
# 网页刷新
browser.refresh()
browser.close()
```

### 无界面模式

`selenium`开始支持Headless模式，这样爬取的时候就**不会弹出浏览器**

```python
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options = chrome_options)
```

##  利用`selenium`自动化爬取京东商品信息

这里直接上代码，就不一一讲解了

```python
import os
import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 初始化浏览器对象
browser = webdriver.Chrome()
# 指定最长等待时间
wait = WebDriverWait(browser, 10)
url = 'https://www.jd.com/' 
# 搜索关键字
KEYWORD = 'ipad'
def index_page(page):
    # 异常处理
    try:
        browser.get(url) # 请求网页
        wait.until(EC.presence_of_element_located((By.ID,'key'))).send_keys(KEYWORD) # 查找输入框并输入关键字
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button'))).click()# 查找搜索框并点击搜索
        # 判断商品信息是否加载完成,加载完成则保存信息并且查找下一页
        for i in range(page):
            print(f'正在爬取第{i}页')
            # 判断商品信息是否加载完成
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_goodsList > ul')))
            yield get_products() # 通过生成器对象返回
            # 点击下一页，进行下一页的爬取
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pn-next'))).click() 
    # 处理网络超时异常，这里采取重复请求网页的形式
    except TimeoutException:
        index_page()
# 通过xpath定位获取所需要的数据
def get_products():
    html = browser.page_source # 获取网页源代码
    parse_html = etree.HTML(html)
    items = parse_html.xpath('//li[@class="gl-item"]')
    for item in items:
        links = item.xpath('./div[1]/div[1]/a/@href')
        product_link = ['https:'+ link for link in links]
        product_price = item.xpath('./div[1]/div[3]/strong/i/text()')
        product_name = item.xpath('./div[1]/div[4]/a/em/text()')
        product_rating = item.xpath('./div[1]/div[5]/strong/a/text()')
        product_shop = item.xpath('./div[1]/div[7]/span/a/text()')
        yield {
            '商品链接': product_link,
            '商品名称': product_name,
            '店铺': product_shop,
            '商品价格': product_price,
            '评价人数': product_rating
        }     
def save_to_file(data):
    filename = 'data/jd/'
    if not os.path.exists(filename):
        os.makedirs(filename)
    with open(filename + 'jd.json','a',encoding='utf-8') as f:
        f.write(json.dumps(data,indent = 4,ensure_ascii=False))
def main():
    for product_generator in index_page(2):
        for product in product_generator:
            print(product)
            save_to_file(product)
if __name__ == '__main__':
    main()
```





