import numpy as np
import pandas as pd
import statsmodels.formula.api as sm

'''
Tablewise Function Application: pipe()
Row or Column-wise Function Application: apply()
Aggregation API: agg() and transform()
Applying Elementwise Functions: applymap()
'''
# Tablewise Function Application
# 使用pipe()方法来进行链式调用,下面是2种等价方法
# f(g(h(df), arg1=1), arg2=2, arg3=3)
# df.pipe(h).pipe(g, arg1=1).pipe(f, arg2=2, arg3=3)
bb = pd.read_csv('baseball.csv', index_col='id')
print(bb.query('h > 0')
      .assign(ln_h=lambda df: np.log(df.h))
      .pipe((sm.ols, 'data'), 'hr ~ ln_h + year + g + C(lg)')
      .fit()
      .summary())

# Row or Column-wise Function Application
data = {'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
        'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
        'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df.apply(np.mean))
print(df.apply(np.mean, axis=1))
print(df.apply(lambda x: x.max() - x.min()))
print(df.apply(np.cumsum))
print(df.apply(np.exp))
print(df.apply('mean'))
print(df.apply('mean', axis=1))

tsdf = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=1000))
print(tsdf.apply(lambda x: x.idxmax()))


def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide


# 在apply的同时传入参数
print(df.apply(subtract_and_divide, args=(5,), divide=3))

# 使用Series方法
tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=10))
tsdf.iloc[3:7] = np.nan
print(tsdf)
print(tsdf.apply(pd.Series.interpolate))

# Aggregation API
tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=10))
tsdf.iloc[3:7] = np.nan
print(tsdf)
# 使用单一函数是与apply函数一致的
print(tsdf.agg(np.sum))
print(tsdf.agg('sum'))
print(tsdf.sum())
print(tsdf.A.agg('sum'))

# Aggregating with multiple functions
print(tsdf.agg(['sum']))
print(tsdf.agg(['sum', 'mean']))
print(tsdf.A.agg(['sum', 'mean']))
print(tsdf.A.agg(['sum', lambda x: x.mean()]))
print(tsdf.A.agg(['sum', lambda x: x.mean(), lambda x: x.mean()]))


def mymean(x):
    return x.mean()


print(tsdf.A.agg(['sum', mymean]))

# Aggregating with a dict
print(tsdf.agg({'A': 'mean', 'B': 'sum'}))
print(tsdf.agg({'A': ['mean', 'min'], 'B': 'sum'}))

# 混合类型无法agg
mdf = pd.DataFrame({'A': [1, 2, 3],
                    'B': [1., 2., 3.],
                    'C': ['foo', 'bar', 'baz'],
                    'D': pd.date_range('20130101', periods=3)})
print(mdf.dtypes)
print(mdf.agg(['min', 'sum']))

# Custom describe
from functools import partial

q_25 = partial(pd.Series.quantile, q=0.25)
q_25.__name__ = '25%'
q_75 = partial(pd.Series.quantile, q=0.75)
q_75.__name__ = '75%'
print(tsdf.agg(['count', 'mean', 'std', 'min', q_25, 'median', q_75, 'max']))

# Transform API
tsdf = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
                    index=pd.date_range('1/1/2000', periods=10))
tsdf.iloc[3:7] = np.nan
print(tsdf)
print(tsdf.transform(np.abs))
print(tsdf.transform('abs'))
print(tsdf.transform(lambda x: x.abs()))
print(np.abs(tsdf))
print(tsdf.A.transform(np.abs))

# Transform with multiple functions
# 传递多个函数会生成一个多级索引列的DataFrame
print(tsdf.transform([np.abs, lambda x: x + 1]))
print(tsdf.A.transform([np.abs, lambda x: x + 1]))
# Transforming with a dict
print(tsdf.transform({'A': np.abs, 'B': lambda x: x + 1}))
print(tsdf.transform({'A': np.abs, 'B': [lambda x: x + 1, 'sqrt']}))

# Applying Elementwise Functions
print(df)
f = lambda x: len(str(x))
print(df['one'].map(f))
print(df.applymap(f))

# Series.map()可以传入Series
s = pd.Series(['six', 'seven', 'six', 'seven', 'six'],
              index=['a', 'b', 'c', 'd', 'e'])
t = pd.Series({'six': 6., 'seven': 7.})
print(s)
print(s.map(t))

# Applying with a Panel
import pandas.util.testing as tm

panel = tm.makePanel(5)
print(panel)
print(panel['ItemA'])
result = panel.apply(lambda x: x * 2, axis='items')
print(result)
print(result['ItemA'])

# A reduction operation
print(panel.apply(lambda x: x.dtype, axis='items'))
print(panel.apply(lambda x: x.sum(), axis='major_axis'))
print(panel.sum('major_axis'))

result = panel.apply(
    lambda x: (x - x.mean()) / x.std(),
    axis='major_axis')
print(result)
print(result['ItemA'])

f = lambda x: ((x.T - x.mean(1)) / x.std(1)).T
result = panel.apply(f, axis=['items', 'major_axis'])
print(result)
print(result.loc[:, :, 'ItemA'])
# 等价于下式
result = pd.Panel(dict([(ax, f(panel.loc[:, :, ax]))
                        for ax in panel.minor_axis]))
print(result)
print(result.loc[:, :, 'ItemA'])
