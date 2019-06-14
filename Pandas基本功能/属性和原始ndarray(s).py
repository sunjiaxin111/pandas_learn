import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(8, 3), index=pd.date_range('1/1/2000', periods=8), columns=['A', 'B', 'C'])
print(df)
print(df[:2])

df.columns = [x.lower() for x in df.columns]
print(df)

# 通过访问values属性来获得数据结构中的实际值
print(df.values)
