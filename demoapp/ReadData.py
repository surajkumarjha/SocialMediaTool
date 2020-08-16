import pymongo
import json


class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value
def ReadMongoData():
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = client["Twitter"]
	mycol = mydb["sentiment_store"]       
	mydict = create_dict()

	i = 1
	for y in mycol.find():
		mydict.add(i,({"text":y['text']}))
		i = i+1
	stud_json = json.dumps(mydict, indent=2, sort_keys=True)
	output = open("sanaa.json", "w")
	output.write(str(stud_json))
	output.write('\n')
	output.close()

ReadMongoData()
	
	
	
	
	

