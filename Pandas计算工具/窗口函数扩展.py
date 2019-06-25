import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# .rolling, with the .expanding method returning an Expanding object.
df = pd.DataFrame(np.random.randn(1000, 4),
                  index=pd.date_range('1/1/2000', periods=1000),
                  columns=['A', 'B', 'C', 'D'])
print(df.rolling(window=len(df), min_periods=1).mean()[:5])
# 等价方法
# Expanding windows 截止每个时间点累计求和的平均值
print(df.expanding(min_periods=1).mean()[:5])

sn = pd.Series([1, 2, np.nan, 3, np.nan, 4])
print(sn)
print(sn.rolling(2).max())
print(sn.rolling(2, min_periods=1).max())
print(sn.expanding().sum())
print(sn.cumsum())
print(sn.cumsum().fillna(method='ffill'))

s = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
s = s.cumsum()
s.plot(style='k--')
s.expanding().mean().plot(style='k')
plt.show()

# expanding方法 累计计算
data = {"date": pd.date_range("2018-12-04", periods=7),
        "income": [1000, 2000, np.nan, 3000, 4000, 5000, 6000]}
df = pd.DataFrame(data=data)
print(df.expanding(min_periods=1, axis=0)['income'].sum())
print(df.expanding(min_periods=2, axis=0)['income'].sum())
