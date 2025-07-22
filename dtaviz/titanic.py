# titanic 
# Playing with seaborn titanic data set 
# Double Donut showing relation between island and species
# AUTHOR Sven Schrodt
# SINCE 20250704
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

mpl.use("TkAgg") # Workaround for MacOS Bug with ⌘+Q - use new backend
mpl.rcParams["font.size"] = 12.0

titanic = sns.load_dataset("titanic")

survivors = titanic.groupby("class")["alive"].value_counts().unstack(level=0)
print(survivors)

plot_surv= survivors.plot(kind="bar",
title="Survivors",
color=["orange", "magenta", "blue"],
ec="black",
xlabel="",
stacked=True
);

for container in plot_surv.containers:
    plot_surv.bar_label(container)
plt.show()