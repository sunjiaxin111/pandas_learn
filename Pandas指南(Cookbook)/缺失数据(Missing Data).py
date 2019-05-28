import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 1), index=pd.date_range('2013-08-01', periods=6, freq='B'), columns=list('A'))
df.loc[df.index[3], 'A'] = np.nan
print(df)
# ffill()函数用缺失值前的值来填充
print(df.reindex(df.index[::-1]).ffill())
