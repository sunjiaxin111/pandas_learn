import numpy as np
import pandas as pd

# By Index
df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

unsorted_df = df.reindex(index=['a', 'd', 'c', 'b'],
                         columns=['three', 'two', 'one'])
print(unsorted_df)
# DataFrame排序
print(unsorted_df.sort_index())
print(unsorted_df.sort_index(ascending=False))
print(unsorted_df.sort_index(axis=1))
# Series排序
print(unsorted_df['three'].sort_index())

# By Values
df1 = pd.DataFrame({'one': [2, 1, 1, 1], 'two': [1, 3, 2, 4], 'three': [5, 4, 3, 2]})
print(df1.sort_values(by='two'))
print(df1[['one', 'two', 'three']].sort_values(by=['one', 'two']))

# 这些方法通过na_position参数对NaN值进行特殊处理
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s[2] = np.nan
print(s.sort_values())
print(s.sort_values(na_position='first'))

# By Indexes and Values
# Build MultiIndex
idx = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('a', 2),
                                 ('b', 2), ('b', 1), ('b', 1)])
idx.names = ['first', 'second']
# Build DataFrame
df_multi = pd.DataFrame({'A': np.arange(6, 0, -1)}, index=idx)
print(df_multi)
# Sort by ‘second’ (index) and ‘A’ (column)
print(df_multi.sort_values(by=['second', 'A']))
# 注意：如果字符串同时匹配了列名和索引名，优先匹配列名，未来版本中会报错

# searchsorted
# 查找一个合适的位置，将元素插入已排好序的一维数组中，并且保持数组元素的顺序不被打乱。
ser = pd.Series([1, 2, 3])
# 将0插入到ser中，插入后的索引为0
# 将3插入到ser中，插入后的索引为2
print(ser.searchsorted([0, 3]))
print(ser.searchsorted([0, 4]))
# side='right' -> 插入到相同值的最右边
print(ser.searchsorted([1, 3], side='right'))
print(ser.searchsorted([1, 3], side='left'))
ser = pd.Series([3, 1, 2])
print(ser.searchsorted([0, 3], sorter=np.argsort(ser)))

# smallest / largest values
s = pd.Series(np.random.permutation(10))
print(s)
print(s.sort_values())
print(s.nsmallest(3))
print(s.nlargest(3))

# DataFrame
df = pd.DataFrame({'a': [-2, -1, 1, 10, 8, 11, -1],
                   'b': list('abdceff'),
                   'c': [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0]})
print(df)
print(df.nlargest(3, 'a'))
print(df.nlargest(5, ['a', 'c']))
print(df.nsmallest(3, 'a'))
print(df.nsmallest(5, ['a', 'c']))

# Sorting by a multi-index column
print(df1)
df1.columns = pd.MultiIndex.from_tuples([('a', 'one'), ('a', 'two'), ('b', 'three')])
print(df1)
print(df1.sort_values(by=('a', 'two')))
