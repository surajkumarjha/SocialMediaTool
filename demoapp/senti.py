def Sentiment_Return():
	f=open("positive.txt","r")
	pos=f.read()
	pos=int(pos)
	f1=open("negative.txt","r")
	neg=f1.read()
	neg=int(neg)

	f2=open("neutral.txt","r")
	ne=f2.read()
	ne=int(ne)
	return pos,neg,ne