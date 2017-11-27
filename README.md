### Python- Challenges
Project: Python Challenge

This project consist of 4 sub-divisions as mentioned below.

## Project 1: PyBank

In this challenge, we create a Python script for analyzing the financial records of a company. We have two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`) given. Each dataset is composed of two columns: `Date` and `Revenue`. 

This Python script analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The total amount of revenue gained over the entire period

* The average change in revenue between months over the entire period

* The greatest increase in revenue (date and amount) over the entire period

* The greatest decrease in revenue (date and amount) over the entire period

The analysis should looks similar to the one below:

```
Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
```

In addition, our final script prints the analysis to both the terminal and exports a text file with the results.

## Project 2: PyPoll

In this challenge, we are tasked with helping a small, rural town modernize its vote-counting process. 

We are given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The Python script analyzes the votes and calculates each of the following combining both the poll data file:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

Our analysis looks similar to the one below:

```
Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
```

In addition, our final script prints the analysis to both the terminal and exports a text file with the results.

## Project 3: PyBoss

In this challenge, the Python script bridges the gap converting employee records to the desired format. The script does the following formatting changes.

* Imports the `employee_data1.csv` and `employee_data2.csv` files, which currently holds employee records like the below:

```
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then converts and exports the data to use the following format instead:

```
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

* In summary, the required conversions are as follows:

  * The `Name` column should be split into separate `First Name` and `Last Name` columns.

  * The `DOB` data should be re-written into `DD/MM/YYYY` format.

  * The `SSN` data should be re-written such that the first five numbers are hidden from view.

  * The `State` data should be re-written as simple two-letter abbreviations.


## Option 4: PyParagraph

In this challenge, the Python script is responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. 

The Python script automatically analyses the paragraphs based on certain metrics. The script does the following:

* Imports a text file filled with a paragraph of your choosing.

* Assess the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

Our analysis looks similar to the one below:

```
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.56557377049
Average Sentence Length: 24.4
```

In addition, our final script prints the analysis to both the terminal and exports a text file with the results.

