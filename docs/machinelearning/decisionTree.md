# 分类技术——决策树

!> 分类技术是数据挖掘、机器学习和模式识别中一个重要的研究领域

## 基本概念

### 分类(classification)

* 给定一条记录$(\boldsymbol{x}, y)$，其中，$y$是分类属性或者目标属性，$\boldsymbol{x}$是该记录预测属性的集合
* 通过学习得到一个**目标函数**（target function）$f$，把每个属性集$\boldsymbol{x}$映射到一个预先定义的**类标签**$y$
$$
y = f(\boldsymbol{x})
$$
* 目标函数也被称作**分类模型**（classification model）

### 分类模型的功能

* **描述性建模**：识别哪些属性决定一个数据记录属于哪个类别
* **预测性建模**：根据已知的数据记录的属性，自动识别该数据记录属于的类别

### 分类模型的适用领域

* 非常适合分类属性是**二元**或者**标称类型**的数据集
* 不适用于分类属性是**序数**或**连续类型**的数据集
    * 因为没有考虑标签之间的顺序大小关系

任务|属性集$\boldsymbol{x}$|分类属性$y$
---|---|---
分类e-mail|从e-mail的header和内容中提取的特征|垃圾邮件`or`非垃圾邮件
识别癌变细胞|通过磁共振扫描提取的特征|恶性的`or`良性的
分类星系|从天文望远镜获取的图像中提取特征|椭圆的、螺旋的、`or`不规则星系


## 建立分类模型的一般方法

<div style="txt-align: center">
    <img src='https://pic1.zhimg.com/v2-b2a660c48ecfcc27f70442a14fabf584_720w.jpg?source=d16d100b'>
</div>

### 训练集与检验集

* 训练集（training set）：由类标签已知的数据记录组成，用于建立分类模型
* 检验集（test set）：用来检验分类规则的数据记录集合

```python
from sklearn.model_selection import train_test_split
train_test_split(*arrays, test_size=0.25, random_state=None)
```

* `*arrays`：需要被划分的数据序列，可以是`list`类型、`numpy.arrays`类型，`pandas.DataFrame`类型
* `test_size`：检验集的规模, 默认为$0.25$
    * `float`类型，取值范围$[0,1]$，表示检验集占原数据集的比例
    * `int`类型，表示检验集包含的数据记录的绝对数量
* `random_state`：随机数种子
    * `int`类型，范围为$[0, 2^{32}-1]$
    * 控制在划分检验集之前对数据的随机排序

### 分类算法

* k最近邻分类
* **决策树**
* **随机森林**
* 朴素贝叶斯分类
* 逻辑回归
* **神经网络**
* 支持向量机

### 混淆矩阵（confusion matrix）

* 由分类模型做出的正确和错误的分类结果构成的矩阵
* 二元分类问题的混淆矩阵

<div style="text-align: center;"><img alt='202404211321997' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211321997.png' width=500px> </div>

### 分类问题的性能度量（performance metric）

<div style="text-align: center;"><img alt='202404211345622' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211345622.png'> </div>

#### 汇总混淆矩阵的信息

```python
from sklearn import metrics    
metrics.confusion_matrix(y_true, y_pred) # 计算混淆矩阵 
metrics.plot_confusion_matrix(estimator, X, y_true, values_format=None) # 绘制混淆矩阵
```

* `estimator`：训练好的分类器
* `X`：预测属性
* `y_true`：分类属性
* `values_format`：数字的显示格式

#### 准确率

$$
准确率=\frac{正确预测数}{预测总数}=\frac{f_{11}+f_{00}}{f_{11}+f_{10}+f_{01}+f_{00}}
$$  

```python
from sklearn import metrics
metrics.accuracy_score(y_true, y_pred)
```
* `y_true`：真实类标签构成的数组
* `y_pred`：分类模型预测的类标签构成的数组

#### 召回率 （recall score）

```python
metrics.recall_score(y_true, y_pred, pos_label=1)
```

#### 精确率（precision score）

```python
from sklearn import metrics
metrics.precision_score(y_true, y_pred, pos_label=1)
```

#### $F_1$ score

!> 同时考虑召回率和精确率，是召回率和精确率的调和均值

```python
from sklearn import metrics
metrics.f1_score(y_true, y_pred, pos_label=1)
```

#### P-R曲线

* 由精确率和召回率构成的图线
* x轴为召回率，y轴为精确率

```python
from sklearn import metrics
metrics.precision_recall_curve(y_true, probas_pred, *, pos_label=None)
```
* `probas_pred`：预测的每个样本属于`pos_label`指定类别的概率
* 返回在每个阈值下的精确率、召回率和按升序排列的阈值
* 给定一个阈值，计算`probas_pred`>=该阈值时候的精确率和召回率

#### ROC曲线

* Receiver Operating Characteristic (ROC) Curve, 由“真正例率”（True Positive Rate）和“假正例率”（False Positive Rate）构成的曲线
$$
TPR = \frac{TP}{TP+FN}\\
FPR = \frac{FP}{FP+TN}
$$
* x轴是FPR，y轴是TPR

```python
from sklearn import metrics
metrics.plot_roc_curve(estimator, X, y, pos_label)
```
*`estimator`：训练过的分类模型
*`X`：输入的属性
*`y`：标签值（二元标签）
*`pos_label`：`int`或`str`，指定类别，默认为1

!> `AUC`：area under curve，ROC曲线下面积，越大越好

* 两种曲线的选用条件
    * ROC，适用于类别均衡情况
    * PR，适用于类别不均衡情况

## 决策树

 <div style="text-align: center;"><img alt='202404211334743' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211334743.png' width=500px> </div>

 > 对于同一个问题而言，决策树不是唯一的

 ### 基本概念

* **根结点**（root node）
    * 没有入边，但有零条或多条出边
* **内部结点**（internal node）
    * 恰有一条入边和两条或多条出边
* **叶结点**（leaf node）
    * 恰有一条入边，但没有出边
    * 又被称为终结点（terminal node）
* 每个叶结点赋予一个类标签
* 每个**非叶**结点包含属性测试的条件

<div style="text-align: center;"><img alt='202404211335989' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211335989.png' width=500px> </div>

### 构造决策树

* `Hunt` 算法
* CART
* ID3, C4.5
* SLIQ, SPRINT

#### Hunt算法基本思路

假设$D_t$是一个训练集，构成一个结点$t$
* 如果$D_t$包含的所有数据对象都属于同一个类别$y_t$，那么结点$t$是一个叶结点，标记为$y_t$
* 如果$D_t$包含的数据对象属于多个类别，那么用一个属性尝试将数据对象分成子集。之后，对每个子集再递归应用以上步骤

<div style="text-align: center;"><img alt='202404211340611' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211340611.png' width=500px> </div>

#### 构造决策树需要考虑的问题 

* 如何选择测试条件？
    * 选择哪个属性作为分裂的条件？
    * 针对每个条件应当如何选择划分点？即，如何评估划分的优劣
* 如何停止树的增长？
    * 直到所有的数据对象都属于**相同**的类别，或都有**相同**的属性值
    * 其他方法

### 选择最佳划分

* 最佳选择划分通常根据结点的**不纯性的程度**（degree of impurity）
* 不纯的程度越低，类分布就越倾斜

#### 不纯性度量 

令$p(i|t)$表示给定结点$t$中属于类$i$的记录所占的比例，类别个数为$c$

* 熵（Entropy）：衡量系统中混乱或不确定性的程度

$$ \text{Entropy}(t)=-\sum_{i=0}^{c-1}p(i|t)\log_2p(i|t) $$

?> ID3、C4.5算法用熵选择最佳划分

* Gini系数

$$ \text{Gini}(t)=1-\sum_{i=0}^{c-1}\left[p(i|t)\right]^2 $$

* Gini系数可以直观认为是衡量分类错误的概率

$$\text{Gini}(t)=\sum_{i=0}^{c-1}p(i|t)\bigl(1-p(i|t)\bigr)$$

?> CART算法用Gini系数选择最佳划分

#### 确定测试条件

对于选择的一个测试条件（特征），计算父结点（划分前）的不纯度与子结点（划分后）的不纯度的差(即信息增益，information gain)，差越大，测试条件的效果就越好

对一个内部节点$p$，选择特征$f$划分的信息增益的计算如下：

$$IG(D_p, f)=I(D_p)-\sum_{j=1}^c\frac{N_j}{N_p}I(D_j)$$

其中，$D_p$和$D_j$分别是父节点和划分后的子节点对应的数据集，$I(\cdot)是不纯度的度量$，$N_p$和$N_j$分别是父节点和划分后的子节点中的样本数量
$$\underset{f\in\mathcal{F}}{\max}IG(D_p,f)$$

其中，$\mathcal{F}$是特征的集合

通常为了降低搜索空间，决策树算法通常构建二叉树，即，每个父节点只被划分成**两个**子节点。此时的信息增益为

$$IG(D_p,f)=I(D_p)-\frac{N_\text{left}}{N_p}I(D_\text{left})-\frac{N_\text{right}}{N_p}I(D_\text{right})$$

## sklearn实现 

### 数据预处理

#### **One-Hot Encoding**：将标称属性转换成二元属性

```python
pandas.get_dummies(data, columns=None)
```
* `data`：`Series`类型，或者`DataFrame`类型
* `columns`：列名的`list`类型，数据集中哪些列需要转换，默认是将数据集中所有列进行转换
* 返回值：由二元化的属性构成的`DataFrame`

#### 分割训练集与测试集

```python
from sklearn.model_selection import train_test_split
train_test_split(*arrays, test_size=0.25, random_state=None)
```

* `*arrays`：需要被划分的数据序列，可以是`list`类型、`numpy.arrays`类型，`pandas.DataFrame`类型
* `test_size`：检验集的规模, 默认为$0.25$
    * `float`类型，取值范围$[0,1]$，表示检验集占原数据集的比例
    * `int`类型，表示检验集包含的数据记录的绝对数量
* `random_state`：随机数种子
    * `int`类型，范围为$[0, 2^{32}-1]$
    * 控制在划分检验集之前对数据的随机排序

### 建立模型

```python
from sklearn import tree
tree.DecisionTreeClassifier(criterion='gini')
```
* `criterion`：`str`类型，不纯性的度量，可以是`gini`和`entropy`，默认是`gini`

* 生成的决策树的属性（Attributes）
    * `classes_ `：由类标签构成的数组
    * `n_classes_`：`int`，类别的数量
    * `tree_`：建立的决策树
* `feature_importances_`：每个属性在构造决策树中的重要性，即每个属性导致`Gini`系数的减少量（标准化）

### 训练模型

```python
dt.fit(X, y)
```
* `X`：输入的属性矩阵，形状为`[n_samples, n_features]`
* `y`：类别标签数组，形状为`[n_samples]`

### 决策树可视化

#### 决策规则以文本形式输出

```python
tree.export_text(decision_tree, feature_names=None)
```
* `decision_tree`：训练过的决策树模型
* `feature_names`：由预测属性名称构成的列表

#### 决策规则以图形形式输出

```python
tree.plot_tree(decision_tree,max_depth=None,feature_names=None,class_names=None,filled=False,ax=None)
```
* `max_depth`：`int`类型，显示的最大树深
* `class_names`：`list`类型，类的名称，按照每个类对应数值的升序顺序
* `filled`：用颜色填充节点
* `ax`：`matplotlib`的`axis`，在指定的轴上绘制决策树

### 用决策树预测

```python
dt.predict(X)
```
* `X`：输入的属性矩阵，形状为`[n_samples, n_features]`
* 返回值：预测的类别，形状为`[n_samples]`的数组

```python
dt.predict_proba(X)
```
* 返回值：预测属于每个类别的概率，形状为[n_samples, n_classes]的矩阵，每个样本属于每个类别的概率的顺序与`dt.classes_`一致

## 模型过拟合

<div style="text-align: center;"><img alt='202404211354494' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404211354494.png' width=500px> </div>

* **训练误差（training error）**：在训练集上误分类样本的比例
* **泛化误差（generalization error）**：分类模型在未知记录上的期望误差

!> 过拟合（model overfitting）: 生成的决策树模型在**训练集**上的分类性能优异，但是在**检验集**上的分类性能一般，即一个对训练集过度匹配的分类模型可以取得非常低的训练误差，但是其泛化误差却高于训练误差

随着分类模型**复杂度**（complexity）的增加，训练误差会持续降低，但是这种模型会匹配了训练集中存在的噪声，从而导致较高的泛化误差

### 决策树的剪枝

* 剪枝方法
    * 先剪枝
    * 后剪枝

#### 先剪枝（Forward-Pruning）

?> 提前停止树的构造而对树进行剪枝

* 在决策树到达一定高度的情况下就停止树的生长
* 到达结点的样本个数小于某一个阈值可停止树的生长

```python
tree.DecisionTreeClassifier(max_depth=None, min_samples_split=2, min_samples_leaf=1)
```

* `max_depth`：`int`类型或`None`，树的最大深度。若为`None`，则所有的叶结点都只包含纯类，或者所有叶结点包含的样本数量小于`min_samples_leaf`
    * 值过大会导致算法对训练集的**过拟合**，而过小会妨碍算法对数据的学习
    * 推荐初始设置为3，先观察生成的决策树对数据的初步拟合状况，再决定是否要增加深度
* `min_samples_split`：`int`类型或`float`类型，划分一个内部结点需要的最少的样本数量。
    * `int`类型，`min_samples_split`为最小值，默认是2个样本
    * `float`类型，在全部样本中的占比，`ceil(min_samples_split * n_samples)`为最小值
    * 值越大，决策树的枝越少，达到一定的先剪枝效果
* `min_samples_leaf`：`int`类型或`float`类型，每个叶结点需要包含的最少的样本数量。
    * `int`类型，`min_samples_leaf`为最小值，默认是1个样本
    * `float`类型，在全部样本中的占比，`ceil(min_samples_leaf * n_samples)`为最小值
    * 值越大，决策树的枝越少，达到一定的先剪枝效果

#### 后剪枝（Post-Pruning）

!> 构造完整的决策树，然后用叶结点替换那些置信度不够的结点的子树，该叶结点所应标记的类别为被替换的子树中大多数样本所属的类别

```python
tree.DecisionTreeClassifier(ccp_alpha=None)
```
- `ccp_alpha`：非负的浮点数，子树的复杂度系数，复杂度系数低于该参数的子树会被剪枝

* 利用成本复杂度剪枝（cost-complexity pruning）

对于决策树$T$，定义成本复杂度的测量函数$R_{\alpha}(T)$，

$$R_{\alpha}(T)=R(T)+\alpha|\tilde{T}|$$

其中，$R(T)$是所有叶结点总不纯度（由叶结点包括的样本数量加权的）；$|\tilde{T}|$是决策树$T$中所有叶结点的数量。$\alpha$是**复杂度系数**，越大，越惩罚决策树的规模

- 如何计算$\alpha$？

定义子树$T_t$为决策树$T$中的一个内部结点$t$与该内部结点的所有子结点。$\alpha$的取值使得该内部结点本身的成本复杂度`=`子树$T_t$的成本复杂度，即

$$R_{\alpha}(T_t)=R_{\alpha}(t)$$

##### 如何选择$ccp\_alpha$?

```python
dt.cost_complexity_pruning_path(self, X, y)
```
* 返回利用成本复杂度剪枝计算过程，字典结构，包括`ccp_alpha`数组和`impurities`数组
* `X`：训练集的预测属性
* `y`：类别列表

1. 得到剪枝的`ccp_alpha`

```python
from sklearn import tree
dt = tree.DecisionTreeClassifier(criterion='gini')
ccp_path = dt.cost_complexity_pruning_path(titTrainX, titTrainY)
alphas = ccp_path['ccp_alphas']
```

2. 生成具有不同`ccp_alpha`决策树列表

```python
dts = []
for ccp_alpha in alphas[:-1]:
    # alphas[:-1]去除掉最大值，因为只包含一个节点
    dt = tree.DecisionTreeClassifier(random_state=10, ccp_alpha=ccp_alpha)
    dt.fit(titTrainX, titTrainY)
    dts.append(dt)
```

3. 计算每个决策树在训练集和检验集上的`f1-score`

```python
trainScoreLst = [metrics.f1_score(TrainY,dt.predict(TrainX)) for dt in dts]
testScoreLst = [metrics.f1_score(TestY,dt.predict(TestX)) for dt in dts]
alphaTestDf = pd.DataFrame({'a':alphas[:-1],'train':trainScoreLst,'test':testScoreLst})
ax = alphaTestDf.plot(x='a',y='train',kind='line',figsize=(12,6),marker='o')
alphaTestDf.plot(x='a',y='test',kind='line',marker='d',ax=ax)
ax.set(title='ccp_alpha v.s. accuracy',xlabel='ccp_alpha',ylabel='accuracy')
```

##### 选取最佳的`ccp_alpha`

```python
alphaTestDf.loc[(alphaTestDf['train']>=0.8)& (alphaTestDf['test']==alphaTestDf['test'].max()),:]
```



