import numpy as np
import pandas as pd

'''
当存在缺失值时，会发生数据转换
integer -> float
boolean -> object
float -> float
object -> object
'''
s = pd.Series(np.random.randn(5), index=[0, 2, 4, 6, 7])
print(s > 0)
print((s > 0).dtype)
crit = (s > 0).reindex(list(range(8)))
print(crit)
print(crit.dtype)

reindexed = s.reindex(list(range(8))).fillna(0)
# ValueError: cannot index with vector containing NA / NaN values
# print(reindexed[crit])
print(reindexed[crit.fillna(False)])
print(reindexed[crit.fillna(True)])
