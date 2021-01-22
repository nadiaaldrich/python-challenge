import os 
import csv 

#set path
csvpath = os.path.join("Resources/election_data.csv")

#Open and read csv
with open(csvpath, newline="")as csvfile:
    csv_reader = csv.reader (csvfile, delimiter=",")
    

    #Read and skip the header (first row)
    csv_header = next(csv_reader, None)



    #Create lists and variable 
    
    candidate_list = []
    count_votes = 0

    
    
    for row in csv_reader:

        if row[2] not in candidate_list:
            count_votes += 1
            candidate_list.append(row[2])
        else:
            count_votes += 1

    i = 0
    total_candidates = len(candidate_list) 
    candidate_votes = [0]*total_candidates

    for i in range(total_candidates):
        
        if row[2]==candidate_list[i]:
            candidate_votes[i]+=1

    max_vote = max(candidate_votes)
    vote_index = candidate_votes.index(max_vote)
    max_votes = max(candidate_votes)
    winner = candidate_list[vote_index]

    #Percentage breakdown for each candidate

    j = 0
    percent_of_votes = []
    for j in range(total_candidates):
        percent = round((candidate_votes[j]/count_votes)* 100, 2)
        percent_of_votes.append(percent)
        
dashes = "-------------------------"
print("Election Results")
print(dashes)
print(f"Total Votes: {count_votes}")
print(dashes)
print(f"{candidate_list}, {percent_of_votes}, {candidate_votes}")
print(dashes)
print(f"Winner: {winner}")

exportpath=("Results.txt")
with open (exportpath, "w") as textfile:
    textfile.write("Election Results")
    textfile.write(dashes)
    textfile.write(f"Total Votes: {count_votes}")
    textfile.write(dashes)
    textfile.write(f"{candidate_list}, {percent_of_votes}, {candidate_votes}")
    textfile.write(dashes)
    textfile.write(f"Winner:{winner}")


  
    