import numpy as np
import pandas as pd

# Warning: In 0.20.0, Panel is deprecated and will be removed in a future version.
# From 3D ndarray with optional axis labels
wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
              major_axis=pd.date_range('1/1/2000', periods=5),
              minor_axis=['A', 'B', 'C', 'D'])
print(wp)

# From dict of DataFrame objects
data = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
        'Item2': pd.DataFrame(np.random.randn(4, 2))}
print(pd.Panel(data))

# Panel.from_dict方法，设置参数orient='minor'
# to use DataFrames’ columns as panel items
print(pd.Panel.from_dict(data, orient='minor'))

# Orient is especially useful for mixed-type DataFrames.
# If you pass a dict of DataFrame objects with mixed-type columns,
# all of the data will get upcasted to dtype=object
# unless you pass orient='minor'
df = pd.DataFrame({'a': ['foo', 'bar', 'baz'],
                   'b': np.random.randn(3)})
print(df)
print(df.dtypes)
data = {'item1': df, 'item2': df}

# 这样处理，b的类型会变为object
panel1 = pd.Panel.from_dict(data)
print(panel1['item1'])
print(panel1['item2'])
print(panel1['item2'].dtypes)

# 这样处理，b的类型可以保持为float
panel2 = pd.Panel.from_dict(data, orient='minor')
print(panel2['a'])
print(panel2['b'])
print(panel2['b'].dtypes)

# From DataFrame using to_panel method
midx = pd.MultiIndex(levels=[['one', 'two'], ['x', 'y']], labels=[[1, 1, 0, 0], [1, 0, 1, 0]])
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=midx)
print(df)
print(df.to_panel())

# Item selection / addition / deletion
# Similar to DataFrame functioning as a dict of Series, Panel is like a dict of DataFrames
print(wp['Item1'])
wp['Item3'] = wp['Item1'] / wp['Item2']
print(wp['Item3'])

# Transposing
print(wp)
print(wp.transpose(2, 0, 1))

# Indexing / Selection
# 选择item->wp[item]->DataFrame
# major_axis切片->wp.major_xs(val)->DataFrame
# minor_axis切片->wp.minor_xs(val)->DataFrame
print(wp['Item1'])
print(wp.major_xs(wp.major_axis[2]))
print(wp.minor_axis)
print(wp.minor_xs('C'))

# Squeezing
print(wp.reindex(items=['Item1']).squeeze())
print(wp.reindex(items=['Item1'], minor=['B']).squeeze())

# Conversion to DataFrame
panel = pd.Panel(np.random.randn(3, 5, 4), items=['one', 'two', 'three'],
                 major_axis=pd.date_range('1/1/2000', periods=5),
                 minor_axis=['a', 'b', 'c', 'd'])
print(panel.to_frame())
