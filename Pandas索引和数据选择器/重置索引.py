import pandas as pd

data = pd.DataFrame({'a': pd.Series(['bar', 'bar', 'foo', 'foo']),
                     'b': pd.Series(['one', 'two', 'one', 'two']),
                     'c': pd.Series(['z', 'y', 'x', 'w']),
                     'd': pd.Series([1, 2, 3, 4])})
print(data)
indexed1 = data.set_index('c')
print(indexed1)
indexed2 = data.set_index(['a', 'b'])
print(indexed2)

frame = data.set_index('c', drop=False)
frame = frame.set_index(['a', 'b'], append=True)
print(frame)

print(data.set_index('c', drop=False))
data.set_index(['a', 'b'], inplace=True)
print(data)

# Reset the index
print(data.reset_index())
print(frame)
print(frame.reset_index(level=1))

# 给data赋一个index
# data.index = index
