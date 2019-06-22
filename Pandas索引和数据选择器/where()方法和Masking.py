import numpy as np
import pandas as pd

s = pd.Series(np.arange(5), index=np.arange(5)[::-1], dtype='int64')
print(s[s > 0])

# 返回一个与原始Series有相同大小的Series
print(s.where(s > 0))

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df[df < 0])
# 等价方法
print(df.where(df < 0))

# where的other参数，当条件不满足时用other中的值替代
print(df.where(df < 0, -df))

s2 = s.copy()
s2[s2 < 2] = 0
print(s2)

df2 = df.copy()
df2[df2 < 0] = 0
print(df2)

# 默认情况下where返回数据的copy，当inplace参数设置为True时直接在原数据上修改
df_orig = df.copy()
df_orig.where(df > 0, -df, inplace=True)
print(df_orig)

# df1.where(m, df2) is equivalent to np.where(m, df1, df2)
print(df.where(df < 0, -df) == np.where(df < 0, df, -df))

df2 = df.copy()
df2[df2[1:4] > 0] = 3
print(df2)

# where的axis和level参数
df2 = df.copy()
print(df2.where(df2 > 0, df2['A'], axis='index'))
# 等价方法
df2 = df.copy()
print(df.apply(lambda x, y: x.where(x > 0, y), y=df['A']))

df3 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]})
print(df3.where(lambda x: x > 4, lambda x: x + 10))

# Mask与where相反
print(s.mask(s >= 0))
print(df.mask(df >= 0))
