import numpy as np
import pandas as pd

s1 = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
print(s1)
print(s1.iloc[:3])
print(s1.iloc[3])
s1.iloc[:3] = 0
print(s1)

# DataFrame
df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 8, 2)))
print(df1)
print(df1.iloc[:3])
print(df1.iloc[1:5, 2:4])
print(df1.iloc[[1, 3, 5], [1, 3]])
print(df1.iloc[1:3, :])
print(df1.iloc[:, 1:3])
print(df1.iloc[1, 1])
print(df1.iloc[1])

x = list('abcdef')
print(x)
print(x[4:10])
print(x[8:10])
s = pd.Series(x)
print(s)
print(s.iloc[4:10])
print(s.iloc[8:10])

dfl = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))
print(dfl)
# 切片越界会返回空的DataFrame
print(dfl.iloc[:, 2:3])
print(dfl.iloc[:, 1:3])
print(dfl.iloc[4:6])

# 一个单独的index越界会报IndexError
# print(dfl.iloc[[4, 5, 6]])
# print(dfl.iloc[:, 4])
