import numpy as np
import pandas as pd

index = pd.Index(['e', 'd', 'a', 'b'])
print(index)
print('d' in index)

index = pd.Index(['e', 'd', 'a', 'b'], name='something')
print(index.name)

# 如果设置了名字，那么会在打印中显示
index = pd.Index(list(range(5)), name='rows')
columns = pd.Index(['A', 'B', 'C'], name='cols')
df = pd.DataFrame(np.random.randn(5, 3), index=index, columns=columns)
print(df)
print(df['A'])

# Setting metadata
ind = pd.Index([1, 2, 3])
print(ind.rename("apple"))
print(ind)
ind.set_names(["apple"], inplace=True)
print(ind)
ind.name = "bob"
print(ind)

index = pd.MultiIndex.from_product([range(3), ['one', 'two']], names=['first', 'second'])
print(index)
print(index.levels[1])
print(index.set_levels(["a", "b"], level=1))

# Set operations on Index objects
a = pd.Index(['c', 'b', 'a'])
b = pd.Index(['c', 'e', 'd'])
print(a | b)
print(a & b)
print(a.difference(b))

idx1 = pd.Index([1, 2, 3, 4])
idx2 = pd.Index([2, 3, 4, 5])
print(idx1.symmetric_difference(idx2))
print(idx1 ^ idx2)

# Missing values
idx1 = pd.Index([1, np.nan, 3, 4])
print(idx1)
print(idx1.fillna(2))
idx2 = pd.DatetimeIndex([pd.Timestamp('2011-01-01'), pd.NaT, pd.Timestamp('2011-01-03')])
print(idx2)
print(idx2.fillna(pd.Timestamp('2011-01-02')))
