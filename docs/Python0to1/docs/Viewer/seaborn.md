# `seaborn`

`Matplotlib` 应该是基于 Python 语言最优秀的绘图库了，但是它也有一个十分令人头疼的问题，那就是太过于复杂了。3000 多页的官方文档，上千个方法以及数万个参数，属于典型的你可以用它做任何事，但又无从下手。尤其是，当你想通过 `Matplotlib` 调出非常漂亮的效果时，往往会伤透脑筋，非常麻烦

`Seaborn` 基于 `Matplotlib` 核心库进行了更高阶的 API 封装，可以让你轻松地画出更漂亮的图形。 `Seaborn` 的漂亮主要体现在配色更加舒服、以及图形元素的样式更加细腻

## 快速优化图形

当我们使用 `Matplotlib` 绘图时，默认的图像样式算不上美观。此时，就可以使用 `Seaborn` 完成快速优化。下面，我们先使用 `Matplotlib` 绘制一张简单的图像

```python
import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
y_bar = [3, 4, 6, 8, 9, 10, 9, 11, 7, 8]
y_line = [2, 3, 5, 7, 8, 9, 8, 10, 6, 7]

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
```

<div style="text-align: center;"><img alt='202404012028004' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404012028004.png' width=500px> </div>

`sns.set()` 的默认参数为:
```python
sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=False, rc=None)
```

使用 `Seaborn` 完成图像快速优化的方法非常简单。只需要将 `Seaborn` 提供的样式声明代码 `sns.set()` 放置在绘图前即可

```python
import seaborn as sns

sns.set()  # 声明使用 Seaborn 样式

plt.bar(x, y_bar)
plt.plot(x, y_line, '-o', color='y')
```

<div style="text-align: center;"><img alt='202404012029902' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404012029902.png' width=500px> </div>
