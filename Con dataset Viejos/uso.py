import pandas as pd
import re
import matplotlib.pyplot as plt
#plt.style.use('ggplot')

 
#2,2,2017-01-01 00:07:13,M,01/01/2017 00:07:13,11, Tribunales,84, Lavalle,0h 25min 8seg




def agrupador(valor):
    arra = valor.split(' ')

   #$ print(arra)
   # print (valor)
   # print(arra[0])
   # raise SystemExit

    minutos = int(re.sub('[^0-9]','', arra[1])) + int(re.sub('[^0-9]','', arra[0]))*60


    if minutos <= 15:
        return 'menos de 15 minutos'
    if minutos <= 30:
        return 'entre 15 minutos y 30 minutos'
    if minutos <= 60:
        return 'entre 30 minutos y 1 hora'
    if minutos <= 60:
        return 'entre 1 hora y 1 hora y media'     
    if minutos <= 90:
        return 'entre 1 hora y media y 2 horas'     
    
    return 'mas de dos horas'





dataFrameViajes = pd.read_csv('2017parsed.csv', header=0,sep = ',')
dataFrameViajes['date']=pd.to_datetime(dataFrameViajes['date'],dayfirst=1)
dataFrameViajes['tiempo_uso']=dataFrameViajes['tiempo_uso'].map(lambda a: agrupador(a))



##dataFrameViajes['tiempo_uso']=pd.to_datetime(dataFrameViajes['tiempo_uso'],format='%Hh %Mmin %Sseg',errors='coerce',dayfirst=1)


# cambiar a > 4 para tener el finde. Aca selecciono dias de semana
dataFrameViajesLV = dataFrameViajes[pd.to_datetime(dataFrameViajes['date']).dt.dayofweek  <= 4]
dataFrameViajesSD = dataFrameViajes[pd.to_datetime(dataFrameViajes['date']).dt.dayofweek  > 4]




dataFrameSumatoriaViajesLV=dataFrameViajesLV.groupby(by=dataFrameViajesLV['tiempo_uso'])['tiempo_uso'].count()
dataFrameSumatoriaViajesSD=dataFrameViajesSD.groupby(by=dataFrameViajesSD['tiempo_uso'])['tiempo_uso'].count()



#dataFrameSumatoriaViajesLV.plot.pie( title="Duracion del viaje dias de semana", figsize=(5, 5), y='', labels=['','','','',''], autopct='%1.1f%%')
dataFrameSumatoriaViajesSD.plot.pie( title="Duracion del viaje fines de semana", figsize=(5, 5), y='', labels=['','','','',''], autopct='%1.1f%%')

#plt.legend(dataFrameSumatoriaViajesLV.index, loc="best")
plt.legend(dataFrameSumatoriaViajesSD.index, loc="best")

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()


plt.show()
#print(dataFrameSumatoriaViajes)

#dataFrameSumatoriaViajes.index.name = None



