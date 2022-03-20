import os
import csv

#Read CSV file

csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
    
    #Set counter to 0

    total_number_votes = 0

    list_candidates = []
    total_votes_candidates = {}
    winner = ""
    winner_count = 0



    for row in csvreader:
        print(". ", end=""),

        total_number_votes = total_number_votes + 1

        candidate = row[2] 
        if candidate not in list_candidates:
            list_candidates.append(candidate)
            total_votes_candidates[candidate] = 0
            total_votes_candidates[candidate] = total_votes_candidates[candidate] + 1


final_output = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_number_votes}\n"
        f"-------------------------\n") 
print(final_output, end="")
