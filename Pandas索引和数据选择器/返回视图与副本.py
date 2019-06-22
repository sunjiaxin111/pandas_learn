import numpy as np
import pandas as pd

dfmi = pd.DataFrame([list('abcd'),
                     list('efgh'),
                     list('ijkl'),
                     list('mnop')],
                    columns=pd.MultiIndex.from_product([['one', 'two'],
                                                        ['first', 'second']]))
print(dfmi)

# 两个访问方法,推荐第二种方式
print(dfmi['one']['second'])
print(dfmi.loc[:, ('one', 'second')])

dfmi.loc[:, ('one', 'second')] = 'x'
print(dfmi)
dfmi['one']['second'] = 'y'  # SettingWithCopyWarning
print(dfmi)

# Evaluation order matters
dfb = pd.DataFrame({'a': ['one', 'one', 'two',
                          'three', 'two', 'one', 'six'],
                    'c': np.arange(7)})
dfb['c'][dfb.a.str.startswith('o')] = 42
pd.set_option('mode.chained_assignment', 'warn')
dfb['c'][dfb.a.str.startswith('o')] = 42

# 正确方法
dfc = pd.DataFrame({'A': ['aaa', 'bbb', 'ccc'], 'B': [1, 2, 3]})
dfc.loc[0, 'A'] = 11
print(dfc)

# 有时候能成功，但不推荐的方法
dfc = dfc.copy()
dfc['A'][0] = 111
print(dfc)

# 不能成功的方法
pd.set_option('mode.chained_assignment', 'raise')
dfc.loc[0]['A'] = 1111
print(dfc)
