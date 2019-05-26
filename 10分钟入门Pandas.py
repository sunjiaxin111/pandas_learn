import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 创建Series,通过传递一个列表，让pandas自动创建默认的整数索引
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 创建DataFrame，通过传递一个numpy数组，一个datetime索引和列名
dates = pd.date_range('20130101', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 创建DataFrame，通过传递一个字典类型（每个元素可以被转换成Series类型）
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df2)
# 每一列的类型都不一样
print(df2.dtypes)

# 查看数据
# 查看顶部数据和底部数据
print(df.head())
print(df.tail(3))

# 查看index,columns和values
print(df.index)
print(df.columns)
print(df.values)

# describe()函数展示一个快速的统计摘要
print(df.describe())

# 转置数据
print(df.T)

# 按index进行排序
# 按列索引降序
print(df.sort_index(axis=1, ascending=False))
# 按行索引降序
print(df.sort_index(axis=0, ascending=False))

# 按values进行排序
print(df.sort_values(by='B'))

# 选择数据
# 选择单个列，生成一个Series
print(df['A'])
print(df.A)

# 通过切片来选择行
print(df[0:3])
print(df['20130102':'20130104'])

# 通过Label选择
print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])

# label切片，结束点也是包括的
print(df.loc['20130102':'20130104', ['A', 'B']])

# 减少返回对象的维度
print(df.loc['20130102', ['A', 'B']])

# 得到一个标量
print(df.loc[dates[0], 'A'])

# 用于快速访问标量
print(df.at[dates[0], 'A'])

# 通过位置选择
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
# 显式地切片行
print(df.iloc[1:3, :])
# 显式地切片列
print(df.iloc[:, 1:3])
# 显式地得到一个值
print(df.iloc[1, 1])
# 快速访问一个标量
print(df.iat[1, 1])

# 布尔索引
print(df[df.A > 0])
# 选择满足布尔条件的值
print(df[df > 0])

# 使用isin()方法过滤
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])

# 设置数据
# 设置一个新列，通过index自动对齐
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1
print(df)

# 通过label设置值
df.at[dates[0], 'A'] = 0
print(df)

# 通过position设置值
df.iat[0, 1] = 0
print(df)

# 设置一列
df.loc[:, 'D'] = np.array([5] * len(df))
df.iloc[:, 2] = np.array([6] * len(df))
print(df)

# 通过where操作来设置数据
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

# 缺失数据
# reindex函数允许改变（添加/删除）索引，并返回数据的复制
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
# 删除行中有缺失值的数据
print(df1.dropna(how='any'))
# 填充缺失值
print(df1.fillna(value=5))
# 得到布尔掩码
print(pd.isna(df1))

# 操作
# 通常排除缺失值数据
print(df)
print(df.mean())
# 相同的操作在其他轴
print(df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)
# df - s
print(df.sub(s, axis='index'))

# Apply
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

# Histogramming直方图化
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

# 字符串方法
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())

# Merge
# Concat
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
# print(df[:3])
# print(df[3:7])
# print(df[7:])
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))
# 另一个例子
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

# Append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
print(s)
print(df.append(s, ignore_index=True))

# Grouping
#   Splitting the data into groups based on some criteria
#   Applying a function to each group independently
#   Combining the results into a data structure
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)
'''
1、把数据划分到组
2、每个组单独apply函数
3、合并每组的结果
'''
print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())

# Reshaping
# Stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df2)

# The stack() method “compresses” a level in the DataFrame’s columns.
stacked = df2.stack()
print(stacked)

# stack()方法对应的是unstack()，默认unstacks最后一层
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

# Pivot Tables 数据透视表
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

# Time Series
# freq参数为日期偏移量
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# resample为重新采样，0.5Min为采样频率
print(ts.resample('0.5Min').sum())

# 时区表示
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)

# 转换到另一个时区
print(ts_utc.tz_convert('US/Eastern'))

# 在时间跨度表示之间转换
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts.head())

# Categoricals
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
# 把raw_grade字段转换为category数据类型
df['grade'] = df['raw_grade'].astype('category')
print(df['grade'])
# 类别重命名
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df['grade'])
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df['grade'])
# 排序
print(df.sort_values(by="grade"))
# Grouping by a categorical column also shows empty categories.
print(df.groupby('grade').size())

# Plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()
