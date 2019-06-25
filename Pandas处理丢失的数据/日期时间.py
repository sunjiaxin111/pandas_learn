import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])
df['four'] = 'bar'
df['five'] = df['one'] > 0
df2 = df.copy()
df2['timestamp'] = pd.Timestamp('20120101')
print(df2)
df2.loc[['a', 'c', 'h'], ['one', 'timestamp']] = np.nan
print(df2)
print(df2.get_dtype_counts())
