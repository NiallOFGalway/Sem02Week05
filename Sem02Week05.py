# The following lines of code import numpy, pandas and matplotlib libraries so we can use their functions.
#import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt

# Load the data from the CSV file into a data frame
# index_col will allow us to use column 1 in the CSV file to name the professions in the X axis.
df=pd.read_csv("data.csv")

# Creating datasets so we can analyse the data. This will result in 4 bar charts as there are 4 catagories we are comparing.
df1 = df.sort_values('income')
df2 = df.sort_values('hours')
df3 = df.sort_values('difficulty')
df4 = df.sort_values('education')

# How the barchart will look and define the plot axes
fig = plt.figure(figsize=(10,3))


ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.bar(df1.index, df1['income'])
ax1.set_xticklabels(df1.index, rotation=60, horizontalalignment='right', fontsize='10')
ax1.set_title('Income as Percentage', fontsize='10')
ax1.set_ylabel('Income')

ax2.bar(df2.index, df2['hours'])
ax2.set_xticklabels(df2.index, rotation=60, horizontalalignment='right', fontsize='10')
ax2.set_title('Hours as Percentage', fontsize='10')
ax2.set_ylabel('Hours')


ax3.bar(df3.index, df3['difficulty'])
ax3.set_xticklabels(df3.index, rotation=60, horizontalalignment='right', fontsize='10')
ax3.set_title('Difficulty as Percentage', fontsize='10')
ax3.set_ylabel('Difficulty')


ax4.bar(df4.index, df4['education'])
ax4.set_xticklabels(df4.index, rotation=60, horizontalalignment='right', fontsize='10')
ax4.set_title('Education as Percentage', fontsize='10')
ax4.set_ylabel('Education')



plt.show()