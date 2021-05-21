#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#최고기온 날짜
import csv
f = open('seoul.csv')
data = csv.reader(f)
# header(필요없는 부분 skip)
header = next(data)
max_temp = -999
max_date = ''
for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    
    if max_temp < row[-1]:
        max_temp = row[-1]
        max_date = row[0]
f.close()
print('최고기온')
print('날짜: ',max_date, '기온: ', max_temp)

#최저기온 날짜
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
min_temp = 999
min_date = ''
for row in data:
    if row[-1] == '':
        row[-1] = 999
    row[-1] = float(row[-1])
    
    if min_temp > row[-1]:
        min_temp = row[-1]
        min_date = row[0]
f.close()
print('최저기온')
print('날짜: ',min_date, '기온: ', min_temp)

#일교차 가장 큰 날
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
max_diff = -999
md_date = ''
for row in data:
    row[-1] = float(row[-1])
    row[-2] = float(row[-2])

    if max_diff < row[-1] - row[-2]:
        max_diff = row[-1] - row[-2]
        md_date = row[0]
f.close()
print('일교차 최대')
print('날짜: ',md_date, '일교차: ', max_diff)


# In[ ]:


import csv

f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
max_use = -999
max_station = ''
max_station_id = ''
max_use1 = -999
max_station1 = ''
max_station_id1 = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))

    if max_use < row[-1] + row[-2]:
        max_use = row[-1] + row[-2]
        max_station = row[3]
        max_station_id = row[1]

f.close()
print('이용객이 가장 많은 역 순위')
print('1. 역 이름:',max_station_id, max_station,'이용객 수:', max_use)

f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
max_use1 = -999
max_station1 = ''
max_station_id1 = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))
    
    if max_use > row[-1] + row[-2]:
        if max_use1 < row[-1] + row[-2]:
            max_use1 = row[-1] + row[-2]
            max_station1 = row[3]
            max_station_id1 = row[1]
f.close()
print('2. 역 이름:',max_station_id1, max_station1,'이용객 수:', max_use1)

f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
max_use2 = -999
max_station2 = ''
max_station_id2 = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))
    
    if max_use1 > row[-1] + row[-2]:
        if max_use2 < row[-1] + row[-2]:
            max_use2 = row[-1] + row[-2]
            max_station2 = row[3]
            max_station_id2 = row[1]
f.close()
print('3. 역 이름:',max_station_id2, max_station2,'이용객 수:', max_use2)


#이용객 가장 적은 역 순위
f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
min_use = 9999999
min_station = ''
min_station_id = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))

    if min_use > row[-1] + row[-2]:
        min_use = row[-1] + row[-2]
        min_station = row[3]
        min_station_id = row[1]

f.close()
print('이용객이 가장 적은 역 순위')
print('1. 역 이름:',min_station_id, min_station,'이용객 수:', min_use)

f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
min_use1 = 9999999
min_station1 = ''
min_station_id1 = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))
    if min_use < row[-1] + row[-2]:
        if min_use1 > row[-1] + row[-2]:
            min_use1 = row[-1] + row[-2]
            min_station1 = row[3]
            min_station_id1 = row[1]

f.close()
print('2. 역 이름:',min_station_id1, min_station1,'이용객 수:', min_use1)

f = open('subwayuse.csv')
data = csv.reader(f)
next(data)
min_use2 = 9999999
min_station2 = ''
min_station_id2 = ''
for row in data:    
    for i in range(4,6):
        row[i] = int(row[i].replace(',', ''))
    if min_use1 < row[-1] + row[-2]:
        if min_use2 > row[-1] + row[-2]:
            min_use2 = row[-1] + row[-2]
            min_station2 = row[3]
            min_station_id2 = row[1]

f.close()
print('3. 역 이름:',min_station_id2, min_station2,'이용객 수:', min_use2)

