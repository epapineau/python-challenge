# Import modules
import os
import csv

# Define file path; script will be run from python-challenge
csv_path = os.path.join('.', 'PyPoll', 'election_data.csv')
output_path = os.path.join(".", 'PyPoll', "output.txt")

# Initialize lists
candidate = []

with open(csv_path, newline = '', encoding = 'utf8') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter = ',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        candidate.append(row[2])

# Get stats
total_votes = len(candidate)

# Initiate dictionary to store candidates and vote count
vote_counts = {}
for i in set(candidate):
    vote_counts[i] = 0

# Count votes and determine winner
for row in candidate:
    vote_counts[row] = vote_counts[row] + 1

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in set(candidate):
    perc = round((vote_counts[i] / total_votes) * 100, 2)
    print(f"{i}: {perc}% ({vote_counts[i]})")
print("-------------------------")
print(f"Winner: {max(vote_counts, key = vote_counts.get)}")
print("-------------------------")

# Write to text file
txt = open(output_path, 'w')
txt.write("Election Results\n")
txt.write("-------------------------\n")
txt.write(f"Total Votes: {total_votes}\n")
txt.write("-------------------------\n")
for i in set(candidate):
    perc = round((vote_counts[i] / total_votes) * 100, 2)
    txt.write(f"{i}: {perc}% ({vote_counts[i]})\n")
txt.write("-------------------------\n")
txt.write(f"Winner: {max(vote_counts, key = vote_counts.get)}\n")
txt.write("-------------------------\n")
txt.close()