import os
import csv


csvpath =  "C:\\Users\\nprab\\OneDrive\\Desktop\\repos\\python-challenge\\PyPoll\\resources\\election_data.csv"



pathout = "C:\\Users\\nprab\\OneDrive\\Desktop\\repos\\python-challenge\\PyPoll\\analysis\\electionresults.txt"



#pathout = os.path.join("Resources", "poll_analysis.txt")

#initialize variables
candidates = []
num_votes = 0
vote_counts = []


#open the file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    line = next(csvreader,None)

    #go line by line and process each vote
    for line in csvreader:

        #add to total number of votes
        num_votes = num_votes + 1

        #candidate voted for
        candidate = line[2]

        #if candidate has other votes then add to vote tally
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")

output = (
    f"Total Votes: {num_votes}\n"
    f"candidatescount: {percentages[count]}% ({vote_counts[count]}\n"
    f"Winner: {winner}\n"
    )

print(output)
with open(pathout, "w") as txt_file:
    txt_file.write(output)


with open(pathout, "w") as txt_file:
    txt_file.write(output)