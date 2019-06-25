import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])
df['four'] = 'bar'
df['five'] = df['one'] > 0
print(df)
df2 = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df2)

'''
注意:
通过设置pandas.options.mode.use_inf_as_na = True
来把inf和-inf当做NaN来计算
'''
print(df2['one'])
print(pd.isna(df2['one']))
print(df2['four'].notna())
print(df2.isna())

'''
注意:
np.nan != np.nan
None == None
'''
print(None == None)
print(np.nan == np.nan)

# 与np.nan进行标量的等价比较是没有意义的
print(df2['one'] == np.nan)
