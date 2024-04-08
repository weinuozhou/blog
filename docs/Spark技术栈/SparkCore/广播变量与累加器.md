# 广播变量与累加器

## 广播变量

在 PySpark RDD 和 DataFrame 中, 广播变量是**只读共享变量**, 它们被缓存并在集群中的所有节点上可用, 以便任务访问或使用。 PySpark 不是将这些数据与每个任务一起发送, 而是使用**高效的广播算法**将广播变量分发给工作人员, 以降低通信成本

### 使用案例

广播变量（Broadcast Variables）是将一个只读变量有效地广播到所有集群节点上的机制。广播变量在任务执行期间只被复制一次，而不是每个任务都复制一次。这样可以大大**减少网络传输的开销**，提高性能。广播变量通常在算子的闭包函数中使用，以便在集群节点上访问共享数据。广播变量的值在所有节点上都是一致的，并且只能在任务执行期间被读取，不能被修改。广播变量适用于需要在任务之间传递大量只读数据的场景，如广播配置信息、字典或机器学习模型参数等

用一个例子来解释何时使用广播变量, 假设您在文件中获得的国家/地区代码, 并且您希望将其转换为完整的州名称（例如 China 到中国, American到美国等）通过查找参考映射。在某些情况下, 这些数据可能很大, 并且您可能有很多此类查找（例如邮政编码等）

我们可以使用广播变量在每台计算机上缓存此查找信息, 并且任务在执行转换时使用此缓存信息, 而不是通过网络将这些信息与每个任务一起分发（开销和耗时）

### PySpark 广播如何工作

当您运行 PySpark RDD、定义和使用广播变量的 DataFrame 应用程序时, PySpark 会执行以下操作: 

* PySpark 将作业分成具有**分布式改组**的阶段, 并在该阶段中执行操作
* 后期阶段也分为任务
* Spark 广播每个阶段内任务所需的公共数据（可重用）
* 广播的数据以**序列化格式**缓存, 并在执行每个任务之前**反序列化**

!> 请注意, 广播变量不会通过`sc.broadcast(variable)`调用发送到执行器, 而是在第一次使用时发送到执行器

### 创建广播变量

```python
spark.SparkContext.broadcast(value)
```

下面是一个简单的例子来演示如何使用广播变量:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

states = {"China": "中国", "Amercian": "美国", "India": "印度"}
broadcastStates = spark.sparkContext.broadcast(states) # 创建广播变量
data = [("James","Smith","Amercian"),
    ("Michael","Rose","China"),
    ("Robert","Williams","India"),
    ("Maria","Jones","China")
  ]
rdd = spark.sparkContext.parallelize(data)
# 定义转换函数
def state_convert(code):
    return broadcastStates.value[code]
# 使用广播变量
result = rdd.map(lambda x: (x[0], x[1], state_convert(x[2]))).collect()
print(result)
```

## 累加器

累加器(PySpark Accumulator) 是一个共享变量，与 RDD 和 DataFrame 一起使用来执行类似于 Map-reduce 计数器的求和和计数器操作。这些变量由所有执行器共享，以通过聚合或计算操作更新和添加信息

累加器是**只写**的，并且初始化一次变量，其中只有在工作线程上运行的任务才允许更新，并且来自工作线程的更新会自动传播到驱动程序。但是，仅允许驱动程序使用value属性访问 Accumulator 变量

累加器（Accumulators）是一种用于在并行操作中聚合数据的变量。与广播变量不同，累加器是可写变量，可以在任务执行期间对其进行累加操作。累加器通常用于计数、求和等聚合操作，可以在任务执行过程中将结果累加到累加器中。累加器的值可以在任务执行完毕后读取，但不能在任务执行期间直接获取其值。累加器适用于需要在任务执行期间聚合数据的场景

### 创建累加器变量

使用SparkContext 类中的accumulator ()，我们可以在 PySpark 编程中创建一个累加器

```python
spark.SparkContext.accumulator(initialValue, accumulatorName=None)
```

* initialValue（可选）: 累加器的初始值。默认情况下，累加器的初始值为0。可以通过将初始值作为参数传递给构造函数来设置不同的初始值

当然，还提供了以下其他方法用于访问累加器

* `add(value)`：将给定的值累加到累加器的当前值上
* `value` ：获取累加器的当前值
* `reset()`：将累加器的值重置为初始值

### 使用累加器变量


1. 创建累加器变量并使用它对 RDD 中的所有值求和
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("accumulator").getOrCreate()
accum = spark.sparkContext.accumulator(0) # 创建累加器变量
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd.foreach(lambda x: accum.add(x))
print(accum.value)
```

2. 使用累加器来做计数器
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("accumulator").getOrCreate()
accum = spark.sparkContext.accumulator(0) # 创建累加器变量
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd.foreach(lambda x: accum.add(1))
print(accum.value)
```
