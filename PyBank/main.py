#Importing the modules
import os
import csv
import datetime


budget_files=['2','1']
number_of_months=0
total_revenue=0
months=[]
month_revenue=[]
allowed_date_format=['%MMM-%YY','%MMM-%YYYY']

for filenumber in budget_files:
	#Creating the path of input files
	csvpath=os.path.join('Resources', 'budget_data_'+filenumber+'.csv')
	with open(csvpath) as csvfile:
		csvreader=csv.reader(csvfile,delimiter=',')
		next(csvreader,None)
		for row in csvreader:
			for format in allowed_date_format:
				
			#if row[0]datetime.datetime.strptime(row[2], "%Y-%m-%d").strftime("%d/%m/%Y")
			if date not in months:
				months.append(date)
				index=months.index(date)
				month_revenue.insert(index,row[1])
				number_of_months=number_of_months+1
			else:
				index=months.index(date)
				monthlyrevenue=month_revenue[index]+row[1]
				month_revenue.insert(index,monthlyrevenue)
			total_revenue=total_revenue+int(row[1])

print("\n\nFinancial Analysis")
print("-----------------------")
print("Total Months: " + str(number_of_months))
print("Total Revenue: " + str(total_revenue))
for item in months:
	print(item)

