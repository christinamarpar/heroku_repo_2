# Dependencies
import tweepy
import time
from os import environ
#from config import consumer_key, consumer_secret, access_token, access_token_secret

#consumer_key = consumer_key
#consumer_secret = consumer_secret
#access_token = access_token
#access_token_secret = access_token_secret

# Twitter API Keys
consumer_key = environ.get('consumer_key')
consumer_secret = environ.get('consumer_secret')
access_token = environ.get('access_token')
access_token_secret = environ.get('access_token_secret')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
gabo_quotes = [
    "It's enough for me to be sure that you and I exist at this moment.",
    "There is always something left to love.",
    "Then he made one last effort to search in his heart for the place where his affection had rotted away, and he could not find it.",
    "...time was not passing...it was turning in a circle...",
    "They were so close to each other that they preferred death to separation.”
]

# Create function for tweeting
def TweetOut(quote, tweet_number):
    api.update_status("Gabo Quote # " + str(tweet_number) + ": " + quote)
    print("success")
    
# Set timer to run every minute
tweet_number = 5
for quote in gabo_quotes:
    TweetOut(quote, tweet_number)
    time.sleep(60)
    tweet_number=tweet_number+1