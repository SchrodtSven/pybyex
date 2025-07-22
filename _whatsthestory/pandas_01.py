import pandas as pd
import numpy as np
index = pd.Index([3, 1, 2, 3, 4, np.nan])

print(index.value_counts())

s = pd.Series([3, 1, 2, 3, 4, np.nan])

print(s.value_counts(normalize=True))


print(s.value_counts(bins=3))
# With normalize set to True, returns the relative frequency by dividing all values by the sum of values.