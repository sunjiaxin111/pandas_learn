import numpy as np
import pandas as pd

# 变化百分比
ser = pd.Series(np.random.randn(8))
print(ser)
# 此函数将每个元素与其前一个元素进行比较，并计算变化百分比。
print(ser.pct_change())

df = pd.DataFrame(np.random.randn(10, 4))
print(df)
# periods参数指的是当前元素与前面比较元素所隔的距离
print(df.pct_change(periods=3))

# 协方差
s1 = pd.Series(np.random.randn(1000))
s2 = pd.Series(np.random.randn(1000))
# Series.cov() can be used to compute covariance between series (excluding missing values)
print(s1.cov(s2))

# Analogously, DataFrame.cov() to compute pairwise covariances among the series in the DataFrame,
# also excluding NA/null values.
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame.cov())

# min_periods参数表示列中最少不为NaN的个数
frame = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
frame.loc[frame.index[:5], 'a'] = np.nan
frame.loc[frame.index[5:10], 'b'] = np.nan
print(frame.cov())
print(frame.cov(min_periods=12))

# Correlation 相关系数
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
frame.iloc[::2] = np.nan
print(frame['a'].corr(frame['b']))
print(frame['a'].corr(frame['b'], method='spearman'))
print(frame.corr())
# corr也支持min_periods参数
frame = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
frame.loc[frame.index[:5], 'a'] = np.nan
frame.loc[frame.index[5:10], 'b'] = np.nan
print(frame.corr())
print(frame.corr(min_periods=12))

# corrwith()用于不同DataFrame对象之间
index = ['a', 'b', 'c', 'd', 'e']
columns = ['one', 'two', 'three', 'four']
df1 = pd.DataFrame(np.random.randn(5, 4), index=index, columns=columns)
df2 = pd.DataFrame(np.random.randn(4, 4), index=index[:4], columns=columns)
print(df1.corrwith(df2))
print(df2.corrwith(df1, axis=1))

# Data ranking
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
print(s)
s['d'] = s['b']  # so there's a tie
print(s)
# 这里的b和d假设是第2、3名，则其值都为2.5
print(s.rank())

df = pd.DataFrame(np.random.np.random.randn(10, 6))
df[4] = df[2][:5]  # some ties
print(df)
print(df.rank(axis=1))
