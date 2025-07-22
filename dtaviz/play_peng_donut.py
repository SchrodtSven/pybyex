# Playing with seaborn penguins data set 
# Double Donut 
# AUTHOR Sven Schrodt
# SINCE 20250704

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib as mpl

mpl.use("TkAgg") # Workaround for MacOS Bug with ⌘+Q - use new backend
mpl.rcParams["font.size"] = 12.0

# Chart width and  Δ for radius
width = 0.4
# Radius
radius = 1.2

peng = sns.load_dataset("penguins")
col_dct = {"Gentoo": "#f5ded2", "Adelie": "#f7ede2", "Chinstrap": "#e1cab7"}

# Get multiIndexed { tuple('Island', 'Species') } Series
dta_midx = peng.groupby("island")["species"].value_counts()




# Generate lists for labels
spec = list(dta_midx.index.get_level_values(1))
isl = list(set(list(dta_midx.index.get_level_values(0))))

 # Mapping species -> color
col_dct = {"Gentoo": "#f5ded2", "Adelie": "#f7ede2", "Chinstrap": "#e1cab7"}

# Setting up list with colors in order corr. species
col = [col_dct[x] for x in spec]



outer_dta = peng["island"].value_counts()
inner_dta = pd.Series(dta_midx)
inner_dta = dta_midx

fig, ax = plt.subplots()
fig.set_size_inches(18.5, 10.5, forward=True)




# Außenring (Island)
pie_outer, _ = ax.pie(
    outer_dta, 
    radius=radius,
    labels=isl,
    labeldistance=.75,
)

plt.setp(
    pie_outer, 
    width=width, 
    edgecolor="gray"
)

pie_inner, _ = ax.pie(
    x=inner_dta,
    radius = radius-width,
    labels=spec,
    labeldistance=0.65,
    colors=col
)

plt.setp(
    pie_inner, 
    width=width, 
    edgecolor="gray")
 
plt.title("Penguins: species / island")

plt.savefig('donut.png')
plt.show()


