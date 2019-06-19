import numpy as np
import pandas as pd

'''
reindex()方法：
1、以新的index对数据进行排序
2、在不存在label对应的数据的位置上插入NaN
3、通过指定fill_value来替代NaN值
'''
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.reindex(['e', 'b', 'f', 'd']))
print(s.reindex(['e', 'b', 'f', 'd'], fill_value=4))

# 对于DataFrame,可以同时reindex行和列
data = {'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
        'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
        'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['one', 'two'])
print(df)
print(df.reindex(index=['c', 'f', 'b'], columns=['three', 'two', 'one']))

# 使用axis关键字
print(df.reindex(['c', 'f', 'b'], axis='index'))
print(df.reindex(['three', 'two', 'one'], axis='columns'))

# index对象可以在对象之间共享
rs = s.reindex(df.index)
print(rs)
print(rs.index is df.index)

# Reindexing to align with another object
print(df)
print(df2)
print(df.reindex_like(df2))

# Aligning objects with each other with align
# align()方法是对齐两个对象最快的方法
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s1 = s[:4]
s2 = s[1:]
print(s1.align(s2))
print(s1.align(s2, join='inner'))
print(s1.align(s2, join='left'))

# 对于DataFrame，join方法默认是应用到index和columns中
print(df.align(df2, join='inner'))

# 也可以传递axis参数来指定对齐的轴
print(df.align(df2, join='inner', axis=0))

# 当传递一个Series到DataFrame.align()方法时，axis参数用于确定延哪个轴对齐
print(df.align(df2.iloc[0], axis=1))

'''
Filling while reindexing
pad / ffill -> Fill values forward
bfill / backfill -> Fill values backward
nearest -> Fill from the nearest index value
'''
rng = pd.date_range('1/3/2000', periods=8)
ts = pd.Series(np.random.randn(8), index=rng)
ts2 = ts[[0, 3, 6]]
print(ts)
print(ts2)
print(ts2.reindex(ts.index))
# 这些方法都需要indexes是递增或递减排序的
print(ts2.reindex(ts.index, method='ffill'))
# 等价方法
print(ts2.reindex(ts.index).fillna(method='ffill'))
print(ts2.reindex(ts.index, method='bfill'))
print(ts2.reindex(ts.index, method='nearest'))

# Limits on filling while reindexing
print(ts2.reindex(ts.index, method='ffill', limit=1))
print(ts2.reindex(ts.index, method='ffill', tolerance='1 day'))

# Dropping labels from an axis
print(df)
print(df.drop(['a', 'd'], axis=0))
# 等价方法
print(df.reindex(df.index.difference(['a', 'd'])))
print(df.drop(['one'], axis=1))

# Renaming / mapping labels
print(s)
print(s.rename(str.upper))
print(df.rename(columns={'one': 'foo', 'two': 'bar'},
                index={'a': 'apple', 'b': 'banana', 'd': 'durian'}))
print(df.rename({'one': 'foo', 'two': 'bar'}, axis='columns'))
print(df.rename({'a': 'apple', 'b': 'banana', 'd': 'durian'}, axis='index'))

# inplace参数
print(s.name)
s.rename("scalar-name")
print(s.name)
s.rename("scalar-name", inplace=True)
print(s.name)
