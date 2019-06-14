import timeit

import numpy as np
import pandas as pd


def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def run(df1, df2):
    df = df1 > df2


df1 = pd.DataFrame(np.random.randn(100000, 100))
df2 = pd.DataFrame(np.random.randn(100000, 100))
# 加速用时:24ms
run(df1, df2)
# 禁用加速
pd.set_option('compute.use_bottleneck', False)
pd.set_option('compute.use_numexpr', False)
# 未加速用时:332ms
run(df1, df2)
