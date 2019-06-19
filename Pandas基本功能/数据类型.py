import numpy as np
import pandas as pd

dft = pd.DataFrame(dict(A=np.random.rand(3),
                        B=1,
                        C='foo',
                        D=pd.Timestamp('20010102'),
                        E=pd.Series([1.0] * 3).astype('float32'),
                        F=False,
                        G=pd.Series([1] * 3, dtype='int8')))
print(dft)
print(dft.dtypes)
print(dft['A'].dtype)

# int值被转换成float类型
print(pd.Series([1, 2, 3, 4, 5, 6.]))

# 全部转换成object类型
print(pd.Series([1, 2, 3, 6., 'foo']))

# 获取每种类型的列数
print(dft.get_dtype_counts())

df1 = pd.DataFrame(np.random.randn(8, 1), columns=['A'], dtype='float32')
print(df1)
print(df1.dtypes)
df2 = pd.DataFrame(dict(A=pd.Series(np.random.randn(8), dtype='float16'),
                        B=pd.Series(np.random.randn(8)),
                        C=pd.Series(np.array(np.random.randn(8), dtype='uint8'))))
print(df2)
print(df2.dtypes)

# 默认的整型类型是int64,默认的浮点数类型是float64
print(pd.DataFrame([1, 2], columns=['a']).dtypes)
print(pd.DataFrame({'a': [1, 2]}).dtypes)
print(pd.DataFrame({'a': 1}, index=list(range(2))).dtypes)

# numpy在创建数组时会选择平台依赖的类型。
# 下面的代码在32位平台会产生int32的结果
print(pd.DataFrame(np.array([1, 2])).dtypes)

# upcasting
df3 = df1.reindex_like(df2).fillna(value=0.0) + df2
print(df3)
print(df3.dtypes)
print(df3.values.dtype)

# astype 返回副本
print(df3)
print(df3.dtypes)
print(df3.astype('float32').dtypes)

dft = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
dft[['a', 'b']] = dft[['a', 'b']].astype(np.uint8)
print(dft)
print(dft.dtypes)

dft1 = pd.DataFrame({'a': [1, 0, 1], 'b': [4, 5, 6], 'c': [7, 8, 9]})
dft1 = dft1.astype({'a': np.bool, 'c': np.float64})
print(dft1)
print(dft1.dtypes)

dft = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
print(dft.loc[:, ['a', 'b']].astype(np.uint8).dtypes)
# 意想不到的结果
dft.loc[:, ['a', 'b']] = dft.loc[:, ['a', 'b']].astype(np.uint8)
print(dft.dtypes)

# object conversion
import datetime

df = pd.DataFrame([[1, 2],
                   ['a', 'b'],
                   [datetime.datetime(2016, 3, 2), datetime.datetime(2016, 3, 2)]])
print(df)
df = df.T
print(df)
print(df.dtypes)
# 得到正确的类型
print(df.infer_objects().dtypes)

# 硬转换
m = ['1.1', 2, 3]
print(pd.to_numeric(m))
m = ['2016-07-09', datetime.datetime(2016, 3, 2)]
print(pd.to_datetime(m))
m = ['5us', pd.Timedelta('1day')]
print(pd.to_timedelta(m))

# errors参数
m = ['apple', datetime.datetime(2016, 3, 2)]
print(pd.to_datetime(m, errors='coerce'))
m = ['apple', 2, 3]
print(pd.to_numeric(m, errors='coerce'))
m = ['apple', pd.Timedelta('1day')]
print(pd.to_timedelta(m, errors='coerce'))

m = ['apple', datetime.datetime(2016, 3, 2)]
print(pd.to_datetime(m, errors='ignore'))
m = ['apple', 2, 3]
print(pd.to_numeric(m, errors='ignore'))
m = ['apple', pd.Timedelta('1day')]
print(pd.to_timedelta(m, errors='ignore'))

# to_numeric() downcast 向下转换
m = ['1', 2, 3]
print(pd.to_numeric(m, downcast='integer').dtype)  # 最小的整型
print(pd.to_numeric(m, downcast='signed').dtype)
print(pd.to_numeric(m, downcast='unsigned').dtype)
print(pd.to_numeric(m, downcast='float').dtype)  # 最小的浮点型

# 这些方法只能应用到一维数组，通过apply方法可以应用到DataFrame
df = pd.DataFrame([['2016-07-09', datetime.datetime(2016, 3, 2)]] * 2, dtype='O')
print(df.dtypes)
print(df.apply(pd.to_datetime).dtypes)
df = pd.DataFrame([['1.1', 2, 3]] * 2, dtype='O')
print(df.dtypes)
print(df.apply(pd.to_numeric).dtypes)
df = pd.DataFrame([['5us', pd.Timedelta('1day')]] * 2, dtype='O')
print(df.dtypes)
print(df.apply(pd.to_timedelta).dtypes)

# 陷阱
# integer类型上进行选择操作很容易把数据向上转化为float类型
dfi = df3.astype('int32')
dfi['E'] = 1
print(dfi)
print(dfi.dtypes)
casted = dfi[dfi > 0]
print(casted)
print(casted.dtypes)

# float类型不会受影响
dfa = df3.copy()
dfa['A'] = dfa['A'].astype('float32')
print(dfa.dtypes)
casted = dfa[df2 > 0]
print(casted)
print(casted.dtypes)
