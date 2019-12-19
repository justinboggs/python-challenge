#Importing os module
import os

#Module for reading csv files
import csv

#Path to collect bank data
bank_csv = os.path.join("budget_data.csv")

date = []
profit = []
change = []

#Open and read the csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    
    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))

total_months = len(date)
total_profit = sum(profit)

print("Financial Analysis")
print("------------------")
print(f"Total Months: " + str(total_months))
print(f"Total: $" + str(total_profit))
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")