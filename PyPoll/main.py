import os
import csv


#analysis_csv = os.path.join('.','resources','budget_data.csv')
INPUT_PATH = os.path.join('resources','election_data.csv')
OUTPUT_PATH = os.path.join('analysis','output.txt')


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_PATH, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #print(csvreader)

total_votes = 0
candidates = []
candidate_votes = {}

for row in csvreader:
        print(row)  
        total_votes += 1


    # Loop through each row in the dataset
   
     

        # Add candidate to the list if not already in it
        candidate = row[2]
        if candidate not in candidates:
             candidates.append(candidate)
             candidate_votes[candidate] = 0

        # Count the votes for each candidate
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Determine the winner based on the most votes
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")