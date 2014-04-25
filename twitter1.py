import oauth2 as oauth
import json
import twitter

CONSUMER_KEY = 'AYVGhtju04luQxaZNZQwGnNme'
CONSUMER_SECRET = 'fc9Ddxf7JLxBuZQLqhz5KNIzEB3YlRSFgqRXXytn5rKkZUR9fo'
ACCESS_KEY = '273619912-Cl3clDtrQ5FfoswvR0oC4eOy9xi18dY7ObLyoMGF'
ACCESS_SECRET = 'lrzncKOozzbaWGSaEhKxOV34bUAwCZzwWE4NIDCLizSeK'


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
# Nothing to see by displaying twitter_api except that it's now a
# defined variable
print twitter_api