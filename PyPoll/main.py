##kcharlesr

#import modules
import os
import csv

#csv path -- beginning in 'JHU_Git_Repo/Python' directory
csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#read in csv file and skip header
with open(csvpath, newline='') as csvfile:        
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #Define variables and variable types
    candidates = []
    vote_count = []
    winner_count = 0
    total_votes = 0

    #Create loop to tally total vote counts and vote counts for each individual candidate
    for row in csvreader:
        total_votes += 1
        if(row[2] not in candidates):
            candidates.append(row[2])
            vote_count.append(0)
        candidateIndex = candidates.index(row[2])
        vote_count[candidateIndex] += 1

    
    #Create Loop and Print summary of results to terminal
    print(f'Election Results')
    print('-' * 25)
    print(f'Total Votes: {total_votes}')
    print('-' * 25)
    for x in range(len(candidates)):
        votePercent = round((vote_count[x]/total_votes)*100,3)
        print(f"{candidates[x]}: {votePercent}% ({vote_count[x]})")
        if (winner_count<vote_count[x]):
            winner_count = vote_count[x]
            winner = candidates[x]
    print('-' * 25)
    print(f"Winner: {winner}")
    print('-' * 25)


#Formatting and sending summary of results to summary text document
results = os.path.join('PyPoll', 'Analysis', 'Results.txt')
with open(results, 'w') as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('-' * 25 + '\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write('-' * 25 + '\n')
    for x in range(len(candidates)):
        votePercent = round((vote_count[x]/total_votes)*100,3)
        txt_file.write(str(candidates[x]) +" : " + str(votePercent) + "% ("+ str(vote_count[x]) + ")\n")
        if (winner_count<vote_count[x]):
            winner_count = vote_count[x]
            winner = candidates[x]   
    txt_file.write('-' * 25 + '\n')
    txt_file.write(f'Winner:  {winner} \n')
    txt_file.write('-' * 25 + '\n')

