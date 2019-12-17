#Importing os module
import os

#Module for reading csv files
import csv

#Path to collect bank data
bankCSV = os.path.join('..', 'PyBank', 'budget_data.csv')

#Read in the CSV file
with open(bankCSV, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    months = string.count(column[0])
    sum = sum(int(column[1].replace(',', '')) for column in csvreader)

    print(months)
    print(f"Total: $" + str(sum))

