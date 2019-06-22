import numpy as np
import pandas as pd

se = pd.Series([1, 2, 3])
print(se)
se[5] = 5.
print(se)

dfi = pd.DataFrame(np.arange(6).reshape(3, 2),
                   columns=['A', 'B'])
print(dfi)
dfi.loc[:, 'C'] = dfi.loc[:, 'A']
print(dfi)

dfi.loc[3] = 5
print(dfi)
