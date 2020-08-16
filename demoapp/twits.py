import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import time
#import pymongo
#from pymongo import MongoClient
import time
consumer_key ="OeTQue5kUC9Tmipnc50UJ3pQp"
consumer_secret="PY1p2456qi7AbUEBKCE75I4Ou0srM9Sfd32JN8FYJLfvs0E2X2"
access_token="1217743421038661632-uqNzvnw5NEpzaI5O3utIFdkaAfKywp"
access_secret="xS1dLltrc0bQxdLYZ4ctjxbWlwtC339g97xtcD9bMM8nB"
auth=OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)
class MyListener(StreamListener):
    def __init__(self, time_limit=60,positive = 0,negative = 0,neutral = 0,polarity = 0):
        self.start_time = time.time()
        self.limit = time_limit
        self.positive=positive
        self.negative=negative
        self.neutral=neutral
        self.polarity=polarity
        #self.saveFile = open('update.json', 'a')
        super(MyListener, self).__init__()
    def on_data(self, data):
        try: 
            if(time.time() - self.start_time) < self.limit:
                #conn=pymongo.MongoClient("mongodb://localhost")
                #database=conn.Twitter
                #coll=database.sentiment_store
                 
                all_data=json.loads(data)
                tweet = all_data["text"]
                #coll.insert_one({"text" : tweet})
                txtblb = TextBlob(tweet).sentiment
                analysis = TextBlob(tweet)
                self.polarity += analysis.sentiment.polarity
                if (analysis.sentiment.polarity == 0):
                    self.neutral += 1
                elif (analysis.sentiment.polarity < 0.00):
                    self.negative += 1
                elif (analysis.sentiment.polarity > 0.00):
                    self.positive += 1
                f= open("positive.txt","w+")
                f1= open("negative.txt","w+")
                f2= open("neutral.txt","w+")
                f.write(str(self.positive))
                f1.write(str(self.negative))
                f2.write(str(self.neutral))
                #print(tweet, txtblb.polarity, txtblb.subjectivity)
                if(txtblb.subjectivity*100 >=60):
                    output = open("sana1.json", "a")
                    output.write(str(tweet))
                    output.write('\n')
                    output.close()
                    return True
                
            else:
                return False
            
              
        except BaseException as e:
            print("error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True
def callData(a):
    twitter_stream=Stream(auth ,listener=MyListener(time_limit=50 ,positive = 0,negative = 0,neutral = 0,polarity = 0))

    twitter_stream.filter(track=[a],is_async=True,languages=["en"])
    #time.sleep(60)
