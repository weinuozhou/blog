# pyecharts的作图方法与修饰逻辑

```python
# 系统库
import datetime
import random
import math
# 数据分析库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 不展示警告信息
import warnings

warnings.filterwarnings('ignore')
# 使一个单元格可以输出多次
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
# pyecharts相关
from pyecharts.globals import CurrentConfig, OnlineHostType, ThemeType, ChartType, SymbolType

CurrentConfig.ONLINE_HOST = OnlineHostType.NOTEBOOK_HOST
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.charts import *  # 图表类型
from pyecharts import options as opts  # 配置项
```

## python的两种数据作图方案

* matplotlib 简单方便，适合数值作图与科学作图（论文发表）
* pyecharts 流程略微复杂但功能强大，图形为交互式，适合项目开发和商业分析报告(国人开发)；但是这个库的问题也在于是一个非常新的库，开发很不稳定,本文所使用的**pyecharts 2.0.3**


### 作图的通用流程

1. 选择图的类型
2. 导入图需要展示的数据
3. 修改图形的配置项(如标题,坐标轴等)

```python
x = range(1,8)
y = [114, 55, 27, 101, 125, 27, 105]
plt.bar(x,y)
```

<div style="text-align: center;"><img alt='202403301809121' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301809121.png' width=500px> </div>

```python
bar = Bar()
bar.add_xaxis(list(x))  # pyecharts作图仅支持python基本数据类型
bar.add_yaxis("ylabel", y)
bar.render_notebook()  # 用来在notebook中展示图形，使用render则会直接保存为html文件
```

<div style="text-align: center;"><img alt='202403301810935' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301810935.png' width=500px> </div>

## pyecharts的安装

`pip install pyecharts`

pyecharts的具体配置及渲染请参考此文档:[pyecharts官方文档](https://pyecharts.org/#/zh-cn/assets_host?id=notebook-server)

## pyecharts支持的代码格式

* pyecharts支持**函数式调用**
* pyecharts也支持**链式调用**(推荐使用)

### 产生伪数据

```python
from pyecharts.faker import Faker
```
> 这是用来产生伪数据的包

```python
# pyecharts支持链式调用
def bar_base() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
    )
    return c
bar_base().render_notebook()
```

<div style="text-align: center;"><img alt='202403301813109' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301813109.png' width=500px> </div>

### 设置主题

* 有些配置需要在图形函数中配置，比如主题的设定
* 默认主题类型为WHITE
* 内置主题类型包括LIGHT、DARK、CHALK、ESSOS、INFOGRAPHIC、MACARONS、PURPLE_PASSION、ROMA、ROMANTIC、SHINE、VINTAGE、WALDEN、WESTEROS、WONDERLAND
* pyecharts支持使用自己构建的主题,详情请参考[pyecharts官方文档](https://pyecharts.org/#/zh-cn/themes)

?> 所有内置的主题风格预览如下:

#### 默认主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301813560' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301813560.png' width=500px> </div>

#### `LIGHT`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301814669' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301814669.png' width=500px> </div>

#### `CHALK`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301814862' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301814862.png' width=500px> </div>

#### `DARK`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301816683' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301816683.png' width=500px> </div>

#### `ESSOS`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301816377' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301816377.png' width=500px> </div>

#### `INFOGRAPHIC`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301816760' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301816760.png' width=500px> </div>

#### `MACARONS`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301817609' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301817609.png' width=500px> </div>

#### `PURPLE_PASSION`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301818762' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301818762.png' width=500px> </div>

#### `ROMA`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301818943' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301818943.png' width=500px> </div>

#### `ROMANIC`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301818459' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301818459.png' width=500px> </div>

#### `SHINE`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301819876' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301819876.png' width=500px> </div>

#### `VINTAGE`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301819346' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301819346.png' width=500px> </div>

#### `WALDEN`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301820346' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301820346.png' width=500px> </div>

#### `WESTEROS`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301820650' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301820650.png' width=500px> </div>

#### `WONDERLAND`主题

```python
(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301821961' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301821961.png' width=500px> </div>

## pyecharts的图形修饰逻辑

* pyecharts的官方文档，也是最重要的学习资源： [https://pyecharts.org](https://pyecharts.org)

### 全局配置项

```python
from pyecharts import options as opts
```

* 全局配置项可通过`set_global_opts`方法设置
* 全局配置项具体包括:
    * 标题和副标题配置项
    * 图例配置项
    * 工具箱配置项
    * 提示框配置项
    * 视觉映射配置项
    * 区域缩放配置项
    
!> 本文只介绍了一些常用的全局配置项，其他具体相关配置项可以参考[pyecharts官方文档](https://pyecharts.org/#/zh-cn/global_options)

#### InitOpts:初始化配置项

* 初始化配置项可以配置**画布的大小**、**图表的背景颜色**、**主题**、**动画**等等

属性|含义
:---:|:---:
`width`|str类型,画布宽度,例如900px
`height`|str类型,画布高度,例如500px
`chart_id`|str类型,图表id，唯一标识
`renderer`|渲染风格
`page_title`|网页标题
`theme`|图表主题
`bg_color`|图表背景颜色
`animation_opts`|动画初始配置项

##### 画布大小的设置

设置`width`和`height`即可确定画布大小

```python
bar = (Bar(init_opts=opts.InitOpts(width = '1000px',height= '800px'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301823671' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301823671.png' width=500px> </div>

##### 主题配置

```python
bar = (Bar(init_opts=opts.InitOpts(theme = 'Dark'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301824777' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301824777.png' width=500px> </div>

##### 背景颜色

* pyecharts所有颜色几乎都支持以下三种格式:
    * 常见的颜色可以通过`white`、`green`等来配置
    * 支持rgb和rgba(a表示不透明度,设置成1表示黑色(完全不透明)，设置成0表示白色(完全透明))通道颜色配置,如`rgb(1,3,4).rgba(1,2,3,0.6)`
    * 支持16进制格式颜色，如`#ccc`

```python
bar = (Bar(init_opts=opts.InitOpts(bg_color='rgba(1,3,4,0.5)'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301824838' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301824838.png' width=500px> </div>

#### TitleOpts:标题配置项

* 标题配置项可以设置**标题的内容**、**字体样式**、**标题的位置**等等

属性|含义
:---:|:---:
`is_show`|bool类型,是否显示标题组件
`title`|标题,支持用\n换行
`title_link`|主标题跳转链接
`title_target`|跳转链接的方式,有`self`(当前窗口打开)和`blank`(新建窗口打开)
`subtitle`|副标题
`subtitle_link`|同上
`subtitle_target`|同上
`pos_left`|title组件距离容器左侧的距离
`pos_right`|title组件距离容器右侧的距离
`pos_bottom`|title组件距离容器底部的距离
`pos_top`|title组件距离容器顶部的距离
`padding`|设置四个方向的标题内边距,如[5,10,7,8]，默认是[5,5,5,5]
`item_gap`|设置主副标题之间的边距
`title_textstyle_opts`|主标题字体样式配置
`subtitle_textstyle_opts`|副标题字体样式配置

##### 标题的位置

`pos_top`、`pos_bottom`、`pos_left`、`pos_right`分别对应容器的上/下/左/右

* 可以接受20这样的具体像素值
* 也可以接受`20%`这样相对于容器高宽的百分比
* 也接受`left`,`right`,`center`

```python
bar = (
    Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle = '副标题',pos_left='center',pos_top='5%'))
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301825868' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301825868.png' width=500px> </div>

##### 标题字体样式配置

字体样式配置位于`TextStyleOpts`类下,具有的属性如下:

* `color`:文字颜色
* `font_style`:字体风格,可选`normal`,`italic`,`oblique`
* `font_weight`:字体粗细，可选`bold`,`bolder`,`normal`
* `font_size`:字体大小
* `font_famliy`:字体系列,例如:`Microsoft YaHei`...
* `background_color`:文字块的背景颜色
* `padding`:文字内边距

```python
(
    Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle = '副标题',
                                                title_textstyle_opts=opts.TextStyleOpts(color='red',font_size=20),
                                                subtitle_textstyle_opts=opts.TextStyleOpts(color='green',font_size=16)
                                                )
                      )
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301826514' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301826514.png' width=500px> </div>

#### LegendOpts:图例配置项

属性|含义
:---:|:---
`type_`|图例的类型,可取值有`plain`(普通图例)和`scroll`(可滚动的图例)
`selected_mode`|图例的选择模式,可以设置成开启或者关闭,或者设置成`single`(单选)或`muliple`(多选)
`pos_left`|legend组件距离容器左侧的距离
`pos_right`|ledeng组件距离容器右侧的距离
`pos_bottom`|legend组件距离容器底部的距离
`pos_top`|legend组件距离容器顶部的距离
`orient`|图例的布局朝向,可设置成`horizontal`(水平)或`vertical`(垂直)
`inactive_color`|图例关闭时的颜色,默认是`#ccc`
`item_gap`|图例之间的间距
`padding`|图例内边距
`textstyle_opts`|图例字体样式
`backdround_color`|图例的背景颜色,默认是透明的
`legend_icon`|图例项的icon,可选项有`circle`,`rect`,`roundRect`,`triangle`,`diamond`,`pin`,`arrow`,`none`

##### 是否显示图例

```python
(
    (Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(is_show=True))# 默认是True,表示显示图例,可设置成False关闭图例
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301827309' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301827309.png' width=500px> </div>

##### 图例显示的位置

`pos_top`、`pos_bottom`、`pos_left`、`pos_right`分别对应容器的上/下/左/右

* 可以接受20这样的具体像素值
* 也可以接受`20%`这样相对于容器高宽的百分比
* 也接受`left`,`right`,`center`

```python
bar = (Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(pos_right='20%',pos_top='10%'))        
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301827176' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301827176.png' width=500px> </div>

##### 图例的布局(水平或垂直)

```python
(
    (
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(orient='vertical'))# 默认是horizontal，表示水平放置      
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301828573' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301828573.png' width=500px> </div>

##### 图例的间距

* 不同系列的图例之间的间距可设置`item_gap`来实现
* 图例之间的内边距可设置`padding`来实现

```python
(
    (
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(item_gap=50,padding=20))      
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301828303' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301828303.png' width=500px> </div>

##### 图例的形状

```python
(
    (
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(legend_icon='circle')) # 图例的性质默认是'roundRect'       
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301829336' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301829336.png' width=500px> </div>

##### 图例的文本样式

```python
(
    (
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color='red',font_size=14)))      
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301829700' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301829700.png' width=500px> </div>

#### ToolboxOpts:工具箱配置项

* 工具箱配置项主要配置一些工具以及工具的位置和布局:
    * 保存为图片
    * 区域缩放
    * 折线图、柱状图、层叠柱状图之间的转换
    * 数据视图

属性|含义
:---:|:---
`is_show`|是否显示工具栏组件
`orient`|工具栏的布局朝向，可选择`horizontal`或`vertical`
`pos_left`|组件距离容器左侧的距离
`pos_right`|组件距离容器右侧的距离
`pos_bottom`|组件距离容器底部的距离
`pos_top`|组件距离容器顶部的距离
`feature`|各工具配置项,详情如下

##### 工具箱工具配置项(ToolBoxFeatureOpts)

属性|含义
:---:|:---
`save_ax_image`|保存为图片,`ToolBoxFeatureSaveAsImageOpts()`
`restore`|配置项还原,`ToolBoxFeatureRestoreOpts()`
`data_view`|数据视图工具,`ToolBoxFeatureDataViewOpts()`
`data_zoom`|数据区域缩放(目前只支持直角坐标系的缩放)`ToolBoxFeatureDataZoomOpts()`
`magic_type`|动态类型切换,`ToolBoxFeatureMagicTypeOpts()`
`brush`|选框组件的控制按钮,`ToolBoxFeatureBrushOpts()`

* ToolBoxFeatureSaveAsImagesOpts:工具箱保存图片配置项
* ToolBoxFeatureRestoreOpts:工具箱还原配置项
* ToolBoxFeatureDataViewOpts:工具箱数据视图工具
* ToolBoxFeatureDataZoomOpts:工具箱区域缩放配置项
* ToolBoxFeatureMagicTypeOpts:工具箱动态类型切换配置项
* ToolBoxFeatureBrushOpts:工具箱选框组件配置项

> 具体请参考[pyecharts官方文档](https://pyecharts.org/#/zh-cn/global_options)

```python
bar = (Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',chart_id= 1,bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'))
      .set_global_opts(legend_opts=opts.LegendOpts(type_='scroll',selected_mode= 'multiple',orient='horizontal',padding=10)) 
      .set_global_opts(toolbox_opts=opts.ToolboxOpts(feature=opts.ToolBoxFeatureOpts(
                      save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(type_='png',pixel_ratio=2),
                      restore=opts.ToolBoxFeatureRestoreOpts()))
                      )
      )
bar.render_notebook()
```

<div style="text-align: center;"><img alt='202403301941584' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301941584.png' width=500px> </div>

#### AxisOpts：坐标轴配置项

属性|含义
:---:|:---
`is_show`|是否显示x轴
` type_`|坐标轴的类型，可选值有['value','category','time','log']
`name`|坐标轴的名称
`name_location`|坐标轴名称的位置,可选值有['start','middle','end']
`name_rotate`|坐标轴名称旋转的角度
`min_`|坐标轴刻度的最小值
`max_`|坐标轴刻度的最大值
`axisline_opts`|坐标轴刻度线配置项
`axistick_opts`|坐标轴刻度配置项
`axislabel_opts`|坐标轴标签配置项
`axispointer_opts`|坐标轴指示器配置项
`name_textstyle_opts`|坐标轴名称的文字样式

`axisline_opts`、`axistick_opts`、`axislabel_opts`、`axispointer_opts`等配置项请参考[pyecharts官方文档](https://pyecharts.org/#/zh-cn/global_options)

##### 坐标轴的类型

可通过指定`type_`来确定坐标轴的类型
* `value`,`category`,`time`,`log`

```python
(
    (Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       yaxis_opts=opts.AxisOpts(type_ = 'value'),
                       xaxis_opts=opts.AxisOpts(type_ = 'category'))
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301941578' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301941578.png' width=500px> </div>

##### 添加坐标轴名称

* 添加坐标轴名称可以通过设置`name`来实现
* 坐标轴名称的位置可以通过`name_location`来调整
* 坐标轴名称文字样式可以通过`name_teststyle_opts`来调整

```python
(
    (Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       yaxis_opts=opts.AxisOpts(name = '销售额',name_location = 'end',name_textstyle_opts=opts.TextStyleOpts(color='red',font_size=16)),
                       xaxis_opts=opts.AxisOpts(name = '商家类别',name_location = 'middle',name_textstyle_opts=opts.TextStyleOpts(color='red',font_size=16))
                      )
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301942415' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301942415.png' width=500px> </div>

#### DataZoomOpts：区域缩放配置项

属性|含义
:---:|:---
`is_show`|是否显示组件
`type_`|组件类型,可选值包括`slider`, `inside`
`is_realtime`|bool类型,拖动时是否实时更新视图
`range_start`|数据窗口范围的起始百分比
`range_end`|数据窗口范围的结束百分比
`pos_left`|组件距离容器左侧的距离
`pos_right`|组件距离容器右侧的距离
`pos_bottom`|组件距离容器底部的距离
`pos_top`|组件距离容器顶部的距离
`filter_mode`|数据过滤的方式,可选值包括`filter`,`weakfilter`,`empty`,`none`
`orient`|数据缩放的轴，默认是horizontal,表示x轴,可设置成vertical

```python
x = range(1,8)
y = [114, 55, 27, 101, 125, 27, 105]
(Bar()
       .add_xaxis(list(x))
       .add_yaxis("name", y)
       .set_global_opts(title_opts=opts.TitleOpts(title="title"),
                        datazoom_opts=opts.DataZoomOpts(range_start=20,range_end=80))
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301942159' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301942159.png' width=500px> </div>

#### VisualMapOpts：视觉映射配置项

属性|含义
:---:|:---
`is_show`|是否显示组件
`type_`|映射过渡类型,可选值有`color`,`size`
`min_`|指定 visualMapPiecewise 组件的最小值
`max_`|指定 visualMapPiecewise 组件的最大值
`range_text`|两端的文本,如['high','low']
`range_color`|组件过渡的颜色
`pos_left`|组件距离容器左侧的距离
`pos_right`|组件距离容器右侧的距离
`pos_bottom`|组件距离容器底部的距离
`pos_top`|组件距离容器顶部的距离
`is_piecewise`|颜色是否分段显示

```python
(
    (
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',chart_id= 1,bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       visualmap_opts=opts.VisualMapOpts(type_='color',min_=30,max_=150,range_text=['max','min'])
                      )
      .render_notebook()
    )
)
```

<div style="text-align: center;"><img alt='202403301943681' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301943681.png' width=500px> </div>

#### TooltipOpts：提示框配置项

属性|含义
:---:|:---
`is_show`|是否显示组件
`trigger`|触发类型,可选值有`item`,`axis`,`none`
`trigger_on`|提示框触发的条件,可选值有`mousemove`,`click`,`mousemove\|click`,`none`
`axis_pointer_type`|指示器的类型,可选值包括`line`,`shadow`,`none`,`cross`
`formatter`|提示框的内容格式
`background_color`|提示框的背景颜色
`teststyle_opts`|文字样式配置

##### 触发条件设置

触发条件的设置可通过调整`trigger_on`来实现,具体触发条件有以下三种:
* `mousemove`:鼠标移动
* `click`:鼠标点击
* `mousemove|click`:鼠标移动或者点击

```python
(
    Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       tooltip_opts=opts.TooltipOpts(trigger_on='mousemove|click'))
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301944310' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301944310.png' width=500px> </div>

##### 提示框的背景颜色

```python
(
    Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       tooltip_opts=opts.TooltipOpts(background_color='red'))
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301944858' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301944858.png' width=500px> </div>

##### 提示框的内容格式

模板变量如下:
* {a}:系列名称
* {b}:数据名
* {c}:数值
* {d}:百分比,只在特定图表中生效

```python
(
    Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       tooltip_opts=opts.TooltipOpts(formatter='{a}|{b}:{c}'))
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301945096' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301945096.png' width=500px> </div>

#### BrushOpts：区域选择组件配置项

* 区域选择组件(`tool_box`)包括以下内容:
   * `rect`：开启矩形选框选择功能。
   * `polygon`：开启任意形状选框选择功能。
   * `lineX`：开启横向选择功能。
   * `lineY`：开启纵向选择功能。
   * `keep`：切换『单选』和『多选』模式。后者可支持同时画多个选框。前者支持单击清除所有选框。
   * `clear`：清空所有选框。
* 默认只有`rect`,`polygon`,`keep`,`clear`

属性|含义
:---:|:---
`tool_box`|默认值为 ["rect", "polygon", "keep", "clear"]

```python
(
      Bar(init_opts=opts.InitOpts(width = '1000px',height= '600px',bg_color= 'white'))
      .add_xaxis(Faker.choose())
      .add_yaxis('商家A',Faker.values())
      .add_yaxis('商家B',Faker.values())
      .set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='副标题'),
                       brush_opts=opts.BrushOpts(tool_box=['rect','polygon','keep','lineX','lineY','clear'])
                      )
      .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301945358' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301945358.png' width=500px> </div>

### 系列配置项

* set_series_opts负责很多系列配置项的定义，比如TextStyleOpts、LabelOpts、MarkPointOpts、MarkLineItem等等
* 系列配置项有两种传参的方式:
    * 通过`set_series_opts`进行配置
    * 添加数据时进行配置
* 具体系列配置项可以参考[pyecharts官方文档](https://pyecharts.org/#/zh-cn/series_options)

#### TextStyleOpts:文字样式配置项

* `color`:文字颜色
* `font_style`:文字字体的风格,可选值包括`normal`，`italic`，`oblique`
* `font_weight`:文字字体的粗细，可选值包括`normal`，`bold`，`bolder`，`lighter`
* `font_family`:文字的字体系列
* `font_size`:文字的字体大小
* `align`:文字水平对齐方式
* `vertical_align`:文字的垂直对齐方式
* `background_color`:文字块的背景颜色
* `paddind`:文字的内边距

```python
(
    Bar()
       .add_xaxis(Faker.choose())
       .add_yaxis("name", Faker.values())
       .add_yaxis("number",Faker.values())
       .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.TextStyleOpts(font_size=20)))
       .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301946361' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301946361.png' width=500px> </div>

#### LineStyleOpts:线样式配置项

* `is_show`:是否显示组件
* `width`:线宽
* `opacity`:图形透明度
* `type_`:线的类型,可选值包括`solid`(实线), `dashed`(虚线), `dotted`(虚线)
* `color`:颜色

```python
(
    Line()
       .add_xaxis(Faker.choose())
       .add_yaxis("name", Faker.values(),linestyle_opts=opts.LineStyleOpts(width=5,type_='solid'))
       .add_yaxis("number",Faker.values(),linestyle_opts=opts.LineStyleOpts(width=3,type_='dotted'))
       .render_notebook()
    )
```

<div style="text-align: center;"><img alt='202403301946139' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301946139.png' width=500px> </div>

#### LabelOpts:标签配置项

* `is_show`:是否显示组件
* `color`:标签的颜色
* `position`:标签的位置
* `font_style`:文字字体的风格,可选值包括`normal`，`italic`，`oblique`
* `font_weight`:文字字体的粗细，可选值包括`normal`，`bold`，`bolder`，`lighter`
* `font_family`:文字的字体系列
* `font_size`:文字的字体大小
* `align`:文字水平对齐方式
* `vertical_align`:文字的垂直对齐方式

```python
(
    Bar()
       .add_xaxis(Faker.choose())
       .add_yaxis("name", Faker.values()) 
       .add_yaxis("number",Faker.values())
       .set_series_opts(label_opts=opts.LabelOpts(is_show=False,color =None)) # 这里的color只是更改标签的颜色，不能改变柱体的颜色
       .render_notebook()
    )
```

<div style="text-align: center;"><img alt='202403301947762' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301947762.png' width=500px> </div>

#### MarkPointOpts:标记点配置项

* `data`:标记点的数据,数据类型为`MarkPointItem`对象
* `symbol`:标记的图形,可选值包括`circle`, `rect`, `roundRect`, `triangle`
* `symbol_size`:标记的大小
* `label_opts`:标签配置项
* `MarkPointItem`对象
    * `name`:标注的名称
    * `type_`:标注的类型，可选值包括`min`,`max`,`average`
    * `symbol`:标记的图形,可选值包括`circle`, `rect`, `roundRect`, `triangle`
    * `symbol_size`:标记的大小
    * `coord`:标注的坐标

##### 特殊值标记

```python
(
    Bar()
       .add_xaxis(Faker.choose())
       .add_yaxis("name", Faker.values()) 
       .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                    opts.MarkPointItem(type_="average", name="平均值"),
                ])
       )
       .render_notebook()
      )
```

<div style="text-align: center;"><img alt='202403301948322' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301948322.png' width=500px> </div>

##### 自定义标记点

```python
x = range(1,8)
y = [114, 55, 27, 101, 125, 27, 105]
(
    Bar()
       .add_xaxis(list(x))
       .add_yaxis("name", y) 
       .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    # 通过坐标来自定义标记点
                    opts.MarkPointItem(coord=[1,55],name = '坐标',value=55),
                    # 通过像素值来自定义标记点
                    opts.MarkPointItem(x=450,y=180,name='像素值',value=101),
                ])
       )
       .render_notebook()
   )
```

<div style="text-align: center;"><img alt='202403301948794' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301948794.png' width=500px> </div>

#### MarkLineOpts:标记线配置项

* `is_silent`:图形是否不响应和触发鼠标事件，默认为 false，即响应和触发鼠标事件
* `data`:标记线的数据，数据类型为`MarkLineItem`对象
* `symbol`:标线两端的标记类型
* `symbol_size`:标线两端的标记大小
* `label_opts`:标签配置项
* `linestyle_opts`:标记线样式配置项
* `MarkLineItem`对象
    * `name`:标注的名称
    * `type_`:标注的类型，可选值包括`min`,`max`,`average`
    * `symbol`:标记的图形,可选值包括`circle`, `rect`, `roundRect`, `triangle`
    * `symbol_size`:标记的大小

##### 特殊值标记

```python
    (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
        .add_xaxis(list(x))
        .add_yaxis("name", y)
        .set_series_opts(label_opts=opts.LabelOpts(font_style="italic",font_size=16),
                       markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="max",name="最大值"),
                                                             opts.MarkLineItem(type_="min",name="最小值"),
                                                             opts.MarkLineItem(type_="average",name="平均值")
                                                            ]))
        .set_global_opts(yaxis_opts=opts.AxisOpts(max_=135))
        .render_notebook()
        )
```

<div style="text-align: center;"><img alt='202403301949445' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301949445.png' width=500px> </div>

##### 自定义标记

```python
    (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
        .add_xaxis(list(x))
        .add_yaxis("name", y)
        .set_series_opts(label_opts=opts.LabelOpts(font_style="italic",font_size=16),
                       markline_opts=opts.MarkLineOpts(
                           data=[
                                   opts.MarkLineItem(x=1,name="x轴标签"),
                                   opts.MarkLineItem(y=27,name="y轴标签"),
                                ]
                               )
                        )
        .set_global_opts(yaxis_opts=opts.AxisOpts(max_=135))
        .render_notebook()
        )
```

<div style="text-align: center;"><img alt='202403301950718' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301950718.png' width=500px> </div>

#### ItemStyleOpts:图元样式配置项

* 有一些系列配置是放在其他地方的，这取决于此配置项用来修饰的对象。比如itemstyle_opts用来修饰bar的颜色时就放在add_yaxis里。要确定配置的使用位置，比如add_yaxis这种函数包含哪些配置项建议先阅读每个图形最前面的class说明
* `color`:图形的颜色
* `opacity`:图形的透明度,$0-1$的浮点数
* `border_color`:边框颜色

```python
(
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("name", Faker.values(),itemstyle_opts=opts.ItemStyleOpts(color='pink',opacity=0.6,border_color='red'))
    .render_notebook()
    )
```

<div style="text-align: center;"><img alt='202403301950911' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301950911.png' width=500px> </div>

## pyecharts的数据类型问题

* 由于pyecharts背后封装的js库，会涉及到数据类型转化。它要求输入数据必须是python的基础数据类型，比如字符串，列表，字典,而不能是range函数生成的序列这样的数据类型。因此序列输入量需要事先被转化为list等基础数据类型才能被pyecharts支持
* 具体可以参考:[https://pyecharts.org/#/zh-cn/data_format](https://pyecharts.org/#/zh-cn/data_format)
* 这也就意味着在你将数据传入到 `pyecharts` 的时候，需要自行将数据格式转换成上述 `Python` 原生的数据格式。使用数据分析大都需要使用 `numpy/pandas`，但是 `numpy` 的 `numpy.int64`/`numpy.int32`/... 等数据类型并不继承自 `Python.int`,转换方式如下

### 转换方式1

* 对于整数型的数据
```python
[int(x) for x in your_numpy_array_or_something_else]
```

```python
x = np.array([1,2,3,4,56])
y = [123,124,125,125,200]
(
    Bar()
    .add_xaxis([int(i) for i in x])
    .add_yaxis('name',y)
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301951704' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301951704.png' width=500px> </div>

* 对于浮点数的类型
```python
[float(x) for x in your_numpy_array_or_something_else]
```

```python
x = ['xiaomi','huawei','apple','oppo','vivo']
y = np.array([123.4,145.6,345.4,234.3,23.2])
(
    Bar()
    .add_xaxis(x)
    .add_yaxis('name',[float(i) for i in y])
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301952906' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301952906.png' width=500px> </div>

* 对于字符串
```python
[str(x) for x in your_numpy_array_or_something_else]
```

### 转换方式2

```python
pd.Series.tolist()
```

```python
x = pd.Series([1,2,3,4,5])
y = [123,124,125,125,200]
(
    Bar()
    .add_xaxis(pd.Series.tolist(x))
    .add_yaxis('name',y)
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301953331' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301953331.png' width=500px> </div>

## 基本图表

### 日历图

```python
begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

c = (
    Calendar(init_opts=opts.InitOpts(width = '1000px',height = '500px'))
    .add(
        "微信步数统计",
        data,
        calendar_opts=opts.CalendarOpts(
            range_="2017",
            daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
            monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况(中文 Label)"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
)
c.render_notebook()
```

<div style="text-align: center;"><img alt='202403301954898' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301954898.png' width=500px> </div>

### 漏斗图

```python
c = (
    Funnel()
    .add(
        "商品",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        sort_="ascending",
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）",pos_top='20%'))
)
c.render_notebook()
```

<div style="text-align: center;"><img alt='202403301954981' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301954981.png' width=500px> </div>

### 仪表盘

```python
(
    Gauge()
    .add(series_name="业务指标", data_pair=[["完成率", 55.5]])
    .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
    )
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301954566' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301954566.png' width=500px> </div>

### 关系图

```python
nodes = [
    {"name": "结点1", "symbolSize": 10},
    {"name": "结点2", "symbolSize": 20},
    {"name": "结点3", "symbolSize": 30},
    {"name": "结点4", "symbolSize": 40},
    {"name": "结点5", "symbolSize": 50},
    {"name": "结点6", "symbolSize": 40},
    {"name": "结点7", "symbolSize": 30},
    {"name": "结点8", "symbolSize": 20},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get("name"), "target": j.get("name")})
c = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="Graph-基本示例"))
)
c.render_notebook()
```

<div style="text-align: center;"><img alt='202403301955362' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301955362.png' width=500px> </div>

### 水球图

```python
(
    Liquid()
    .add("lq", [0.6, 0.7])
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301955183' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301955183.png' width=500px> </div>

### 饼图

```python
cate = ['Apple','Huawei','Xiaomi','Oppo','Vivo','Meizu']
data = [123,109,67,87,98,43]
(
    Pie()
    .add('饼图',[list (z) for z in zip(cate,data)])
    .set_global_opts(title_opts=opts.TitleOpts(title='手机销售占比(虚假数据)',pos_left='center'),
                        legend_opts=opts.LegendOpts(pos_right='right'))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301956218' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301956218.png' width=500px> </div>

### 词云图

```python
words = [
    ("花鸟市场", 1446),
    ("汽车", 928),
    ("视频", 906),
    ("电视", 825),
    ("Lover Boy 88", 514),
    ("动漫", 486),
    ("音乐", 53),
    ("直播", 163),
    ("广播电台", 86),
    ("戏曲曲艺", 17),
    ("演出票务", 6),
    ("给陌生的你听", 1),
    ("资讯", 1437),
    ("商业财经", 422),
    ("娱乐八卦", 353),
    ("军事", 331),
    ("科技资讯", 313),
    ("社会时政", 307),
    ("时尚", 43),
    ("网络奇闻", 15),
    ("旅游出行", 438),
    ("景点类型", 957),
    ("国内游", 927),
    ("远途出行方式", 908),
    ("酒店", 693),
    ("关注景点", 611),
    ("旅游网站偏好", 512),
    ("出国游", 382),
    ("交通票务", 312),
    ("旅游方式", 187),
    ("旅游主题", 163),
    ("港澳台", 104),
    ("本地周边游", 3),
    ("小卖家", 1331),
    ("全日制学校", 941),
    ("基础教育科目", 585),
    ("考试培训", 473),
    ("语言学习", 358),
    ("留学", 246),
    ("K12课程培训", 207),
    ("艺术培训", 194),
    ("技能培训", 104),
    ("IT培训", 87),
    ("高等教育专业", 63),
    ("家教", 48),
    ("体育培训", 23),
    ("职场培训", 5),
    ("金融财经", 1328),
    ("银行", 765),
    ("股票", 452),
    ("保险", 415),
    ("贷款", 253),
    ("基金", 211),
    ("信用卡", 180),
    ("外汇", 138),
    ("P2P", 116),
    ("贵金属", 98),
    ("债券", 93),
    ("网络理财", 92),
    ("信托", 90),
    ("征信", 76),
    ("期货", 76),
    ("公积金", 40),
    ("银行理财", 36),
    ("银行业务", 30),
    ("典当", 7),
    ("海外置业", 1),
    ("汽车", 1309),
    ("汽车档次", 965),
    ("汽车品牌", 900),
    ("汽车车型", 727),
    ("购车阶段", 461),
    ("二手车", 309),
    ("汽车美容", 260),
    ("新能源汽车", 173),
    ("汽车维修", 155),
    ("租车服务", 136),
    ("车展", 121),
    ("违章查询", 76),
    ("汽车改装", 62),
    ("汽车用品", 37),
    ("路况查询", 32),
    ("汽车保险", 28),
    ("陪驾代驾", 4),
    ("网络购物", 1275),
    ("做我的猫", 1088),
    ("只想要你知道", 907),
    ("团购", 837),
    ("比价", 201),
    ("海淘", 195),
    ("移动APP购物", 179),
    ("支付方式", 119),
    ("代购", 43),
    ("体育健身", 1234),
    ("体育赛事项目", 802),
    ("运动项目", 405),
    ("体育类赛事", 337),
    ("健身项目", 199),
    ("健身房健身", 78),
    ("运动健身", 77),
    ("家庭健身", 36),
    ("健身器械", 29),
    ("办公室健身", 3),
    ("商务服务", 1201),
    ("法律咨询", 508),
    ("化工材料", 147),
    ("广告服务", 125),
    ("会计审计", 115),
    ("人员招聘", 101),
    ("印刷打印", 66),
    ("知识产权", 32),
    ("翻译", 22),
    ("安全安保", 9),
    ("公关服务", 8),
    ("商旅服务", 2),
    ("展会服务", 2),
    ("特许经营", 1),
    ("休闲爱好", 1169),
    ("收藏", 412),
    ("摄影", 393),
    ("温泉", 230),
    ("博彩彩票", 211),
    ("美术", 207),
    ("书法", 139),
    ("DIY手工", 75),
    ("舞蹈", 23),
    ("钓鱼", 21),
    ("棋牌桌游", 17),
    ("KTV", 6),
    ("密室", 5),
    ("采摘", 4),
    ("电玩", 1),
    ("真人CS", 1),
    ("轰趴", 1),
    ("家电数码", 1111),
    ("手机", 885),
    ("电脑", 543),
    ("大家电", 321),
    ("家电关注品牌", 253),
    ("网络设备", 162),
    ("摄影器材", 149),
    ("影音设备", 133),
    ("办公数码设备", 113),
    ("生活电器", 67),
    ("厨房电器", 54),
    ("智能设备", 45),
    ("个人护理电器", 22),
    ("服饰鞋包", 1047),
    ("服装", 566),
    ("饰品", 289),
    ("鞋", 184),
    ("箱包", 168),
    ("奢侈品", 137),
    ("母婴亲子", 1041),
    ("孕婴保健", 505),
    ("母婴社区", 299),
    ("早教", 103),
    ("奶粉辅食", 66),
    ("童车童床", 41),
    ("关注品牌", 271),
    ("宝宝玩乐", 30),
    ("母婴护理服务", 25),
    ("纸尿裤湿巾", 16),
    ("妈妈用品", 15),
    ("宝宝起名", 12),
    ("童装童鞋", 9),
    ("胎教", 8),
    ("宝宝安全", 1),
    ("宝宝洗护用品", 1),
    ("软件应用", 1018),
    ("系统工具", 896),
    ("理财购物", 440),
    ("生活实用", 365),
    ("影音图像", 256),
    ("社交通讯", 214),
    ("手机美化", 39),
    ("办公学习", 28),
    ("应用市场", 23),
    ("母婴育儿", 14),
    ("游戏", 946),
    ("手机游戏", 565),
    ("PC游戏", 353),
    ("网页游戏", 254),
    ("游戏机", 188),
    ("模拟辅助", 166),
    ("个护美容", 942),
    ("护肤品", 177),
    ("彩妆", 133),
    ("美发", 80),
    ("香水", 50),
    ("个人护理", 46),
    ("美甲", 26),
    ("SPA美体", 21),
    ("花鸟萌宠", 914),
    ("绿植花卉", 311),
    ("狗", 257),
    ("其他宠物", 131),
    ("水族", 125),
    ("猫", 122),
    ("动物", 81),
    ("鸟", 67),
    ("宠物用品", 41),
    ("宠物服务", 26),
    ("书籍阅读", 913),
    ("网络小说", 483),
    ("关注书籍", 128),
    ("文学", 105),
    ("报刊杂志", 77),
    ("人文社科", 22),
    ("建材家居", 907),
    ("装修建材", 644),
    ("家具", 273),
    ("家居风格", 187),
    ("家居家装关注品牌", 140),
    ("家纺", 107),
    ("厨具", 47),
    ("灯具", 43),
    ("家居饰品", 29),
    ("家居日常用品", 10),
    ("生活服务", 883),
    ("物流配送", 536),
    ("家政服务", 108),
    ("摄影服务", 49),
    ("搬家服务", 38),
    ("物业维修", 37),
    ("婚庆服务", 24),
    ("二手回收", 24),
    ("鲜花配送", 3),
    ("维修服务", 3),
    ("殡葬服务", 1),
    ("求职创业", 874),
    ("创业", 363),
    ("目标职位", 162),
    ("目标行业", 50),
    ("兼职", 21),
    ("期望年薪", 20),
    ("实习", 16),
    ("雇主类型", 10),
    ("星座运势", 789),
    ("星座", 316),
    ("算命", 303),
    ("解梦", 196),
    ("风水", 93),
    ("面相分析", 47),
    ("手相", 32),
    ("公益", 90),
]

c = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 100],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义文字样式"))
)
c.render_notebook()
```

<div style="text-align: center;"><img alt='202403301956194' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301956194.png' width=500px> </div>

## 直角坐标系图表

### 柱状图

* 新增 X 轴数据:`add_xaxis`
    * `xaxis_data`:x轴数据项
* 新增 Y 轴数据:`add_yaxis`
    * `series_name`:系列名称，用于 tooltip 的显示，legend 的图例筛选
    * `y_axis`:y轴数据项
    * `is_selected`：是否选中图例
    * `color`:柱体的颜色
    * `stack`:数据堆叠，同个类目轴上系列配置相同的stack值可以堆叠放置
    * `bar_max_width`:柱条的最大宽度
    * `bar_min_width`:柱条的最小宽度
    * `category_gap`: 同一系列的柱间距离
    * `gap`:不同系列的柱间距离
    * `label_opts`:标签配置项
    * `markpoint_opts`:标记点配置项
    * `markline_opts`:标记线配置项
    * `tooltip_opts`:提示框组件配置项
    * `itemstyle_opts`:图元样式配置项

```python
(
    Bar(init_opts=opts.InitOpts(animation_opts=opts.AnimationOpts(animation_delay=10)))
    .add_xaxis(xaxis_data=Faker.choose())
    .add_yaxis(series_name="商家A",y_axis=Faker.values(),bar_min_width=40)
    .add_yaxis(series_name="商家B",y_axis=Faker.values(),bar_min_width=40)
    .set_global_opts(title_opts=opts.TitleOpts(title="标题",subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301958293' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301958293.png' width=500px> </div>

#### 旋转x轴标签

通过设置**坐标轴配置项**可以旋转x轴标签

```python
(
    Bar()
    .add_xaxis(
        [
            "名字很长的X轴标签1",
            "名字很长的X轴标签2",
            "名字很长的X轴标签3",
            "名字很长的X轴标签4",
            "名字很长的X轴标签5",
            "名字很长的X轴标签6",
        ]
    )
    .add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
    .add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题"),
    )
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301958724' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301958724.png' width=500px> </div>

#### 层叠柱状图

指定**相同的stack值**可以层叠数据

```python
(
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), stack="stack1")
    .add_yaxis("商家B", Faker.values(), stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301959719' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301959719.png' width=500px> </div>

#### 横向柱状图

横向柱状图可以通过`reversal_axis()`反转x,y轴来控制

```python
(
    Bar(init_opts=opts.InitOpts(height = '800px',width = '600px',animation_opts=opts.AnimationOpts(animation_delay=10)))
    .add_xaxis(xaxis_data=Faker.choose())
    .add_yaxis(series_name="商家A",y_axis=Faker.values(),bar_min_width=40)
    .add_yaxis(series_name="商家B",y_axis=Faker.values(),bar_min_width=40)
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="标题",subtitle="副标题"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403301959608' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301959608.png' width=500px> </div>

### 箱线图

```python
v1 = [
    [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
    [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790]
]

v2 = [
    [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
    [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870]
]

(
    Boxplot()
    .add_xaxis(['ex1','ex2'])
    .add_yaxis("name",v1)
    .add_yaxis("label",v2)
    .set_global_opts(title_opts=opts.TitleOpts(title="BoxPlot-基本示例"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302000722' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302000722.png' width=500px> </div>

### 散点图

```python
(
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(),symbol_size=20)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Scatter-显示分割线"),
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    )
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302000707' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302000707.png' width=500px> </div>

### 热力图

```python
value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
(
    HeatMap()
    .add_xaxis(Faker.clock)
    .add_yaxis(
        "",
        Faker.week,
        value,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-Label 显示"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302001833' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302001833.png' width=500px> </div>

### 层叠多图

```python
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]


bar = (
    Bar()
    .add_xaxis(Faker.months)
    .add_yaxis("蒸发量", v1)
    .add_yaxis("降水量", v2)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} ml")),
    )
)
line = Line().add_xaxis(Faker.months).add_yaxis("平均温度", v3, yaxis_index=1)
bar.overlap(line).render_notebook()
```

<div style="text-align: center;"><img alt='202403302001845' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302001845.png' width=500px> </div>

## 地理图表

内置的地理图表数据集放置在`pyecharts\datasets\city_coordinates.json`、`pyecharts\datasets\countries_regions_db.json`、`pyecharts\datasets\map_filename.json`

### Geo：地理坐标系

* 方法:`add_schema`
    * `maptype`:地图类型
    * `is_roam`:是否开启鼠标缩放和平移漫游,默认开启
    * `zoom`:当前视角的缩放比例,默认为1
    * `min_scale_limit`:最小缩放值
    * `max_scale_limit`:最大缩放值
    * `label_opts`:标签配置项
    * `itemstyle_opts`:图形样式配置项
    * `regions_opts`:地图区域配置项
* 地图区域配置项(GeoRegionsOpts)的具体内容:
    * `name`:地图区域的名称，例如 '广东'，'浙江'
* 方法:`add`
    * `series_name`:系列名称，用于 tooltip 的显示，legend 的图例筛选
    * `data_pair`:数据项 (坐标点名称，坐标点值)
    * `type_`:Geo 图类型,有`scatter`, `effectScatter`, `heatmap`, `lines` 4 种,默认为`scatter`
    * `symbol_size`:标记点的大小
    * `color`:系列label颜色
    * `label_opts`:标签配置项
    * `linestyle_opts`:线条样式配置项
    * `tooltip_opts`:提示框组件配置项
    * `itemstyle_opts`:图元样式配置项

```python
(
    Geo()
    .add_schema(maptype="广东")
    .add(
        "geo",
        [list(z) for z in zip(Faker.guangdong_city, Faker.values())],
        type_=ChartType.EFFECT_SCATTER
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Geo-广东地图")
    )
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302002027' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302002027.png' width=500px> </div>

### Map：地图

* 方法:`add`
    * `series_name`:系列名称，用于 tooltip 的显示，legend 的图例筛选
    * `data_pair`:地图数据项 (坐标点名称，坐标点值)
    * `maptype`:地图类型
    * `is_roam`:是否开启鼠标缩放和平移漫游,默认开启
    * `min_scale_limit`:最小缩放值
    * `max_scale_limit`:最大缩放值
    * `label_opts`:标签配置项
    * `linestyle_opts`:线条样式配置项
    * `tooltip_opts`:提示框组件配置项
    * `itemstyle_opts`:图元样式配置项
* `MapItem`：地图数据项
  * `name`:区域的名称
  * `value`:区域的值
  * `label_opts`:标签配置项
  * `tooltip_opts`:提示框组件配置项
  * `itemstyle_opts`:图元样式配置项

```python
province = [
    '广东省',
    '湖南省',
    '江西省',
    '北京市',
    '四川省',
    '天津市',
    '湖北省',
    '山东省',
    '山西省',
]
data = [(i,random.randint(50,150)) for i in province]
(
    Map()
    .add(series_name="map",data_pair=data,maptype='china')
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302003241' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302003241.png' width=500px> </div>

## 3D图表

### 散点图

```python
data = [(random.randint(50,250),random.randint(0,100),random.randint(100,200)) for i in range(100)]
(
    Scatter3D()
    .add("name",data)
    .render_notebook()
 )
```

<div style="text-align: center;"><img alt='202403302003980' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302003980.png' width=500px> </div>

### 折线图

```python
data = []
for i in range(10000):
    x =  math.cos(i/10)
    y = math.sin(i/10)
    z = 10-x**2-y**2
    data.append((x,y,z))
(
    Line3D()
    .add("name",data)
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302004225' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302004225.png' width=500px> </div>

## 组合图表

* 更多组合图表详情请见:https://pyecharts.org/#/zh-cn/composite_charts

### Grid：并行多图

```python
scatter = (
    Scatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Scatter"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
    )
)
line = (
    Line()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
        legend_opts=opts.LegendOpts(pos_right="20%"),
    )
)

(
    Grid()
    .add(scatter, grid_opts=opts.GridOpts(pos_left="55%"))
    .add(line, grid_opts=opts.GridOpts(pos_right="55%"))
    .render_notebook()
)
```

<div style="text-align: center;"><img alt='202403302005321' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302005321.png' width=500px> </div>

### 选项卡多图

```python
def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("商家A", Faker.days_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
    )
    return c


def pie_rosetype() -> Pie:
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例"))
    )
    return c


def grid_mutil_yaxis() -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "蒸发量",
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "降水量",
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="蒸发量",
                type_="value",
                min_=0,
                max_=250,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="温度",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="降水量",
                min_=0,
                max_=250,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            ),
            title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


tab = Tab()
tab.add(bar_datazoom_slider(), "bar-example")
tab.add(line_markpoint(), "line-example")
tab.add(pie_rosetype(), "pie-example")
tab.add(grid_mutil_yaxis(), "grid-example")
tab.render_notebook()
```

<div style="text-align: center;"><img alt='202403302006299' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302006299.png' width=500px> </div>

### Timeline：时间线轮播多图

* 方法:`add_schema`
    * `axis_type`:坐标轴的类型
    * `orient`:时间轴的布局
    * `symbol`:标记的图形
    * `symbol_size`:标记图形的大小
    * `play_interval`:播放的速度，单位为ms
    * `is_auto_play`:是否自动播放，默认False
    * `is_loop_play`:是否循环播放，默认True
    * `control_position`:播放按钮的位置,可选值包括`left`、`right`
    * `width`:时间轴区域的宽度
    * `heoght`:时间轴区域的高度
    * `linestyle_opts`:时间轴的坐标轴线配置
    * `label_opts`: 时间轴的轴标签配置
    * `itemstyle_opts`:时间轴的图形样式
* 方法:`add`
    * `chart`:图表实例
    * `time_point`:时间点

```python
attr = Faker.choose()
t = Timeline()
for i in range(2015, 2020):
    pie = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    t.add(pie, "{}年".format(i))
t.render_notebook()
```

<div style="text-align: center;"><img alt='202403302007552' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403302007552.png' width=500px> </div>






