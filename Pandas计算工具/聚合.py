import numpy as np
import pandas as pd

dfa = pd.DataFrame(np.random.randn(1000, 3),
                   index=pd.date_range('1/1/2000', periods=1000),
                   columns=['A', 'B', 'C'])
r = dfa.rolling(window=60, min_periods=1)
print(r)
print(r.aggregate(np.sum))
print(r['A'].aggregate(np.sum))
print(r[['A', 'B']].aggregate(np.sum))

# apply多个函数
print(r['A'].agg([np.sum, np.mean, np.std]))
print(r.agg([np.sum, np.mean]))

# apply不同的函数到不同的列
print(r.agg({'A': np.sum,
             'B': lambda x: np.std(x, ddof=1)}))
print(r.agg({'A': 'sum', 'B': 'std'}))
print(r.agg({'A': ['sum', 'std'], 'B': ['mean', 'std']}))
