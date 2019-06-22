import numpy as np
import pandas as pd

# Series[]中填的是index
# DataFrame[]中填的是column
# Panel[]中填的是item
sa = pd.Series([1, 2, 3], index=list('abc'))
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
dfa = df.copy()
panel = pd.Panel({'one': df, 'two': df - df.mean()})

print(sa.b)
print(dfa.A)
print(panel.one)

sa.a = 5
print(sa)
dfa.A = list(range(len(dfa.index)))  # 当列A存在时是可以的
print(dfa)
dfa['A'] = list(range(len(dfa.index)))  # 这个表达式可以用于创建新列
print(dfa)

# 将一个dict赋值到DataFrame的一行
x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
x.iloc[1] = dict(x=9, y=99)
print(x)

# You can use attribute access to modify an existing element of a Series or column of a DataFrame
df = pd.DataFrame({'one': [1., 2., 3.]})
df.two = [4, 5, 6]
print(df)
