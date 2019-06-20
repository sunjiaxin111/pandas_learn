import pandas as pd

print(pd.Series(['a1', 'b2', 'c3']).str.extract('([ab])(\d)', expand=False))
# 有名称的捕获组
print(pd.Series(['a1', 'b2', 'c3']).str.extract('(?P<letter>[ab])(?P<digit>\d)', expand=False))
# 可选组
print(pd.Series(['a1', 'b2', '3']).str.extract('([ab])?(\d)', expand=False))

# 如果仅使用正则表达式捕获一个组，而expand=True，那么仍然将返回一个数据表
print(pd.Series(['a1', 'b2', 'c3']).str.extract('[ab](\d)', expand=True))
# 如果expand=False，则会返回一个序列
print(pd.Series(['a1', 'b2', 'c3']).str.extract('[ab](\d)', expand=False))

# 在索引上使用正则表达式，并且仅捕获一个组时，将会返回一个数据表，如果expand=True
s = pd.Series(["a1", "b2", "c3"], ["A11", "B22", "C33"])
print(s)
print(s.index.str.extract("(?P<letter>[a-zA-Z])", expand=True))
# 如果expand=False，则返回一个Index
print(s.index.str.extract("(?P<letter>[a-zA-Z])", expand=False))
# 如果在索引上使用正则并捕获多个组，则返回一个数据表，如果expand=True
print(s.index.str.extract("(?P<letter>[a-zA-Z])([0-9]+)", expand=True))
# 如果 expand=False，则抛出ValueError
# print(s.index.str.extract("(?P<letter>[a-zA-Z])([0-9]+)", expand=False))

# 提取所有的匹配 (extractall)
# extract（只返回第一个匹配）
s = pd.Series(["a1a2", "b1", "c1"], index=["A", "B", "C"])
print(s)
two_groups = '(?P<letter>[a-z])(?P<digit>[0-9])'
print(s.str.extract(two_groups, expand=True))
# extractall方法返回所有的匹配。extractall总是返回一个带有行多重索引的数据表，最后一级被命名为match，它指出匹配的顺序
print(s.str.extractall(two_groups))

# 当所有的对象字串都只有一个匹配时，extractall(pat).xs(0, level='match') 的返回与extract(pat)相同
s = pd.Series(['a3', 'b3', 'c2'])
print(s)
extract_result = s.str.extract(two_groups, expand=True)
print(extract_result)
extractall_result = s.str.extractall(two_groups)
print(extractall_result)
print(extractall_result.xs(0, level="match"))

# 索引也支持.str.extractall。 它返回一个数据表，其中包含与Series.str.estractall相同的结果
print(pd.Index(["a1a2", "b1", "c1"]).str.extractall(two_groups))
print(pd.Series(["a1a2", "b1", "c1"]).str.extractall(two_groups))
