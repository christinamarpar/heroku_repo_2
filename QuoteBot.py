# Dependencies
import tweepy
import time
from os import environ

# Twitter API Keys
consumer_key = environ.get('consumer_key')
consumer_secret = environ.get('consumer_secret')
access_token = environ.get('access_token')
access_token_secret = environ.get('access_token_secret')
api_key = environ.get('api_key')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
gabo_quotes = [
    "It is not true that people stop pursuing dreams because they grow old, they grow old because they stop pursuing dreams.",
    "What matters in life is not what happens to you but what you remember and how you remember it.",
    "No matter what, nobody can take away the dances you've already had.",
]

# Create function for tweeting
def TweetOut(quote, tweet_number):
    api.update_status("Gabo Quote # " + str(tweet_number) + ": " + quote)
    print("success")
    
# Set timer to run every minute
tweet_number = 2
for quote in gabo_quotes:
    TweetOut(quote, tweet_number)
    time.sleep(60)
    tweet_number=tweet_number+1