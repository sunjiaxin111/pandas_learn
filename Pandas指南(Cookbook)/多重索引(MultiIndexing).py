import itertools

import numpy as np
import pandas as pd

df = pd.DataFrame({'row': [0, 1, 2],
                   'One_X': [1.1, 1.1, 1.1],
                   'One_Y': [1.2, 1.2, 1.2],
                   'Two_X': [1.11, 1.11, 1.11],
                   'Two_Y': [1.22, 1.22, 1.22]})
print(df)

# 把一列设置为index
df = df.set_index('row')
print(df)

# 设置层次列
df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])
print(df)

# stack & Reset
# reset_index()函数用于把index转化为列
df = df.stack(0).reset_index(1)
print(df)

df.columns = ['Sample', 'All_X', 'All_Y']
print(df)

# Arithmetic
cols = pd.MultiIndex.from_tuples([(x, y) for x in ['A', 'B', 'C'] for y in ['O', 'I']])
df = pd.DataFrame(np.random.randn(2, 6), index=['n', 'm'], columns=cols)
print(df)

# level=1表示按MultiIndex的第1层广播
df = df.div(df['C'], level=1)
print(df)

# Slicing
coords = [('AA', 'one'), ('AA', 'six'), ('BB', 'one'), ('BB', 'two'), ('BB', 'six')]
index = pd.MultiIndex.from_tuples(coords)
df = pd.DataFrame([11, 22, 33, 44, 55], index, ['MyData'])
print(df)

print(df.xs('BB', level=0, axis=0))  # Note : level and axis are optional, and default to zero
print(df.xs('six', level=1, axis=0))

# 使用xs对MultiIndex切片
index = list(itertools.product(['Ada', 'Quinn', 'Violet'], ['Comp', 'Math', 'Sci']))
headr = list(itertools.product(['Exams', 'Labs'], ['I', 'II']))
indx = pd.MultiIndex.from_tuples(index, names=['Student', 'Course'])
cols = pd.MultiIndex.from_tuples(headr)
data = [[70 + x + y + (x * y) % 3 for x in range(4)] for y in range(9)]
df = pd.DataFrame(data, indx, cols)
print(df)

All = slice(None)
print(df.loc['Violet'])
print(df.loc[(All, 'Math'), All])
print(df.loc[(slice('Ada', 'Quinn'), 'Math'), All])
print(df.loc[(All, 'Math'), 'Exams'])
print(df.loc[(All, 'Math'), (All, 'II')])

# Sorting
print(df.sort_values(by=('Labs', 'II'), ascending=False))
df.loc[('Violet', 'Comp'), ('Labs', 'II')] = 66
print(df.sort_values(by=('Labs', 'II'), ascending=False))
