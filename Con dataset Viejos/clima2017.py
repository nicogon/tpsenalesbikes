import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

 





dataFrameViajes = pd.read_csv('2017parsed.csv', header=0,sep = ',')
dataFrameViajes['date']=pd.to_datetime(dataFrameViajes['date'],dayfirst=1)
dataFrameViajes.index=pd.to_datetime(dataFrameViajes['date'],dayfirst=1)


dataFrameViajes = dataFrameViajes[pd.to_datetime(dataFrameViajes['date']).dt.dayofweek  <= 4]

dataFrameClima = pd.read_csv('clima2017.csv', header=0,sep = ';', index_col=False)
dataFrameClima['date']=pd.to_datetime(dataFrameClima['date'],infer_datetime_format=False, exact=True,dayfirst=1)



# columna RRR = lluvia
# cuando hay poca lluvia ponen un string en la columna que lo remplazo por 3 mm de lluvia
dataFrameClima.loc[dataFrameClima['RRR'].str.len() > 4, 'RRR'] = 3



dataFrameClima[["RRR"]] = dataFrameClima[["RRR"]].apply(pd.to_numeric)

# Cuando no hay valores, remplazo los NaN por 0
dataFrameClima=dataFrameClima.fillna(0)

dataFrameClima.index=pd.to_datetime(dataFrameClima['date'],dayfirst=1)

# Filtro horarios de lluvia que no sean los de uso de bicicletas
dataFrameClima = dataFrameClima.between_time('8:30', '19:00')


# Como hay cuatro entradas por dia, sumo las llovisnas de los 4 y me quedo con una sola entrada diaria
dataFrameMergeado = dataFrameClima.fillna(0).groupby(by=dataFrameClima['date'].dt.date)['RRR'].sum().reset_index(name='lluvia(mm)')


def agrupador(valor):

    if valor > 6:
        return 'con lluvia'

    return 'sin lluvia'



dataFrameMergeado['llueve'] =dataFrameMergeado['lluvia(mm)'].map(lambda a: agrupador(a))


# Sumo todos los viajes por dia y me quedo con una sola entrada por dia

dataFrameSumatoriaViajes=dataFrameViajes.groupby(by=dataFrameViajes['date'].dt.date)['date'].count().reset_index(name='viajes')

# Saco los findes 
dataFrameSumatoriaViajes = dataFrameSumatoriaViajes[pd.to_datetime(dataFrameSumatoriaViajes['date']).dt.dayofweek  <= 4]


dataFrameSumatoriaViajes.index.name = None
dataFrameClima.index.name = None


dataFrameViajesClima = pd.merge(dataFrameMergeado, dataFrameSumatoriaViajes, on='date')

# Agrupo el datagrame por lluvias de 0 , 1 a 10, 11 a 20 ....

#dataFrameViajesClimaAgrupado = dataFrameViajesClima.groupby(by=((dataFrameViajesClima['lluvia(mm)']+1)//10))



dataFrameViajesClimaAgrupado = dataFrameViajesClima.groupby(by=(dataFrameViajesClima['llueve']))


dataFrameViajesClimaAgrupado.boxplot(column='viajes')



print(dataFrameViajesClima.describe())

print(dataFrameViajesClimaAgrupado.describe())


#pepe.corr()

#ax1 = pepe.plot.scatter(x='count',y='sum',c='DarkBlue')


plt.show()


#print(pepe)

#df['DESTINOFECHA']

#print((a['DATEPARSED']))

