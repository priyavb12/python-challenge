import os, csv

#filePath = os.path.join('Resources', 'election_data.csv')#import csv block of code

filePath = "C:\\Users\\nprab\\OneDrive\\Desktop\\repos\\python-challenge\\PyPoll\\resources\\election_data.csv"
with open(filePath) as csvfile:#open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader
    csv_header = next(csvreader) #skipping the header so we get the correct count of rows
    initialCandidateList, electionResults = ["Khan", "Correy", "Li", "O'Tooley"], [] #populating list with the initial known candidates. creating new empty list for electionResults.
    #storing the list of candidate names in a dictionary so I can map vote count to candidate. starting all candidates at 0 votes
    candidates = { initialCandidateList[0]:0, initialCandidateList[1]:0, initialCandidateList[2]:0, initialCandidateList[3]:0 }
    rowCounter = 0

    for row in csvreader:#Read each row of data after the header
        rowCounter+=1 #keep track of number of rows since each row is a vote
        #if the candidate is not already in initialCandidateList (is a candidate which has not recieved a vote yet) then append this candidate to the list
        if row[2] not in initialCandidateList:
            initialCandidateList.append(row[2])
        if row[2] == initialCandidateList[0]:#if the CSV "Candidate" column for this row matches one of our candidates, give that candidate a vote
            candidates[initialCandidateList[0]]+=1
        elif row[2] == initialCandidateList[1]:
            candidates[initialCandidateList[1]]+=1
        elif row[2] == initialCandidateList[2]:
            candidates[initialCandidateList[2]]+=1
        elif row[2] == initialCandidateList[3]:
            candidates[initialCandidateList[3]]+=1

    print(f"Election Results\n-------------------------\nTotal Votes: {rowCounter}\n-------------------------")#each row is a vote so row count is equal to the number of votes

    def GenerateResults():#using a function so I can both write to a file and print the results to terminal without having to repeat my code
        #with dictionaries you cannot look up a key by a value, so using a for loop to map the key and value pairs of the dictionary together 
        #to allow searching in the opposite direction (searching for a key by a known value)
        for candidateName, voteCount in candidates.items():
            #store the candidate name, the percent of the total votes that candidate received, and the actual number of votes that candidate received
            electionResults.append((f"{candidateName}: {round((voteCount/rowCounter)*100, 1)}% ({voteCount})"))
            if voteCount == max(candidates[initialCandidateList[0]], candidates[initialCandidateList[1]], candidates[initialCandidateList[2]], candidates[initialCandidateList[3]]):
                winningCandidate = candidateName #creating a variable to keep track of the winner so I can print that data when I'm outside the for loop
        #return the results of the election for all the candidates and list the winner.
        return (f"{electionResults[0]}\n{electionResults[1]}\n{electionResults[2]}\n{electionResults[3]}\n-------------------------\nWinner: {winningCandidate}\n-------------------------")

def OutputResults(resultType):#function to print the results to terminal or export the results to a text file
    if (resultType == "print"):#print results to terminal
        print(GenerateResults())
    elif(resultType == "file"):#export the same information to a text file
        #output_path = os.path.join("output", "pollResults.txt")

        output_path = "C:\\Users\\nprab\\OneDrive\\Desktop\\repos\\python-challenge\\PyPoll\\analysis\\electionresults.txt"
        with open(output_path, 'w') as txtFile:
            txtFile.write(GenerateResults())
           # txtFile.write(f"Total Months: {rowCounter}\nTotal: ${total}\nAverage Change: ${avgChange}\nGreatest Increase in Profits: {maxIncreaseMonth} (${maxIncreaseAmount})\nGreatest Decrease in Profits: {minIncreaseMonth} (${minIncreaseAmount})")

OutputResults("print")
OutputResults("file")