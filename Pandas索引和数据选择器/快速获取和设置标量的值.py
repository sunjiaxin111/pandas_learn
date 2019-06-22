import numpy as np
import pandas as pd

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
s = pd.Series([0, 1, 2, 3, 4, 5])

print(df)
print(s.iat[5])
print(df.at[dates[5], 'A'])
print(df.iat[3, 0])

# 设置值
df.at[dates[5], 'E'] = 7
df.iat[3, 0] = 7
df.at[dates[-1] + 1, 0] = 7
print(df)
