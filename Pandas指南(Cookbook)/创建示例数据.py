import itertools

import pandas as pd


def expand_grid(data_dict):
    rows = itertools.product(*data_dict.values())
    return pd.DataFrame.from_records(rows, columns=data_dict.keys())


df = expand_grid(
    {'height': [60, 70],
     'weight': [100, 140, 180],
     'sex': ['Male', 'Female']})
print(df)
