from flask import Flask, render_template
from flask import request
import time
import twits
import twittest
import facesent
import facebook
#import ReadData
import os
import senti
import tdict
import tdict1
import Suraj_Project
import Suraj_Project1
#import classification
#import ClearAnalysis
#import cleardatabase


PEOPLE_FOLDER = os.path.join('static', 'people_photo')
PEOPLE_FOLDER1 = os.path.join('static', 'people_photo1')
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['UPLOAD_FOLDER1'] = PEOPLE_FOLDER1


@app.route('/')

def index():
	return render_template("tab.html")

@app.route('/',methods=['POST'])
def getdata():
	search=request.form['search']
	face=request.form['face']
	if(face == 'Facebook'):
		output = open("sana1.json","w")
		output.write(str("test"))
		output.close()
		facebook.getFacebook(search)
		my_list = tdict.TDict()
		Suraj_Project.WordCloudGen()
		positive,negative,neutral = facesent.ClassificationOfTweeter()
		positive = positive[1]
		negative = negative[1]
		neutral = neutral[1]
		labels = ["January","February","March","April","May","June","July","August"]
		values = [10,9,8,7,6,4,7,8]
		full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'N.png')
		return render_template('index.html',s=search,p=positive,n=negative,ne=neutral,my_list=my_list,user_image = full_filename,values=values, labels=labels)
	else:
		output = open("sana.json", "w")
		output.write(str("test"))
		output.close()
		#twits.callData(search)
		#ReadData.ReadMongoData()
		positive,negative,neutral=twittest.callData(search,10) # sentiment result
		my_list = tdict1.TDict()
		Suraj_Project1.WordCloudGen()
		labels = ["January","February","March","April","May","June","July","August"]
		values = [10,9,8,7,6,4,7,8]
		#cleardatabase.ClearDataBaseData()
		full_filename = os.path.join(app.config['UPLOAD_FOLDER1'], 'N2.png')
		return render_template('index.html',s=search,p=positive,n=negative,ne=neutral,my_list=my_list,user_image = full_filename,values=values, labels=labels)
		#return face
app.run()

	 
	
	


