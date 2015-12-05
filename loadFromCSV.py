# data load to parse

#!/usr/bin/env python3

import createObject,datetime,csv

# get file name
fileName = input("CSV file to upload?: ")

#initialize dictionary arrays to hold CSV rows
load = {}
load['name'] = []
load['donor'] = []
load['price'] = []
load['desc'] = []
load['imgurl'] = []
load['openTimeNew'] = []
load['openDateNew'] = []
load['closeTimeNew'] = []
load['closeDateNew'] = []


#load to dictionary
loadReader = csv.DictReader(open(fileName, 'r'), fieldnames = ['name', 'donor', 'price', 'desc', 'imgurl', 'openTimeNew', 'openDateNew', 'closeTimeNew', 'closeDateNew'], delimiter = ',', quotechar = '"')

for row in loadReader:
	for key in row:
		load[key].append(row[key])


# Convert times to rest API format
# -------------------------------------------------------------------

# date format:	"2015-11-07"
# time format:	"23:59" (24 hour time)


# Process date/time into correct formats

openTime = []
closeTime = []

for i in range(1,len(load['name'])):
	openYear = int(load['openDateNew'][i][0:4])
	openMonth = int(load['openDateNew'][i][5:7])
	openDay = int(load['openDateNew'][i][8:10])
	openHour = int(load['openTimeNew'][i][0:2])+5
	openMin = int(load['openTimeNew'][i][3:5])

	closeYear = int(load['closeDateNew'][i][0:4])
	closeMonth = int(load['closeDateNew'][i][5:7])
	closeDay = int(load['closeDateNew'][i][8:10])
	closeHour = int(load['closeTimeNew'][i][0:2])+5
	closeMin = int(load['closeTimeNew'][i][3:5])

	openTime.append(datetime.datetime(openYear,openMonth,openDay,openHour,openMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
	closeTime.append(datetime.datetime(closeYear,closeMonth,closeDay,closeHour,closeMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))


# print details and then create objects in Parse
for i in range(1,len(load['name'])):
	print("name:  %s" % load['name'][i])
	print("donor:  %s" % load['donor'][i])
	print("price:  %s" % load['price'][i])
	print("desc:  %s" % load['desc'][i])
	print("imgurl:  %s" % load['imgurl'][i])
	print("openTime:  %s" % openTime[i-1])
	print("closeTime:  %s" % closeTime[i-1])
	
	name = load['name'][i]
	donor = load['donor'][i]
	price = load['price'][i]
	desc = load['desc'][i]
	img = load['imgurl'][i]
	
	print(createObject.create(name, desc, donor, float(price), img, openTime[i-1], closeTime[i-1]))
	print("")


print("done!")
