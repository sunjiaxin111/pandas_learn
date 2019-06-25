import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# We work with rolling, expanding and exponentially weighted data through the corresponding objects,
# Rolling, Expanding and EWM.
s = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(s)
s = s.cumsum()
print(s)

r = s.rolling(window=60)
print(r)
print(r.mean())
s.plot(style='k--')
r.mean().plot(style='k')
plt.show()

df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2000', periods=1000),
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.rolling(window=60).sum().plot(subplots=True)
plt.show()

# apply
mad = lambda x: np.fabs(x - x.mean()).mean()
s.rolling(window=60).apply(mad, raw=True).plot(style='k')
plt.show()

# Rolling Windows
ser = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
print(ser.rolling(window=5, win_type='triang').mean())
print(ser.rolling(window=5, win_type='boxcar').mean())
print(ser.rolling(window=5).mean())
print(ser.rolling(window=5, win_type='gaussian').mean(std=0.1))

# Time-aware Rolling
dft = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]},
                   index=pd.date_range('20130101 09:00:00', periods=5, freq='s'))
print(dft)
print(dft.rolling(2).sum())
print(dft.rolling(2, min_periods=1).sum())
print(dft.rolling('2s').sum())  # 此时默认的min_periods是1

dft = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]},
                   index=pd.Index([pd.Timestamp('20130101 09:00:00'),
                                   pd.Timestamp('20130101 09:00:02'),
                                   pd.Timestamp('20130101 09:00:03'),
                                   pd.Timestamp('20130101 09:00:05'),
                                   pd.Timestamp('20130101 09:00:06')],
                                  name='foo'))
print(dft)
print(dft.rolling(2).sum())
print(dft.rolling('2s').sum())
dft = dft.reset_index()
print(dft.rolling('2s', on='foo').sum())

# Rolling Window Endpoints
df = pd.DataFrame({'x': 1},
                  index=[pd.Timestamp('20130101 09:00:01'),
                         pd.Timestamp('20130101 09:00:02'),
                         pd.Timestamp('20130101 09:00:03'),
                         pd.Timestamp('20130101 09:00:04'),
                         pd.Timestamp('20130101 09:00:06')])
df["right"] = df.rolling('2s', closed='right').x.sum()  # default
df["both"] = df.rolling('2s', closed='both').x.sum()
df["left"] = df.rolling('2s', closed='left').x.sum()
df["neither"] = df.rolling('2s', closed='neither').x.sum()
print(df)

# Centering Windows
print(ser.rolling(window=5).mean())
print(ser.rolling(window=5, center=True).mean())

# Binary Window Functions
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2000', periods=1000),
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df2 = df[:20]
print(df2.rolling(window=5).corr(df2['B']))

covs = df[['B', 'C', 'D']].rolling(window=50).cov(df[['A', 'B', 'C']], pairwise=True)
print(covs.loc['2002-09-22':])
correls = df.rolling(window=50).corr()
print(correls.loc['2002-09-22':])
correls.unstack(1)[('A', 'C')].plot()
plt.show()
