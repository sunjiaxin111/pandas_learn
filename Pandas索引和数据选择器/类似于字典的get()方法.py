import pandas as pd

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s.get('a'))
print(s.get('x', default=-1))
