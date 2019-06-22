import numpy as np
import pandas as pd

s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print(s)
print(s.isin([2, 4, 6]))
print(s[s.isin([2, 4, 6])])

# isin用于index
print(s[s.index.isin([2, 4, 6])])
print(s.reindex([2, 4, 6]))

s_mi = pd.Series(np.arange(6), index=pd.MultiIndex.from_product([[0, 1], ['a', 'b', 'c']]))
print(s_mi)
print(s_mi.iloc[s_mi.index.isin([(1, 'a'), (2, 'b'), (0, 'c')])])
print(s_mi.iloc[s_mi.index.isin(['a', 'c', 'e'], level=1)])

# isin用于DataFrame
df = pd.DataFrame({'vals': [1, 2, 3, 4], 'ids': ['a', 'b', 'f', 'n'], 'ids2': ['a', 'n', 'c', 'n']})
values = ['a', 'b', 1, 3]
print(df.isin(values))

# 当你想让不同列匹配不同值时
values = {'ids': ['a', 'b'], 'vals': [1, 3]}
print(df.isin(values))

print(df)
values = {'ids': ['a', 'b'], 'ids2': ['a', 'c'], 'vals': [1, 3]}
row_mask = df.isin(values).all(1)
print(df[row_mask])

row_mask = df.isin(values).any(1)
print(df[row_mask])
