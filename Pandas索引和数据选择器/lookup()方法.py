import numpy as np
import pandas as pd

dflookup = pd.DataFrame(np.random.rand(20, 4), columns=['A', 'B', 'C', 'D'])
print(dflookup.lookup(list(range(0, 10, 2)), ['B', 'C', 'A', 'B', 'D']))
