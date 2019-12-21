# python-challenge

This python challenge directory contains two python directories, PyBank and PyPoll.

# PyBank analyzes monthly bank profits.
First, it takes a .csv file containing two inputs, date and monthly profits. It calculates the month over month change by taking each month' profits and subtracting the prior months' profits. 
Next, it prints out to terminal and a .txt file named budget_output the following: total # of months, total profit, average monthly change and both the greatest increase and greatest in decrease month over month profit.

# PyPoll analyzes polling data.
First, it takes a .csv file containing three values, Voter ID, County name, and Candidate name, from a list of election data. Net, it takes a count of the number of times each candidate's name appears on ths list. This give total vote count per candidate. This vote count is then turned into a percentage by dividing it by the total number of votes. Finally, the total number of votes, vote and percentage per candidate, and the election winner are printed to terminal and to a .txt file named election_results.