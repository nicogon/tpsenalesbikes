import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob



#with open('157-05-30.txt') as json_file:  
#    data = json.load(json_file)
#    
#    for station in data:
#        print('Name: ' + station['status']['total_available_docks'])

#data = pd.read_json('157-05-30.txt', lines=True)


all_files = sorted(glob.glob("*.txt"))

print(all_files)

df = pd.DataFrame(columns=('lib'))

df.append([1])

for file in all_files:
    with open(file) as f:
        print(file)
        stations = json.load(f)
    if len(stations) > 0:
        df.append([stations[0]['status']['total_available_bikes']])

print(df)

with open('156-18-45.txt') as f:
    stations = json.load(f)



print(stations[0]['status']['total_available_bikes'])

#print(stations[0]['status']['total_available_bikes'])

count = 0
sum = 0
for station in stations:
    #print(station['status']['total_available_bikes'])
    #sum = station['status']['total_available_bikes'] + sum
    sum = station['status']['total_available_bikes'] + sum

    count = count + 1

#print(count)
#print(sum/count)
#asd = np.asarray(stations)

#dataset = pd.DataFrame.from_records(stations)


#print(dataset.head())

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#plt.show()



##
#{'id': 82066,
 ##'system': 13, 
 #'station_number': '418',
 # 'main_brand': 'ecobici', 
 # 'name': '345 - Plaza Mafalda',
 #  'capacity': 20,
 #   'address': {'street': 'Arenal, Concepcion & Martinez, Enrique, Gral.', 'latitude': -34.5811376, 'longitude': -58.4446136},
 #    'status': {'total_available_bikes': 0, 'total_available_docks': 20, 'total_disabled_bikes': 0, 'total_disabled_docks': 0}, 'is_favorite': False}]
