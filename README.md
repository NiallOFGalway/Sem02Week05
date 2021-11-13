# Programming & Security - Sem02Week05
## Niall O Flaherty - G00398819

## Assignment
*Analyse the data from the memory dump or another data set of your choosing. Use any python package you wish.*
I decided to create my own data set and save it to a CSV. The aim was to use Python to import the data and output in a visual way so that the data could be analysed. This was achieved usin pandas and matplotlib.
For the data, I used the example of different professions. The comparsion was between salary, hours per week, difficulty and education required based on a percentage, with 100% being most difficult.

Code:
```
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt


df=pd.read_csv("data.csv")


df1 = df.sort_values('income')
df2 = df.sort_values('hours')
df3 = df.sort_values('difficulty')
df4 = df.sort_values('education')


fig = plt.figure(figsize=(10,3))


ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.bar(df1.index, df1['income'])
ax1.xaxis.set_ticks(df.index)
ax1.xaxis.set_ticklabels(df1['profession'], rotation=60, horizontalalignment='right', fontsize='8')
ax1.set_title('Income as Percentage', fontsize='10')
ax1.set_ylabel('Income (100% being highest paid)')

ax2.bar(df2.index, df2['hours'])
ax2.xaxis.set_ticks(df.index)
ax2.xaxis.set_ticklabels(df2['profession'], rotation=60, horizontalalignment='right', fontsize='8')
ax2.set_title('Hours as Percentage', fontsize='10')
ax2.set_ylabel('Hours (100% being longest hours)')

ax3.bar(df3.index, df3['difficulty'])
ax3.xaxis.set_ticks(df.index)
ax3.xaxis.set_ticklabels(df3['profession'], rotation=60, horizontalalignment='right', fontsize='8')
ax3.set_title('Difficulty as Percentage', fontsize='10')
ax3.set_ylabel('Difficulty (100% being most difficult)')

ax4.bar(df4.index, df4['education'])
ax4.xaxis.set_ticks(df.index)
ax4.xaxis.set_ticklabels(df4['profession'], rotation=60, horizontalalignment='right', fontsize='8')
ax4.set_title('Education as Percentage', fontsize='10')
ax4.set_ylabel('Education (100% being longest education / training)')

plt.show()
```
**NOTE** Comments included in the .py file to show uderstanding of code

**REFERENCES**

StatsModels "The Datasets Package"
https://www.statsmodels.org/stable/datasets/index.html

TowardsScience "Datasets in Python"
https://towardsdatascience.com/datasets-in-python-425475a20eb1

Alpharithms "3 Easy Ways to get Financial Data in Python for Stock Analysis"
https://www.alpharithms.com/python-financial-data-491110/

LearnProgramming "Data Analysis with Python"
http://apmonitor.com/che263/index.php/Main/PythonDataAnalysis

W3Resource "Pandas Exercises, Practice, Solution"
https://www.w3resource.com/python-exercises/pandas/index.php

Numpy.org "Absolute Beginners"
https://numpy.org/doc/stable/user/absolute_beginners.html

Import CSV to NumPy
https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy

https://stackoverflow.com/questions/61104991/how-to-get-all-data-on-my-x-axis-in-python-from-csv-file

https://pythonguides.com/python-numpy-read-csv/

https://www.kite.com/python/answers/how-to-plot-data-from-a-csv-file-in-python

https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html

https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html

https://stackoverflow.com/questions/58590646/plot-csv-file-taking-the-first-column-as-x-axis-and-the-others-as-y-axis

https://365datascience.com/tutorials/python-tutorials/bar-chart-python-matplotlib/
