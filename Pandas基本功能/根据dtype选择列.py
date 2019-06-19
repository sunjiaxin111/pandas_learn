import numpy as np
import pandas as pd

df = pd.DataFrame({'string': list('abc'),
                   'int64': list(range(1, 4)),
                   'uint8': np.arange(3, 6).astype('u1'),
                   'float64': np.arange(4.0, 7.0),
                   'bool1': [True, False, True],
                   'bool2': [False, True, False],
                   'dates': pd.date_range('now', periods=3).values,
                   'category': pd.Series(list("ABC")).astype('category')})
df['tdeltas'] = df.dates.diff()
df['uint64'] = np.arange(3, 6).astype('u8')
df['other_dates'] = pd.date_range('20130101', periods=3).values
df['tz_aware_dates'] = pd.date_range('20130101', periods=3, tz='US/Eastern')
print(df)
print(df.dtypes)

# select_dtypes()
print(df.select_dtypes(include=[bool]))
print(df.select_dtypes(include=['bool']))
print(df.select_dtypes(include=['number', 'bool'], exclude=['unsignedinteger']))
print(df.select_dtypes(include=['object']))


# 打印子类型
def subdtypes(dtype):
    subs = dtype.__subclasses__()
    if not subs:
        return dtype
    return [dtype, [subdtypes(dt) for dt in subs]]


print(subdtypes(np.generic))
