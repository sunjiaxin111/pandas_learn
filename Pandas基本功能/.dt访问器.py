import pandas as pd

s = pd.Series(pd.date_range('20130101 09:10:12', periods=4))
print(s)
print(s.dt.hour)
print(s.dt.second)
print(s.dt.day)
print(s[s.dt.day == 2])

# time zone
stz = s.dt.tz_localize('US/Eastern')
print(stz)
print(stz.dt.tz)

# 链式操作
print(s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern'))

# 格式化
# DatetimeIndex
s = pd.Series(pd.date_range('20130101', periods=4))
print(s)
print(s.dt.strftime('%Y/%m/%d'))
# PeriodIndex
s = pd.Series(pd.period_range('20130101', periods=4))
print(s)
print(s.dt.strftime('%Y/%m/%d'))

# .dt访问符也适用于period和timedelta类型
# period
s = pd.Series(pd.period_range('20130101', periods=4, freq='D'))
print(s)
print(s.dt.year)
print(s.dt.day)
# timedelta
s = pd.Series(pd.timedelta_range('1 day 00:00:05', periods=4, freq='s'))
print(s)
print(s.dt.days)
print(s.dt.seconds)
print(s.dt.components)
