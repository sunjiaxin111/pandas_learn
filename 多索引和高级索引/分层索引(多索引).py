import numpy as np
import pandas as pd

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
s = pd.Series(np.random.randn(8), index=index)
print(s)

# MultiIndex.from_product
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
print(pd.MultiIndex.from_product(iterables, names=['first', 'second']))

# 可以直接把arrays列表传入Series或DataFrame中去自动构建MultiIndex
arrays = [np.array(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux']),
          np.array(['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'])]
s = pd.Series(np.random.randn(8), index=arrays)
print(s)
df = pd.DataFrame(np.random.randn(8, 4), index=arrays)
print(df)

# MultiIndex的名字
print(df.index.names)

df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
print(df)
print(pd.DataFrame(np.random.randn(6, 6), index=index[:6], columns=index[:6]))
# display.multi_sparse控制索引的显示方式
with pd.option_context('display.multi_sparse', False):
    print(df)

print(pd.Series(np.random.randn(8), index=tuples))

# get_level_values
print(index.get_level_values(0))
print(index.get_level_values('second'))

# Basic indexing on axis with MultiIndex
print(df['bar'])
print(df['bar', 'one'])
print(df['bar']['one'])
print(s)
print(s['qux'])

# Defined Levels
# 下面2行代码输出的MultiIndex的level一样，codes不同
print(df.columns)
print(df[['foo', 'qux']].columns)
# 只输出使用到的level,3个方式
print(df[['foo', 'qux']].columns.values)
print(df[['foo', 'qux']].columns.get_level_values(0))
print(df[['foo', 'qux']].columns.remove_unused_levels())

# Data alignment and using reindex
print(s + s[:-2])
print(s + s[::2])
print(s.reindex(index[:3]))
print(s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one')]))
