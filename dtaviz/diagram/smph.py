# Gantt charting
# AUTHOR Sven Schrodt
# SINCE 20250708

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt

mpl.use("TkAgg")  # Workaround for MacOS Bug with ⌘+Q - use new backend

dta = pd.read_csv('Smartphones_cleaned_dataset.csv')
midx = dta.groupby('brand_name').value_counts()

print(midx.keys())