#!/usr/bin/env python
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import json
import time
import csv
import sys

def getJson(url):
    response = urlopen(url)
    data = str(response.read())
    return json.loads(data)

def getReviews(appID, page=1):
    try:
        url = 'https://itunes.apple.com/rss/customerreviews/id=%s/page=%d/sortby=mostrecent/json' % (appID, page)
        #print("test1")
        data = getJson(url).get('feed')
        #print("test2")
        if data.get('entry') == None:
            getReviews(appID, page+1)
            return
        #print("test3")
        for entry in data.get('entry'):
            #print("test")
            if entry.get('im:name'):
                continue
            #review_id = entry.get('id').get('label')
            title = entry.get('title').get('label')
            #print(title)
            
            author = entry.get('author').get('name').get('label')
            #author_url = entry.get('author').get('uri').get('label')
            version = entry.get('im:version').get('label')
            rating = entry.get('im:rating').get('label')
            review = entry.get('content').get('label')	
            vote_count = entry.get('im:voteCount').get('label')
            
            csvData = [title.encode("utf-8"),  author.encode("utf-8"), version.encode("utf-8"), rating.encode("utf-8"), review.encode("utf-8"), vote_count]
            #writer.writerow(unicode(csvData).encode("utf-8") )
            writer.writerow(csvData)
            
            #print('"'+'","'.join(csvData)+'"')
            print(csvData)
        
        if page<=10:
            print ("\n\n\n"+str(page)+"\n\n\n")
            getReviews(appID, page+1)
    
    except Exception:
        time.sleep(1)


csvTitles = ['title',  'author', 'version', 'rating', 'review', 'vote_count']
myFile = open('/home/mitu/Downloads/AppleStore/16_rev.csv',"w")
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(csvTitles)
    #print ','.join(csvTitles)
    getReviews(920869470)
    myFile.close()
