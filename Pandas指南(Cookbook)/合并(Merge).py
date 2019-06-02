import numpy as np
import pandas as pd

rng = pd.date_range('2000-01-01', periods=6)
df1 = pd.DataFrame(np.random.randn(6, 3), index=rng, columns=['A', 'B', 'C'])
df2 = df1.copy()

# ignore_index设置为True后，原始的index会被删除，新的index会从0开始编号
print(df1.append(df2))
print(df1.append(df2, ignore_index=True))

df = pd.DataFrame(data={'Area': ['A'] * 5 + ['C'] * 2,
                        'Bins': [110] * 2 + [160] * 3 + [40] * 2,
                        'Test_0': [0, 1, 0, 1, 2, 0, 1],
                        'Data': np.random.randn(7)})
df['Test_1'] = df['Test_0'] - 1
print(df)
print(pd.merge(df, df, left_on=['Bins', 'Area', 'Test_0'], right_on=['Bins', 'Area', 'Test_1'], suffixes=('_L', '_R')))
