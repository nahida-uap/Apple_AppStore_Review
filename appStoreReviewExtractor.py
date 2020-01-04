#!/usr/bin/env python
# @author Nahida Sultana Chowdhury <nschowdh@iu.edu>
# Python version 3.7.3

import urllib.request, json, time, csv, sys

def getReviews(appID, page=1):
    try:
        url = 'https://itunes.apple.com/rss/customerreviews/id=%s/page=%d/sortby=mostrecent/json' % (appID, page) 
        with urllib.request.urlopen(url) as f:
            data = json.loads(f.read().decode()).get('feed')
            #print(data)
          
        if data.get('entry') == None:
            getReviews(appID, page+1)
            return
        
        for entry in data.get('entry'):
            if entry.get('im:name'):
                continue
            
            title = entry.get('title').get('label')
            print(title)
            author = entry.get('author').get('name').get('label')            
            version = entry.get('im:version').get('label')
            rating = entry.get('im:rating').get('label')
            review = entry.get('content').get('label')
            vote_count = entry.get('im:voteCount').get('label')
            
            csvData = [title.encode("utf-8"),  author.encode("utf-8"), version.encode("utf-8"), rating.encode("utf-8"), review.encode("utf-8"), vote_count]
            writer.writerow(csvData)
            print(csvData)
        
        if page<=10:            
            getReviews(appID, page+1)
    
    except Exception:
        time.sleep(1)


csvTitles = ['title',  'author', 'version', 'rating', 'review', 'vote_count']
myFile = open('reviews.csv',"w")
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(csvTitles)    
    getReviews(310633997)
