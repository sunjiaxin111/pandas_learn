import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
print(df1)
print(df1.loc[lambda df: df.A > 0, :])
print(df1.loc[:, lambda df: ['A', 'B']])
print(df1.iloc[:, lambda df: [0, 1]])
print(df1[lambda df: df.columns[0]])
print(df1.A.loc[lambda s: s > 0])

# 链式数据选择操作
bb = pd.read_csv('baseball.csv', index_col='id')
print((bb.groupby(['year', 'team']).sum().loc[lambda df: df.r > 100]))
