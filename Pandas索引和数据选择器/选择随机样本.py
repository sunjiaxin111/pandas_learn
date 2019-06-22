import pandas as pd

s = pd.Series([0, 1, 2, 3, 4, 5])
print(s.sample())
print(s.sample(n=3))
print(s.sample(frac=0.5))

# 默认为不放回采样，replace=False
print(s.sample(n=6, replace=False))
# replace=True表示放回采样
print(s.sample(n=6, replace=True))

# 采样权重
s = pd.Series([0, 1, 2, 3, 4, 5])
example_weights = [0, 0, 0.2, 0.2, 0.2, 0.4]
print(s.sample(n=3, weights=example_weights))
# 如果权重之和不为1，则自动标准化
example_weights2 = [0.5, 0, 0, 0, 0, 0]
print(s.sample(n=1, weights=example_weights2))

# DataFrame可以使用列作为采样权重
df2 = pd.DataFrame({'col1': [9, 8, 7, 6], 'weight_column': [0.5, 0.4, 0.1, 0]})
print(df2.sample(n=3, weights='weight_column'))

# 使用axis参数去采样列
df3 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})
print(df3.sample(n=1, axis=1))

# 设置随机数种子
df4 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 3, 4]})
print(df4.sample(n=2, random_state=2))
print(df4.sample(n=2, random_state=2))
