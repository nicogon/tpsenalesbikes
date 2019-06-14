import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

 





dataFrameViajes = pd.read_csv('2017parsed.csv', header=0,sep = ',')
dataFrameViajes['date']=pd.to_datetime(dataFrameViajes['date'],dayfirst=1)



# cambiar a > 4 para tener el finde. Aca selecciono dias de semana
dataFrameViajes = dataFrameViajes[pd.to_datetime(dataFrameViajes['date']).dt.dayofweek  <= 4]


#print(dataFrameViajes['date'].count)
#dataFrameViajes.index=pd.to_datetime(dataFrameViajes['fecha_hora_retiro'],dayfirst=1)
#dataFrameViajes.to_csv("2017parsed.csv")
# Sumo todos los viajes por dia y me quedo con una sola entrada por dia
#dataFrameSumatoriaViajes=dataFrameViajes.groupby(by=((dataFrameViajes['date'].dt.hour*60+dataFrameViajes['date'].dt.minute)//10))['date'].count().reset_index(name='viajes')


dataFrameSumatoriaViajes=dataFrameViajes.groupby(by=((dataFrameViajes['date'].dt.hour)))['date'].count().reset_index(name='viajes')

cantiadDias = len(dataFrameSumatoriaViajes.index)


del dataFrameSumatoriaViajes['date']

dataFrameSumatoriaViajes['viajes'] = dataFrameSumatoriaViajes['viajes'] / cantiadDias

print(dataFrameSumatoriaViajes.describe())


dataFrameSumatoriaViajes.plot()





plt.show()
print(dataFrameSumatoriaViajes)

dataFrameSumatoriaViajes.index.name = None



