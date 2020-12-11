import pandas as pd
import glob
import numpy as np

#The following section merges the AOD files together

all_files = glob.glob("*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df = df[df['AOD1']>0]
df = df[df['value']>0]

df.to_csv('test5.csv', index=False)

import scipy.stats
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['AOD1'],df['value'])
print(r_value)

import matplotlib.pyplot as plt
plt.scatter(df['AOD1'],df['value'])
plt.show()
