from pandas.util import testing as tm

p = tm.makePanel()
print(p)

# Convert to a MultiIndex DataFrame
print(p.to_frame())

# Alternatively, one can convert to an xarray DataArray
print(p.to_xarray())
