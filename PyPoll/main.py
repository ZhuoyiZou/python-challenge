# Import modules 
import csv
import os
import numpy as np


# Select the csv file through directory 
pypoll_data = os.path.join(".", "PyPoll_Resources_election_data.csv") 


voter_id = []
county = []
candidates = []
# Read the csv file 
with open (pypoll_data, newline = "") as csvfile:
    pypoll_data_reader = csv.reader(csvfile, delimiter = ",")
    for row in pypoll_data_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

        
# Calculate the number of votes.
total_votes = len(voter_id) - 1


# To detect how many candidates do we have
candidate_names = []
for i in range(len(candidates)):
    if candidates[i] != candidates[i-1] and candidates[i] not in candidate_names:
        candidate_names.append(candidates[i])

        
# The number of votes each candidate won 
number_of_vote_candidate_1 = 0
number_of_vote_candidate_2 = 0
number_of_vote_candidate_3 = 0
number_of_vote_candidate_4 = 0
for i in candidates:
    if i == candidate_names[1]:
        number_of_vote_candidate_1 = number_of_vote_candidate_1 + 1
    elif i == candidate_names[2]:
        number_of_vote_candidate_2 = number_of_vote_candidate_2 + 1
    elif i == candidate_names[3]:
        number_of_vote_candidate_3 = number_of_vote_candidate_3 + 1
    elif i == candidate_names[4]:
        number_of_vote_candidate_4 = number_of_vote_candidate_4 + 1

        
# The percentage of votes each candidate won
percentage_of_vote_candidate_1 = format((number_of_vote_candidate_1/total_votes) * 100, '.3f')
percentage_of_vote_candidate_2 = format((number_of_vote_candidate_2/total_votes) * 100, '.3f')
percentage_of_vote_candidate_3 = format((number_of_vote_candidate_3/total_votes) * 100, '.3f')
percentage_of_vote_candidate_4 = format((number_of_vote_candidate_4/total_votes) * 100, '.3f')


# Find the winner candidate
if number_of_vote_candidate_1 > number_of_vote_candidate_2 and \
number_of_vote_candidate_1 > number_of_vote_candidate_3 and \
number_of_vote_candidate_1 > number_of_vote_candidate_4:
    winner = candidate_names[1]
elif number_of_vote_candidate_2 > number_of_vote_candidate_1 and \
number_of_vote_candidate_2 > number_of_vote_candidate_3 and \
number_of_vote_candidate_2 > number_of_vote_candidate_4:
    winner = candidate_names[2]
elif number_of_vote_candidate_3 > number_of_vote_candidate_1 and \
number_of_vote_candidate_3 > number_of_vote_candidate_2 and \
number_of_vote_candidate_3 > number_of_vote_candidate_4:
    winner = candidate_names[3]
else: winner = candidate_names[4]
    

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {total_votes}")
print("-------------------------")
print(f"{candidate_names[1]}: {percentage_of_vote_candidate_1}% ({number_of_vote_candidate_1})")
print(f"{candidate_names[2]}: {percentage_of_vote_candidate_2}% ({number_of_vote_candidate_2})")
print(f"{candidate_names[3]}: {percentage_of_vote_candidate_3}% ({number_of_vote_candidate_3})")
print(f"{candidate_names[4]}: {percentage_of_vote_candidate_4}% ({number_of_vote_candidate_4})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")