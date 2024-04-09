# PySpark 读写 csv文件

## PySpark将CSV文件读入DataFrame

在PySpark中，可以使用`read.csv()`方法将CSV文件读入DataFrame

```python
spark.read_csv(path, header, inferSchema, sep, nullValue, mode)
```

- `path`: CSV文件的路径, 可以是本地文件系统或者hdfs文件系统
- `header`: 是否包含表头，默认为`True`  
- `inferSchema`: 是否自动推断数据类型，默认为`False`
- `sep`: CSV文件的分隔符，默认为`,`       
- `nullValue`: 用于表示空值的字符串。默认为空字符串    
- `mode`: 确定如何处理解析错误的参数，默认为`"PERMISSIVE"`, 将错误的记录放入一个单独的列

## 将 PySpark DataFrame 写入 CSV 文件

在PySpark中，可以使用`write.csv()`方法将DataFrame写入CSV文件
    

```python
df.write.csv(path, header, mode, sep, quote, escape, nullValue, nanValue, dateFormat, compression, escapeQuotes)
```

* `path` ：CSV 文件的输出路径
* `mode` ：确定如何处理现有文件或目录的参数。可选值包括 "append"（追加到现有文件）、"overwrite"（覆盖现有文件）和 "ignore"（如果文件已存在，则忽略写入操作）
* `sep` ：用于分隔字段的字符串。默认为逗号
* `quote` ：用于引用字段的字符串。默认为双引号
* `escape` ：用于转义字段的字符串。默认为反斜杠
* `nullValue` ：用于表示空值的字符串。默认为空字符串
