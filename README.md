#Crawler for Apple AppStore Review
Access to the reviews is publically available via RSS feeds.
  https://itunes.apple.com/rss/customerreviews/id=appId/page=1/sortby=mostrecent/json
  
  
This is a Python based script which require:
    - Python 2.7+
    
As Input user need to pass the app's ID which can be found at the end of the url of app in appstore. E.g.
https://apps.apple.com/us/app/whatsapp-messenger/id310633997  --->> Here, 310633997 is the appId for WhatsApp.

In returns the program will retrun the following fields and will store into CSV files:
   - title
   - author
   - version
   - rating
   - review
   - vote_count

To run the code type the following command:

    python appStoreReviewExtractor.py

