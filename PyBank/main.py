#Importing os module
import os

#Module for reading csv files
import csv

#Path to collect bank data
bank_csv = os.path.join("..", "PyBank", "budget_data.csv")

def print_data(bankData):
    date = str(bankData[0])
    profit = int(bankData[1])

    print(f"{date} {profit}")


#Open and read the csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #Read the header row first
    header = next(csvfile)
    print(f"Header: {header}")

    for row in csvreader:
        print_data(row)

print("")
print("Financial Analysis")
print("------------------")
print(f"Total Months: ")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")
    