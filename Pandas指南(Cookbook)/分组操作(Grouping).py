import functools

import numpy as np
import pandas as pd

df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
                   'size': list('SSMMMLL'),
                   'weight': [8, 10, 11, 1, 20, 12, 12],
                   'adult': [False] * 5 + [True] * 2})
print(df)
# 列出每种animal中有最高weight的size
# idxmax() 返回当前对象第一个出现最小值的索引
print(df.groupby('animal').apply(lambda x: x['size'][x['weight'].idxmax()]))

# 使用get_group
gb = df.groupby(['animal'])
print(gb.get_group('cat'))


# 在group内apply不同的项目
def GrowUp(x):
    avg_weight = sum(x[x['size'] == 'S'].weight * 1.5)
    avg_weight += sum(x[x['size'] == 'M'].weight * 1.25)
    avg_weight += sum(x[x['size'] == 'L'].weight)
    avg_weight /= len(x)
    return pd.Series(['L', avg_weight, True], index=['size', 'weight', 'adult'])


expected_df = gb.apply(GrowUp)
print(expected_df)

# Expanding Apply
S = pd.Series([i / 100.0 for i in range(1, 11)])


def CumRet(x, y):
    return x * (1 + y)


def Red(x):
    # reduce(function, sequence[, initial]) -> value
    # 对sequence连续使用function, 如果不给出initial,
    # 则第一次调用传递sequence的两个元素, 以后把前一次调用的结果和sequence的下一个元素传递给function.
    # 如果给出initial, 则第一次传递initial和sequence的第一个元素给function.
    return functools.reduce(CumRet, x, 1.0)


print(S.expanding().apply(Red, raw=True))

# Replacing some values with mean of the rest of a group
df = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [1, -1, 1, 2]})
gb = df.groupby('A')


def replace(g):
    mask = g < 0
    g.loc[mask] = g[~mask].mean()
    return g


print(gb.transform(replace))

# Sort groups by aggregated data
df = pd.DataFrame({'code': ['foo', 'bar', 'baz'] * 2,
                   'data': [0.16, -0.21, 0.33, 0.45, -0.59, 0.62],
                   'flag': [False, True] * 3})
code_groups = df.groupby('code')
agg_n_sort_order = code_groups[['data']].transform(sum).sort_values(by='data')
sorted_df = df.loc[agg_n_sort_order.index]
print(sorted_df)

# Create multiple aggregated columns
rng = pd.date_range(start="2014-10-07", periods=10, freq='2min')
ts = pd.Series(data=list(range(10)), index=rng)


def MyCust(x):
    if len(x) > 2:
        return x[1] * 1.234
    return pd.NaT


mhc = {'Mean': np.mean, 'Max': np.max, 'Custom': MyCust}
print(ts.resample("5min").apply(mhc))
print(ts)

# Create a value counts column and reassign back to the DataFrame
df = pd.DataFrame({'Color': 'Red Red Red Blue'.split(),
                   'Value': [100, 150, 50, 50]})
print(df)
df['Counts'] = df.groupby(['Color']).transform(len)
print(df)

# 特点: transform返回与数据同样长度的行，而apply则进行了聚合
# Shift groups of the values in a column based on the index
df = pd.DataFrame(
    {u'line_race': [10, 10, 8, 10, 10, 8],
     u'beyer': [99, 102, 103, 103, 88, 100]},
    index=[u'Last Gunfighter', u'Last Gunfighter', u'Last Gunfighter',
           u'Paynter', u'Paynter', u'Paynter'])
print(df)
df['beyer_shifted'] = df.groupby(level=0)['beyer'].shift(1)
print(df)

# Select row with maximum value from each group
df = pd.DataFrame({'host': ['other', 'other', 'that', 'this', 'this'],
                   'service': ['mail', 'web', 'mail', 'mail', 'web'],
                   'no': [1, 2, 1, 2, 1]}).set_index(['host', 'service'])
print(df)
mask = df.groupby(level=0).agg('idxmax')
df_count = df.loc[mask['no']].reset_index()
print(df_count)

# Grouping like Python’s itertools.groupby
df = pd.DataFrame([0, 1, 0, 1, 1, 1, 0, 1, 1], columns=['A'])
print(df.A.groupby((df.A != df.A.shift()).cumsum()).groups)
print(df.A.groupby((df.A != df.A.shift()).cumsum()).cumsum())

# Splitting
df = pd.DataFrame(data={'Case': ['A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A'],
                        'Data': np.random.randn(9)})
dfs = list(zip(*df.groupby((1 * (df['Case'] == 'B')).cumsum().rolling(window=3, min_periods=1).median())))[-1]
print(dfs[0])
print(dfs[1])
print(dfs[2])

# Pivot
df = pd.DataFrame(data={'Province': ['ON', 'QC', 'BC', 'AL', 'AL', 'MN', 'ON'],
                        'City': ['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Edmonton', 'Winnipeg', 'Windsor'],
                        'Sales': [13, 6, 16, 8, 4, 3, 1]})
table = pd.pivot_table(df, values=['Sales'], index=['Province'], columns=['City'], aggfunc=np.sum, margins=True)
print(table.stack('City'))

# Frequency table like plyr in R
grades = [48, 99, 75, 80, 42, 80, 72, 68, 36, 78]
df = pd.DataFrame({'ID': ["x%d" % r for r in range(10)],
                   'Gender': ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'M', 'M'],
                   'ExamYear': ['2007', '2007', '2007', '2008', '2008', '2008', '2008', '2009', '2009', '2009'],
                   'Class': ['algebra', 'stats', 'bio', 'algebra', 'algebra', 'stats', 'stats', 'algebra', 'bio',
                             'bio'],
                   'Participated': ['yes', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes'],
                   'Passed': ['yes' if x > 50 else 'no' for x in grades],
                   'Employed': [True, True, True, False, False, False, False, True, True, False],
                   'Grade': grades})
print(df.groupby('ExamYear').agg({'Participated': lambda x: x.value_counts()['yes'],
                                  'Passed': lambda x: sum(x == 'yes'),
                                  'Employed': lambda x: sum(x),
                                  'Grade': lambda x: sum(x) / len(x)}))

# Plot pandas DataFrame with year over year data
df = pd.DataFrame({'value': np.random.randn(36)},
                  index=pd.date_range('2011-01-01', freq='M', periods=36))
print(pd.pivot_table(df, index=df.index.month, columns=df.index.year,
                     values='value', aggfunc='sum'))

# Apply
df = pd.DataFrame(data={'A': [[2, 4, 8, 16], [100, 200], [10, 20, 30]], 'B': [['a', 'b', 'c'], ['jj', 'kk'], ['ccc']]},
                  index=['I', 'II', 'III'])


def SeriesFromSubList(aList):
    return pd.Series(aList)


df_orgz = pd.concat(dict([(ind, row.apply(SeriesFromSubList)) for ind, row in df.iterrows()]))
df = pd.DataFrame(data=np.random.randn(2000, 2) / 10000,
                  index=pd.date_range('2001-01-01', periods=2000),
                  columns=['A', 'B'])
print(df)


def gm(aDF, Const):
    v = ((((aDF.A + aDF.B) + 1).cumprod()) - 1) * Const
    return (aDF.index[0], v.iloc[-1])


S = pd.Series(dict([gm(df.iloc[i:min(i + 51, len(df) - 1)], 5) for i in range(len(df) - 50)]))
print(S)

rng = pd.date_range(start='2014-01-01', periods=100)
df = pd.DataFrame({'Open': np.random.randn(len(rng)),
                   'Close': np.random.randn(len(rng)),
                   'Volume': np.random.randint(100, 2000, len(rng))}, index=rng)
print(df)


def vwap(bars): return ((bars.Close * bars.Volume).sum() / bars.Volume.sum())


window = 5
s = pd.concat([(pd.Series(vwap(df.iloc[i:i + window]), index=[df.index[i + window]])) for i in range(len(df) - window)])
print(s.round(2))
