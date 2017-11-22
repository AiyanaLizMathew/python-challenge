#Importing the modules
import os
import csv
import sys
#Filepath for the us state abbrev library
us_filepath=os.path.join("library")
sys.path.append(us_filepath)
import us_state_abbrev
#Import to change format of date and time
import datetime

#Intializing the file names to loop
employee_data_files=['1','2']

#Intializing the output path name
outputfilename=os.path.join("Output","output.csv")

#Open the file using "write" mode
with open(outputfilename, 'w', newline='') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=',')
	#Writing the first row of the output file
	csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

	for filenumber in employee_data_files:
		#Creating the path of input files
		csvpath=os.path.join('Resources', 'employee_data'+filenumber+'.csv')
		with open(csvpath) as csvfile:
			csvreader=csv.reader(csvfile,delimiter=',')
			#Skip the header 
			next(csvreader,None)
			for row in csvreader:
				FirstName,LastName=row[1].split(" ")
				DOB=datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%d/%m/%Y")
				last4SSN=row[3][-4:]
				newSSN="***-**-"+str(last4SSN)
				csvwriter.writerow([row[0],FirstName,LastName,DOB,newSSN,us_state_abbrev.us_state_abbrev[row[4]]])
#End of program