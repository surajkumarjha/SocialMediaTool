import json
import pandas as pd
import re
import spacy 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from docx import Document
#from docx.shared import Inches
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
def ClassificationOfTweeter():
	nlp = spacy.load('en_core_web_sm')
	df = pd.read_table('sana1.json',names=['comments'])
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
	for comment in newDf['Comment']:
		semifinalComment=""
		match1 = re.findall('@\w+',comment)
		for i in range(len(match1)):
			comment = comment.replace(match1[i],"") 
		finalComment.append(comment)
	preprocessedComment = []
	for i in df['comments']:
		lst=[]
		for j in nlp(i):
			if j.is_alpha:
				if (j.is_stop==False):
					if(j.is_digit==False):
						lst.append(str(j.lemma_).lower())
		comment=" ".join(lst)
		if len(comment)!=0:
			preprocessedComment.append(comment)
	preprocessedComment
	newDf = pd.DataFrame()
	newDf['comments']=preprocessedComment
	corpus = newDf['comments']
	bow = CountVectorizer()
	X = bow.fit_transform(corpus)
	X=bow.fit_transform(corpus)
	X=X.toarray()
	kmeans = KMeans(n_clusters=3)
	model  = kmeans.fit(X)
	predictions = model.predict(X)
	newDf['cluster'] = predictions
	count0=newDf[newDf['cluster']==0].count()
	count1=newDf[newDf['cluster']==1].count()
	count2=newDf[newDf['cluster']==2].count()
	return count0,count1,count2



