import re
import csv 
import pandas as pd 
import re

#################################### News API Data Cleaning ###############################################

inputfile = csv.reader(open('newsapi.csv', 'r'))

outputfile = open('newsapicleaned.csv', 'w')
writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for row in inputfile:
    row[0] = row[0].encode('ascii', 'ignore').decode('ascii')           #Title     #Cleaning special Characters
    row[0] = re.sub(r'[^\x00-\x7F]+',' ',row[0])
    if(pd.isna(row[1])):
        row[1] = " "                                                    #Author    #If found null then appending space
    else:
        row[1] = re.sub(r'http\S+','',str(row[1]),flags=re.MULTILINE)   #Author    #Removing URLs
    row[4] = row[4].encode('ascii', 'ignore').decode('ascii')           #Content   #Cleaning special Characters
    row[4] = re.sub(r'[^\x00-\x7F]+',' ',row[4])
    row[2] = row[2].encode('ascii', 'ignore').decode('ascii')           #Description #Cleaning special Characters                                       
    row[2] = re.sub(r'[^\x00-\x7F]+',' ',row[2])
    writer.writerow(row)  

#################################### Twitter API Data Cleaning ###############################################

inputfile = csv.reader(open('tweets_SearchAPI.csv', 'r'))

outputfile = open('Twitter_SearchAPI_cleaned.csv', 'w')
writer = csv.writer(outputfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for row in inputfile:
    x = re.sub(r'http\S+','',str(row[0]),flags=re.MULTILINE)           #Cleaning URLs
    row[0] = x.encode('ascii','ignore').decode('ascii')                #Tweet     #Cleaning special Characters and Emojis
    row[0] = re.sub(r'[^\x00-\x7F]+',' ',row[0])
    if(pd.isna(row[1])):
        row[1] = " "                                                   #Location  #If found null then appending space
    else:
        row[1] = row[1].encode('ascii','ignore').decode('ascii')       #Location  #Cleaning special Characters
        row[1] = re.sub(r'[^\x00-\x7F]+',' ',row[1])
    row[3] = row[3].encode('ascii','ignore').decode('ascii')           #Username  #Cleaning special Characters
    row[3] = re.sub(r'[^\x00-\x7F]+',' ',row[3])
    clean = re.compile('<.*?>')
    row[0] = re.sub(r'@+','',str(row[0]),flags=re.MULTILINE)           #Remove username starting with @
    row[0] = row[0].replace("RT","").strip()
    
    writer.writerow(row)








