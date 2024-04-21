# 回归预测

## 多元线性回归模型

* 一种预测建模技术
* 研究**一个或多个自变量**与**一个因变量**之间的显著关系
* 展示自变量对因变量的影响强度
* 通过已经建立的回归模型预测新的目标值

### 模型表述

假设数据集有$d$个特征，对于第$i$个样本，特征为集合$\{x_{1}^{(i)},x_{2}^{(i)},\cdots,x_{d}^{(i)}\}$则该样本的预测结果$\hat{y}^{(i)}$,可以表示为 $$\hat{y}^{(i)}=w_1x_{1}^{(i)}+w_2x_{2}^{(i)}+\cdots+w_dx_{d}^{(i)}+b$$

第$i$个样本的所有特征用向量$\boldsymbol{x}_i\in\mathbb{R}^d$表示，所有权重用向量$\boldsymbol{w}\in \mathbb{R}^d$表示，则可用向量表示为

$$
\hat{y}^{(i)}=\boldsymbol{w}^T\boldsymbol{x}^{(i)}+b
$$

全部数据集（含有$n$个样本）的特征用矩阵$\mathbf{X}\in\mathbb{R}^{n\times d}$表示，所有样本的预测值用向量$\hat{\boldsymbol{y}}\in\mathbb{R}^n$表示，则线性模型可表示为

$$
\hat{\boldsymbol{y}}=\mathbf{X}\boldsymbol{w}+b 
$$

线性模型的目标是求解**模型参数**（model parameters）
* $\boldsymbol{w}$
* $b$

### 模型求解

?> 损失函数（loss function）: 量化目标的实际值与预测值之间的差距

对于线形模型, 真实值为$y^{(i)}$，预测值为$\hat{y}^{(i)}$，可以用**平方误差**函数作为损失函数

$$l^{(i)}(\boldsymbol{w}, b) = \frac{1}{2} \left(\hat{y}^{(i)} - y^{(i)}\right)^2$$

为度量模型在整个数据集上的质量，需计算在训练集$n$个样本上的损失均值，即

$$L(\boldsymbol{w}, b) =\frac{1}{n}\sum_{i=1}^n l^{(i)}(\boldsymbol{w}, b) =\frac{1}{n} \sum_{i=1}^n \frac{1}{2}\left(\boldsymbol{w}^\top \boldsymbol{x}^{(i)} + b - y^{(i)}\right)^2$$

线形模型的优化目标为

$$\boldsymbol{w}^*, b^* = \operatorname*{argmin}_{\boldsymbol{w}, b}\  L(\boldsymbol{w}, b)
$$

最优解为
$$\hat{\boldsymbol{w}}=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\boldsymbol{y}$$

## 房价受到哪些因素影响 -- 一元线性回归

### 读入数据

```python
import pandas as pd
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['target'] = pd.Series(boston.target)
print(df)
```

变量|含义
---|---
CRIM|犯罪率
ZN|住宅用地所占比例
INDUS|城镇中非住宅用地所占比例
CHAS|虚拟变量
NOX|环保指数
RM|每栋住宅的房间数
AGE|1940年以前建成的自住单位的比例
DIS|距离5个波士顿的就业中心的加权距离
RAD|距离高速公路的便利指数
TAX|每一万美元的不动产税率
PTRATIO|城镇中的教师学生比例
B|城镇中的黑人比例
LSTAT|地区中有多少房东属于低收入人群
target|自住房屋房价中位数（即均价）

### 数据预处理

#### 重复值

```python
df.duplicated().unique()
```

#### 缺失值

```python
df.isna().sum(axis=0)
```

### 一元线性回归

#### 可视化各个因素与房价之间的关系

```python
for each in df.columns[:-1]:
    _ = df.plot(x=each, y='target', kind='scatter', figsize=(12, 6))
```

#### 建立回归模型

```python
from scipy import stats
stats.linregress(x, y)
```

* 进行最小二乘回归, `x`为自变量, `y`为因变量
* 返回回归系数、截距、$R$相关系数、$p$值、标准误

```python
rmb1, rmb0, rmr, rmpv, _ = stats.linregress(df['RM'], df['target'])
print(f'房屋数量的回归系数是{rmb1:.3f}，p值是{rmpv:.3f}, 回归方程的截距是{rmb0:.3f}，R-squared是{rmr**2:.3f}')
```

#### 计算拟合值

$$
\hat{y} = \beta_1\times x + \beta_0
$$

```python
df['rmtarget'] = rmb1 * np.array(df['RM']) + rmb0
df['lsttarget'] = lstb1 * np.array(df['LSTAT']) + lstb0
df.head()
```

#### 绘制回归线

```python
axrm = df.plot(x='RM', y='target', kind='scatter',igsize=(12, 6), label='原始数据')
_ = df.plot(x='RM', y='rmtarget', kind='line', label='拟合值', ax=axrm)
_ = axrm.legend()
```

### 多元线性回归

```python
import statsmodels.formula.api as smf

md = smf.ols(formula,data,subset)
res = md.fit() # 拟合数据
print(res.summary()) # 显示结果
```
* `formula`：`str`类型，描述公式
* `data`：`pandas.DataFrame`
* `subset`：布尔、整数、索引数组，指定原始数据中的子集用于回归分析
* `md`：返回的是`model`实例

```python
resBoston = smf.ols('target~RM+LSTAT+CRIM+NOX+RAD',data=df, subset=df['RAD'] > 20).fit()
resBoston.summary()
```

## sklearn建模

### 划分训练集与检验集

```python
from sklearn.model_selection import train_test_split
bsTrainX, bsTestX, bsTrainY, bsTestY = train_test_split(df.iloc[:,:df.shape[1]-1],df['target'],test_size=0.3,random_state=100)
```

### 建立模型

```python
from sklearn import linear_model
bstLearModel = linear_model.LinearRegression()
bstLearModel
```

#### 训练模型

```python
bstLearModel.fit(bsTrainX,bsTrainY)
```

#### 得到回归系数与截距

* 回归系数：`bstLearModel.coef_`
* 截距：`bstLearModel.intercept_`

```python
print(f'回归系数为{[round(x,3) for x in bstLearModel.coef_]}')
print(f'截距为{bstLearModel.intercept_:.3f}')
```

#### 预测

```python
predicted = bstLearModel.predict(bsTrainX)
resDf = pd.DataFrame({'原价格':bsTrainY,'预测价格':predicted})
resDf
```

### 拟合度

#### 决定系数$R^2$

$$R^2(y,\hat{y})=1-\frac{\sum_{i=1}^n(y_i-\hat{y}_i)^2}{\sum_{i=1}^n(y_i-\bar{y})^2}$$

其中，$\hat{y}_i$为预测值，$\bar{y}$为均值

```python
# 训练集的R2
bstR2 = bstLearModel.score(bsTrainX,bsTrainY)
print(f'训练集的R-square为{bstR2:.3f}')
bstR2Test = bstLearModel.score(bsTestX,bsTestY)
print(f'检验集的R-square为{bstR2Test:.3f}')
```

#### 平均绝对误差 mean absolute error (MAE)

$$\rm{MAE}(y,\hat{y})=\frac{1}{n}\sum_{i=1}^n|y_i-\hat{y}_i|$$

```python
from sklearn.metrics import mean_absolute_error
# 训练集的MAE
bstMAE = mean_absolute_error(bsTrainY,bstLearModel.predict(bsTrainX))
print(f'训练集的MAE为{bstMAE:.3f}')
# 检验集的MAE
bstMAETest = mean_absolute_error(bsTestY,bstLearModel.predict(bsTestX))
print(f'训练集的MAE为{bstMAETest:.3f}')
```

#### 平均绝对百分比误差 mean absolute percentage error (MAPE)

$$\rm{MAPE}(y,\hat{y})=\frac{1}{n}\sum_{i=1}^n\frac{|y_i-\hat{y}_i|}{\max(\epsilon,|y_i|)}$$

```python
from sklearn.metrics import mean_absolute_percentage_error
# 训练集的MAE
bstMAPE = mean_absolute_percentage_error(bsTrainY,bstLearModel.predict(bsTrainX))
print(f'训练集的MAE为{bstMAPE:.3f}')
# 检验集的MAE
bstMAPETest = mean_absolute_percentage_error(bsTestY,bstLearModel.predict(bsTestX))
print(f'训练集的MAE为{bstMAPETest:.3f}')
```

#### 均方误差 mean squared error (MSE)

$$\rm{MSE}(y,\hat{y})=\frac{1}{n}\sum_{i=1}^n(y_i-\hat{y}_i)^2$$

```python
from sklearn.metrics import mean_squared_error
# 训练集的MAE
bstMSE = mean_squared_error(bsTrainY,bstLearModel.predict(bsTrainX))
print(f'训练集的MAE为{bstMSE:.3f}')
# 检验集的MAE
bstMSETest = mean_squared_error(bsTestY,bstLearModel.predict(bsTestX))
print(f'训练集的MAE为{bstMSETest:.3f}')
```

## 逻辑回归

因变量是**二元**变量(binary response)

### 线性回归的问题

<div style="text-align: center;"><img alt='202404192342674' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404192342674.png' width=500px> </div>

<div style="text-align: center;"><img alt='202404192342471' src='https://cdn.jsdelivr.net/gh/weno861/image@main/img/202404192342471.png' width=500px> </div>

### 逻辑回归的原理

令$\pi$表示事件{Y=1}发生的概率，$\mathbf{\beta}$为回归系数向量，则

$$
\pi = \frac{\rm{e}^{\mathbf{\beta^T X}}}{1+\rm{e}^{\mathbf{\beta^T X}}}=\frac{1}{1+\rm{e}^{-\mathbf{\beta^T X}}}
$$

* 上式即为sigmoid函数
* 转变为$\mathbf{\beta^T X}$的线性函数

$$
\log\frac{\pi}{1-\pi}=\mathbf{\beta^T X}
$$

* $\frac{\pi}{1-\pi}$被称为odds
* $\log\frac{\pi}{1-\pi}$被称为log odds

#### 极大似然估计参数（maximum likelihood）

- 优化模型参数以最大可能得到样本数据
- 假设有$n$个样本，则样本发生的概率

$$
P\{Y_1=y_1,Y_2=y_2,\cdots,Y_n=y_n\}=P\{Y_1=y_1\}P\{Y_2=y_2\}\cdots P\{Y_n=y_n\}
$$
- 二元因变量服从二项分布

$$
\max \Pi_{i=1}^n\; \pi_i^{y_i}(1-\pi_i)^{1-y_i}
$$

令$L=\Pi_{i=1}^n\; \pi_i^{y_i}(1-\pi_i)^{1-y_i}$，则
$$
l = \log(L)=\sum_{i=1}^n\left(y_i\mathbf{\beta^T X_i}-\log(1+\rm{e}^{\mathbf{\beta^T X_i}})\right)
$$
- 逻辑回归系数含义
    - 令$\beta_i$为第$i$个自变量的回归系数
$$
\frac{\frac{\pi'}{1-\pi'}}{\frac{\pi}{1-\pi}}=\rm{e}^{\beta_i}
$$
    - 即$\beta_i$为第$i$个自变量的log odds

#### 逻辑回归建模

```python
import statsmodels.formula.api as smf

md = smf.logit(formula,data,subset) # 构建模型
res = md.fit() # 拟合数据
res.summary() # 显示结果
```

##### 评价模型优劣

* 整体模型优劣，Log-Likelihood，LLR p-value
* 每个属性（自变量）的系数，log odds ratio 和显著性

### sklearn 建模

```python
pandas.get_dummies(data, columns=None)
```
* `data`：`Series`类型，或者`DataFrame`类型
* `columns`：列名的`list`类型，数据集中哪些列需要转换，默认是将数据集中所有列进行转换
* 返回值：由二元化的属性构成的`DataFrame`

#### 建立模型

```python
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(C=1e9, max_iter=4000, solver='lbfgs', random_state=10)
```

* `C`：正则强度的倒数，降低过拟合
* `max_iter`：最大迭代次数
* `solver`：优化器，可选'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'


