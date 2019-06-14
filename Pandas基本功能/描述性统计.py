import numpy as np
import pandas as pd

data = {'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
        'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
        'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df)
print(df.mean())
print(df.mean(0))
print(df.mean(1))

# skipna参数决定是否排除缺失数据
print(df.sum(0, skipna=False))
print(df.sum(axis=1, skipna=True))

# 标准化
ts_stand = (df - df.mean()) / df.std()
print(ts_stand.std())
xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
print(xs_stand.std(1))

# Note that methods like cumsum() and cumprod() preserve the location of NaN values.
print(df)
print(df.cumsum())

'''
count（非空数目）
sum（求和）
mean（求均值）
mad（平均绝对偏差）Mean absolute deviation
median（求中位数）
min（求最小值）
max（求最大值）
mode（求众数）
abs（求绝对值）
prod（求乘积）
std（求标准差）
var（求方差）Unbiased variance
sem（求平均值的标准误差）Standard error of the mean
skew（样本偏斜（第3个时刻））Sample skewness (3rd moment)
kurt（样本峰度（第4个时刻））Sample kurtosis (4th moment)
quantile（样本分位数（值为％））Sample quantile (value at %)
cumsum（累积求和）
cumprod（累积乘积）
cummax（累积最大值）
cummin（累积最小值）
'''

# 一些NumPy方法，例如mean、std和sum，默认会排除Series输入的NaN值
print(np.mean(df['one']))
print(np.mean(df['one'].values))

# Series.nunique()会返回Series中非空的唯一值的个数
series = pd.Series(np.random.randn(500))
series[20:500] = np.nan
series[10:20] = 5
print(series.nunique())

# Summarizing data: describe
# describe()会计算一些统计信息（排除NaN值）
series = pd.Series(np.random.randn(1000))
series[::2] = np.nan
print(series.describe())
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
frame.iloc[::2] = np.nan
print(frame.describe())

# 可以选择特定的分位数输出
print(series.describe(percentiles=[.05, .25, .75, .95]))

# 对于非数值型的Series，describe()将给出count、unique、top(频率最高的值)、freq指标
s = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
print(s.describe())

# 对于混合类型的DataFrame对象，describe()将只给出数值列的信息
frame = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})
print(frame.describe())
# 可以通过include/exclude来控制展示哪些属性的列
print(frame.describe(include=['object']))
print(frame.describe(include=['number']))
print(frame.describe(include='all'))

# Index of Min/Max Values
# idxmin()和idxmax()方法会返回Series和DataFrame中对应的索引标签
s1 = pd.Series(np.random.randn(5))
print(s1)
print(s1.idxmin(), s1.idxmax())
df1 = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
print(df1)
print(df1.idxmin(axis=0))
print(df1.idxmax(axis=1))
# 当有多个最小值或最大值时，返回第一个匹配的索引标签
df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=['A'], index=list('edcba'))
print(df3)
print(df3['A'].idxmin())

# Value counts (histogramming) / Mode
data = np.random.randint(0, 7, size=50)
print(data)
s = pd.Series(data)
print(s.value_counts())
print(pd.value_counts(data))

# 求众数
s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
print(s5.mode())
df5 = pd.DataFrame({"A": np.random.randint(0, 7, size=50),
                    "B": np.random.randint(-10, 15, size=50)})
print(df5.mode())

# Discretization and quantiling
arr = np.random.randn(20)
# cut函数基于值来切分bin
factor = pd.cut(arr, 4)
print(factor)
factor = pd.cut(arr, [-5, -1, 0, 1, 5])
print(factor)
# qcut函数基于样本分位数来切分bin
arr = np.random.randn(30)
factor = pd.qcut(arr, [0, .25, .5, .75, 1])
print(factor)
print(pd.value_counts(factor))
# 也可以传入无穷大来定义bin
arr = np.random.randn(20)
factor = pd.cut(arr, [-np.inf, 0, np.inf])
print(factor)
