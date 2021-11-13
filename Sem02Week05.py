# Author: Niall O Flaherty
# Assignment: Sem02Week05 "Aalyse data from the memory dump or another data set of your choosing. Use any Python package you wish"
# I created a CSV file with various different professions which included (by percentage rating) hours worked per week, salary, difficulty, education required.

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

# How the bar-charts will look like
# In this example, a 2 x 2 is being created, the final numbers (1,2,3,4) defining where each plot will be located
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# Defining each barchart

# Where the information is sourced from
ax1.bar(df1.index, df1['income'])
# Defining where the x-axis labels are sourced from within the CSV file
ax1.xaxis.set_ticks(df.index)
ax1.xaxis.set_ticklabels(df1['profession'], rotation=60, horizontalalignment='right', fontsize='8')
# Tidying up and labelling the Barchart
ax1.set_title('Income as Percentage', fontsize='10')
# Labellingn the Y axis
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

# Show the results 
# NOTE: This does not save as a file. This has been done in previous assignments.
plt.show()