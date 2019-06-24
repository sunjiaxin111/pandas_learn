import numpy as np
import pandas as pd

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
df = df.T
print(df)
print(df.loc[('bar', 'two')])
print(df.loc[('bar', 'two'), 'A'])
print(df.loc[('bar',)])
print(df.loc['baz':'foo'])
print(df.loc[('baz', 'two'):('qux', 'one')])
print(df.loc[('baz', 'two'):'foo'])
print(df.loc[[('bar', 'two'), ('qux', 'one')]])

s = pd.Series([1, 2, 3, 4, 5, 6], index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]]))
print(s.loc[[("A", "c"), ("B", "d")]])  # list of tuples
print(s.loc[(["A", "B"], ["c", "d"])])  # tuple of lists


# Using slicers
# loc最好指定所有轴
# you should do this
# df.loc[(slice('A1','A3'),.....), :]
# you should not do this
# df.loc[(slice('A1','A3'),.....)]


def mklbl(prefix, n):
    return ["%s%s" % (prefix, i) for i in range(n)]


miindex = pd.MultiIndex.from_product([mklbl('A', 4),
                                      mklbl('B', 2),
                                      mklbl('C', 4),
                                      mklbl('D', 2)])
micolumns = pd.MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'),
                                       ('b', 'foo'), ('b', 'bah')],
                                      names=['lvl0', 'lvl1'])
dfmi = pd.DataFrame(np.arange(len(miindex) * len(micolumns)).reshape((len(miindex), len(micolumns))),
                    index=miindex,
                    columns=micolumns).sort_index().sort_index(axis=1)
print(dfmi)
# slice
# slice('A1', 'A3')指的是A1、A2、A3
# slice(None)指的是全选
# ['C1', 'C3']指的是C1、C3
print(dfmi.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :])

# 使用pandas.IndexSlice去得到更方便的语法
idx = pd.IndexSlice
print(dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']])
print(dfmi.loc['A1', (slice(None), 'foo')])

# mask
mask = dfmi[('a', 'foo')] > 200
print(dfmi.loc[idx[mask, :, ['C1', 'C3']], idx[:, 'foo']])

# 使用axis参数去解释.loc中的单一slicer
print(dfmi.loc(axis=0)[:, :, ['C1', 'C3']])

# 设置值
df2 = dfmi.copy()
df2.loc(axis=0)[:, :, ['C1', 'C3']] = -10
print(df2)

df2 = dfmi.copy()
df2.loc[idx[:, :, ['C1', 'C3']], :] = df2 * 1000
print(df2)

# Cross-section
print(df)
print(df.xs('one', level='second'))
print(df.loc[(slice(None), 'one'), :])
df = df.T
print(df.xs('one', level='second', axis=1))
print(df.loc[:, (slice(None), 'one')])
print(df.xs(('one', 'bar'), level=('second', 'first'), axis=1))
print(df.loc[:, ('bar', 'one')])
print(df.xs('one', level='second', axis=1, drop_level=False))
print(df.xs('one', level='second', axis=1, drop_level=True))

# Advanced reindexing and alignment
midx = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
df = pd.DataFrame(np.random.randn(4, 2), index=midx)
print(df)
df2 = df.mean(level=0)
print(df2)
print(df2.reindex(df.index, level=0))

# aligning
df_aligned, df2_aligned = df.align(df2, level=0)
print(df_aligned)
print(df2_aligned)

# Swapping levels with swaplevel()
print(df[:5])
print(df[:5].swaplevel(0, 1, axis=0))

# Reordering levels with reorder_levels()
print(df[:5].reorder_levels([1, 0], axis=0))
