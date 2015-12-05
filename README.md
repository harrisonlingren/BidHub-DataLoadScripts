#Data Load Scripts
-----------------

There are 3 files necessary for loading data to Parse:

  1. Data file in CSV format 
       Must have 9 columns as of now:  
       [name, donor, price, desc, imgurl, openTimeNew, openDateNew, closeTimeNew, closeDateNew] 
       * First row of CSV will be skipped in the load
       * name: Item name
       * donor: Item donor
       * price: Item price
       * desc: Item description
       * imgurl: URL of image to display
       * openTimeNew: Item open time (24hr format - HH:MM)
       * openDateNew: Item open date (formatted as YYYY-MM-DD)
       * closeTimeNew: Item close time
       * closeDateNew: Item close date
       
  2. loadFromCSV.py
       Python class -- this is the file you want to run to upload the data. It will
	   prompt for the CSV filename (must be in same directory) and then will process it
	   and create objects in parse
	   
  3. createObject.py
       Python class -- this class is simply a function that takes in each argument necessary
	   for the Silent Auction app to function and uploads it to the Parse data using 
	   the Application ID and REST API keys for your Parse application.
