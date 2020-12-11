import pandas as pd
import glob
import numpy as np
import os

#The following section merges the AOD files together, and returns the average

all_files = glob.glob("*.csv")
for f in all_files:
    os.remove(f)

#['anaheim','clarita','glendora','nmain','reseda','slb']
for x in ['anaheim','clarita','glendora','nmain','reseda','slb']:
    path = 'City/' + x # use the path
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)

    #Convert the dates to datetime format, and group them together to find the mean

    df['Date'] = pd.to_datetime(df['YYYY'].astype(str) + '-' + df['MM'].astype(str)+'-'+df['DD'].astype(str))
    df = df.drop(['YYYY','MM','DD'], axis=1)

    #Make new Date column the first column
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]
    df = df.sort_values(by='Date')
    df["Longitude"]= round(df["Longitude"],3)
    df["Latitude"]= round(df["Latitude"],3)

    df.to_csv('test.csv', index=False)

    #Similar to the AOD section, this merges and groups the PM2.5 values together

    path = r'Citypm25/' + x # use the path
    all_files = glob.glob(path + "/*.csv")
    df = pd.read_csv(all_files[0])

    df.loc[df['date'].astype(str).str[48:50].astype(int) < 12, 'Time'] = 1
    df.loc[df['date'].astype(str).str[48:50].astype(int) >= 12, 'Time'] = 2
    
    df['Date'] = pd.to_datetime(df['date'].astype(str).str[5:15])
    df = df.sort_values(by='Date')

    df = df.drop(['date'], axis=1)
    cols = list(df.columns)
    cols = [cols[-1]] + cols[:-1]
    df = df[cols]

    df = df[df['parameter']=='pm25']
    df = df[df['value']>0]

    #Filter out extraneous values
    q_low = df["value"].quantile(0.01)
    q_hi  = df["value"].quantile(0.99)

    df = df[(df["value"] < q_hi) & (df["value"] > q_low)]

    #Create Latitude and Longitude columns for PM2.5 Data
    new = df['coordinates'].str.split(", | |latitude|longitude|=|{|}", expand = True)
    df["Longitude"]= round(new[3].astype(float),3)
    df["Latitude"]= round(new[6].astype(float),3)

    df = df.groupby(['Date','Time']).median()

    df.to_csv('test2.csv', index=True)

    all_files = glob.glob("*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)

    #Merge dates together without averaging

    df = df.groupby(['Date','Time',"Longitude","Latitude"]).first().reset_index()
    df = df[df['AOD1']>-2]
    df = df[df['value']>0]

    os.remove("test.csv")
    os.remove("test2.csv") 

    df.to_csv('test3/'+x+'.csv', index=False)

    import scipy.stats
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['AOD3'],df['value'])
    print(r_value)

all_files = glob.glob("test3/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)

df = df[df['value']>0]

for f in all_files:
    os.remove(f)

df["YYYY"]= df["Date"].str.split("-", n = -1, expand = True)[0]
df["MM"]= df["Date"].str.split("-", n = -1, expand = True)[1]
df["DD"]= df["Date"].str.split("-", n = -1, expand = True)[2]
df["Weekday"] = pd.to_datetime(df["Date"]).dt.dayofweek

df.to_csv('test5.csv', index=False)

import scipy.stats
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['AOD3'],df['value'])
print(r_value)

import matplotlib.pyplot as plt
plt.scatter(df['AOD3'],df['value'])
m, b = np.polyfit(df['AOD3'], df['value'], 1)
regression, = plt.plot(df['AOD3'], m*df['AOD3'] + b,'-',color='orange')
plt.xlabel('AOD')
plt.ylabel('PM2.5 (µg/m$^3$)')
plt.title('AOD vs PM2.5 for Los Angeles')
first_legend = plt.legend([regression], ['r = ' + str(round(r_value,2))])

plt.show()

import machinelearning
