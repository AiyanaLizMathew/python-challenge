#Programe to calculate the financial records of company

#Importing the modules
import os
import csv

#Intializing the file number
budget_files=['1','2']

#Intializing the output path
filename=os.path.join("Output","output.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(filename, 'w') as fileobject:

	#For each file in the budget_files
	for filenumber in budget_files:

		no_of_months=0
		total_revenue=0
		previous_change=0
		greatest_Inc_revenue=0
		greatest_Dec_revenue=0
		Average_revenue_change=0

		#Creating a list for months and their change in revenue
		months=[]
		change_revenue=[]

		#Creating the path of input files
		csvpath=os.path.join('Resources', 'budget_data_'+filenumber+'.csv')

		with open(csvpath) as csvfile:
			csvreader=csv.reader(csvfile,delimiter=',')
			
			#Skip the first line which is the header line in all csv file
			next(csvreader,None)

			for row in csvreader:
				#Assigning the first column elements as date
				date=row[0]

				#Appending date to the months list
				months.append(date)

				#Calculating total revenue
				total_revenue=total_revenue+int(row[1])

				#Finding the index for months
				index=months.index(date)
				#Calculating the change in revenue with the previous year
				revenue_change=int(row[1])-previous_change
				#Appending the change in revenue to corresponding months using the index
				change_revenue.insert(index,revenue_change)
				
				#Intializing the previous crevenue for the next iteration
				previous_change=int(row[1])

		#Change in revenue for the first month will be 0 
		change_revenue[0]=0
		#Calculating the number of months in each budget file
		no_of_months=len(months)


		#Printing to terminal
		print("\nFinancial Analysis for Budget File "+ str(filenumber))
		print("---------------------------------------------------------------------")
		print("Number of months: " + str(len(months)))
		print("Total Revenue: $" + str(total_revenue))

		#Calculating average change in revenue
		Average_revenue_change=round(sum(change_revenue)/(len(change_revenue)-1),3)
		print("Average Revenue Change: $"+ str(Average_revenue_change))

		#Finding greatest Increase in revenue
		greatest_Inc_revenue=max(change_revenue)
		month_Greatest_Inc_revenue=months[change_revenue.index(greatest_Inc_revenue)]
		print("Greatest Increase in Revenue: " + month_Greatest_Inc_revenue + "($" + str(greatest_Inc_revenue)+")")

		#Finding the greatest Decrease in revenue
		greatest_Dec_revenue=min(change_revenue)
		month_Greatest_Dec_revenue=months[change_revenue.index(greatest_Dec_revenue)]
		print("Greatest Derease in Revenue: " + month_Greatest_Dec_revenue + "($" + str(greatest_Dec_revenue)+")")


		#Writing the financial analysis results to the output file
		fileobject.write("\nFinancial Analysis for Budget File "+ str(filenumber) + "\n")
		fileobject.write("---------------------------------------------------------------------" + "\n")
		fileobject.write("Number of months: " + str(len(months)) + "\n")
		fileobject.write("Total Revenue: $" + str(total_revenue) + "\n")
		fileobject.write("Average Revenue Change: $"+ str(Average_revenue_change) + "\n")
		fileobject.write("Greatest Increase in Revenue: " + month_Greatest_Inc_revenue + "($" + str(greatest_Inc_revenue)+")" + "\n")
		fileobject.write("Greatest Derease in Revenue: " + month_Greatest_Dec_revenue + "($" + str(greatest_Dec_revenue)+")" + "\n")

 #End of project