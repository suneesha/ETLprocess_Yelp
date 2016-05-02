
# coding: utf-8

# In[3]:

# Author : Suneesha Kudipudi
# DataLoader.py  - Program to ingest database with the data from flatfile .
import mysql.connector
import re
def loadData():
    global cnx
    cursor = cnx.cursor()
    f=open('feed.txt','r')
    for line in f:
        line=line.split('|')
        # type casting logic
        line[4]=re.sub('[^A-Za-z0-9|]+',' ',line[4])
        line[0]=re.sub('[^A-Za-z0-9|]+',' ',line[0])

        print line[0],float(line[1]),int(line[2]),line[3],line[4],float(line[5]),float(line[6])
        query = "INSERT INTO YELPFEED                   VALUES ('%s','%f','%d','%s','%s','%f','%f','%s')"%(line[0],float(line[1]),int(line[2]),line[3],line[4],
                                                                 float(line[5]),float(line[6]),line[7])
        print type(query)
        cursor.execute(query)
    cursor.close()
    cnx.commit()
    f.close()

def createTable():
    global cnx
    cursor = cnx.cursor()
    query = "CREATE TABLE YELPFEED(                                    name varchar(255),                                    Rating FLOAT,                                    review_count INT,                                    category_labels varchar(255),                                    address varchar(255),                                    latitude FLOAT,                                    longitude FLOAT,                                    searchtag varchar(255))"
    cursor.execute(query)
    cursor.close()
    cnx.commit()
    
if __name__=="__main__":    
    cnx = mysql.connector.connect(user='root', password='root',
                                  host='localhost',
                                  database='FUNDINGCIRCLE')
    createTable()
    loadData()
    print "DataLoading to the database is successful"
    cnx.close()
    
       


# In[3]:

cnx.close()


# In[ ]:



