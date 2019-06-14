import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv('test.csv', header=0,sep = ',')

dfc = pd.read_csv('clima2017.csv', header=0,sep = ';', index_col=False)

#print(df)

dfc['date']=pd.to_datetime(dfc['date'],infer_datetime_format=False, exact=True,dayfirst=1)




dfc.loc[dfc['RRR'].str.len() > 4, 'RRR'] = 0

dfc[["RRR"]] = dfc[["RRR"]].apply(pd.to_numeric)

dfc=dfc.fillna(0)

#print(dfc.head())
#dfc['RRR']= pd.to_numeric(dfc['RRR'])

#print(dfc['RRR'])


josesito = dfc.fillna(0).groupby(by=dfc['date'].dt.date)['RRR'].sum().reset_index(name='sum')

#print(josesito)



#print(dfc['RRR'])

#print(df)


df['date']=pd.to_datetime(df['fecha_hora_retiro'],dayfirst=1)


df.index=pd.to_datetime(df['fecha_hora_retiro'],dayfirst=1)
df.set_index('date')

df.to_csv('test.csv')

df = df.between_time('10:00', '19:00')


#print(df)
#df.loc[(df['date'].dt.hour) > 22]

a=df.groupby(by=df['date'].dt.date)['date'].count().reset_index(name='count')



#print(f)


#print(a)

#print(a.head())

a.index.name = None
josesito.index.name = None




#a = a.reset_index()

#josesito = josesito.reset_index()


pepe = pd.merge(josesito,a, on='date')

#pepe['WEEKDAY'] = pd.to_datetime(pepe['date']).dt.dayofweek 

#pepe["WEEKDAY"] = (pepe["WEEKDAY"]<5).astype(bool)

pepe.corr()

ax1 = pepe.plot.scatter(x='count',y='sum',c='DarkBlue')


plt.show()


print(pepe)

#df['DESTINOFECHA']

#print((a['DATEPARSED']))

