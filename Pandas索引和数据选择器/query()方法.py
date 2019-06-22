import numpy as np
import pandas as pd

n = 10
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print(df)
# 纯python写法
print(df[(df.a < df.b) & (df.b < df.c)])
# query写法
print(df.query('(a < b) & (b < c)'))
# query可以使用index
df = pd.DataFrame(np.random.randint(n / 2, size=(n, 2)), columns=list('bc'))
df.index.name = 'a'
print(df)
print(df.query('a < b and b < c'))
# 如果你不想命名index，可以直接在query语句中使用index关键字
df = pd.DataFrame(np.random.randint(n, size=(n, 2)), columns=list('bc'))
print(df)
print(df.query('index < b < c'))

# 如果index名和列名重复了，优先使用列名
df = pd.DataFrame({'a': np.random.randint(5, size=5)})
df.index.name = 'a'
print(df)
print(df.query('a > 2'))  # # uses the column 'a', not the index

print(df.query('index > 2'))  # 使用index标志符,此时index的优先级高于列

# MultiIndex query() Syntax
n = 10
colors = np.random.choice(['red', 'green'], size=n)
foods = np.random.choice(['eggs', 'ham'], size=n)
print(colors)
print(foods)
index = pd.MultiIndex.from_arrays([colors, foods], names=['color', 'food'])
df = pd.DataFrame(np.random.randn(n, 2), index=index)
print(df)
print(df.query('color == "red"'))

# 如果MultiIndex未命名，可以通过特殊的名字引用
df.index.names = [None, None]
print(df)
print(df.query('ilevel_0 == "red"'))

# query() Use Cases
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
print(df)
df2 = pd.DataFrame(np.random.rand(n + 2, 3), columns=df.columns)
print(df2)
expr = '0.0 <= a <= c <= 0.5'
print(map(lambda frame: frame.query(expr), [df, df2]))

# query() Python versus pandas Syntax Comparison
df = pd.DataFrame(np.random.randint(n, size=(n, 3)), columns=list('abc'))
print(df)
print(df.query('(a < b) & (b < c)'))
print(df[(df.a < df.b) & (df.b < df.c)])
# 去掉括号
print(df.query('a < b & b < c'))
# 使用英文代替符号
print(df.query('a < b and b < c'))
# 更贴近实际的写法
print(df.query('a < b < c'))

# The in and not in operators
df = pd.DataFrame({'a': list('aabbccddeeff'), 'b': list('aaaabbbbcccc'),
                   'c': np.random.randint(5, size=12),
                   'd': np.random.randint(9, size=12)})
print(df)
print(df.query('a in b'))
# 纯python的写法
print(df[df.a.isin(df.b)])

print(df.query('a not in b'))
# 纯python的写法
print(df[~df.a.isin(df.b)])

print(df.query('a in b and c < d'))
# 纯python的写法
print(df[df.a.isin(df.b) & (df.c < df.d)])

# Special use of the == operator with list objects
# Comparing a list of values to a column using ==/!= works similarly to in/not in.
print(df.query('b == ["a", "b", "c"]'))
# 纯python的写法
print(df[df.b.isin(["a", "b", "c"])])

print(df.query('c == [1, 2]'))
print(df.query('c != [1, 2]'))
# using in/not in
print(df.query('[1, 2] in c'))
print(df.query('[1, 2] not in c'))
# 纯python的写法
print(df[df.c.isin([1, 2])])

# Boolean Operators
# 可以使用not或者~对布尔表达式求反
df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))
df['bools'] = np.random.rand(len(df)) > 0.5
print(df.query('~bools'))
print(df.query('not bools'))
print(df.query('not bools') == df[~df.bools])

shorter = df.query('a < b < c and (not bools) or bools > 2')
longer = df[(df.a < df.b) & (df.b < df.c) & (~df.bools) | (df.bools > 2)]
print(shorter)
print(longer)
print(shorter == longer)

# 结论：当超过20万行数据时，DataFrame.query()的性能要比纯python写法好
