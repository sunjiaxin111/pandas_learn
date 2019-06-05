import datetime

import numpy as np
import pandas as pd

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
print(s - s.max())
print(s.max() - s)
print(s - datetime.datetime(2011, 1, 1, 3, 5))
print(s + datetime.timedelta(minutes=5))
print(datetime.datetime(2011, 1, 1, 3, 5) - s)
print(datetime.timedelta(minutes=5) + s)

# Adding and subtracting deltas and dates
deltas = pd.Series([datetime.timedelta(days=i) for i in range(3)])
df = pd.DataFrame(dict(A=s, B=deltas))
print(df)

df['New Dates'] = df['A'] + df['B']
df['Delta'] = df['A'] - df['New Dates']
print(df)
print(df.dtypes)

# Values can be set to NaT using np.nan, similar to datetime
# NaT是时间类型的null值
y = s - s.shift()
print(y)
y[1] = np.nan
print(y)
