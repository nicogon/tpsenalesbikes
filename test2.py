 
import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('junk.csv',header=0, parse_dates = ['date'])

##print(df['bikes'])

#df = df.sort_values('date', ascending=True)

df['date'] = pd.to_datetime(df['date'],unit='s')


#print(df)
#plt.figure()

print(df)

plt.plot(df['date'],df['bikes'])
plt.plot(df['date'],df['broken'])

#plt.gcf()


plt.show()