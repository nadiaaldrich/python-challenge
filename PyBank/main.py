import os
import csv


csvpath = os.path.join("Resources/budget_data.csv")

#Open and read csv
with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    

    #Read and skip the header (first row) 
    csv_header = next(csv_reader, None)
    


#Create lists to store months and profit 
    months = []
    profit = []
    
    print(f"Financial Analysis")
    print(f"----------------------------------------")

#Read through each row of data after the header 
    for row in csv_reader: 
    
    
        months.append(row[1])
        profit.append(int(row[1]))

    total_months = len(months)
    print (f"Total Months: {total_months}")

    #add to get revenues
    revenues = 0
    i = 1
    
    for i in range(total_months):
            revenues = revenues + int(profit[i])
    print(f"Total: ${revenues}")

    #find average change
    change = []
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
    #print(f"${max_change}")

    min_change = min(change)
   # print(f"${min_change}")

    max_change = max(change)
    print(f"Greatest Increase in Profits: ${max_change}")

    min_change = min(change)
    print(f"Greatest Decrease in Profits: ${min_change}")






exportpath = "Results.txt"
with open(exportpath, "w") as textfile:
        textfile.write(f"\nFinancial Analysis")
        textfile.write(f"\n----------------------------------------")
        textfile.write(f"\nTotal Months: {total_months} ")
        textfile.write(f"\nTotal: ${revenues}")
        textfile.write(f"\nAverage Change: ${round((average_month), 2)}")
        textfile.write(f"\nGreatest Increase in Profits: ${max_change}")
        textfile.write(f"\nGreatest Decrease in Revenues: ${min_change}")



Shortcut