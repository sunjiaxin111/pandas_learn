import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

# CategoricalIndex
df = pd.DataFrame({'A': np.arange(6),
                   'B': list('aabbca')})
df['B'] = df['B'].astype(CategoricalDtype(list('cab')))
print(df)
print(df.dtypes)
print(df.B.cat.categories)

# Setting the index will create a CategoricalIndex.
df2 = df.set_index('B')
print(df2.index)
print(df2.loc['a'])
print(df2.loc['a'].index)

# Sorting the index will sort by the order of the categories
print(df2.sort_index())

# Groupby操作
print(df2.groupby(level=0).sum())
print(df2.groupby(level=0).sum().index)

# reindex
print(df2.reindex(['a', 'e']))
print(df2.reindex(['a', 'e']).index)
print(df2.reindex(pd.Categorical(['a', 'e'], categories=list('abcde'))))
print(df2.reindex(pd.Categorical(['a', 'e'], categories=list('abcde'))).index)

'''
警告
Reshaping and Comparison operations on a CategoricalIndex 
must have the same categories or a TypeError will be raised.
'''
df3 = pd.DataFrame({'A': np.arange(6),
                    'B': pd.Series(list('aabbda')).astype('category')})
df3 = df3.set_index('B')
print(df3.index)
# TypeError: categories must match existing categories when appending
# pd.concat([df2, df3])

# Int64Index and RangeIndex
# Float64Index
indexf = pd.Index([1.5, 2, 3, 4.5, 5])
print(indexf)
sf = pd.Series(range(5), index=indexf)
print(sf)

# 这里的3等价于3.0
print(sf[3])
print(sf[3.0])
print(sf.loc[3])
print(sf.loc[3.0])

print(sf[2:4])
print(sf.loc[2:4])
print(sf.iloc[2:4])
# Float64Index中允许使用float切片，其他类型的Index则不行
print(sf[2.1:4.6])
print(sf.loc[2.1:4.6])

dfir = pd.concat([pd.DataFrame(np.random.randn(5, 2),
                               index=np.arange(5) * 250.0,
                               columns=list('AB')),
                  pd.DataFrame(np.random.randn(6, 2),
                               index=np.arange(4, 10) * 250.1,
                               columns=list('AB'))])
print(dfir)
print(dfir[0:1000.4])
print(dfir.loc[0:1001, 'A'])
print(dfir.loc[1000.4])
print(dfir[0:1000])
print(dfir.iloc[0:5])

# IntervalIndex
df = pd.DataFrame({'A': [1, 2, 3, 4]},
                  index=pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4]))
print(df)
print(df.loc[2])
print(df.loc[[2, 3]])
print(df.loc[2.5])
print(df.loc[[2.5, 3.5]])

c = pd.cut(range(4), bins=2)
print(c)
print(c.categories)
print(pd.cut([0, 3, 5, 1], bins=c.categories))

# Generating Ranges of Intervals
print(pd.interval_range(start=0, end=5))
print(pd.interval_range(start=pd.Timestamp('2017-01-01'), periods=4))
print(pd.interval_range(end=pd.Timedelta('3 days'), periods=3))
print(pd.interval_range(start=0, periods=5, freq=1.5))
print(pd.interval_range(start=pd.Timestamp('2017-01-01'), periods=4, freq='W'))
print(pd.interval_range(start=pd.Timedelta('0 days'), periods=3, freq='9H'))
print(pd.interval_range(start=0, end=4, closed='both'))
print(pd.interval_range(start=0, end=4, closed='neither'))
print(pd.interval_range(start=0, end=6, periods=4))
print(pd.interval_range(pd.Timestamp('2018-01-01'), pd.Timestamp('2018-02-28'), periods=3))

# loc切片是包括前后的，iloc切片是只包括前的，尽量不使用[]（情况多）
df = pd.Series(range(5))
print(df)
print(df.index)
print(df.loc[1:4])
print(df.iloc[1:4])
