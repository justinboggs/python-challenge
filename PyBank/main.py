#Importing os module
import os

#Module for reading csv files
import csv

#Path to collect bank data
bank_csv = os.path.join("..", "PyBank", "budget_data.csv")

date = []
profit = []
change = []

#Open and read the csv
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    print(f"{header}")



print("Financial Analysis")
print("------------------")
print(f"Total Months: ")
print(f"Total: ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")

