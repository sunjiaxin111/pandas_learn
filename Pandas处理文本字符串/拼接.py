import numpy as np
import pandas as pd

# 将单个序列拼接为一个完整字符串
s = pd.Series(['a', 'b', 'c', 'd'])
print(s.str.cat(sep=','))
# 默认sep=''
print(s.str.cat())
# 默认情况下，缺失值会被忽略。使用na_rep参数，可以对缺失值进行赋值
t = pd.Series(['a', 'b', np.nan, 'd'])
print(t.str.cat(sep=','))
print(t.str.cat(sep=',', na_rep='-'))

# 拼接序列和其他类列表型对象为新的序列
print(s.str.cat(['A', 'B', 'C', 'D']))
# 任何一端的缺失值都会导致之中结果为缺失值，除非使用na_rep
print(s.str.cat(t))
print(s.str.cat(t, na_rep='-'))

# 拼接序列与类数组对象为新的序列
# others 参数可以是二维的。此时，行数需要与序列或索引的长度相同
d = pd.concat([t, s], axis=1)
print(s)
print(d)
print(s.str.cat(d, na_rep='-'))

# 对齐拼接序列与带索引的对象成为新的序列
# 对于拼接序列或者数据表，我们可以使用 join关键字来对齐索引
u = pd.Series(['b', 'd', 'a', 'c'], index=[1, 3, 0, 2])
print(s)
print(u)
# 如果不使用join关键字，cat()方法则是无对齐模式
print(s.str.cat(u))
print(s.str.cat(u, join='left'))

# 对齐操作使得两个对象可以是不同的长度
v = pd.Series(['z', 'a', 'b', 'd', 'e'], index=[-1, 0, 1, 3, 4])
print(s)
print(v)
print(s.str.cat(v, join='left', na_rep='-'))
print(s.str.cat(v, join='outer', na_rep='-'))
# 当others是一个数据表时，也可以执行相同的对齐操作
f = d.loc[[3, 2, 1, 0], :]
print(s)
print(f)
print(s.str.cat(f, join='left', na_rep='-'))

# 将一个序列与多个对象拼接为一个新的序列
print(s)
print(u)
print(s.str.cat([u, pd.Index(u.values), ['A', 'B', 'C', 'D'], map(str, u.index)], na_rep='-'))

# 所有的元素必须与序列或索引有相同的长度，除了那些有索引的，且join不为None的对象
print(v)
print(s.str.cat([u, v, ['A', 'B', 'C', 'D']], join='outer', na_rep='-'))

# 如果在一个包含不同的索引的others列表上使用join='right'，所有索引的并集将会被作为最终拼接的基础
print(u.loc[[3]])
print(v.loc[[-1, 0]])
print(s.str.cat([u.loc[[3]], v.loc[[-1, 0]]], join='right', na_rep='-'))
