#import modules
import os
import csv
#input
csvpath=os.path.join('Resources', 'election_data.csv')
#output
outfile = os.path.join('Analysis', 'pypoll.txt')
#declare variables   
totalvotes = 0; kvotes = 0; ccount = 0; lcount = 0; ocount = 0; maxvotecount = 0

with open(csvpath) as csvfile:
    header = csvfile.readline()
    rows = csv.reader(csvfile)

#votes by candidate
    for candidate in candidates:

        #total vote count
        totalcount = (len(votes))
        print(totalcount)

        if candidate =="Khan":
            kcount = kcount + 1
        if candidate =="Correy":
            ccount = ccount + 1
        if candidate =="Li":
            lcount = lcount + 1
        if candidate =="O'Tooley":
            ocount = ocount + 1

# Define (dictionary) list : candidate and votes
candidatevote = {"Khan": kcount,"Correy": ccount,"Li" :lcount, "O'Tooley": ocount}
# Find winner  
for candidate, value in candidatevote.items():
 if value > maxvotecount:
    maxvotecount = value
    winner = candidate

#Output
output = f"""
Election Results
-------------------------
Total Votes: {totalVotes}
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




