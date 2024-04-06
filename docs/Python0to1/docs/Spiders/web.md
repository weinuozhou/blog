# web 相关技术

网页可以分为三大部分：**HTML**、**CSS** 和 **JavaScript**。如果把网页比作一个人的话，HTML 相当于骨架，JavaScript 相当于肌肉，CSS 相当于皮肤，三者结合起来才能形成一个完善的网页。下面我们分别来介绍一下这三部分的功能

## HTML

HTML 是用来描述网页的一种语言，其全称叫作 Hyper Text Markup Language，即超文本标记语言。网页包括文字、按钮、图片和视频等各种复杂的元素，其基础架构就是 HTML。不同类型的元素通过不同类型的标签来表示，如图片用 img 标签表示，视频用 video 标签表示，段落用 p 标签表示，它们之间的布局又常通过布局标签 div 嵌套组合而成，各种标签通过不同的排列和嵌套才形成了网页的框架

* 超文本(Hypertext)：使用**超链接**的方法，把文字和图片信息相互联结，形成具有相关信息的体系。
* 标记语言：在文档内使用标记标签（Markup Tag）来定义页面内容的语言

### HTML基本标签

* \<html\>：文件开始标签，表示该文件是以超文本标识语言（HTML）编写的
* \<head\>：文件头部标签
* \<body\>：页面的主体标签
* \<title\>：文件标题标签，表示该网页的名称
* \<meta\>：元信息标签，提供关于HTML文档的元数据，一般用来定义页面信息的名称、关键字、作者、字符编码、关键词、页面描述、最后修改时间等,meta标签提供的信息是用户不可见的，不显示在页面中，不需要设置结束标签
* \<base\>：用来指定页面中所有超链接的基准路径
* \<link\>：用于链接外部css样式表等其他相关外部资源
* \<p\>：定义段落
* \<a\>：定义超链接，用于从一张页面链接到另一张页面，其最重要的属性是href，它指示链接的目标
  * target属性
    * _self：默认值，在相同的框架或者当前窗口中打开链接
    * _blank:在一个新的窗口中打开链接
    * _parent：在上一层窗口中打开链接
    * _top：会清除所有被包含的框架，并打开链接
* \<img\>：向网页中嵌入一幅图像，没有结束标签
  * src属性:规定显示图像的URL
  * alt属性:规定在图像无法显示时的提示信息
* \<ul\>：无序列表标签
* \<ol\>：有序列表标签
* \<li\>：表示无序列表的每一项，用于包含每一行的内容
* \<table\>：定义页面的表格
* \<div\>：用来定义文档中的分区或节
* \<form\>：可以把用户输入的数据传送到服务器端，这样服务器端程序就可以处理表单传过来的数据
* \<script\>：用于在html页面内插入脚本。其type属性为必选的属性，用来指示脚本的MIME 类型

其他的html标签含义可见:[HTML标签参考手册](https://www.w3school.com.cn/tags/index.asp)

<div style="text-align: center;"><img alt='202404012233182' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404012233182.png' width=500px> </div>

## CSS

层叠样式表单(Cascading Style Sheet)是一种标记语言，用于为HTML文档定义布局。CSS涉及字体、颜色、边距、高度、宽度、背景图像、高级定位等方面

* **内联样式**：在相关的标签中使用样式属性，当特殊的样式需要应用到个别元素时可以使用；样式属性可以是任何CSS属性，主要使用的属性为style。例如：`<p style="color:blue">This is a paragraph.</p>` 设置段落颜色。
* **内部样式表**：头部通过标签(\<style\>)定义内部样式表
* **外部引用**：当样式需要被很多页面引用时，可以使用独立的外部CSS文件，这样可以简单页面模式的设计

### CSS选择器

* 属性选择器: `[color=red]{color:red}`
* 类选择器: `.classname {color:red}`
* id选择器: `#idname {color: red}`

有关css样式可以参数[CSS参考手册](https://www.w3school.com.cn/cssref/index.asp)

## JavaScript

* JavaScript是一种可以**嵌入在HTML**代码中由客户端浏览器运行的脚本语言
* 在页面中直接嵌入JavaScript代码
  * `<script type="text/javascript">document.write("Hello World!")</script>`
* 链接外部JavaScript文件
  * `<script language="javascript" src=“your-Javascript.js”></script>`

有关 JavaScript 的教程可以参考[JavaScript入门教程](https://www.w3school.com.cn/js/index.asp)

## Web页面类型

* **静态页面**：以html文件的形式存在于Web服务器的硬盘上；内容和最终显示效果是事先设计好的
* **动态页面**
  * 具有明显交互性，一般需要数据库等其他计算、存储服务的支持。
  * 页面内容是可变的，不同人、不同时间访问页面时，显示的内容可能不同；
  * 页面结构也是允许变化的，但不频繁；
  * 表现效果，随内容的变化而变化；
  * 要进一步执行内容生成步骤，通常的方式有访问数据库等
* **伪静态页面**:是以静态页面展现出来，但实际上是用动态脚本来处理的