import os
import csv


# Set up variables
total_votes = 0
candidate_votes = {}
candidate_percentages = {}

# Read the CSV file and loop over the rows
with open('election_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Increment the total number of votes
        total_votes += 1
        
        # Increment the vote count for this candidate
        candidate = row['Candidate']
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
for candidate in candidate_votes:
    candidate_percentages[candidate] = candidate_votes[candidate] / total_votes * 100

# Determine the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")