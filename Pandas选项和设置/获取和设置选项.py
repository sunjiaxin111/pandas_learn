import pandas as pd

print(pd.get_option('mode.sim_interactive'))
pd.set_option('mode.sim_interactive', True)
print(pd.get_option('mode.sim_interactive'))

# reset_option
print(pd.get_option("display.max_rows"))
pd.set_option("display.max_rows", 999)
print(pd.get_option("display.max_rows"))
pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))

# 使用正则表达式同时重置多个选项
pd.reset_option("^display")

# option_context
with pd.option_context("display.max_rows", 10, "display.max_columns", 5):
    print(pd.get_option("display.max_rows"))
    print(pd.get_option("display.max_columns"))
print(pd.get_option("display.max_rows"))
print(pd.get_option("display.max_columns"))
