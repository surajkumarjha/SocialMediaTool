#import pymongo
#from pymongo import MongoClient

import pandas as pd
import re
import spacy 
def TDict():
	#conn=pymongo.MongoClient("mongodb://localhost")
	#database=conn.Twitter
	#coll=database.sentiment_store
	#coll2=database.fewsent
	#mylist = []
	#for x in coll.find({},{"text":1,"_id":0}):
	  #database.fewsent.insert_one(x)
	  #mylist.append(x.values())
	#return mylist
	df = pd.read_table('sana1.json',names=['comments'])
	#------------------------#
	Comment=[]
	finalComment = []
	for comment in df['comments']:
		semifinalComment = ""
		try:
			match1 = re.findall('RT @\w+:',comment)
			semifinalComment = comment.replace(match1[0],"")
			Comment.append(semifinalComment)
		except: 
			Comment.append(comment)	
			pass
	newDf = pd.DataFrame()
	newDf['Comment']=Comment   	 
#----------------------------#
	for comment in newDf['Comment']:
		semifinalComment=""
		match1 = re.findall('@\w+',comment)
		for i in range(len(match1)):
			comment = comment.replace(match1[i],"")
		finalComment.append(comment)      	  
    	 
	return finalComment
	
