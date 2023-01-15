import os
import csv

# Specify the source data file
csvpath = os.path.join('Resources/election_data.csv')

# Open the data source
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read past the header row
    csv_header = next(csvreader)
    
    # Create a variable to store the total votes cast
    totalVotes = 0

    # Create a list to store the candidate names
    candidates = []

    # Create a dictionary to store the candidate names and votes
    candidateVotes = {}

    # Iterate through each row
    for row in csvreader:
        # Increment the total vote value
        totalVotes += 1

        # Store the candidate value in a vairable
        candidate = row[2]

        # Check if the candidate is in the list of candidates
        if(candidate in candidates):
            # If so, find them in the dictionary and increment their total votes by 1
            candidateVotes[candidate] += 1
        else:
            # If not, add the candidate to the list of candidates and add them to the dictionary with a vote of 1
            candidates.append(candidate)
            candidateVotes[candidate] = 1

# Create a varaible to store the winner and top vote count
winner = ""
winningVote = 0

# Create the output file path
outputPath = os.path.join("analysis/output.txt")

with open(outputPath, "w", newline='') as datafile:

    # Print the results to the console and write them to the file at the same time
    print(f"Election Results")
    datafile.writelines(f"Election Results\n")

    print(f"---------------------")
    datafile.writelines(f"---------------------\n")

    # For each candidate in the list, find how many votes they got to list
    for c in candidates:
        votes = candidateVotes.get(c)
        
        # Calculate the winner of the votes
        if(votes > winningVote):
            winner = c
            winningVote = votes

        # Calculate the % of total votes a candidate received and round to 3 decimals
        votePer = round((votes / totalVotes)*100, 3)

        print(f"{c}: {votePer}% ({votes})")
        datafile.writelines(f"{c}: {votePer}% ({votes})\n")

    print(f"---------------------")
    datafile.writelines(f"---------------------\n")
    print(f"Winner: {winner}")
    datafile.writelines(f"Winner: {winner}\n")
    print(f"---------------------\n")
    datafile.writelines(f"---------------------\n")

    datafile.close()
