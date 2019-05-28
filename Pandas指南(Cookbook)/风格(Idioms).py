import functools

import numpy as np
import pandas as pd

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)

# if-then风格
# 一列
df.loc[df.AAA >= 5, 'BBB'] = -1
print(df)

# 二列
df.loc[df.AAA >= 5, ['BBB', 'CCC']] = 555
print(df)

df.loc[df.AAA < 5, ['BBB', 'CCC']] = 2000
print(df)

# 使用掩码
df_mask = pd.DataFrame({'AAA': [True] * 4, 'BBB': [False] * 4, 'CCC': [True, False] * 2})
# DataFrame.where df_mask中是True的保存原值，是False的设置为-1000
print(df.where(df_mask, -1000))

# 使用numpy的where
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
df['logic'] = np.where(df.AAA > 5, 'high', 'low')
print(df)

# 使用布尔掩码
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
dflow = df[df.AAA <= 5]
print(dflow)
dfhigh = df[df.AAA > 5]
print(dfhigh)

# 通过多列条件选择
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']
print(newseries)

newseries = df.loc[(df['BBB'] > 25) | (df['CCC'] >= -40), 'AAA']
print(newseries)

df.loc[(df['BBB'] > 25) | (df['CCC'] >= 75), 'AAA'] = 0.1
print(df)

# 选择离确定值最近的数据行
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
aValue = 43.0
print(df.loc[(df.CCC - aValue).abs().argsort()])

# 使用二元运算符动态减少条件列表
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
Crit1 = df.AAA <= 5.5
Crit2 = df.BBB == 10.0
Crit3 = df.CCC > -40.0
# 把3个条件合并成一个条件
AllCrit = Crit1 & Crit2 & Crit3
# 另一种做法
CritList = [Crit1, Crit2, Crit3]
AllCrit = functools.reduce(lambda x, y: x & y, CritList)
print(df[AllCrit])
