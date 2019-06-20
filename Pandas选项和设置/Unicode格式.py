import pandas as pd

df = pd.DataFrame({u'国籍': ['UK', u'日本'], u'名前': ['Alice', u'しのぶ']})
print(df)
pd.set_option('display.unicode.east_asian_width', True)
print(df)

df = pd.DataFrame({'a': ['xxx', u'¡¡'], 'b': ['yyy', u'¡¡']})
print(df)
pd.set_option('display.unicode.ambiguous_as_wide', True)
print(df)
