# Dependencies
import csv
import os

# 1. Assign a variable for the file to load and path 

file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# vote counter
total_votes = 0

# empty list
candidate_options = []

#empty dict
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open file
with open(file_to_load) as election_data:
    
    # read file
    file_reader = csv.reader(election_data)
    
    # read header
    headers = next(file_reader)

    # print each row in csv file
    for row in file_reader:
        total_votes += 1

        # print candidate name
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # add candidate name to candidate list
            candidate_options.append(candidate_name)


            # track candidate votes
            candidate_votes[candidate_name] = 0

        # increment candidate votes
        candidate_votes[candidate_name] += 1 

    with open(file_to_save, "w") as txt_file:

        #print final vote count
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------\n")

        print(election_results, end="")

        txt_file.write(election_results)

        # calculate vote percentage
        for candidate_name in candidate_options:
            votes = candidate_votes[candidate_name]

            vote_percent = votes / total_votes*100


            # determine winning candidate 
            if (votes>winning_count) and (vote_percent>winning_percentage):
                
                winning_count = votes
                winning_percentage = vote_percent

                winning_candidate = candidate_name

            candidate_results = ( f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
            print(candidate_results)

            txt_file.write(candidate_results)

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        txt_file.write(winning_candidate_summary)








   
        
