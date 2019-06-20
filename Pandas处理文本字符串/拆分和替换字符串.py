import numpy as np
import pandas as pd

s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
print(s2.str.split('_'))
# 读取切分后的列表中的元素
print(s2.str.split('_').str.get(1))
print(s2.str.split('_').str[1])
# 使用expand方法展开为一个数据表
print(s2.str.split('_', expand=True))
# 限制切分的次数
print(s2.str.split('_', expand=True, n=1))
# rsplit 从字串的尾端向首段切分
print(s2.str.rsplit('_', expand=True, n=1))

# replace 方法默认使用 正则表达式
s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'])
print(s3)
print(s3.str.replace('^.a|dog', 'XX-XX ', case=False))
# 使用正则表达式要格外小心，例如'$'符号
dollars = pd.Series(['12', '-$10', '$10,000'])
print(dollars.str.replace('$', ''))
print(dollars.str.replace('-$', '-'))
print(dollars.str.replace(r'-\$', '-'))

# 如果只是想单纯地替换字符，可以将regex参数设置为False
print(dollars.str.replace(r'-\$', '-'))
# 等价方法
print(dollars.str.replace('-$', '-', regex=False))

# 反转每个小写字母单词
pat = r'[a-z]+'
repl = lambda m: m.group(0)[::-1]
print(pd.Series(['foo 123', 'bar baz', np.nan]).str.replace(pat, repl))

# Using regex groups
pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
repl = lambda m: m.group('two').swapcase()
print(pd.Series(['Foo Bar Baz', np.nan]).str.replace(pat, repl))

# replace 方法也可以接受一个来自 re.compile() 编译过的正则表达式对象，来做为表达式。
import re

regex_pat = re.compile(r'^.a|dog', flags=re.IGNORECASE)
print(s3.str.replace(regex_pat, 'XX-XX '))
