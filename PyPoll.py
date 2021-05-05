import csv
import os

# 1. Assign a variable for the file to load and path 

file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# open and read file
with open(file_to_load) as election_data:

# ** ANALYZE HERE **

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print Header Row
    headers = next(file_reader)
    print(headers)




# open output file

    with open(file_to_save,'w') as txt_file:
        txt_file.write("Counties in the Election\n")

        txt_file.write("Arapahoe\n")
        txt_file.write("Denver\n")
        txt_file.write("Jefferson")


# 2. get candidate names





# 3. find total votes



# 4. find percentage of votes for each candidate



# 5. get vote total for each candidate 



# 6. determine which candidate won 



