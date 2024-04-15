# 机器学习与数据挖掘基础

?> 机器学习(machine learning):研究如何通过计算的手段，利用经验来改善系统自身的性能。在计算机上从数据中产生“模型”的算法，即“学习算法”(learning algorithm)

?> 数据挖掘（data mining）: 从大量的数据中通过<strong>算法</strong>搜索<strong>隐藏</strong>于其中的信息的过程

<div style="text-align: center;"><img alt='202404082100402' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082100402.png' width=500px> </div>

## 机器学习分类

<div style="text-align: center;"><img alt='202404082114110' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082114110.png' width=500px> </div>

?> **有监督学习**: 输入数据带有标签

?> **无监督学习**: 输入数据不带标签

<div style="text-align: center;"><img alt='202404082104422' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082104422.png' width=500px> </div>

### 监督v.s.无监督在数据集中的表现

<div style="text-align: center;"><img alt='202404082105152' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082105152.png' width=500px> </div>

<div style="text-align: center;"><img alt='202404082105362' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082105362.png' width=500px> </div>

## 数据挖掘建模流程

<div style="text-align: center;"><img alt='202404082119422' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082119422.png' width=500px> </div>

### `scikit-learn` 介绍

```bash
pip install -U scikit-learn
```

* `scikit-learn` 是Python的一个开源机器学习模块，它建立在 `NumPy` ， `SciPy` 和 `matplotlib` 模块之上
* 为用户提供各种机器学习算法接口，可以让用户简单、高效地进行数据挖掘和数据分析

#### 内置数据

两种类型数据的加载方式
* 小规模数据：`load_数据名称()`
* 大规模数据：`fetch_数据名称()`

返回的数据的结构：字典结构，至少包括两个关键字
* `data` ：属性（特征）， `numpy` 格式的矩阵，有`n_samples`行和`n_features`列
* `target` ：标签， `numpy` 格式的数组，长度是`n_samples`
* 返回的数据具有`DESCR`属性，给予数据集详细描述

##### 小规模数据集

命令|数据描述|适合的方法
---|---|---
`load_boston()`|波士顿的房价数据|回归
`load_iris()`|鸢尾花（iris）数据集|分类
`load_diabetes()`|糖尿病(diabetes)数据集|回归
`load_digits()`|手写体数据集|分类
`load_linnerud()`|体能训练数据集|多元回归
`load_wine()`|酒类数据集|分类
`load_breast_cancer()`|威斯康星乳腺癌|分类

##### 大规模数据集

命令|数据描述|适合的方法
---|---|---
`fetch_olivetti_faces()`|Olivetti人脸识别数据|分类
`fetch_20newsgroups()`|包括20个话题的新闻文本数据|分类
`fetch_20newsgroups_vectorized()`|包括20个话题的新闻文本向量化数据|分类
`fetch_lfw_people()`|带标签的人脸识别数据|分类
`fetch_lfw_pairs()`|带标签的人脸识别数据|分类
`fetch_covtype()`|森林植被类型数据|分类
`fetch_rcv1()`|路透社英文新闻文本数据|分类
`fetch_kddcup99()`|网络入侵检测数据|分类
`fetch_california_housing()`|加利福尼亚房价数据|回归

### 机器学习的一般流程

<div style="text-align: center;"><img alt='202404082118831' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404082118831.png' width=500px> </div>

