# Gantt charting
# AUTHOR Sven Schrodt
# SINCE 20250708

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt

mpl.use("TkAgg")  # Workaround for MacOS Bug with ⌘+Q - use new backend

dta = pd.read_csv('titanic.csv', sep=';')
#print(len(dta))
#print(dta.head(), dta.keys())
#


mdx = dta.groupby('Sex')['Pclass'].value_counts()
#
#midx = dta.groupby('personality_type')['social_energy'].value_counts()


# Chart width and  Δ for radius
width = 0.4
# Radius
radius = 1.2

outer = list(set(list(mdx.index.get_level_values(0))))

#print(mdx)
inner_label = []
outer_dta = {'female': 0, 'male': 0}
for i, v in mdx.items():
    #inner_label.append(i[0][:2] + ' cl:' + str(i[1]))
    inner_label.append(' class' + str(i[1]))
    if i[0] == 'female':
         outer_dta['female'] += v
    else:
        outer_dta['male'] += v

#print(outer_dta, mdx, mdx.sum())

fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5, forward=True)

# Outer ring (Sex)
pie_outer, _ = ax.pie(
    outer_dta.values(), 
    radius=radius,
    labels=outer_dta.keys(),
    labeldistance=.75,
)
plt.setp(
    pie_outer, 
    width=width, 
    edgecolor="black"
)

# Inner ring (sex::class)
pie_inner, _ = ax.pie(
    mdx, 
    labels=inner_label,
    radius = radius-width,
    labeldistance=0.65,
)

plt.setp(
    pie_inner, 
    width=width, 
    edgecolor="black"  
)
plt.show()