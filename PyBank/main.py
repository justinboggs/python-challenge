#Importing os module
import os

#Module for reading csv files
import csv

#Path to collect bank data
bank_csv = os.path.join("budget_data.csv")

date = []
profit = []

#Open and read the csv
with open(bank_csv, newline="") as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")
    #Set the header row
    header = next(csvfile)
    
    for row in csvreader:       
        date.append(row[0])
        profit.append(int(row[1]))
        change = [profit[i+1] - profit[i] for i in range(len(profit)-1)]

#Define variables
total_months = len(date)
total_profit = sum(profit)
total_change = round(sum(change) / len(change),2)
max_change = max(change)
min_change = min(change)

output = os.path.join("bank_output.txt")

with open(output, "w") as writefile:
    writefile.writelines("Financial Analysis\n")
    writefile.writelines("------------------\n")
    writefile.writelines(f"Total Months: {str(total_months)}\n")
    writefile.writelines(f"Total: $ {str(total_profit)}\n")
    writefile.writelines(f"Average Change: $ {str(total_change)}\n")
    writefile.writelines(f"Greatest Increase in Profits: {str(max_change)}\n")
    writefile.writelines(f"Greatest Decrease in Profits: {str(min_change)}")

with open(output, "r") as readfile:
        print(readfile.read())
        
