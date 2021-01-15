#import modules
import os
import csv
#input
csvpath = os.path.join('Resources', 'budget_data.csv')
#output
outfile = os.path.join('Analysis', 'pybankstatements.txt')

#declare variables
months = []; total_m = 1; net_total = 0; total_change = 0; monthly_changes = []; greatest_inc = ['', 0]; greatest_dec = ['', 0]

#open & read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    net_total = int(first_row[1])

#loop
    for row in csvreader:

        net_total += int(row[1])
        total_m = total_m+1
        current_value = int(row[1])
        
        change_value = int(current_value-previous_row)

        monthly_changes.append(change_value)
        months.append(row[0])
        previous_row = int(row[1])

        total_change = total_change + change_value 
        if change_value > greatest_inc[1]:
           greatest_inc[0] = str(row[0])
           greatest_inc[1] = change_value


        if change_value < greatest_dec[1]:
           greatest_dec[0] = str(row[0])
           greatest_dec[1] = change_value
		
    
        avg_change = total_change/len(months)
   
output = (
   f"\n Financial Analysis \n"
   f"------------------------------\n"
   f"Total Months: {total_m}\n"
   f"Total: ${net_total}\n"
   f"Average  Change: ${avg_change:.2f}\n"
   f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
   f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")

with open(outfile, "w") as txt_file:
   txt_file.write(output)  

   outfile   