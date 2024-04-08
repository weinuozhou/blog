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