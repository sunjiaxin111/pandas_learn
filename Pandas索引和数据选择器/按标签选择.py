import numpy as np
import pandas as pd

dfl = pd.DataFrame(np.random.randn(5, 4), columns=list('ABCD'), index=pd.date_range('20130101', periods=5))
print(dfl)
# loc中填的是label, iloc中填的是position
# print(dfl.loc[2:3])
print(dfl.loc['20130102':'20130104'])

s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
print(s1)
print(s1.loc['c':])
print(s1.loc['b'])
s1.loc['c':] = 0
print(s1)

# DataFrame
df1 = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
print(df1)
print(df1.loc[['a', 'b', 'd'], :])
print(df1.loc['d':, 'A':'C'])
print(df1.loc['a'])
print(df1.loc['a'] > 0)
print(df1.loc[:, df1.loc['a'] > 0])
print(df1.loc['a', 'A'])

# Slicing with labels
s = pd.Series(list('abcde'), index=[0, 3, 2, 5, 4])
# both the start and the stop labels are present in the index
print(s.loc[3:5])
# at least one of the two is absent, but the index is sorted
print(s.sort_index())
print(s.sort_index().loc[1:6])
