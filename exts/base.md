# docsify 快速开始

建议`docsify-cli`全局安装，有助于本地初始化和预览网站

```shell
npm i docsify-cli -g
```

## 初始化

如果想在./docs子目录中写入文档，可以使用该`init`命令

```shell
docsify init ./docs
```

完成后`init`可以看到./docs子目录下的文件列表。

* `index.html`作为入口文件
* `README.md`作为主页
* `.nojekyll`防止 GitHub Pages 忽略以下划线开头的文件

## 预览网站

使用运行本地服务器`docsify serve`。您可以在浏览器中预览您的网站 `http://localhost:3000`

```shell
docsify serve docs
```

## 手动预览您的网站

如果您的系统上安装了 Python，您可以轻松地使用它来运行静态服务器来预览您的站点

```python
cd docs && python -m http.server 3000
```

## 加载对话框

如果需要，您可以在 docsify 开始渲染文档之前显示一个加载对话框

```html
<!-- index.html -->

<div id="app">Please wait...</div>
```

## Markdown 扩展说明

### 重要内容

```markdown
!> **Time** is money, my friend!
```

### 一般提示

一般提示如：

```markdown
?> _TODO_ unit test
```

### 图像设置

#### 调整图像大小

```markdown
![logo](https://docsify.js.org/_media/icon.svg ':size=WIDTHxHEIGHT')
![logo](https://docsify.js.org/_media/icon.svg ':size=50x100')
![logo](https://docsify.js.org/_media/icon.svg ':size=100')

<!-- Support percentage -->

![logo](https://docsify.js.org/_media/icon.svg ':size=10%')
```

#### 设置图像元素的 class 属性

```markdown
![logo](https://docsify.js.org/_media/icon.svg ':class=someCssClass')
```

#### 设置图像元素的 id 属性

```markdown
![logo](https://docsify.js.org/_media/icon.svg ':id=someCssId')
```

### 自定义标题 ID

```markdown
### Hello, world! :id=hello-world
```

## docsify 扩展说明

### 笔记块

```markdown
> [!NOTE]
> An alert of type 'note' using global style 'callout'.
```

### 提示块

```markdown
> [!TIP]
> An alert of type 'tip' using global style 'callout'.
```

### 警告块

```markdown
> [!WARNING]
> An alert of type 'warning' using global style 'callout'.
```

### 注意块

```markdown
> [!ATTENTION]
> An alert of type 'attention' using global style 'callout'.
```

### markmap

```markdown
```markmap
# hello
## world
## nihao
```(end)
```





