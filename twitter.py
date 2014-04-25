import oauth2 as oauth
import json
 
CONSUMER_KEY = 'xlay6t4zsl1rJtbGZdknYCqaY'
CONSUMER_SECRET = '4QrDTrKhkkvAE5svUVwgRzf16R2wdmP9AXj6LSya0M10TRSjsN'
ACCESS_KEY = '273619912-1KH4ZeToG5nY0QkPJVYw7JQinJljQoRHNVNaKgA5'
ACCESS_SECRET = 'jce78F7nPe0XRp2USRthP9CDV4X3rhMPvVTIgLlph4gQI'
 
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
 
timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)
data = json.loads(data)
for i in data: print i['text']