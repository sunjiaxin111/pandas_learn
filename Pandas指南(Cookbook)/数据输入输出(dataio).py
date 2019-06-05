import glob
from io import StringIO
from time import clock

import numpy as np
import pandas as pd

# 从多个文件读取数据，以创建一个DataFrame
for i in range(3):
    data = pd.DataFrame(np.random.randn(10, 4))
    data.to_csv('file_{}.csv'.format(i))

files = ['file_0.csv', 'file_1.csv', 'file_2.csv']
result = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# 可以通过glob来读取满足条件的所有文件
files = glob.glob('file_*.csv')
result1 = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# 解析多列中的日期组件
# 使用format解析多列中的日期组件会更快
i = pd.date_range('20000101', periods=10000)
df = pd.DataFrame(dict(year=i.year, month=i.month, day=i.day))
print(df.head())
start = clock()
pd.to_datetime(df.year * 10000 + df.month * 100 + df.day, format='%Y%m%d')
end = clock()
print(end - start)

start = clock()
ds = df.apply(lambda x: "%04d%02d%02d" % (x['year'], x['month'], x['day']), axis=1)
print(ds.head())
pd.to_datetime(ds)
end = clock()
print(end - start)

# Skip row between header and data
data = """;;;;
     ;;;;
     ;;;;
     ;;;;
     ;;;;
     ;;;;
    ;;;;
     ;;;;
     ;;;;
    ;;;;
    date;Param1;Param2;Param4;Param5
        ;m²;°C;m²;m
    ;;;;
    01.01.1990 00:00;1;1;2;3
    01.01.1990 01:00;5;3;4;5
    01.01.1990 02:00;9;5;6;7
    01.01.1990 03:00;13;7;8;9
    01.01.1990 04:00;17;9;10;11
    01.01.1990 05:00;21;11;12;13
    """

# 方法1：显式地跳过行
print(pd.read_csv(StringIO(data), sep=';', skiprows=[11, 12],
                  index_col=0, parse_dates=True, header=10))

# 方法2：先读列名，再读数据
print(pd.read_csv(StringIO(data), sep=';', header=10, nrows=10).columns)
columns = pd.read_csv(StringIO(data), sep=';', header=10, nrows=10).columns
print(pd.read_csv(StringIO(data), sep=';', index_col=0,
                  header=12, parse_dates=True, names=columns))

# Storing Attributes to a group node
df = pd.DataFrame(np.random.randn(8, 3))
store = pd.HDFStore('test.h5')
store.put('df', df)
store.get_storer('df').attrs.my_attribute = dict(A=10)
print(store.get_storer('df').attrs.my_attribute)
