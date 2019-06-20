import numpy as np
import pandas as pd

# 从字符串列可以抽出一个哑变量。例如，是否他们由|分割
s = pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(s.str.get_dummies(sep='|'))

# 索引也支持get_dummies，它返回一个多重索引
idx = pd.Index(['a', 'a|b', np.nan, 'a|c'])
print(idx.str.get_dummies(sep='|'))
