import numpy as np
import pandas as pd

df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'two', 'two', 'three', 'four'],
                    'b': ['x', 'y', 'x', 'y', 'x', 'x', 'x'],
                    'c': np.random.randn(7)})
print(df2)
# duplicated方法返回这个值是否是重复的，True或False
print(df2.duplicated('a'))
# keep参数设置为last，表示从后往前的第一个重复值为True,其余为False
print(df2.duplicated('a', keep='last'))
# keep参数设置为False，表示重复值全部设置为True
print(df2.duplicated('a', keep=False))

# 删除列a中的重复值
print(df2.drop_duplicates('a'))
# keep参数设置为last，表示保留从后往前的第一个重复值
print(df2.drop_duplicates('a', keep='last'))
# keep参数设置为False，表示删除全部重复值
print(df2.drop_duplicates('a', keep=False))

print(df2)
print(df2.duplicated(['a', 'b']))
print(df2.drop_duplicates(['a', 'b']))

# Index.duplicated
df3 = pd.DataFrame({'a': np.arange(6),
                    'b': np.random.randn(6)},
                   index=['a', 'a', 'b', 'c', 'b', 'a'])
print(df3)
print(df3.index.duplicated())
print(df3[~df3.index.duplicated()])
print(df3[~df3.index.duplicated(keep='last')])
print(df3[~df3.index.duplicated(keep=False)])
