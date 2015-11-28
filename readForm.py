#!/usr/bin/env python3

import cgi,cgitb,createObject,datetime

cgitb.enable()

print("Content-Type: text/html")
print()
print("""
    <hmtl><head><title>Add Item</title>
	<link href='http://fonts.googleapis.com/css?family=Roboto:400,300,100,500' rel='stylesheet' type='text/css'>
	<link href="style.css" rel="stylesheet" type="text/css"></head>
	<body><h1>Add Item</h1>
	""")


formData = cgi.FieldStorage()
	
desc = formData['itemDesc'].value
donor = formData['itemDonorName'].value
imgurl = formData['itemImgURL'].value
name = formData['itemName'].value
startPrice = int(formData['itemPrice'].value)

openDate = str(formData['itemOpenDate'].value)
openTimeRaw = str(formData['itemOpenTime'].value)

closeDate = str(formData['itemCloseDate'].value)
closeTimeRaw = str(formData['itemCloseTime'].value)

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

print("<p>name:", name, "</p>")
print("<p>desc:", desc, "</p>")
print("<p>donor:", donor, "</p>")
print("<p>startPrice:", startPrice, "</p>")
print("<p>imgurl:", imgurl, "</p>")
print("<p>openTime:", openTime, "</p>")
print("<p>closeTime:", closeTime, "</p>")


print("<p>", createObject.create(name,desc,donor,startPrice,imgurl,openTime,closeTime), "</p>")

print("""
	</body></html>
	""")