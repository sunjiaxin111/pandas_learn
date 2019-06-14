import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# From dict of Series or dicts
# df的index是所有Series的index的并集
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(pd.DataFrame(d, index=['d', 'b', 'a']))
print(pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three']))
print(df.index)
print(df.columns)

# From dict of ndarrays / lists
# The ndarrays must all be the same length.
# If an index is passed, it must clearly also be the same length as the arrays.
d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}
print(pd.DataFrame(d))
print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

# From structured or record array
data = np.zeros((2,), dtype=[('A', 'i4'), ('B', 'f4'), ('C', 'a10')])
data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
print(pd.DataFrame(data))
print(pd.DataFrame(data, index=['first', 'second']))
print(pd.DataFrame(data, columns=['C', 'A', 'B']))

# From a list of dicts
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
print(pd.DataFrame(data2))
print(pd.DataFrame(data2, index=['first', 'second']))
print(pd.DataFrame(data2, columns=['a', 'b']))

# From a dict of tuples
print(pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                    ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}}))

# From a Series
# The result will be a DataFrame with the same index as the input Series, and with one column whose name is the
# original name of the Series (only if no other column name provided).

# Alternate Constructors
# DataFrame.from_dict构造器
# 与DataFrame构造器的区别在于，可以通过orient参数使得dict的keys作为行标签
print(pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])])))
print(pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                             orient='index', columns=['one', 'two', 'three']))

# DataFrame.from_records构造器
# 与DataFrame构造器的区别在于，可以把数据中的某一列作为index
print(data)
print(pd.DataFrame.from_records(data, index='C'))

# Column selection, addition, deletion
print(df['one'])
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
print(df)
# Columns can be deleted or popped like with a dict
del df['two']
three = df.pop('three')
print(df)
print(three)
# 插入标量，自动广播
df['foo'] = 'bar'
print(df)
df['one_trunc'] = df['one'][:2]
print(df)
df.insert(1, 'bar', df['one'])
print(df)

# Assigning New Columns in Method Chains
iris = pd.read_csv('iris.data', header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'])
print(iris.head())
print(iris.assign(sepal_ratio=iris['SepalWidth'] / iris['SepalLength']).head())
print(iris.assign(sepal_ratio=lambda x: (x['SepalWidth'] / x['SepalLength'])).head())
iris.query('SepalLength > 5').assign(SepalRatio=lambda x: x.SepalWidth / x.SepalLength,
                                     PetalRatio=lambda x: x.PetalWidth / x.PetalLength).plot(kind='scatter',
                                                                                             x='SepalRatio',
                                                                                             y='PetalRatio')
plt.show()

# python3.6后
# assign()函数允许后面的表达式引用前面刚创建的列
dfa = pd.DataFrame({"A": [1, 2, 3],
                    "B": [4, 5, 6]})
print(dfa.assign(C=lambda x: x['A'] + x['B'],
                 D=lambda x: x['A'] + x['C']))

# 兼容所有python版本
dependent = pd.DataFrame({"A": [1, 1, 1]})
print(dependent.assign(A=lambda x: x['A'] + 1)
      .assign(B=lambda x: x['A'] + 2))
# 如果是python3.5及以前的版本，这里的B将引用A的旧值
print(dependent.assign(A=lambda x: x["A"] + 1,
                       B=lambda x: x["A"] + 2))

# Indexing / Selection
'''
选择列->df[col]->Series
通过label选择行->df.loc[label]->Series
通过integer location选择行->df.iloc[loc]->Series
切片行->df[5:10]->DataFrame
通过boolean向量选择行->df[bool_vec]->DataFrame
'''
print(df)
print(df[[True, False, True, False]])
print(df.loc['b'])
print(df.iloc[2])

# Data alignment and arithmetic
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
print(df + df2)
# 对DataFrame和Series进行操作时，
# 默认将Series的index与DataFrame的columns对应，
# 再进行行广播
print(df - df.iloc[0])

# 特殊情况：时间序列数据
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
print(df)
print(type(df['A']))
print(df - df['A'])
# 正确做法
print(df.sub(df['A'], axis=0))
# 与标量进行运算
print(df * 5 + 2)
print(1 / df)
print(df ** 4)
# 布尔运算
df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1]}, dtype=bool)
df2 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)
print(df1)
print(df2)
print(df1 & df2)
print(df1 | df2)
print(df1 ^ df2)
print(-df1)

# Transposing
print(df[:5].T)

# DataFrame interoperability(互通) with NumPy functions
print(np.exp(df))
print(np.asarray(df))
# DataFrame的dot方法
print(df.T.dot(df))
# Series的dot方法
s1 = pd.Series(np.arange(5, 10))
print(s1.dot(s1))

# Console display
print(iris)
print(iris.info())
print(iris.iloc[-10:, :].to_string())  # 转化为字符串
print(pd.DataFrame(np.random.randn(3, 12)))
# 显示所有列
pd.set_option('display.max_columns', None)
print(pd.DataFrame(np.random.randn(3, 12)))

# 通过display.max_colwidth参数可以调整每一列的最大宽度
datafile = {'filename': ['filename_01', 'filename_02'],
            'path': ["media/user_name/storage/folder_01/filename_01",
                     "media/user_name/storage/folder_02/filename_02"]}
pd.set_option('display.max_colwidth', 30)
print(pd.DataFrame(datafile))
pd.set_option('display.max_colwidth', 100)
print(pd.DataFrame(datafile))

# DataFrame column attribute access and IPython completion
df = pd.DataFrame({'foo1': np.random.randn(5),
                   'foo2': np.random.randn(5)})
print(df)
print(df.foo1)
