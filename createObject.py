# data load to parse

#!/usr/bin/env python3

import json,http.client,datetime

def create(name,desc,donor,startPrice,imgurl,openDate,closeDate):
	
    
    # Connect to parse
	connection = http.client.HTTPSConnection('api.parse.com', 443)
	connection.connect()

    # POST request -- upload data/create items using arguments
    connection.request('POST', '/1/classes/Item', json.dumps({
			"description": desc,
			"donorname": donor,
			"imageurl": imgurl,
			"name": name,
			"price": startPrice,
			"priceIncrement": 2.5,
			"qty": "1",
			"closetime": {
			  "__type": "Date",
			  "iso": closeDate # format = "2011-08-21T18:02:52.249Z" = ""
			},
			"opentime": {
			  "__type": "Date",
			  "iso": openDate # format = "2011-08-21T18:02:52.249Z" = ""
			},			
		 }), {
		   "X-Parse-Application-Id": "WhkQetI8nb0HrIykoaNc8LJ9flHIxOvgaXhFXFxm",
		   "X-Parse-REST-API-Key": "G02koccgg9q6RzqwRmpiQDx3QllASet5iW2XbLob",
		   "Content-Type": "application/json"
		 })
	
	# Print response from connection
	str_response = connection.getresponse().read().decode('utf-8')
	
	results = json.loads(str_response)
	return results