import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(pybank) as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    

months = []
profit = []

for row in csv_reader: 
    months.append(row[1])
    profit.append9int(row[1])

    total_months = len(months)
    print (f"Total Months: {total_months"})
