# Importing modules
import os
import re
words=[]
sentences=[]
wordcount=[]
sentcount=0
filepath=os.path.join("Resources","paragraph_1.txt")

with open(filepath) as txtfile:
	text=txtfile.read()
	sentences=text.split('.')
	sentcount=len(sentences)-1
	for sentence in sentences:
		words=re.split("(?&lt;=[.!?]) +", sentence)
		wordcount.append(len(words))
		print(words)
		#wordcount.append(len(words))
	#sentcount.append(len(sentences))

#average_wordcount=sum(wordcount)/len(wordcount)
#average_sentcount=sum(sentcount)/len(sentcount)

#print("\n\nParagraph Analysis")
#print("------------------------")
#print("Approximate Word Count: " + str(len(wordcount)))
#print("Approximate Sentence Count: " + str(len(sentcount)))
#print("Average Word Count: ") + str(average_wordcount)
#print("Average Sentence Length: " + str(average_sentcount))

