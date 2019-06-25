import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                  columns=['one', 'two', 'three'])
a = df[['one', 'two']]
b = df[['one', 'two', 'three']]
a.iloc[:2, 0] = np.nan
b.iloc[[0, 1, 4], 0] = np.nan
print(a)
print(b)
print(a + b)
df = b
print(df)
# sum时NaN被当做0
print(df['one'].sum())
print(df.mean(1))
print(df.cumsum())
print(df.cumsum(skipna=False))

# The sum of an empty or all-NA Series or column of a DataFrame is 0.
print(pd.Series([np.nan]).sum())
print(pd.Series([]).sum())
# The product of an empty or all-NA Series or column of a DataFrame is 1.
print(pd.Series([np.nan]).prod())
print(pd.Series([]).prod())
# NA groups in GroupBy are automatically excluded.
print(df.groupby('one').mean())
