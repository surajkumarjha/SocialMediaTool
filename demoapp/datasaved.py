from flask import Flask, render_template
from flask import request
import time
import twits
import ReadData
import os
import senti
import tdict
import Suraj_Project
import classification
import ClearAnalysis
import cleardatabase


PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')

def index():
	return render_template("tab.html")

@app.route('/',methods=['POST'])
def getdata():
	search=request.form['search']
	output = open("sana1.json", "w")
	output.write(str(""))
	output.close()
	#ClearAnalysis.ClearAnalysisData() # clear All current Data
	#time.sleep(19)
	#twits.callData(search) # extract tweet
	#time.sleep(54)
	#ReadData.ReadMongoData() # read tweet from mongodb
	positive,negative,neutral=senti.Sentiment_Return() # sentiment result
	my_list = tdict.TDict() # get list of tweet
	Suraj_Project.WordCloudGen()  # generating word cloud
	#labels = ["January","February","March","April","May","June","July","August"]
	#values = [10,9,8,7,6,4,7,8]
	#t0,t1,t2=classification.ClassificationOfTweeter()  # classify the tweet
	#ClearAnalysis.ClearAnalysisData() # clear All current Data
	#cleardatabase.ClearDataBaseData() # completely clear data from database
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'N.png')
	time.sleep(30)
	return render_template('index.html',s=search,p=positive,n=negative,ne=neutral,my_list=my_list,user_image = full_filename,values=values, labels=labels)
