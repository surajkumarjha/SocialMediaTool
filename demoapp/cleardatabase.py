import json
from pymongo import MongoClient

def ClearDataBaseData():
	client=MongoClient('localhost',27017)
	db=client['Twitter']
	col=db['sentiment_store']
	col.drop()







