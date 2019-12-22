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
candidate = []
num_votes = []
vote_percent = []

#set total votes equal to zero
total_votes = 0

#open and read the csv
with open(vote_csv, newline="") as csv_file:
    #split the data on commas
    csv_in = csv.reader(csv_file, delimiter=",")
    #Set the header row
    header = next(csv_file)
    
    #loop through data and count total votes
    for row in csv_in:       
        total_votes += 1
        if row[2] in polls.keys():
            polls[row[2]] = polls[row[2]] + 1
        else:
            polls[row[2]] = 1

#takes dictionary key and values and places them into lists
for j, k in polls.items():
    candidate.append(j)
    num_votes.append(k)

#calculate vote percentage 
for i in num_votes:
    vote_percent.append(round(i/total_votes*100, 1))

#zip candidates, vote total, and vote percentage into list
final_count = list(zip(candidate, num_votes, vote_percent))

#create list to hold winner
winner = []

#find the election winner by finding max vote count
for name in final_count:
    if max(num_votes) == name[1]:
        winner.append(name[0])

#declare variable for holding election winner
first_place = winner[0]

#path and file name to save data
output = os.path.join("election_results.txt")

#Print and save the output to a .txt file
with open(output, "w") as csv_out:
    csv_out.write(" \n")
    csv_out.write("Election Results\n")
    csv_out.write("------------------------\n")
    csv_out.write(f"Total Votes: {total_votes}\n")
    csv_out.write("------------------------\n")
    #Loop to print out all vote-getters from the final_count list.
    for vote_getter in final_count:
        csv_out.write(f"{vote_getter[0]}: {vote_getter[2]:.3f}% ({vote_getter[1]})\n")
    csv_out.write("------------------------\n")
    csv_out.write(f"Winner: {first_place} \n") 
    csv_out.write("------------------------\n")

#Print the output to the terminal
with open(output, "r") as csv_read:
        print(csv_read.read())