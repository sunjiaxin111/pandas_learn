import numpy as np
import pandas as pd

# Integer indexing
# 下面2个注释掉的print都是错误的
s = pd.Series(range(5))
# print(s[-1])
df = pd.DataFrame(np.random.randn(5, 4))
print(df)
# print(df.loc[-2:])

# 非单调索引需要完全匹配
df = pd.DataFrame(index=[2, 3, 3, 4, 5], columns=['data'], data=list(range(5)))
print(df.index.is_monotonic_increasing)
print(df.loc[0:4, :])
print(df.loc[13:15, :])
# 如果index不是单调的，切片的前后都必须是index的唯一成员
df = pd.DataFrame(index=[2, 3, 1, 4, 3, 5], columns=['data'], data=list(range(6)))
print(df.index.is_monotonic_increasing)
print(df.loc[2:4, :])
# print(df.loc[0:4, :])  # KeyError: 0
# print(df.loc[2:3, :])  # KeyError: 'Cannot get right slice bound for non-unique label: 3'

# Index.is_unique()
weakly_monotonic = pd.Index(['a', 'b', 'c', 'c'])
print(weakly_monotonic)
print(weakly_monotonic.is_monotonic_increasing)
print(weakly_monotonic.is_monotonic_increasing & weakly_monotonic.is_unique)

# Endpoints are inclusive 端点是包容性的
s = pd.Series(np.random.randn(6), index=list('abcdef'))
print(s)
print(s[2:5])
print(s.loc['c':'e'])  # 同时包含c和e

# Indexing potentially changes underlying Series dtype
series1 = pd.Series([1, 2, 3])
print(series1.dtype)
res = series1.reindex([0, 4])
print(res.dtype)
print(res)

series2 = pd.Series([True])
print(series2.dtype)
res = series2.reindex_like(series1)
print(res.dtype)
print(res)
