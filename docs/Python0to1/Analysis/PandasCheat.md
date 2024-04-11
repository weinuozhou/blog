<div style="text-align:center">
    <h1>Pandas Cheat Sheet</h1>
    <span class="author">weno</span>
</div>

?> 1. 数据读取

* 读取`csv`文件: `pd.read_csv(filepath_or_buffle, sep, header, names)`
* 读取`excel`文件: `pd.read_excel(io, sheet_name, header, names)`
* 读取`json`文件: `pd.read_json(path_or_buf, orient)`
* 读取`sql`文件: `pd.read_sql(sql, con, index_col)`
* 读取`parequet`文件: `pd.read_parquet(path, engine='auto', columns=None, use_nullable_dtypes=None)`
* 读取`html`文件: `pd.read_html(io)` 

?> 2. 数据结构

* 使用列表创建 `Series`: `pd.Series(data: list, index=None)`
* 使用字典生成`Series`: `pd.Series(data: dict)`
* 使用列表创建 `DataFrame`: `pd.DataFrame(data: list, columns=['Name', 'Age'])`
* 使用字典创建`DataFrame`: `pd.DatFrame(data: dict)`

?> 3. 数据探索

* 获取`DataFrame`的列名: `df.columns`
* 获取`DataFrame`的索引: `df.index`
* 获取`DataFrame`的形状: `df.shape`
* 检查`DataFrame`的数据类型: `df.dtypes`
* 展示前几行数据: `df.head()`
* 展示后几行数据: `df.tail()`
* 展示`DataFrame`的统计信息: `df.describe()`
* 展示`DataFrame`的详细信息: `df.info()`

?> 4. 数据清洗

* 删除`DataFrame`中的重复行: `df.drop_duplicates(keep="first", inplace=True)`
* 删除`DataFrame`中的指定列: `df.drop(columns=['col1', 'col2'], inplace=True)`
* 删除`DataFrame`中的指定行: `df.drop(index=[row1, row2], inplace=True)`
* 检查是否有缺失值: `df.isna().sum(axis=0)`
* 删除`DataFrame`中的缺失值: `df.dropna(subset=['col1','col2'], axis=0, how='any', inplace=True)`
* 使用指定值填充`DataFrame`中的缺失值: `df.fillna(value=None, method=None, axis=None, inplace=False, limit=None)`
* 用插值法填充缺失值: `df.interpolate(method='linear', axis=0, limit=None, inplace=True, downcast=None, limit_area=None)`
* 标记离群点: `df.loc[np.abs((df['column']-df['column'].mean())/df['column'].std())>3, 'column']`
* 将属性的值域划分成相同宽度的区间: `pd.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False, duplicates='raise')`
* 将相同数量的对象放进每个区间: `pd.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')`

?> 5. 数据引用

* 筛选出`DataFrame`中指定列的值在指定范围内的行: `df.loc[(df['col1'] >= start) & (df['col1'] <= end)]`
* 筛选出`DataFrame`中指定列的值等于指定值的行: `df.loc[df['col1'] == value]`
* 筛选出`DataFrame`中指定列的值包含指定值的行: `df.loc[df['col1'].isin(value:list)]`
* 筛选出`DataFrame`中指定列的值不包含指定值的行: `df.loc[~df['col1'].isin(value: list)]`
* 筛选出特定数据类型的数据: `df.select_dtypes(include=['Float'], exclude)`
* 使用`query`方法进行筛选数据: `df.query('col1 > 10 and col2 < 20')`

?> 6. 数据转换

* 将`DataFrame`中的指定列转换为指定数据类型: `df['col1'] = df['col1'].astype(int)`
* 重命名列: `df.rename(columns={'old_col': 'new_col'}, inplace=True)`
* 设置索引: `df,set_index("column", inplace=True)`
* 重置索引: `df.reset_index(drop=True, inplace=True)`
* 按 `values` 排序: `df.sort_values(by, axis=0, ascending=True, inplace=, kind='quicksort', na_position='last')`
* 按 `index` 排序: `df.sort_index(axis=0, ascending=True, inplace=False, level=None, na_position='last')`
* 使用`map`函数进行映射: `df.map(lambda x: x.title())`
* 根据指定条件屏蔽或者替换数据
    * `df.where(condition, other=nan, inplace=False)`
    * `df['col'].mask(df['col'] > 2, np.nan, inplace=True)`
* 数据标准化
    * Min-Max Normalization: `(df['column']-df['column'].min()) / (df['column'].max() - df['column'].min())`
    * Z-Score Standardization: `(df['column'] - df['column'].mean()) / df['column'].std()`

?> 7. 数据分组与集成

* 常见的聚合函数

<div style="display: flex; justify-content: center;">
  <table>
    <tr>
      <th>函数</th>
      <th>说明</th>
    </tr>
    <tr>
      <td>count()</td>
      <td>分组中非NaN的数量</td>
    </tr>
    <tr>
      <td>sum()</td>
      <td>非NaN的和</td>
    </tr>
    <tr>
      <td>mean()</td>
      <td>非NaN的均值</td>
    </tr>
    <tr>
      <td>median()</td>
      <td>非NaN的中位数</td>
    </tr>
    <tr>
      <td>std()</td>
      <td>非NaN的标准差</td>
    </tr>
    <tr>
      <td>var()</td>
      <td>非NaN的方差</td>
    </tr>
    <tr>
      <td>min()</td>
      <td>非NaN的最小值</td>
    </tr>
    <tr>
      <td>max()</td>
      <td>非NaN的最大值</td>
    </tr>
    <tr>
      <td>prod()</td>
      <td>非NaN的积</td>
    </tr>
    <tr>
      <td>first()</td>
      <td>第一个非NaN的值</td>
    </tr>
    <tr>
      <td>last()</td>
      <td>最后一个非NaN的值</td>
    </tr>
  </table>
</div>

* 按指定列进行分组对每一个: `df.groupby("column").agg({"column": "sum"})`
* 按指定列进行分组，并计算每组的数量: `df.groupby("column").size()`
* `apply`函数进行聚合操作: `df["column"].apply(lambda x: function(x))`
* 将 `DataFrame` 中的列标签与行索引的转换: `df.stack()` or `df.unstack()`
* 将 `DataFrame` 从宽格式转换为长格式: `df.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)`
* 将 `DataFrame` 从长格式转换为宽格式: `df.pivot(index=None, columns=None, values=None)`
* 数据透视表: `pd.pivot_table(data=None, values=None, index=None, columns=None, aggfunc=np.mean)`
* 数据横向合并: `pd.merge(right, how='inner', left_index=False, right_index=False)`
* 数据纵向合并: `pd.concat(objs, axis=0, join='outer',ignore_index=False)`

?> 8.数据可视化

* 直方图: `df["column"].hist()`
* 箱线图: `df["column"].plot(kind='box')`
* 折线图: `df["column"].plot(kind='line')`
* 散点图: `df.plot(kind='scatter', x='column1', y='column2')`
* 饼图: `df["column"].plot(kind='pie', subplots=True)`
* 热力图: `df.plot(kind='hexbin', x='column1', y='column2')`
* 柱状图: `df["column"].plot(kind='bar')`
* 横向柱状图: `df["column"].plot(kind='barh')`
* 面积图: `df["column"].plot(kind='area')`

?> 9. 字符串函数

* 将字符串转成小写: `df['column'].str.lower()`
* 将字符串转成大写: `df['column'].str.upper()`
* 去除字符串两端的空格: `df['column'].str.strip()`
* 替换字符串中的指定字符: `df['column'].str.replace('-', '_', regex=True)`
* 获取字符串中的指定部分: `df['column'].str.extract('(\d+)')`
* 判断字符串是否包含指定字符: `df['column'].str.contains('指定字符')`
* 判断字符串是否以指定字符开头: `df['column'].str.startswith('指定字符')`
* 判断字符串是否以指定字符结尾: `df['column'].str.endswith('指定字符')`
* 统计字符串的长度: `df['column'].str.len()`
* 统计字符串中指定字符的个数: `df['column'].str.count('指定字符')`

?> 10. 统计分析

* 连续变量的相关系数矩阵: `df.corr()`
* 连续变量的相关系数热力图: `sns.heatmap(df.corr(), annot=True)`
* 协方差矩阵: `df.cov()`
* 数据打乱: `df.sample(frac=1, random_state=42)`
* 定义函数计算统计性指标
    ```python
    def status(x):
        return pd.Series([x.count(),x.min(),x.idxmin(),x.quantile(.25),x.median(),
                        x.quantile(.75),x.mean(),x.max(),x.idxmax(),x.mad(),x.var(),
                        x.std(),x.skew(),x.kurt()],index=['总数','最小值','最小值位置','25%分位数',
                        '中位数','75%分位数','均值','最大值','最大值位数','平均绝对偏差','方差','标准差','偏度','峰度'])
    ```
* 创建列联表: `pd.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)`
* 窗口计算函数: `df.rolling(window=3).mean()`
* 指数加权函数: `df.ewm(span=3).mean()`

?> 11. 数据存储

* 保存数据为csv文件: `df.to_csv('data.csv', index=False)`
* 保存数据为excel文件: `df.to_excel('data.xlsx', index=False)`
* 保存数据为json文件: `df.to_json('data.json')`
* 保存数据为parquet文件: `df.to_parquet('data.parquet')`
* 保存数据为sql文件: `df.to_sql('data.sql', engine)`



