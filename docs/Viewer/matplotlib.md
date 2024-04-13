# 可视化分析

在数据分析的过程中, 一定会遇到需要针对数据进行绘图的场景。 `Matplotlib` 是支持 Python 语言的开源绘图库, 因为其支持丰富的绘图类型、简单的绘图方式以及完善的接口文档, 深受 Python 工程师、科研学者、数据工程师等各类人士的喜欢。 `Matplotlib` 拥有着十分活跃的社区以及稳定的版本迭代

<div style="text-align: center;"><img alt='202404011930590' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404011930590.png' width=500px> </div>

* 常用的可视化工具
    * matplotlib:简单方便, 适合数值作图和科学作图(论文发表)
    * pyecharts:流程较为复杂但功能强大, 图形为交互式图形, 适合项目开发和商业开发(该库为国人开发)

## matplotlib基本绘图

作图的通用流程:
* 选择图的类型
* 导入展示图所需要的数据
* 修改配置项(如标题, 颜色, 标记,图例等)

### figure类

?> matplotlib.figure模块包含figure类, 它是所有plot元素的顶级容器, 通过调用**figure**函数来实例化Figure对象

```python
plt.figure(figsize=(10, 8), dpi)
```

| figure参数 | 描述                             |
| :--------: | :------------------------------- |
|  Figsize   | (width,height)以英寸为单位的元组 |
|    dpi     | 分辨率(每英寸点数)               |
| Facecolor  | 图的背景颜色                     |
| Edgecolor  | 图的边缘颜色                     |
| Linewidth  | 边缘宽度                         |

### Axes类

Axes对象是具有数据空间的图像区域。figure对象通过调用`add_axes()`方法将Axes对象添加到图中。

它返回轴对象并在位置[left, bottom, width, height]添加一个轴, Axes的参数是4个长度序列的[左, 底, 宽, 高]的数量

```python
#绘制简单的正弦曲线
x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x,y)
ax.set_xlabel('angle')
ax.set_ylabel('sin')
plt.show()
```

<div style="text-align: center;"><img alt='202403301724622' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301724622.png' width=500px> </div>

### 图例

```python
ax.legend(labels,loc)
```

作用:为绘图图形添加一个图例

| 参数      | 说明                                      |
| :-------- | :---------------------------------------- |
| labels    | 描述                                      |
| loc       | 位置(参数如下)                            |
| fontsize  | 设置字体大小(small,medium,large)          |
| frameon   | 设置图例边框(frameon=False为去除图例边框) |
| edgecolor | 设置边缘颜色                              |
| facecolor | 设置图例背景颜色                          |
| title     | 设置图例标题                              |

| loc位置描述  | 位置代码 |
| :----------- | -------- |
| best         | 0        |
| upper right  | 1        |
| upper light  | 2        |
| lower left   | 3        |
| lower right  | 4        |
| right        | 5        |
| center left  | 6        |
| center right | 7        |
| lower center | 8        |
| upper center | 9        |
| center       | 10       |

```python
#绘图正余弦曲线
x = np.arange(0, math.pi*2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y1)
ax.plot(x, y2)
ax.set_xlabel('angle')
ax.set_ylabel('sin or cos')
ax.legend(labels=['sinx','cosx'], loc='best')
plt.show()
```

<div style="text-align: center;"><img alt='202403301725437' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301725437.png' width=500px> </div>

### ax.plot()

作用:这是轴类最基本的用法, 它将一个数组的值与另一个数组的值绘制成线或标记

| 参数                 | 说明                             |
| :------------------- | :------------------------------- |
| color                | 颜色                             |
| alpha                | 透明度,0-1之间,默认为0(即不透明) |
| linestyle(ls)        | 线型                             |
| linewidth(lw)        | 线宽(可以是浮点数)               |
| marker               | 点类型                           |
| markersize(ms)       | 点大小                           |
| markeredgewidth      | 点边缘的宽度                     |
| markeredgecolor(mec) | 点边缘的颜色                     |
| markerfacecolor(mfc) | 点内部的颜色                     |

```python
#绘图正余弦曲线
x = np.arange(0,math.pi*2,0.05)
y1 = np.sin(x)
y2 = np.cos(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, y1,'r-')
ax.plot(x, y2, color='g', linestyle='--', linewidth=1, marker='s', markersize=2, alpha=0.5)
ax.set_xlabel('angle')
ax.set_ylabel('sin or cos')
ax.legend(labels=['sinx','cosx'], loc='best')
plt.show()
```

<div style="text-align: center;"><img alt='202403301726519' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301726519.png' width=500px> </div>

### axes和figure的关系

figure是用于直观性图形输出的窗口个体,层次级别最高级的对象

axes是一个画图区域, 也就是坐标对象, 同时也确定作图的一些方式,如标题,x标签,y标签等

axis对象要考虑轴上表示的数值,定义限制等

figure上可以由对个axes,axes必须在figure上,画图必须有axes

figure,axes和axis的关系图如下:

<div style="text-align: center;"><img alt='202403301727047' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301727047.png' width=500px> </div>

### 画布上创建多个子图

```python
plt.subplot(nrows,ncols,index)
```

作用:返回给定网格的axes对象

注意:

1. 该函数创建并返回一个Axes对象,索引index从$1$到$nrows\times ncols$
2. 若nrows,ncols和index都小于10,则索引也可以作为单个, 连接, 三个数字给出, 即subplot(2,3,3)与subplot(233)等价

```python
fig = plt.figure(figsize=(8,6), dpi=100)
ax1 = plt.subplot(2, 1, 1)
ax1.plot(range(12))
ax2 = plt.subplot(212, facecolor='y')
ax2.plot(range(12), color='g')
plt.show()
```

<div style="text-align: center;"><img alt='202403301728729' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301728729.png' width=500px> </div>

```python
plt.subplots(nrows,ncols)
```

作用:该函数返回一个图形对象和一个包含$nrows\times ncols$的轴对象的元组, 每个轴对象可以通过索引访问

```python
ax, axlist = plt.subplots(2, 2) # ax为图形对象, axlist为轴对象
x = np.arange(1,10)
axlist[0][0].plot(x,x*x,color='b')
axlist[0][1].plot(x,np.exp(x),color='g')
axlist[1][0].plot(x,np.sqrt(x),color='y')
axlist[1][1].plot(x,np.log(x),color='r')
plt.show()
```

<div style="text-align: center;"><img alt='202403301737660' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301737660.png' width=500px> </div>

`subplot2grid()`

特点；创建轴对象提供了更大的灵活性, 允许轴对象跨越多个行或列

| 参数    | 描述               |
| :------ | :----------------- |
| shape   | 形状,即nrows*ncols |
| loc     | 起始位置           |
| colspan | 占的列数           |
| rowspan | 占的行数,默认是1   |

```python
ax1 = plt.subplot2grid(shape=[3,3],loc=[0,0],colspan=2,rowspan=1)
ax2 = plt.subplot2grid(shape=[3,3],loc=[0,2],colspan=1,rowspan=3)
ax3 = plt.subplot2grid(shape=[3,3],loc=[1,0],colspan=2,rowspan=2)
x = np.arange(1,10)
ax1.plot(x,x**3)
ax1.set_title('cubic root')
ax2.plot(x,np.exp(x))
ax2.set_title('exponential')
ax3.plot(x,np.sqrt(x))
ax3.set_title('square root')
plt.show()
```

<div style="text-align: center;"><img alt='202403301738790' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301738790.png' width=500px> </div>

### 网格

axes对象中的grid()函数可以设置网格,具体参数如下: 

| 参数          | 描述                                       |
| :------------ | :----------------------------------------- |
| which         | major(默认),minor,both                     |
| axis          | 设置哪个方向(x,y,both)的网格线(默认是both) |
| color         | 颜色                                       |
| linestyle(ls) | 网格线的样式                               |
| linewidth(lw) | 网格线的宽度                               |

网格默认是关闭的,通过调用grid函数即可打开网格,打开无样式的网格可以使用grid*(True)

```python
x = np.arange(1,10,0.05)
ax,axlist=plt.subplots(2,2)
axlist[0][0].grid(True)
axlist[0][0].plot(x,x*x)
axlist[0][1].plot(x,np.sin(x))
axlist[1][0].grid(color='g',ls='-',lw=2)
axlist[1][0].plot(x,np.cos(x),color='r')
axlist[1][1].grid(color='r')
axlist[1][1].plot(x,np.sqrt(x))
```

<div style="text-align: center;"><img alt='202403301740448' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301740448.png' width=500px> </div>

### `fmt`参数

fmt 参数定义了基本格式, 如标记、线条样式和颜色

| color | 颜色          |
| :---- | :------------ |
| b     | blue          |
| g     | green         |
| r     | red           |
| c     | cyan(青色)    |
| m     | magenta(品红) |
| y     | yellow        |
| k     | black         |
| w     | white         |

| marker | 描述         |
| :----- | :----------- |
| .      | 点标记       |
| ,      | 像素         |
| o      | 圆形标记     |
| ^      | 朝上的三角形 |
| s      | 正方形       |
| p      | 五角形       |
| D      | 钻石形       |
| d      | 小版钻石形   |

| line        | 简写 | 描述     |
| :---------- | :--- | :------- |
| solid(默认) | -    | 实线     |
| dashed      | --   | 虚线     |
| dashdot     | -.   | 单点划线 |
| dotted      | :    | 点虚线   |

```python
fmt = '[marker][line][color]'
```

```python
ypoints = np.array(range(10))
plt.plot(ypoints, 'o:r')
```

<div style="text-align: center;"><img alt='202403301742136' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301742136.png' width=500px> </div>

### 轴标签与标题

* 坐标轴的结构通常包含轴脊和刻度
* 坐标轴是`axis.Axis`类的对象
* 轴脊是`spines.Spines`类的对象
    * x轴是`axis.Xaxis`类的对象
    * y轴是`axis.Yaxis`类的对象

#### 设置x轴

* 可以通过`ax.set_xlabel`来设置x轴的刻度标签
* 常用参数如下:
    * `xlabel`:str类型,设置x轴标签刻度的文本
    * `rotation`:int类型,设置文本方向,rotation=45可以将标签旋转45度
    * `labelpad`:设置文本与坐标轴之间的距离,默认值为4
    * `fontdict`:dict类型,用于设置字体属性,如{'fontsize':12,'fontweight':bold,'color':red}

#### 设置y轴

* 可以通过`ax.set_ylabel`来设置y轴的刻度标签
* 常用参数如下:
    * `ylabel`:str类型,设置x轴标签刻度的文本
    * `rotation`:int类型,设置文本方向,rotation=45可以将标签旋转45度
    * `labelpad`:设置文本与坐标轴之间的距离,默认值为4
    * `fontdict`:dict类型,用于设置字体属性,如{'fontsize':12,'fontweight':'bold','color':'red'}

```python
fig = plt.figure(figsize=(6,4))
ax = fig.add_axes([0,0,1,1])
x = np.arange(10)
ax.plot(x,x**2)
ax.set_xlabel(xlabel = 'x',rotation = 0,fontdict = {'fontsize':16,'fontweight':'bold','color':'green'})
ax.set_ylabel(ylabel = 'y',rotation = 0,labelpad = 20)
```

<div style="text-align: center;"><img alt='202403301744426' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301744426.png' width=500px> </div>

#### 设置刻度线

* `plt.tick_params()` 是matplotlib中pyplot模块的一个函数, 用于设置刻度线和标签的参数。以下是tick_params()函数可接受的参数及其意义: 
* axis（字符串或字符串列表）: 可选参数, 指定要设置的轴。可以是以下值之一: 
    * `x`: x轴
    * `y`: y轴
    * `both`: 同时设置x轴和y轴,默认为`both`
* which（字符串）: 可选参数, 指定要设置的刻度线类型。可以是以下值之一: 
    * `major`: 主刻度线
    * `minor`: 次刻度线
    * `both`: 同时设置主刻度线和次刻度线,默认为`both`。
* direction（字符串）: 可选参数, 指定刻度线的方向。可以是以下值之一: 
    * `in`: 刻度线朝内
    * `out`: 刻度线朝外
    * `inout`: 刻度线朝内外都有,默认为`inout`。
* length（浮点数）: 可选参数, 指定刻度线的长度。默认为4。
* width（浮点数）: 可选参数, 指定刻度线的宽度。默认为1。
* color（字符串或元组）: 可选参数, 指定刻度线的颜色。: 
    * 可以是单一颜色或者是一个表示RGB颜色的元组, 例如(0.5, 0.5, 0.5)代表灰色。默认为'black'。
* pad（浮点数）: 可选参数, 指定刻度线与标签之间的间距。默认为4。
* labelsize（字符串或整数）: 可选参数, 指定刻度标签的字体大小。默认为None, 表示使用默认字体大小。

```python
x = np.array(["C", "C++", "Python", "PHP"])
height = np.array([12, 22, 6, 18])
fig = plt.figure(figsize=(6,4),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.bar(x, height=height, width=0.5, align='center', color=['b','r','g','y'])
plt.tick_params(axis = 'both',labelsize = 16,color = 'g',direction = 'in')
plt.show()
```

<div style="text-align: center;"><img alt='202403301745123' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301745123.png' width=500px> </div>

#### 设置网格

* `ax.xaxis.grid`用于设置x轴的网格, 具体参数如下:
* `b`: 是否显示网格线。布尔值或None, 可选参数。如果没有关键字参数, 则b为True, 如果b为None且没有关键字参数, 相当于切换网格线的可见性
* `which`: 网格线显示的尺度。字符串, 可选参数, 取值范围为{'major', 'minor', 'both'}, 'major'为主刻度、'minor'为次刻度,默认为'major'
* `**kwargs`: 其他参数,例如:color,linewidth(lw),linestyle(ls),详情请见上文`ax.plot()`

```python
x = np.array(["C", "C++", "Python", "PHP"])
height = np.array([12, 22, 6, 18])
fig = plt.figure(figsize=(6,4),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.bar(x,height=height,width=0.5,align='center',color=['b','r','g','y'])
ax.yaxis.grid(which = 'both',lw = 0.4,ls = '-',color = 'k')
plt.tick_params(axis = 'both',labelsize = 16,color = 'g',direction = 'in')
plt.show()
```

<div style="text-align: center;"><img alt='202403301747676' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301747676.png' width=500px> </div>

#### 设置标题和副标题

`ax.set_title()`方法用于设置图表的标题, 参数如下:
* `label`:设置标题文本
* `fondict`:设置标题的字体样式
* `loc`: 设置标题的位置,取值有`center`,`left`和`right`
* `pad`: 设置标题与轴标签之间的间距,默认为6
* `**kwargs`: 其他参数,fontsize、color、backgroudcolor等

`suptitle`用于设置标题, 参数如下:
* `t` : 字符串类型, 表示要设置的图形标题内容
* `x` 和 `y`: 浮点数类型, 表示标题的 x 轴和 y 轴方向上的位置。如果未指定, 则默认为 0.5
* `fontweight` : 可选的字符串类型或整数类型, 表示标题的字体粗细。常用的取值有 "normal"（正常）和 "bold"（加粗）。也可以是数字类型, 表示粗细的程度, 默认为 "normal"
* `fontsize` : 可选的字符串类型或整数类型, 表示标题的字号大小。常用的取值为 "medium"（中等）、"large"（大号）和 "x-large"（特大号）, 也可以是整数类型, 表示具体的字号大小, 默认为 "medium"
* `fontstyle` : 可选的字符串类型, 表示标题的字体样式。常用的取值有 "normal"（正常）和 "italic"（斜体）, 默认为 "normal"
* `color` : 可选的字符串类型, 表示标题的颜色。常用的取值有 "b"（蓝色）、"g"（绿色）、"r"（红色）、"c"（青色）等等, 也可以使用 RGB 格式来指定颜色, 默认为 None
* `backgroundcolor` :背景颜色

```python
x = np.array(["C", "C++", "Python", "PHP"])
height = np.array([12, 22, 6, 18])
fig =p lt.figure(figsize=(6,4),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.bar(x,height=height,width=0.5,align='center',color=['b','r','g','y'])
ax.yaxis.grid(which = 'both',lw = 0.6,ls = '-',color = 'k')
ax.set_title(label = '编程语言流行程度(虚假数据)',loc = 'center',pad = 20,fontsize = 16,backgroundcolor = 'g')
fig.suptitle(t = 'Figure 1',x = 0.5,y = 1.2,fontsize = 12,fontweight = 'bold',backgroundcolor = 'g',color = 'b')
```

<div style="text-align: center;"><img alt='202403301748567' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301748567.png' width=500px> </div>

## 基本绘图类型

### 条形图

```python
plt.bar(x, height, width, bottom=None,align='center',**kwargs)
```

| 参数说明 | 描述                                       |
| :------- | :----------------------------------------- |
| x        | 浮点型数组,柱形图的x轴数据                 |
| height   | 浮点型数组,柱形图的高度                    |
| width    | 浮点型数组, 柱形图的宽度,默认为0.8         |
| bottom   | 浮点型数组, 底座的y坐标,默认为0            |
| align    | 柱形图与x坐标的对齐方式,center(默认)或edge |
| **kwargs | 其他参数,如颜色等                          |

```python
x = np.array(["C", "C++", "Python", "PHP"])
height = np.array([12, 22, 6, 18])
fig = plt.figure(figsize=(8,6),dpi=100)
ax = fig.add_axes([0,0,1,1])
ax.bar(x,height=height,width=0.5,align='center',color=['b','r','g','y'])
plt.show()
```

<div style="text-align: center;"><img alt='202403301749578' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301749578.png' width=500px> </div>

#### 分组条形图

##### 两组label

```python
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig = plt.figure(figsize=(6,4))
ax = fig.add_axes([0,0,1,1])
fig1 = ax.bar(x = x - width / 2, height = men_means,width =  width,label = 'label1')
ax.bar_label(fig1)
fig2 = ax.bar(x = x + width / 2, height = women_means, width = width ,label = 'label2')
ax.bar_label(fig2)
ax.tick_params(which = 'both',labelsize = 16)
ax.set_ylabel('ylabel',rotation = 0,labelpad = 15)
ax.set_title('title',fontsize = 20,fontweight = 'bold',color = 'y')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc = 'best',fontsize = 16)
```

<div style="text-align: center;"><img alt='202403301750922' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301750922.png' width=500px> </div>

##### 两组以上的label

```python
species = ("C", "Java", "Python","PHP")
penguin_means = {
    'label1': (18.35, 18.43, 14.98,12),
    'label2': (38.79, 48.83, 47.50,48),
    'label3': (189.95, 195.82, 199.19,200),
    'label4':(13,45,76,98)
}

x = np.arange(len(species))  # the label locations
width = 0.2  # the width of the bars
multiplier = 0
fig = plt.figure(figsize=(6,4))
ax=fig.add_axes([0,0,1,1])
for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=0)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.tick_params(which = 'both',labelsize = 16)
ax.set_ylabel('Length (mm)',rotation = 0,labelpad = 10)
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=4,fontsize=10)
ax.set_ylim(0, 250)
plt.show()
```

<div style="text-align: center;"><img alt='202403301750941' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301750941.png' width=500px> </div>

#### 层叠柱状图

```python
species = (
    "Adelie\n $\\mu=$3700.66g",
    "Chinstrap\n $\\mu=$3733.09g",
    "Gentoo\n $\\mu=5076.02g$",
)
weight_counts = {
    "Below": np.array([70, 31, 58]),
    "Above": np.array([82, 37, 66]),
}
width = 0.5

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes([0, 0, 1, 1])
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count
    ax.bar_label(p, label_type='center')

ax.tick_params(which='both', labelsize=16)
ax.set_title("Number of penguins with above average body mass", fontsize=16)
ax.legend(loc="upper right", fontsize=16)

plt.show()
```

<div style="text-align: center;"><img alt='202403301750056' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301750056.png' width=500px> </div>

#### 横向条形图

```python
plt.barh(x,height,width,bottom,align,**kwargs)
```

| 参数说明 | 描述                                       |
| :------- | :----------------------------------------- |
| x        | 浮点型数组,柱形图的x轴数据                 |
| height   | 浮点型数组,柱形图的宽度,默认为0.8          |
| width    | 浮点型数组, 柱形图的高度                   |
| bottom   | 浮点型数组, 底座的x坐标,默认为0            |
| align    | 柱形图与y坐标的对齐方式,center(默认)或edge |
| **kwargs | 其他参数,如颜色等                          |

```python
x = np.array(["C", "C++", "Python", "PHP"])
width= np.array([12, 22, 6, 18])

fig = plt.figure(figsize=(8,6),dpi=100)
ax = fig.add_axes([0,0,1,1])
p = ax.barh(x,height=0.5,width=width,align='center',color=['b','r','g','y'])
ax.bar_label(p,padding = 0)

ax.xaxis.grid(which = 'both',lw = 0.5,color = 'k')
plt.show()
```

<div style="text-align: center;"><img alt='202403301751091' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301751091.png' width=500px> </div>

### 散点图

```python
plt.scatter(x,y,s=None,c=None,marker=None,cmap=None,norm=None,vmin=None,vmax=None,alpha=None,linewidths=None,edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

| 参数          | 描述                                                                                  |
| :------------ | :------------------------------------------------------------------------------------ |
| x,y           | 长度相同的数组,输入数据                                                               |
| s             | 点的大小,默认20,也可以是个数组,即每个点大小的参数                                     |
| c             | 点的颜色,默认蓝色 'b'                                                                 |
| marker        | 点的样式,默认小圆圈 'o'                                                               |
| cmap          | Colormap,颜色条,默认None,标量或者是一个colormap的名字,只有c是一个浮点数数组的时才使用 |
| norm          | Normalize默认None,数据亮度在 0-1 之间, 只有c是一个浮点数的数组的时才使用              |
| vmin, vmax    | 亮度设置, 在 norm 参数存在时会忽略                                                    |
| alpha         | 透明度设置, 0-1 之间, 默认 None, 即不透明                                             |
| linewidths    | 标记点的长度                                                                          |
| edgecolors    | 颜色或颜色序列, 默认为 'face', 可选值有 'face', 'none', None                          |
| plotnonfinite | 布尔值, 设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点                             |
| **kwargs      | 其他参数                                                                              |

cmap参数详情请见:[颜色条参数](https://www.runoob.com/matplotlib/matplotlib-scatter.html)

```python
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
fig=plt.figure(figsize=(6,4))
ax=fig.add_axes([0,0,1,1])
ax.scatter(x,y,c=['b','r','y','c','m','k','w','b'])
plt.show()
```

<div style="text-align: center;"><img alt='202403301752116' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301752116.png' width=500px> </div>

#### 气泡图

```python
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
```

<div style="text-align: center;"><img alt='202403301752071' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301752071.png' width=500px> </div>

### 饼图

```python
plt.scatter(x, y, s=None, c=None,marker=None,cmap=None,norm=None,vmin=None,vmax=None,alpha=None,linewidths=None,edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

| 参数          | 描述                                                                                                                  |
| :------------ | :-------------------------------------------------------------------------------------------------------------------- |
| x             | 浮点型数组, 表示每个扇形的面积                                                                                        |
| explode       | 数组, 表示各个扇形之间的间隔, 默认值为0                                                                               |
| labels        | 列表, 各个扇形的标签, 默认值为 None                                                                                   |
| colors        | 数组, 表示各个扇形的颜色, 默认值为 None                                                                               |
| autopct       | 设置饼图内各个扇形百分比显示格式, %d%% 整数百分比,%0.1f一位小数,%0.1f%%一位小数百分比,%0.2f%% 两位小数百分比          |
| labeldistance | 标签标记的绘制位置, 相对于半径的比例, 默认值为 1.1, 如 <1则绘制在饼图内侧。                                           |
| pctdistance   | 类似于labeldistance, 指定autopct的位置刻度, 默认值为 0.6                                                              |
| shadow        | 布尔值True或False,设置饼图的阴影, 默认为 False, 不设置阴影                                                            |
| radius        | 设置饼图的半径, 默认为 1。                                                                                            |
| startangle    | 起始绘制饼图的角度, 默认为从x轴正方向逆时针画起, 如设定=90 则从y轴正方向画起                                          |
| counterclock  | 布尔值, 设置指针方向, 默认为 True, 即逆时针, False 为顺时针。                                                         |
| wedgeprops    | 字典类型, 默认值 None。参数字典传递给 wedge 对象用来画一个饼图。例如: wedgeprops={'linewidth':5} 设置 wedge 线宽为5。 |
| textprops     | 字典类型, 默认值为: None。传递给 text 对象的字典参数, 用于设置标签（labels）和比例文字的格式。                        |
| center        | 浮点类型的列表, 默认值: (0,0)。用于设置图标中心位置。                                                                 |
| frame         | 布尔类型, 默认值: False。如果是 True, 绘制带有表的轴框架。                                                            |
| rotatelabels  | 布尔类型, 默认为 False。如果为 True, 旋转每个 label 到指定的角度                                                      |

```python
fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
labels = ['C', 'C++', 'Python', 'PHP']
colors = ['b', 'r', 'g', 'c']
x = np.array([30, 25, 35, 10])
ax.pie(x, labels=labels, colors=colors, radius=1,
       autopct='%1.2f%%', shadow=True, explode=[0, 0, 0.1, 0.1])
plt.show()
```

<div style="text-align: center;"><img alt='202403301753239' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301753239.png' width=500px> </div>

#### bar of pie

```python
from matplotlib.patches import ConnectionPatch

# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)

# pie chart parameters
overall_ratios = [.27, .56, .17]
labels = ['Approve', 'Disapprove', 'Undecided']
explode = [0.1, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
# bar chart parameters
age_ratios = [.33, .54, .07, .06]
age_labels = ['Under 35', '35-49', '50-65', 'Over 65']
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax2.set_title('Age of approvers')
ax2.legend()
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)
# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(age_ratios)
# draw top connecting line
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]
con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)
# draw bottom connecting line
x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)
plt.show()
```

<div style="text-align: center;"><img alt='202403301754751' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301754751.png' width=500px> </div>

#### 嵌套饼图

```python
fig, ax = plt.subplots()
size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])
ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))
ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```

<div style="text-align: center;"><img alt='202403301754114' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301754114.png' width=500px> </div>

### 箱线图

箱线图也叫须状图, 显示包含最小值, 第一四分位数, 中位数, 第三四分位数和最大值的一组数据的摘要

```python
plt.boxplot(x,notch,sym,vert,whis,positions,
         widths,patch_artist,meanline,
         showmeans,showcaps,showbox,
         showfliers,boxprops,medianprops,
         capprops,whiskerprops)
```

| 参数         | 描述                                                  |
| :----------- | :---------------------------------------------------- |
| x            | 要绘制箱线图的数据                                    |
| notch        | 是否是凹口的形式展现箱线图, 默认非凹口；              |
| sym          | 指定异常点的形状, 默认为+号显示；                     |
| vert         | 是否需要将箱线图垂直摆放, 默认垂直摆放；              |
| whis         | 指定上下须与上下四分位的距离, 默认为1.5倍的四分位差； |
| positions    | 指定箱线图的位置                                      |
| widths       | 指定箱线图的宽度, 默认为0.5；                         |
| patch_artist | 是否填充箱体的颜色；                                  |
| meanline     | 是否用线的形式表示均值, 默认用点来表示；              |
| showmeans    | 是否显示均值, 默认不显示；                            |
| showcaps     | 是否显示箱线图顶端和末端的两条线, 默认显示；          |
| showbox      | 是否显示箱线图的箱体, 默认显示；                      |
| showfliers   | 是否显示异常值, 默认显示；                            |
| boxprops     | 设置箱体的属性, 如边框色, 填充色等；                  |
| labels       | 为箱线图添加标签, 类似于图例的作用；                  |
| flierprops   | 设置异常值的属性, 如异常点的形状、大小、填充色等      |
| medianprops  | 设置中位数的属性, 如线的类型、粗细等；                |
| meanprops    | 设置均值的属性, 如点的大小、颜色等；                  |
| capprops     | 设置箱线图顶端和末端线条的属性, 如颜色、粗细等；      |
| whiskerprops | 设置须的属性, 如颜色、粗细、线的类型等                |

```python
fig = plt.figure(figsize=(8,6))
ax = fig.add_axes([0,0,1,1])
np.random.seed(10)
x_1 = np.random.normal(100,10,200)
x_2 = np.random.normal(80,30,200)
x_3 = np.random.normal(90,20,200)
x_4 = np.random.normal(70,25,200)
ax.boxplot(x = [x_1, x_2, x_3, x_4], showmeans=True, patch_artist=True, widths=0.4)
plt.show()
```

<div style="text-align: center;"><img alt='202403301755231' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202403301755231.png' width=500px> </div>