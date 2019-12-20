#import os module
import os

#import csv module
import csv

#path to collect bank data
bank_csv = os.path.join("budget_data.csv")

#create variables for data in csv file
date = []
profit = []

#open and read the csv
with open(bank_csv, newline="") as csv_file:
    #split the data on commas
    csv_in = csv.reader(csv_file, delimiter=",")
    #Set the header row
    header = next(csv_file)
    
    #loop through file and assign data to the proper variables based on columns
    for row in csv_in:       
        date.append(row[0])
        #set profit to an integer
        profit.append(int(row[1]))
        #define the monthly change variable and set its placement
        change = [profit[i+1] - profit[i] for i in range(len(profit)-1)]

#define total months
total_months = len(date)
#define total profit
total_profit = sum(profit)
#define average change
avg_change = round(sum(change) / len(change),2)
#define max monthly change
max_change = max(change)
#find month corresponding to max monthly change
max_month = date[change.index(max_change)+1]
#define min monthly change
min_change = min(change)
#find month corresponding to min monthly change
min_month = date[change.index(min_change)+1]

#path and file name to save data
output = os.path.join("budget_output.txt")

#Print and save the output to a .txt file
with open(output, "w") as csv_out:
    csv_out.write(" \n")
    csv_out.write("Financial Analysis\n")
    csv_out.write("------------------\n")
    csv_out.write(f"Total Months: {str(total_months)}\n")
    csv_out.write(f"Total: $ {str(total_profit)}\n")
    csv_out.write(f"Average Change: $ {str(avg_change)}\n")
    csv_out.write(f"Greatest Increase in Profits: {max_month} ${str(max_change)}\n")
    csv_out.write(f"Greatest Decrease in Profits: {min_month} ${str(min_change)}\n")
    csv_out.write(" ")

#Print the output to the terminal
with open(output, "r") as csv_read:
        print(csv_read.read())