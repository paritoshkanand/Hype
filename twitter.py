import oauth2 as oauth
import json
 
CONSUMER_KEY = "AYVGhtju04luQxaZNZQwGnNme"
CONSUMER_SECRET = "fc9Ddxf7JLxBuZQLqhz5KNIzEB3YlRSFgqRXXytn5rKkZUR9fo"
ACCESS_KEY = "273619912-Cl3clDtrQ5FfoswvR0oC4eOy9xi18dY7ObLyoMGF"
ACCESS_SECRET = "lrzncKOozzbaWGSaEhKxOV34bUAwCZzwWE4NIDCLizSeK"
 
#now we login in our app
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
 
#we get the timeline json
timeline_endpoint = "http://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)
 
#we load it in our variable
tweets = json.loads(data)
 
#print first tweet
print tweets[6]['text']