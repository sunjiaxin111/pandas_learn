import numpy as np
import pandas as pd

'''
在不同的pandas对象中迭代产生的值
Series -> values
DataFrame -> column labels
Panel -> item labels
'''
df = pd.DataFrame({'col1': np.random.randn(3), 'col2': np.random.randn(3)},
                  index=['a', 'b', 'c'])
for col in df:
    print(col)

# 警告：迭代器返回的是副本
df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c']})
print(df)
for index, row in df.iterrows():
    row['a'] = 10
print(df)

'''
iteritems通过键值对迭代
Series -> (index, scalar value) pairs
DataFrame -> (column, Series) pairs
Panel -> (item, DataFrame) pairs
'''
wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
              major_axis=pd.date_range('1/1/2000', periods=5),
              minor_axis=['A', 'B', 'C', 'D'])
print(wp)
for item, frame in wp.iteritems():
    print(item)
    print(frame)

# iterrows
for row_index, row in df.iterrows():
    print('%s\n%s' % (row_index, row))

# iterrows返回的每行数据不保存dtypes
df_orig = pd.DataFrame([[1, 1.5]], columns=['int', 'float'])
print(df_orig)
print(df_orig.dtypes)
row = next(df_orig.iterrows())[1]
print(row)

# row中的所有值都转换成了float类型
print(row['int'].dtype)
print(df_orig['int'].dtype)

# 转置
df2 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df2)
print(df2.T)
# 等价方法
df2_t = pd.DataFrame(dict((idx, values) for idx, values in df2.iterrows()))
print(df2_t)

# itertuples返回的每行数据保存dtypes
print(df)
for row in df.itertuples():
    print(row)
