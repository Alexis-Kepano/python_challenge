#import modules
import os
import csv
#input
csvpath=os.path.join('Resources', 'election_data.csv')
#output
outfile = os.path.join('Analysis', 'pypoll.txt')

with open(csvpath) as csvfile:
    header = csvfile.readline()
    rows = csv.reader(csvfile)

for i in csvreader:
    voterid = i[0]
    county = i[1]
    candidate = i[2] 

 #declare variables   
totalvotes = 0; kvotes = 0; ccount = 0; lcount = 0; ocount = 0; maxvotecount = 0

 #Total Vote Count
totalcount = totalcount + 1

#OR total vote count
totalcount = (len(votes))
print(totalcount)

#votes by candidate
for candidate in candidates:
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



