# Gantt charting
# AUTHOR Sven Schrodt
# SINCE 20250708

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt

mpl.use("TkAgg")  # Workaround for MacOS Bug with ⌘+Q - use new backend

dta = pd.read_csv('physics_teacher_jobs_linkedin.csv')
mdx = dta.groupby('sector')['experienceLevel'].value_counts()
#print(dta.head())
#midx = dta.groupby('personality_type')['social_energy'].value_counts()

print(mdx)