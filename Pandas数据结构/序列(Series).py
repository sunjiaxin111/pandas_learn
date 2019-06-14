import numpy as np
import pandas as pd

# From ndarray
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)
print(pd.Series(np.random.randn(5)))
# pandas supports non-unique index values.

# From dict
d = {'b': 1, 'a': 0, 'c': 2}
print(pd.Series(d))

d = {'a': 0., 'b': 1., 'c': 2.}
print(pd.Series(d))
print(pd.Series(d, index=['b', 'c', 'd', 'a']))
# Note： NaN (not a number) is the standard missing data marker used in pandas.

# From scalar value
print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))

# Series is ndarray-like
print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 1]])
print(np.exp(s))

# Series is dict-like
print(s['a'])
s['e'] = 12.
print(s)
print('e' in s)
print('f' in s)
# print(s['f'])
print(s.get('f'))
print(s.get('f', np.nan))

# Vectorized operations and label alignment with Series
print(s + s)
print(s * 2)
print(np.exp(s))
print(s[1:] + s[:-1])

# Name attribute
s = pd.Series(np.random.randn(5), name='something')
print(s)
print(s.name)
s2 = s.rename("different")
print(s2.name)
