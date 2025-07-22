import pandas as pd
import seaborn as sns
import matplotlib 
import matplotlib.pyplot as plt


print(matplotlib.__version__)

exit()
taxis = sns.load_dataset("taxis")
# print(taxis.head())
taxis.total.sum()

info = 'max: {} min: {}'.format(taxis.pickup.max(), taxis.pickup.min())
print(len(taxis))
taxis['total./.tip'] = taxis.total - taxis.tip
print(taxis.head())