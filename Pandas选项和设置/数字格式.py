import numpy as np
import pandas as pd

pd.set_eng_float_format(accuracy=3, use_eng_prefix=True)
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s / 1.e3)
print(s / 1.e6)
