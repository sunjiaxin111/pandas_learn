import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(7, 2))
pd.set_option('max_rows', 7)
print(df)
pd.set_option('max_rows', 5)
print(df)
pd.reset_option('max_rows')

# display.expand_frame_repr允许跨页面延伸
df = pd.DataFrame(np.random.randn(5, 100))
pd.set_option('expand_frame_repr', True)
print(df)
pd.set_option('expand_frame_repr', False)
print(df)
pd.reset_option('expand_frame_repr')

# display.large_repr
df = pd.DataFrame(np.random.randn(10, 10))
pd.set_option('max_rows', 5)
pd.set_option('large_repr', 'truncate')
print(df)
pd.set_option('large_repr', 'info')
print(df)
pd.reset_option('large_repr')
pd.reset_option('max_rows')

# display.max_colwidth
df = pd.DataFrame(np.array([['foo', 'bar', 'bim', 'uncomfortably long string'],
                            ['horse', 'cow', 'banana', 'apple']]))
pd.set_option('max_colwidth', 40)
print(df)
pd.set_option('max_colwidth', 6)
print(df)
pd.reset_option('max_colwidth')

# display.max_info_columns
df = pd.DataFrame(np.random.randn(10, 10))
pd.set_option('max_info_columns', 11)
print(df.info())
pd.set_option('max_info_columns', 5)
print(df.info())
pd.reset_option('max_info_columns')

df = pd.DataFrame(np.random.choice([0, 1, np.nan], size=(10, 10)))
print(df)
pd.set_option('max_info_rows', 11)
print(df.info())
pd.set_option('max_info_rows', 5)
print(df.info())
pd.reset_option('max_info_rows')

# display.precision
df = pd.DataFrame(np.random.randn(5, 5))
pd.set_option('precision', 7)
print(df)
pd.set_option('precision', 4)
print(df)
pd.reset_option('precision')

# display.chop_threshold
df = pd.DataFrame(np.random.randn(6, 6))
pd.set_option('chop_threshold', 0)
print(df)
# 绝对值小于0.5的元素，显示为0
pd.set_option('chop_threshold', .5)
print(df)
pd.reset_option('chop_threshold')

# display.colheader_justify控制headers靠左还是靠右对齐
df = pd.DataFrame(np.array([np.random.randn(6), np.random.randint(1, 9, 6) * .1, np.zeros(6)]).T,
                  columns=['A', 'B', 'C'], dtype='float')
pd.set_option('colheader_justify', 'right')
print(df)
pd.set_option('colheader_justify', 'left')
print(df)
pd.reset_option('colheader_justify')
