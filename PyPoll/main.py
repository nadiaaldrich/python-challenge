import os 
import csv 


csvpath = os.path.join("Resources/election_data.csv")

#Open and read csv
with open(csvpath, newline="")as csvfile:
    csv_reader = (csvfile, delimiter=",")

    #Read and skip the header (first row)
    csv_header = next(csv_reader, None)




    #Create lists and variable 
    candite_list = []
    count_votes = 0

    print(f"Election Results")
    print("----------------------------------------")

    #Read through each row of data after the header
    for row in csv_reader:
