import numpy as np
import pandas as pd

# 同时使用行标签和取值条件
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
print(df[(df.AAA <= 6) & (df.index.isin([0, 2, 4]))])

# 使用loc做面向label的切片，使用iloc做位置切片
data = {'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]}
df = pd.DataFrame(data=data, index=['foo', 'bar', 'boo', 'kar'])
print(df)

# 基于label的切片,包括末尾点
print(df.loc['bar':'kar'])
# 基于position的切片，不包括末尾点
print(df.iloc[0:3])

# 当索引由具有非零开始或非单位增量的整数组成时，会出现歧义
df2 = pd.DataFrame(data=data, index=[1, 2, 3, 4])  # Note index starts at 1.
print(df2.iloc[1:3])  # position
print(df2.loc[1:3])  # label

# 使用逆运算符（〜）来获取掩码的补码
df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df)
print(df[~((df.AAA <= 6) & (df.index.isin([0, 2, 4])))])

# Panels
# Panel相当于一个存储Dataframe的字典
# Series一维、Dataframe二维、Panel三维
rng = pd.date_range('1/1/2013', periods=100, freq='D')
data = np.random.randn(100, 4)
cols = ['A', 'B', 'C', 'D']
df1, df2, df3 = pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols), pd.DataFrame(data, rng, cols)
pf = pd.Panel({'df1': df1, 'df2': df2, 'df3': df3})
print(pf)
pf.loc[:, :, 'F'] = pd.DataFrame(np.random.randn(pf.major_axis.shape[0], pf.items.shape[0]), index=pf.major_axis,
                                 columns=pf.items)
print(pf)

# New Columns
df = pd.DataFrame({'AAA': [1, 2, 1, 3], 'BBB': [1, 1, 2, 2], 'CCC': [2, 1, 3, 1]})
print(df)
source_cols = df.columns
new_cols = [str(x) + "_cat" for x in source_cols]
categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie'}
df[new_cols] = df[source_cols].applymap(categories.get)
print(df)

# Keep other columns when using min() with groupby
df = pd.DataFrame({'AAA': [1, 1, 1, 2, 2, 2, 3, 3], 'BBB': [2, 1, 3, 4, 5, 1, 2, 3]})
print(df)

# Method 1 : idxmin() to get the index of the mins
print(df.loc[df.groupby("AAA")["BBB"].idxmin()])
# Method 2 : sort then take first of each
print(df.sort_values(by="BBB").groupby("AAA", as_index=False).first())
