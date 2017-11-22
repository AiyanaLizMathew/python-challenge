#Importing modules
import os
import csv

#Declaring an empty list to store the candidate names
candidate=[]
#Declaring an emptylist to store the votes for each candidate
votes_candidate=[]


#Intializing Total no of votes
total=0
#Intializing count of winner votes
winnervote=0

election_data_files=['1','2']

for filenumber in election_data_files:
	#Creating the path of input files
	csvpath=os.path.join('Resources', 'election_data_'+filenumber+'.csv')
	with open(csvpath) as csvfile:
		csvreader=csv.reader(csvfile,delimiter=',')
		next(csvreader,None)
		for row in csvreader:
			total=total+1
			if ((row[2] not in candidate) and (row[2]!='Candidate')):
				candidate.append(row[2])
				index=candidate.index(row[2])
				votes_candidate.insert(index,int('1'))

			elif ((row[2]  in candidate) and (row[2]!='Candidate')):
				votes_candidate[candidate.index(row[2])]= votes_candidate[candidate.index(row[2])]+1

#Printing the results to the terminal
print("\n\nElection Results")
print("-------------------------")
print("Total Votes:" + str(total))
print("-------------------------")
for item in candidate:
	#print("{:<14s} : {:2.2f} %  ({:10d})".format(item,round(votes_candidate[candidate.index(item)]*100/total,2)),votes_candidate[candidate.index(item)])
	print("{:<14s}".format(item) + ":  " + "{:2.2f}".format(round(votes_candidate[candidate.index(item)]*100/total,2)) + "% (" + "{:<}".format(votes_candidate[candidate.index(item)]) + ")")
	if(votes_candidate[candidate.index(item)]>winnervote):
		winnervote=votes_candidate[candidate.index(item)]
		winner=item
print("-------------------------")
print("Winner:\t" + winner)
print("-------------------------\n")

#Intializing the output path
filename=os.path.join("Output","output.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(filename, 'w') as fileobject:
    fileobject.write("Election Results" + "\n")
    fileobject.write("-------------------------" + "\n")
    fileobject.write("Total Votes:" + str(total) + "\n")
    fileobject.write("-------------------------" + "\n")
    for item in candidate:
    	fileobject.write("{:<14s}".format(item) + ":  " + "{:2.2f}".format(round(votes_candidate[candidate.index(item)]*100/total,2)) + "% (" + "{:<}".format(votes_candidate[candidate.index(item)]) + ")\n")
    fileobject.write("-------------------------" + "\n")
    fileobject.write("Winner:\t" + winner + "\n")
    fileobject.write("-------------------------" + "\n")

 #End of project