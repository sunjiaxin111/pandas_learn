import numpy as np
import pandas as pd

dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

s = pd.Series(range(-3, 4))
print(s)
print(s[s > 0])
print(s[(s < -1) | (s > 0.5)])
print(s[~(s < 0)])

print(df[df['A'] > 0])

# map方法
df2 = pd.DataFrame({'a': ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
                    'b': ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
                    'c': np.random.randn(7)})
criterion = df2['a'].map(lambda x: x.startswith('t'))
print(df2[criterion])
# 等价但更慢的方法
print(df2[[x.startswith('t') for x in df2['a']]])

print(df2[criterion & (df2['b'] == 'x')])
print(df2.loc[criterion & (df2['b'] == 'x'), 'b':'c'])
