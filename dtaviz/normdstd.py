# import required libraries
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib 
 
matplotlib.use('TkAgg')
# Creating the distribution
data = np.arange(1,1000,0.01)
pdf = norm.pdf(data , loc = 5.3 , scale = 2.3 )
 
#Visualizing the distribution
 

sns.boxplot(data)
sns.lineplot(data = pdf)

plt.xlabel('Heights')
plt.ylabel('Probability Density')
plt.show()