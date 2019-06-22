import numpy as np
import pandas as pd

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
s = df['A']
print(s[:5])
print(s[::2])
print(s[::-1])

s2 = s.copy()
s2[:5] = 0
print(s2)

# DataFrame中[]切片行
print(df[:3])
print(df[::-1])
