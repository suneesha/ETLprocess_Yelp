# Perform ETL process on the Yelp API

Author : Suneesha Kudipudi

Files Uploaded:

DataCollection_API.py  - It is programmed to collect the searchfeed from yelp api and store it in flatfile. 
DataLoader.py  - Program to ingest database with the data from flatfile .  
PYTHON_DATABASEQUERY_API.py  - Program to interact with the database and fetch the search results.  

The below files are the ipython notebook versions of the same code.
DataCollection_API.ipynb
DataLoader.ipynb
PYTHON_DATABASEQUERY_API.ipynb

Steps for executing the code:  

Requirements:  
  MySql server   
  Python 2.7/Anaconda  

1.Include the sql access credentials in the DataLoader.py and the yelp API access credentials in DataCollection_API.py.  
2.Run----$ python DataCollection_API.py    
This will generate the flat file with the feed-data  
3.Run----$ python DataLoader.py   
This will inject the data from the flatfile into the Sqldb.  
4.Run----$ python PYTHON_DATABASEQUERY_API.py   
This is the User interactive query page which will query the database and show the results.  

Key Points:
1.Dealing with Unicode strings.  
2.Assumption of Customer position and calculating the distance.  
3.Regular expressions for processing strings.  

