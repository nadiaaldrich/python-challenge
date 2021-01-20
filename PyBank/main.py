import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
#Open and read csv
with open(csvpath) as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    print(csv_reader)

    #Read the header row first 
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

#Create lists to store months and profit 
months = []
profit = []

#Read through each row of data after the header 
for row in csv_reader: 
    print(csv_reader)
    
    months.append(row[1])
    profit.append(int(row[1]))

    total_months = len(months)
    print (f"Total Months: {total_months}")

    #add to get revenues
    revenues = 0
    i = 1
   for i in range(total):
        revenues = revenues + int(profit[i])
    print(f"Total: ${revenues}")

    #find average change
    average_change = []
    j = 0
    k = 0

    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profit[j])-int(profit[k]))
            k += 1

    #add monthly changes and divide by total months 
    average_month = ((sum(change))/(len(change)))
    print(f"Average Change: ${round((average_month), 2)}")

#greatest increase and decrease in profits 
    max_change = max(change)
    print(f"${max_change}")

    min_change = min(change)
    print(f"${min_change")

    max_change = max(change)
    print(f"Greatest Increase in Profits: ${max_change}")

    min_change = min(change)
    print(f"Greatest Decrese in Profits: ${min_change}")




