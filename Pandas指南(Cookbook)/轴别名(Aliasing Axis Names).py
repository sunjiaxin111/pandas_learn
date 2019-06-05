import numpy as np
import pandas as pd


def set_axis_alias(cls, axis, alias):
    if axis not in cls._AXIS_NUMBERS:
        raise Exception("invalid axis [%s] for alias [%s]" % (axis, alias))
    cls._AXIS_ALIASES[alias] = axis


def clear_axis_alias(cls, axis, alias):
    if axis not in cls._AXIS_NUMBERS:
        raise Exception("invalid axis [%s] for alias [%s]" % (axis, alias))
    cls._AXIS_ALIASES.pop(alias, None)


set_axis_alias(pd.DataFrame, 'columns', 'myaxis2')
df2 = pd.DataFrame(np.random.randn(3, 2), columns=['c1', 'c2'], index=['i1', 'i2', 'i3'])
print(df2.sum(axis='myaxis2'))
clear_axis_alias(pd.DataFrame, 'columns', 'myaxis2')
