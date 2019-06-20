import numpy as np
import pandas as pd

# 检查是否一个元素包含一个可以匹配到的正则表达式
pattern = r'[0-9][a-z]'
print(pd.Series(['1', '2', '3a', '3b', '03c']).str.contains(pattern))

# 检查是否元素完整匹配一个正则表达式
print(pd.Series(['1', '2', '3a', '3b', '03c']).str.match(pattern))

s4 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s4.str.contains('A', na=False))
