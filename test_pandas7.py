import pandas as pd
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import seaborn as sns

start = datetime.datetime(2010,1,1)
end = datetime.datetime.now()

data = pd.read_csv('tempelhof.txt', sep=';')
#data.set_index('Stations_id', inplace = True)
#df = web.DataReader('tag00075','eurostat',start,end)

#data.loc[data.TT_TU < -60 , 'TT_TU'] = 'NaN'

print(data.head())
print(data.max())
print(data.min())

#Ein neuer Kommentar für git zum Testen

print("Stefan du bist so gut!!")

print("Beim zweiten mal klappt es")


data['MESS_DATUM']=pd.to_datetime(data.MESS_DATUM, format='%Y%m%d%H')

data.reset_index(inplace = True)
data.set_index('MESS_DATUM', inplace = True)

#print(data.iloc[zeilenbereich,spaltenbereich]) #print(data.iloc[0:2,[3,4]]) oder print(data.iloc[[2],[5]])
print(data.iloc[0:2,[3]])
print(data.head())
print(data.tail())
werte = [[0,0,0]]
for jahr in range(2015,2018 ,1):
	for monat in range(1,13,1):
		data_monat = data[(data.index.year == jahr) & (data.index.month == monat)]
		#print ('Die mittlere Temperatur im ' + str(monat) + ' ' + str(jahr) +' betrug ' + str(data_monat['TT_TU'].mean() ))
		werte.append([jahr,monat,data_monat['TT_TU'].mean()])
#print(werte)
data_ergebnis=pd.DataFrame(werte,columns=['Jahr','Monat','Temperatur'])
print(data_ergebnis)
data_ergebnis.to_csv('wetter2.csv')
plt.plot(data_ergebnis['Monat'],data_ergebnis['Temperatur'])
plt.show()

#t_mittel=[]
#for year in range(1981,2016,1):
	#anfang = str(year)+'-01-01'
	#ende = str(year)+'-12-31'
	#druck_data=data[anfang:ende]
	#print('Mittler Temperatur '+str(year) +'  '+ str(druck_data['TT_TU'].mean()))
	#t_mittel.append(druck_data['TT_TU'].mean())
#print(t_mittel)
#print(data.index.min())
#print(data.index.max()) 
#print(data.index.month)	
#print(data.index[0].month)
#print(data.tail())

#data_monat=[]
#data_monat_df=pd.DataFrame(data_monat)
#for monat in range(1, 2,1):
#	for hour in range(1,1000,1):
#		if data.index[hour].month == monat:
#			#print(str(data.index[hour].month) +'  '+ str(hour) )
			#print(str(data.iloc[hour,3])+ ' '+str(data.index[hour]))
#			data_monat.append(data.iloc[hour,3])
			#print('Mai-Temp.: ' + str(hour))
#		data_monat_temp_df=pd.DataFrame(data_monat)	
#		data_monat_df.append(data_monat)
		

#print(data_monat_df)
#print('Mittler Monatstemperatur im Februar: ' + str(data_monat_df.mean()))


#plt.plot(t_mittel)
#druck_data['TT_TU'].plot()
#plt.show() 
