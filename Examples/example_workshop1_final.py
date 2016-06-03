import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Open CSV file and omit day and month columns
f = pd.read_csv('C:\Users\Meghan\PyCharm_Meghan\SOARS2016_DataWorkshops'
                '\workshop\one\data\sample_demo_weather_data_1981.csv')

print f.head()
f2=f.drop(['month','day'],axis=1)
print " "
print f2.head()
print " "

#Find the max and min values of lon and lat
print "max Longitude:" +' '+ str(f.lon.max())
print "min Longitude:" +' '+ str(f.lon.min())
print " "
print "max Latitude:" +' '+ str(f.lat.max())
print "min Latitude:" +' '+ str(f.lat.min())
print " "

#Find the frequency of the measurements by month

#Dictionary Way to do it
month=f.month[:]
from collections import Counter
dict=Counter(month)

# print dict
print "Frequencies of data by month"
print "Jan:"+ str(dict[1]) +" "+'measurements'
print "Feb:"+ str(dict[2]) +" "+'measurements'
print "Mar:"+ str(dict[3]) +" "+'measurements'
print "Apr:"+ str(dict[4]) +" "+'measurements'
print "May:"+ str(dict[5]) +" "+'measurements'
print "Jun:"+ str(dict[6]) +" "+'measurements'
print "Jul:"+ str(dict[7]) +" "+'measurements'
print "Aug:"+ str(dict[8]) +" "+'measurements'
print "Sept:"+ str(dict[9]) +" "+'measurements'
print "Oct:"+ str(dict[10]) +" "+'measurements'
print "Nov:"+ str(dict[11]) +" "+'measurements'
print "Dec:"+ str(dict[12]) +" "+'measurements'
print " "

#Alternative way to do it
import numpy as np
print "Frequencies of data by month:"
print "Jan:" + str(np.shape(np.where(f.month==1))[1]) +" "+'measurements'
print "Feb:" + str(np.shape(np.where(f.month==2))[1]) +" "+'measurements'
print "Mar:" + str(np.shape(np.where(f.month==3))[1]) +" "+'measurements'
print "Apr:" + str(np.shape(np.where(f.month==4))[1]) +" "+'measurements'
print "May:" + str(np.shape(np.where(f.month==5))[1]) +" "+'measurements'
print "Jun:" + str(np.shape(np.where(f.month==6))[1]) +" "+'measurements'
print "Jul:" + str(np.shape(np.where(f.month==7))[1]) +" "+'measurements'
print "Aug:" + str(np.shape(np.where(f.month==8))[1]) +" "+'measurements'
print "Sept:" + str(np.shape(np.where(f.month==9))[1]) +" "+'measurements'
print "Oct:" + str(np.shape(np.where(f.month==10))[1]) +" "+'measurements'
print "Nov:" + str(np.shape(np.where(f.month==11))[1]) +" "+'measurements'
print "Dec:" + str(np.shape(np.where(f.month==12))[1]) +" "+'measurements'
print " "

#Histogram Frequency Plot
import matplotlib.pyplot as plt
#%matplotlib inline
import calendar
bins = np.arange(14) - 0.5
plt.hist(month, bins)
plt.xticks(range(13))
plt.xticks(np.arange(13), calendar.month_name[0:13], rotation=30)
plt.xlim([0, 13])
plt.title('Frequency of data points per Month')
plt.xlabel('Month')
plt.ylabel("# of measurements")
plt.show()