import os
import csv

from collections import Counter

csvpath = os.path.join('Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    totalVotes = 0

    candidates = []
    candidateVotes = {}

    for row in csvreader:
        totalVotes += 1

        candidate = row[2]

        if(candidate in candidates):
            candidateVotes[candidate] += 1
        else:
            candidates.append(candidate)
            candidateVotes[candidate] = 1


winner = ""
winningVote = 0

outputPath = os.path.join("analysis/output.txt")

with open(outputPath, "w", newline='') as datafile:

    print(f"Election Results")
    datafile.writelines(f"Election Results\n")
    print(f"---------------------")
    datafile.writelines(f"---------------------\n")

    for c in candidates:
        votes = candidateVotes.get(c)

        if(votes > winningVote):
            winner = c
            winningVote = votes

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
