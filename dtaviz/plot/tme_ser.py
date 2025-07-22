# Playing with mpl animations
# Sine wave 
# AUTHOR Sven Schrodt
# SINCE 20250708


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
from datetime import datetime
mpl.use('TkAgg') # Workaround for MacOS Bug with ⌘+Q - use new backend

df = pd.read_csv('euro-daily-hist_1999_2022.csv')
df = df.iloc[:, [0, 4, 28, -2]]
df.columns = ['Date', 'CAD', 'NZD', 'USD']
# Sanitizing data
for col in ['CAD', 'NZD', 'USD']:
    df = df[df[col] != '-']
    df[col] = pd.to_numeric(df[col])
print(df.head())
print(f'\nThe date range: {df.Date.min()}/{ df.Date.max()}')


#exit()   
#df = df[df['Date'] >= '2022-12-01'].reset_index(drop=True)
df['Date'] = pd.to_datetime(df['Date'])




df = df.set_index('Date')


fig, ax = plt.subplots(figsize=(16, 5))
plt.plot(df.index, df['CAD'])
plt.title('EUR-CAD rate', fontsize=20)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Rate', fontsize=15)
plt.xlim(df.index.min(), df.index.max())
ticks = list(df.index)
plt.xticks(ticks, rotation=45)
ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%b %d'))

# Highlighting the time period from 15.12.2022 to 1.01.2023 and customizing the shaded area
plt.axvspan(datetime(2022, 12, 15), datetime(2023, 1, 1), facecolor='yellow', alpha=0.5, hatch='/', edgecolor='red', linewidth=5)
plt.plot(df.index, df['CAD'])
plt.show()