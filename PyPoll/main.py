import os 
import csv

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open and read files
cvspath = os.path.join('..', 'Resources', 'election_data.csv')

with open (cvspath, newline='') as csvfile:
    csvreader =csv.reader(csvfile, delimiter = ",")

    #remove header
    next(csvreader)

    #make row variable filter through each lune in dataset
    row = next(csvreader)

    #turning dataset into lists
    for row in csvreader:

        #establishing variables 
        total_votes += 1

        #candidate's individual by using if statements
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else: 
            otooley_votes += 1
        
    #now find percentage that each candidate got
    khan_percent = khan_votes/total_votes
    correy_percent = correy_votes/total_votes
    li_percent = li_votes/total_votes
    otooley_percent = otooley_votes/total_votes

    #calculate the winner of the election by using max
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    #if statement to format winner_name
    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

    
    #print out results

    
    print(f'---------------------------')
    print(f'Election Results')
    print(f'---------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'---------------------------')
    print(f'Khan: {khan_percent:.3%} ({khan_votes})')
    print(f'Correy: {correy_percent:.3%} ({correy_votes})')
    print(f'Li: {li_percent:.3%} ({li_votes})')
    print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
    print(f'---------------------------')
    print(f'Winner: {winner_name}')
    print(f'---------------------------')


#output
output_file = os.path.join("..", "Analysis.txt")

#open output
with open(output_file, 'w') as textfile:

    textfile.write(f'---------------------------\n')
    textfile.write(f'Election Results\n')
    textfile.write(f'---------------------------\n')
    textfile.write(f'Total Votes: {total_votes}\n')
    textfile.write(f'---------------------------\n')
    textfile.write(f'Khan: {khan_percent:.3%} ({khan_votes})\n')
    textfile.write(f'Correy: {correy_percent:.3%} ({correy_votes})\n')
    textfile.write(f'Li: {li_percent:.3%} ({li_votes})\n')
    textfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    textfile.write(f'---------------------------\n')
    textfile.write(f'Winner: {winner_name}\n')
    textfile.write(f'---------------------------\n')

