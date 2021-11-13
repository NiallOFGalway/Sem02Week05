# The following lines of code import numpy, pandas and matplotlib libraries so we can use their functions.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a data frame
df=pd.read_csv("data.csv")
df[['income','hours','difficulty','education']].hist(figsize=(14,9),bins=16,linewidth='1',grid=True)

df.plot()
plt.show()