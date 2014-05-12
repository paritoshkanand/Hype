from twython import Twython
#import csv

TWITTER_APP_KEY = 'xlay6t4zsl1rJtbGZdknYCqaY' #supply the appropriate value
TWITTER_APP_KEY_SECRET = '4QrDTrKhkkvAE5svUVwgRzf16R2wdmP9AXj6LSya0M10TRSjsN' 
TWITTER_ACCESS_TOKEN = '273619912-1KH4ZeToG5nY0QkPJVYw7JQinJljQoRHNVNaKgA5'
TWITTER_ACCESS_TOKEN_SECRET = 'jce78F7nPe0XRp2USRthP9CDV4X3rhMPvVTIgLlph4gQI'

#csvFile = open('/Users/paritoshanand/Hype/result.csv', 'w')
#csvFile.close()

f=open('/Users/paritoshanand/Hype/hype.csv','w')

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q=raw_input('Hello Shradha, Enter your search word: '),   #**supply whatever query you want here**
                 )

tweets = search['statuses']

for tweet in tweets:
	save=open('/Users/paritoshanand/Hype/hype.csv','a')
	save.write(tweet['text'].encode('utf-8').strip())
	save.write('\n')
	save.close()
#	csvFile = open('/Users/paritoshanand/Hype/result.csv', 'a')
#	csvWriter = csv.writer(csvFile)
#	csvWriter.writerow(tweet['text'].encode('utf-8'))
#	csvFile.close()