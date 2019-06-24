import random

import numpy as np
import pandas as pd

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
random.shuffle(tuples)
s = pd.Series(np.random.randn(8), index=pd.MultiIndex.from_tuples(tuples))
print(s)
print(s.sort_index())
print(s.sort_index(level=0))
print(s.sort_index(level=1))

# 如果MultiIndex levels被命名了，可以在sort_index中传入level名
s.index.set_names(['L1', 'L2'], inplace=True)
print(s.sort_index(level='L1'))
print(s.sort_index(level='L2'))

midx = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
df = pd.DataFrame(np.random.randn(4, 2), index=midx)
print(df.T.sort_index(level=1, axis=1))

# Indexing will work even if the data are not sorted
dfm = pd.DataFrame({'jim': [0, 0, 1, 1],
                    'joe': ['x', 'x', 'z', 'y'],
                    'jolie': np.random.rand(4)})
dfm = dfm.set_index(['jim', 'joe'])
print(dfm)
# PerformanceWarning
print(dfm.loc[(1, 'z')])
# UnsortedIndexError
# print(dfm.loc[(0, 'y'):(1, 'z')])

# The is_lexsorted() method on an Index show if the index is sorted
print(dfm.index.is_lexsorted())
# the lexsort_depth property returns the sort depth
print(dfm.index.lexsort_depth)

dfm = dfm.sort_index()
print(dfm)
print(dfm.index.is_lexsorted())
print(dfm.index.lexsort_depth)
print(dfm.loc[(0, 'y'):(1, 'z')])  # 可以运行
