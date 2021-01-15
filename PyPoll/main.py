#import modules
import os
import csv
#input
csvpath=os.path.join('Resources', 'election_data.csv')
#output
outfile = os.path.join('Analysis', 'pypoll.txt')

#declare variables   
totalvotes = 0; Khan_votes = 0; Correy_votes = 0; Li_votes = 0; OTooley_votes = 0; maxVotes = 0

with open(csvpath) as csvfile:
    header = csvfile.readline()
    rows = csv.reader(csvfile)

#votes by candidate
    for row in rows:

        #total vote count
        totalvotes += 1

        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            OTooley_votes += 1

# Define (dictionary) list : candidate and votes
dict_candidates_and_votes = {
    "Khan": Khan_votes,
    "Correy": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes}
# Find winner  
for candidate, votes in dict_candidates_and_votes.items():
    if votes > maxVotes:
        maxVotes = votes
        winner = candidate

#Output
output = f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Khan: {(Khan_votes/totalVotes)*100:.3f}%  ({Khan_votes})
Correy: {(Correy_votes/totalVotes)*100:.3f}% ({Correy_votes})
Li: {(Li_votes/totalVotes)*100:.3f}%  ({Li_votes})
O'Tooley: {(OTooley_votes/totalVotes)*100:.3f}% ({OTooley_votes})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(outfile, 'w') as outputFile:
    outputFile.write(output)




