from facebook_scraper import get_posts
import pymongo
from pymongo import MongoClient
def getFacebook(a):
	conn=pymongo.MongoClient("mongodb://localhost")
	database=conn.Twitter
	coll=database.sentiment_store
    
	for i in range(0,5):
		for post in get_posts(a, pages=i):
			print(post['text'])
			coll.insert_one({"text" : post['text']})
			output = open("sana1.json", "a")
			output.write(str(post['text']))
			output.write('\n')
			output.write('\n')
			output.close()



