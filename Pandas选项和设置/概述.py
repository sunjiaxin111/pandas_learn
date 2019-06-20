import pandas as pd

print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
print(pd.options.display.max_rows)

print(pd.get_option("display.max_rows"))
pd.set_option("display.max_rows", 101)
print(pd.get_option("display.max_rows"))
pd.set_option("max_r", 102)
print(pd.get_option("display.max_rows"))

# Pattern matched multiple keys
try:
    pd.get_option("column")
except KeyError as e:
    print(e)
