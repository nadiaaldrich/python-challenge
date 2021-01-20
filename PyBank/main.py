import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
#Open and read csv
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    print(csvreader)

    #Read the header row first 
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

#Create lists to store months and profit 
#months = []
#profit = []
#Read through each row of data after the header 
for row in csv_reader: 
    print(csvreader)
    
    #months.append(row[1])
    #profit.append(int(row[1]))

    #total_months = len(months)
    #print (f"Total Months: {total_months}")

    #revenues = 0
    #i = 1
   #for i in range(total):
        #revenues = revenues + int(profit[i])
    #print(f"Total: ${revenues}")

    #average_change = []
    #j = 0
    #k = 0

    #for j in range (1, total_months):
        #if j == 0:
            #change.append(int(profit[j])-int(profit[k]))
            #k += 1



