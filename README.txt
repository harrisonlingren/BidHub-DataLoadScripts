Data Load Scripts
-----------------

There are 3 files necessary for loading data to Parse:

  1. Data file in CSV format 
       Must have 3 columns as of now:  []name, donor, price] -- first row of CSV 
	   will be skipped in the load
  2. loadFromCSV.py
       Python class -- this is the file you want to run to upload the data. It will
	   prompt for the CSV filename (must be in same directory) and then will process it
	   and create objects in parse
  3. createObject.py
       Python class -- this class is simply a function that takes in each argument necessary
	   for the Silent Auction app to function and uploads it to the Parse data using 
	   the Application ID and REST API keys for your Parse application.