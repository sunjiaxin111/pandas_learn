import numpy as np
import pandas as pd

long_series = pd.Series(np.random.randn(1000))
# 默认的展示元素数量是5，但是你可以传入任意的一个数值。
print(long_series.head())
print(long_series.tail(3))
