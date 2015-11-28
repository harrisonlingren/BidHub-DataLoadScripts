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

#load to dictionary
loadReader = csv.DictReader(open(fileName, 'r'), fieldnames = ['name', 'donor', 'price'], delimiter = ',', quotechar = '"')

for row in loadReader:
	for key in row:
		load[key].append(row[key])


# Convert times to rest API format
# -------------------------------------------------------------------

openDate = "2015-11-07"
openTimeRaw = "00:00"

closeDate = "2015-12-07"
closeTimeRaw = "23:59"

# Process date/time into correct formats
	# html date output: YYYY-MM-DD
	# html time output: HH(24):MM

openYear = int(openDate[0:4])
openMonth = int(openDate[5:7])
openDay = int(openDate[8:10])
openHour = int(openTimeRaw[0:2])
openMin = int(openTimeRaw[3:5])

closeYear = int(closeDate[0:4])
closeMonth = int(closeDate[5:7])
closeDay = int(closeDate[8:10])
closeHour = int(closeTimeRaw[0:2])
closeMin = int(closeTimeRaw[3:5])


openTime = datetime.datetime(openYear,openMonth,openDay,openHour,openMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
closeTime = datetime.datetime(closeYear,closeMonth,closeDay,closeHour,closeMin).strftime('%Y-%m-%dT%H:%M:%S.%fZ')



# use white image, bulk description. Load these from CSV in future
img = "https://flordemilonga.files.wordpress.com/2009/12/blank-white-page.jpg"
desc = "testUpload"


# print details and then create objects in parse
for i in range(1,len(load['name'])):
	print("name:", load['name'][i])
	print("donor:", load['donor'][i])
	print("price:", load['price'][i])
	
	name = load['name'][i]
	donor = load['donor'][i]
	price = load['price'][i]
	
	print(createObject.create(name, desc, donor, float(price), img, openTime, closeTime))
	print("")


print("done!")