#Program to analyse the paragraph. Analysing the average word count, average letter count, approximaate word count and apporximate sentence length.

#Importing the required modules
import re,csv,os

#Intializing an empty list for sentences and words
sentences=[]
words=[]
#Intializing wordcount and sentencecount as 0
wordcount=0
sentencecount=0

#Creating the path for the input file to be analyzed
filepath=os.path.join("Resources","paragraph_1.txt")

with open(filepath) as txtfile:
	
	text=txtfile.read()
	#Splitting words using white space charater
	words=re.split(r'\s*',text)
	#Splitting sentence based on the sentence formats
	sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

#Counts an extra sentence always, hene deleting the last sentence which is blank
del sentences[-1]

#Calculating the sentence count
sentencecount=len(sentences)

#Calculating the word count
wordcount=len(words)

#Calculating the average words per sentence
averagesentence=wordcount/sentencecount

#Calculating the average letters per word
averagewords=round(sum(len(word) for word in words)/len(words),2)


#Printing the results to the terminal
print("\nPargraph Analysis")
print("-------------------")
print("Approximate Word Count: " + str(wordcount))
print("Aprroximate Sentence Count: " + str(sentencecount))
print("Average Letter Count: " + str(averagewords))
print("Average Sentence Count: " + str(averagesentence))

#Intializing the output path
filename=os.path.join("Output","output.txt")

#Writing the result to a text file.
#Open the file using "write" mode. Specify the variable to hold the contents
with open(filename, 'w') as fileobject:
    fileobject.write("\nPargraph Analysis" + "\n")
    fileobject.write("-------------------" + "\n")
    fileobject.write("Approximate Word Count: " + str(wordcount) + "\n")
    fileobject.write("Aprroximate Sentence Count: " + str(sentencecount)+ "\n")
    fileobject.write("Average Letter Count: " + str(averagewords) + "\n")
    fileobject.write("Average Sentence Count: " + str(averagesentence) + "\n")

 #End of project
