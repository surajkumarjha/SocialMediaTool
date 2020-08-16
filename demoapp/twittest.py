import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import time
#import pymongo
#from pymongo import MongoClient
def callData(searchTerm,noOfSearchTerms):
    consumer_key ="OeTQue5kUC9Tmipnc50UJ3pQp"
    consumer_secret="PY1p2456qi7AbUEBKCE75I4Ou0srM9Sfd32JN8FYJLfvs0E2X2"
    access_token="1217743421038661632-uqNzvnw5NEpzaI5O3utIFdkaAfKywp"
    access_secret="xS1dLltrc0bQxdLYZ4ctjxbWlwtC339g97xtcD9bMM8nB"
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    for tweet in tweets:
        #print(tweet.text)
        output = open("sana.json", "a")
        output.write(str(tweet.text))
        output.write('\n')
        output.close()
        analysis = TextBlob(tweet.text)
        print(analysis)
        #all_data=json.loads(str(analysis))
        
        polarity += analysis.sentiment.polarity
        if (analysis.sentiment.polarity == 0):
            neutral += 1
        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
        elif (analysis.sentiment.polarity > 0.00):
            positive += 1
    return positive,negative,neutral

