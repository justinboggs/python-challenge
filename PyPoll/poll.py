#import os module
import os

#import csv module
import csv

#path to collect bank data
vote_csv = os.path.join("election_data.csv")

#create a dictionary to hold candidate name and vote count
polls = {}

#create empty lists to hold data 
total_votes = []
county = []
candidate = []
total_votes = 0

#open and read the csv
with open(vote_csv, newline="") as csv_file:
    #split the data on commas
    csv_in = csv.reader(csv_file, delimiter=",")
    #Set the header row
    header = next(csv_file)
    
    #loop through file and assign data to the proper variables based on columns
    for row in csv_in:       
        total_votes += 1
        if row[2] in polls.keys():
            polls[row[2]] = polls[row[2]] + 1
        else:
            polls[row[2]] = 1

#create empty lists for candidates and vote counts
candidates = []
num_votes = []

#takes dictionary key and values and places them into lists
for key, value in polls.items():
    candidates.append(key)
    num_votes.append(value)

#create vote percentage list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

#zip candidates, vote total, and vote percentage into list
final_count = list(zip(candidates, num_votes, vote_percent))

#create list to hold winner
winner = []

for name in final_count:
    if max(num_votes) == name[1]:
        winner.append(name[0])

top = winner[0]

#total_votes = len(voter_id)

#path and file name to save data
output = os.path.join("voter_output.txt")

#Print and save the output to a .txt file
with open(output, "w") as csv_out:
    csv_out.write(" \n")
    csv_out.write("Election Results\n")
    csv_out.write("------------------------\n")
    csv_out.write(f"Total Votes: {total_votes}\n")
    csv_out.write("------------------------\n")
    for entry in final_count:
        csv_out.write(entry[0] + ": " + str(entry[2]) + "% (" + str(entry[1]) + ")\n")
    csv_out.write("------------------------\n")
    csv_out.write(f"Winner: {top} \n") 
    csv_out.write("------------------------\n")

#Print the output to the terminal
with open(output, "r") as csv_read:
        print(csv_read.read())