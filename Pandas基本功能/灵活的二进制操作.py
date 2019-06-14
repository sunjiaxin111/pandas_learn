import numpy as np
import pandas as pd

# 匹配/广播 行为
df = pd.DataFrame({'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})
print(df)
row = df.iloc[1]
column = df['two']
print(df.sub(row, axis='columns'))
print(df.sub(row, axis=1))
print(df.sub(column, axis='index'))
print(df.sub(column, axis=0))

dfmi = df.copy()
dfmi.index = pd.MultiIndex.from_tuples([(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a')],
                                       names=['first', 'second'])
print(dfmi)
print(dfmi.sub(column, axis=0, level='second'))

# 序列与索引也原生支持 divmod() 。这个函数同时计算商与余数，并返回一个二元元组
s = pd.Series(np.arange(10))
print(s)
div, rem = divmod(s, 3)
print(div)
print(rem)
idx = pd.Index(np.arange(10))
print(idx)
div, rem = divmod(idx, 3)
print(div)
print(rem)
# 我们也可以在元素级别使用divmod()
div, rem = divmod(s, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
print(div)
print(rem)

# 缺失值/补全计算
# 在序列与数据表中，运算函数包含一个fill_value参数，
# 它可以在碰到至多1个缺失值的时候替换该缺失值。
print(df)
df2 = df.copy()
df2.iloc[0, 2] = 1.
print(df2)
print(df + df2)
print(df.add(df2, fill_value=0))
print(df2.add(df, fill_value=0))

# 灵活比较
print(df)
print(df2)
print(df.gt(df2))
print(df2.ne(df))

# 布尔降维
print((df > 0).all())
print((df > 0).any())
print((df > 0).any().any())

# 通过empty属性判断pandas对象是否为空
print(df.empty)
print(pd.DataFrame(columns=list('ABC')).empty)

# 使用bool()方法来计算一个单元素布尔型的pandas对象的布尔属性
print(pd.Series([True]).bool())
print(pd.Series([False]).bool())
print(pd.DataFrame([[True]]).bool())
print(pd.DataFrame([[False]]).bool())

'''
警告
1、
if df:
    print(11)
2、
df and df2
会触发错误，因为你在尝试比较多个值
'''

# 比较对象是否相等
print(df + df == df * 2)
print((df + df == df * 2).all())

# np.nan == np.nan -> False
print(np.nan == np.nan)
# NDFrames（如，序列，数据表与面板）拥有一个equal()方法
# 来进行“相等”的测试，此时两个位置相同的NaN被认为是相等的
print((df + df).equals(df * 2))

# 注意，序列和数据表的所索引需要是相同的顺序，才能在“相等”测试中 获得True的返回
df1 = pd.DataFrame({'col': ['foo', 0, np.nan]})
df2 = pd.DataFrame({'col': [np.nan, 0, 'foo']}, index=[2, 1, 0])
print(df1.equals(df2))
print(df1.equals(df2.sort_index()))

# 比较数组型的对象
# 当使用标量类型的pandas数据结构时，你可以轻易地执行元素对元素的比较
print(pd.Series(['foo', 'bar', 'baz']) == 'foo')
print(pd.Index(['foo', 'bar', 'baz']) == 'foo')
# pandas可以处理不同类型，但长度相同的数组型对象
print(pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux']))
print(pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux']))
# 试图比较不同长度的Index 或 Series对象将会引发错误
# pandas中无法广播
# print(pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo', 'bar']))
# print(pd.Series(['foo', 'bar', 'baz']) == pd.Series(['foo']))
# NumPy中比较可以被广播
print(np.array([1, 2, 3]) == np.array([2]))
# 广播失败后返回False
print(np.array([1, 2, 3]) == np.array([1, 2]))

# 合并带有重复数据的数据集
df1 = pd.DataFrame({'A': [1., np.nan, 3., 5., np.nan],
                    'B': [np.nan, 2., 3., np.nan, 6.]})
df2 = pd.DataFrame({'A': [5., 2., 4., np.nan, 3., 7.],
                    'B': [np.nan, np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)
# 优先使用df1的数据，df1的数据为NaN时使用df2的数据
print(df1.combine_first(df2))

# 一般性数据表合并
combiner = lambda x, y: np.where(pd.isna(x), y, x)
print(df1.combine(df2, combiner))
