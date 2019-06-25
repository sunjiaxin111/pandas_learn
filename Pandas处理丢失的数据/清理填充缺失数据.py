import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])
df['four'] = 'bar'
df['five'] = df['one'] > 0
df2 = df.copy()
df2['timestamp'] = pd.Timestamp('20120101')
df2.loc[['a', 'c', 'h'], ['one', 'timestamp']] = np.nan
print(df2)
print(df2.fillna(0))
print(df2['one'].fillna('missing'))

'''
Fill gaps forward or backward
pad/ffill -> Fill values forward
bfill/backfill -> Fill values backward
'''
df = df2[['one', 'two', 'three']]
print(df)
print(df.fillna(method='pad'))
# 限制填充的个数
df['one'] = np.nan
df.iloc[2:4, :] = np.nan
print(df)
print(df.fillna(method='pad', limit=1))

# Filling with a PandasObject
dff = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
dff.iloc[3:5, 0] = np.nan
dff.iloc[4:6, 1] = np.nan
dff.iloc[5:8, 2] = np.nan
print(dff)
print(dff.fillna(dff.mean()))
# 等价方法
print(dff.where(pd.notna(dff), dff.mean(), axis='columns'))
print(dff.fillna(dff.mean()['B':'C']))

# Dropping axis labels with missing data: dropna
print(df)
df[['two', 'three']] = df[['two', 'three']].fillna(0)
print(df)
print(df.dropna(axis=0))
print(df.dropna(axis=1))
print(df['one'].dropna())

# Interpolation 插值
ts = pd.Series(np.random.randn(100), index=pd.date_range('2000-01-31', periods=100, freq='M'))
ts.iloc[1:42] = np.nan
print(ts)
print(ts.count())
print(ts.interpolate().count())
ts.interpolate().plot()
plt.show()

# Index aware interpolation
ts2 = ts.loc[
    [pd.datetime(2000, 1, 31), pd.datetime(2000, 2, 29), pd.datetime(2002, 7, 31), pd.datetime(2005, 1, 31),
     pd.datetime(2008, 4, 30)]]
ts2[0] = 1
ts2[2] = 2
ts2[3] = np.nan
ts2[4] = 3
print(ts2)
print(ts2.interpolate())
# 按照index的大小均匀插值
print(ts2.interpolate(method='time'))

# For a floating-point index, use method='values'
ser = pd.Series([0., np.nan, 10.], index=[0., 1., 10.])
print(ser)
print(ser.interpolate())
print(ser.interpolate(method='values'))

df = pd.DataFrame({'A': [1, 2.1, np.nan, 4.7, 5.6, 6.8],
                   'B': [.25, np.nan, np.nan, 4, 12.2, 14.4]})
print(df)
print(df.interpolate())
# 下面这些方法需要scipy
print(df.interpolate(method='barycentric'))
print(df.interpolate(method='pchip'))
print(df.interpolate(method='akima'))
print(df.interpolate(method='spline', order=2))
print(df.interpolate(method='polynomial', order=2))

# 比较几个插值方法
np.random.seed(2)
ser = pd.Series(np.arange(1, 10.1, .25) ** 2 + np.random.randn(37))
bad = np.array([4, 13, 14, 15, 16, 17, 18, 20, 29])
ser[bad] = np.nan
methods = ['linear', 'quadratic', 'cubic']
df = pd.DataFrame({m: ser.interpolate(method=m) for m in methods})
df.plot()
plt.show()

ser = pd.Series(np.sort(np.random.uniform(size=100)))
new_index = ser.index | pd.Index([49.25, 49.5, 49.75, 50.25, 50.5, 50.75])
interp_s = ser.reindex(new_index).interpolate(method='pchip')
print(interp_s[49:51])

# Interpolation Limits
ser = pd.Series([np.nan, np.nan, 5, np.nan, np.nan, np.nan, 13, np.nan, np.nan])
print(ser.interpolate())
print(ser.interpolate(limit=1))
print(ser.interpolate(limit=1, limit_direction='backward'))
print(ser.interpolate(limit=1, limit_direction='both'))
print(ser.interpolate(limit_direction='both'))
print(ser.interpolate(limit_direction='both', limit_area='inside', limit=1))
print(ser.interpolate(limit_direction='backward', limit_area='outside'))
print(ser.interpolate(limit_direction='both', limit_area='outside'))

# Replacing Generic Values
ser = pd.Series([0., 1., 2., 3., 4.])
print(ser.replace(0, 5))
print(ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0]))
print(ser.replace({0: 10, 1: 100}))
df = pd.DataFrame({'a': [0, 1, 2, 3, 4], 'b': [5, 6, 7, 8, 9]})
print(df.replace({'a': 0, 'b': 5}, 100))
print(ser.replace([1, 2, 3], method='pad'))
print(ser.replace([1, 2, 3], method='bfill'))

# String/Regular Expression Replacement
d = {'a': list(range(4)), 'b': list('ab..'), 'c': ['a', 'b', np.nan, 'd']}
df = pd.DataFrame(d)
print(df.replace('.', np.nan))
print(df.replace(r'\s*\.\s*', np.nan, regex=True))
print(df.replace(['a', '.'], ['b', np.nan]))
print(df.replace([r'\.', r'(a)'], ['dot', '\1stuff'], regex=True))
print(df.replace({'b': '.'}, {'b': np.nan}))
print(df.replace({'b': r'\s*\.\s*'}, {'b': np.nan}, regex=True))
print(df.replace({'b': {'b': r''}}, regex=True))
print(df.replace(regex={'b': {r'\s*\.\s*': np.nan}}))
print(df.replace({'b': r'\s*(\.)\s*'}, {'b': r'\1ty'}, regex=True))
print(df.replace([r'\s*\.\s*', r'a|b'], np.nan, regex=True))
print(df.replace(regex=[r'\s*\.\s*', r'a|b'], value=np.nan))

# Numeric Replacement
df = pd.DataFrame(np.random.randn(10, 2))
df[np.random.rand(df.shape[0]) > 0.5] = 1.5
print(df.replace(1.5, np.nan))
df00 = df.values[0, 0]
print(df.replace([1.5, df00], [np.nan, 'a']))
print(df[1].dtype)
print(df.replace(1.5, np.nan, inplace=True))
