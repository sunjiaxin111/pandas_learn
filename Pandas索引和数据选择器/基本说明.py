import numpy as np
import pandas as pd

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
panel = pd.Panel({'one': df, 'two': df - df.mean()})
print(panel)

s = df['A']
print(s[dates[5]])
print(panel['two'])

print(df)
df[['B', 'A']] = df[['A', 'B']]
print(df)

'''
警告
pandas aligns all AXES when setting Series and DataFrame from .loc, and .iloc. This will not modify df 
because the column alignment is before value assignment.
'''
print(df[['A', 'B']])
df.loc[:, ['B', 'A']] = df[['A', 'B']]
print(df[['A', 'B']])
# 正确的方法
df.loc[:, ['B', 'A']] = df[['A', 'B']].values
print(df[['A', 'B']])
