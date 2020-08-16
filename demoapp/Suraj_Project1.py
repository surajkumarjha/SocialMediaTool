#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:47:16 2020

@author: adityaanand
"""

import pandas as pd
import re
import spacy 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#from docx import Document
#from docx.shared import Inches
def WordCloudGen():
    nlp = spacy.load('en_core_web_sm')
    df = pd.read_table('sana.json',names=['comments'])
    #------------------------#
    Comment=[]
    finalComment = []
    for comment in df['comments']: #for removing RT @iheartmindy (user name)
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
    for comment in newDf['Comment']:#for removing @iheartmindy (tag inside comment)
        semifinalComment=""
        match1 = re.findall('@\w+',comment)
        for i in range(len(match1)):
            comment = comment.replace(match1[i],"")  
        finalComment.append(comment) 
    #----------------------------#
    #Removing stopword,punctuation,digits.
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
    #----------------------------#
    newDf = pd.DataFrame()
    newDf['comments']=preprocessedComment 
    #preprocessed DataFrame.
    #newDf.to_csv('preprocessedSurajData.csv') #uncomment it for creating new csvFile..
    #------------------------------#
    wordsList= {}
    for words in newDf['comments']:
        for word in nlp(words):
            if str(word) in wordsList.keys():
                wordsList[str(word)]+=1
            else:
                wordsList[str(word)]=1
    cloud= WordCloud().generate(str(wordsList))
    cloud.to_file('static/people_photo1/N2.png')
                