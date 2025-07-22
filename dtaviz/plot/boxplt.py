# Boxplotting stuff
#
# AUTHOR Sven Schrodt
# SINCE 20250708
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib as mpl

mpl.use('TkAgg') # Workaround for MacOS Bug with ⌘+Q - use new backend
# Generates some random dataset
np.random.seed(10) 
dta = np.random.normal(0, 1, 100)
print(dta)
# Creates a boxplot
sns.boxplot(data=dta) 

# Generate multiple datasets
data = {
    'Group': ['A']*100 + ['B']*100 + ['C']*100,
    'Value': np.concatenate([np.random.normal(0, 1, 100), 
                             np.random.normal(1, 2, 100), 
                             np.random.normal(2, 1.5, 100)])
}
df = pd.DataFrame(data)
# Create additional grouping data
df['Subgroup'] = np.random.choice(['X', 'Y'], size=300)
# Plots graph
sns.boxplot(x='Group', y='Value', data=df, hue='Subgroup', palette='Set2')
plt.title('Basic Boxplot / Colored Boxplot')
plt.show()

