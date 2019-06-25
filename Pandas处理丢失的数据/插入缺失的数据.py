import numpy as np
import pandas as pd

'''
数值型类型赋值为None,转换为NaN
日期型类型赋值为None,转换为NaT
object类型赋值为None,即为None
'''
s = pd.Series([1, 2, 3])
s.loc[0] = None
print(s)
s = pd.Series(["a", "b", "c"])
s.loc[0] = None
s.loc[1] = np.nan
print(s)
