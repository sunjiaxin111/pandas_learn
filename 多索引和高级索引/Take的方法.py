import numpy as np
import pandas as pd

index = pd.Index(np.random.randint(0, 1000, 10))
print(index)
positions = [0, 9, 3]
print(index[positions])
print(index.take(positions))
ser = pd.Series(np.random.randn(10))
print(ser.iloc[positions])
print(ser.take(positions))

frm = pd.DataFrame(np.random.randn(5, 3))
print(frm.take([1, 4, 3]))
print(frm.take([0, 2], axis=1))

arr = np.random.randn(10)
# False等价于0，True等价于1
print(arr.take([False, False, True, True]))
print(arr[[0, 1]])
ser = pd.Series(np.random.randn(10))
print(ser.take([False, False, True, True]))
print(ser.iloc[[0, 1]])
