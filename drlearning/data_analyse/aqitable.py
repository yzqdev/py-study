import matplotlib.pyplot as plt
import datetime
import csv

readers = csv.reader(open('data/alldatainit.csv'))
i = 0
aqiyaxis = []
xaxis = []
coyaxis = []
so2yaxis = []
o3yaxis = []
for rowre in readers:
    if i < 1500:
        i = i + 1
        aqiyaxis.append(rowre[2])
        coyaxis.append(rowre[3])
        so2yaxis.append(rowre[4])
        o3yaxis.append(rowre[5])
start = '20140101'
end = '20180209'

datestart = datetime.datetime.strptime(start, '%Y%m%d')
dateend = datetime.datetime.strptime(end, '%Y%m%d')
index = []
while datestart < dateend:
    datestart += datetime.timedelta(days=1)
    daye = datestart.strftime('%Y%m%d')
    xaxis.append(daye)

plt.subplot(2, 2, 1)
plt.scatter(xaxis, aqiyaxis, color='red', linewidth=0.1)
plt.title('aqi and years')
plt.xlabel("year")
plt.ylabel("aqi")
plt.xticks(())
plt.yticks(())
plt.subplot(2, 2, 2)
plt.scatter(xaxis, coyaxis, color='black', linewidth=0.1)
plt.title('co and years')
plt.xlabel("year")
plt.ylabel("co")
plt.xticks(())
plt.yticks(())
plt.subplot(2, 2, 3)
plt.scatter(xaxis, so2yaxis, color='blue', linewidth=0.1)
plt.title('so2 and years')
plt.xlabel("year")
plt.ylabel("so2")
plt.xticks(())
plt.yticks(())
plt.subplot(2, 2, 4)
plt.scatter(xaxis, o3yaxis, color='blue', linewidth=0.1)
plt.title('so3 and years')
plt.xlabel("year")
plt.ylabel("so3")
plt.xticks(())
plt.yticks(())
plt.show()
