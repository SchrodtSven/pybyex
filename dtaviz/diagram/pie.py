import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.use('TkAgg') # Workaround for MacOS Bug with ⌘+Q - use new backend
courses = [164, 127, 31, 31,12, 11]
labels = ['Python','R','SQL','Power BI','Excel','ChatGPT']
dictionary = {'courses':courses, 'labels':labels}
python_pie_chart_df = pd.DataFrame(dictionary)

plt.pie(x = python_pie_chart_df.courses, labels = python_pie_chart_df.labels)
plt.show()