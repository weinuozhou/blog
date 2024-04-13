# Numpy

- NumPy是一个功能强大的Python库，主要用于对多维数组执行计算
- NumPy这个词来源于两个单词：Numerical和Python
- NumPy对于执行各种数学任务非常有用，如数值积分、微分、内插、外推等，是一种基于Python的MATLAB的快速替代
- Numpy快速入门教程 [https://www.numpy.org.cn/user/quickstart.html](https://www.numpy.org.cn/user/quickstart.html)

## 数组

```python
numpy.array(list/tuple)
```

## `linspace()`函数 ，生成等差数列

```python
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False)
```

- `stop`：如果`endpoint=False`，结束值不包含在数列中
- `num`：要生成的等步长的样本数量
- `retstep`：如果为 True 时，生成的数组中会显示间距

## `logspace()`函数，生成等比数列

```python
numpy.logspace(start, stop, num=50, endpoint=True, base=10.0)
```

- `base`：对数 log 的底数

## `zeros()`函数

```python
numpy.zeros(shape, dtype=float)
```

## `ones()`函数

```python
numpy.ones(shape, dtype = float)
```

## `random`，创建随机数矩阵 

```python
numpy.random.random(shape)
```

- 创建取值在`[0, 1)`之间的随机数组

