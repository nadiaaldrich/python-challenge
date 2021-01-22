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

        if row[2] not in candidate_list:
            count_votes += 1
            candite_list.append(row[2])
        else:
            count_votes += 1
    
    i = 0
    total_candidates = len(candidate_list)
    candidate_votes = [0]*total_candidates

    for i in range(total_candidates):
        if row[2]==candidate_list[i]:
            candidate_votes[i]+=1

    max_vote = max(candidate_votes)
    vote_index = candidate_votes.index(most_vote)
    winner = candidate_list[vote_index]

    #Percentage breakdown for each candidate

    j = 0 
    percent_of_votes = []

    for j in range(total_candidates):
        percent = round(candidate_votes[j]/count_votes * 100, 2)
        percent_of_ votes.append(percent)
    
    
