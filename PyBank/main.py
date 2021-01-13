
import os 
import csv

#variables
total_months = 0  
net_profits = 0
monthly_change = []
month_list = []
max_increase = 0
max_month_increase = 0
max_decrease = 0
max_month_decrease = 0


#csv path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#open and read
with open (csvpath, newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #take out header so dataset is only info we need
    next(csvreader)

    #make row variable filter through each line in dataset
    row = next(csvreader)

    #calculating variables from above/   #setting up max variables so it knows which column to pull from
    total_months += 1
    net_profits += int(row[1])
    max_increase = int(row[1])
    max_month_increase = row[0]
    previous_row = int(row[1])

    for row in csvreader:

        total_months += 1
        net_profits += int(row[1])
        
        

        #set up variables for change from current month to previous month
        profit_change = int(row[1]) - previous_row
        #inputting profit numbers from row 1 into list called monthly change
        monthly_change.append(profit_change)
        #set up previous month to calculate changes month by month
        previous_row = int(row[1])
        #inputting dates from row 0 into a list called monthlist
        month_list.append(row[0])

        #calculate max increase with if statement
        if int(row[1]) > max_increase:
            max_increase = int(row[1])
            max_month_increase = row[0]

        #calculate max decrease with inverse if statement from above
        if int(row[1]) < max_decrease:
            max_decrease = int(row[1])
            max_month_decrease = row[0]


    #find average change per month
    avg_change = sum(monthly_change)/len(monthly_change)

    #max and min change per month (most and least)
    highest = max(monthly_change)
    lowest = min(monthly_change)


        
    


#msg and input to start script
print("Hey there!")

run_script = input("Would you like to run the script to see the Financial Analysis: (y)es or (n)o?")

if run_script =="y":

    print("Financial Analysis")
    print("------------------------------------")
    print(f'Total Months: {total_months} ')
    print(f'Total: ${net_profits}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_month_increase}, (${highest})')
    print(f'Greatest Decrease in Profits: {max_month_decrease}, (${lowest})')




#output
output_file = os.path.join('..', 'Analysis.txt' )

#open output
with open(output_file, 'w') as textfile:

    #write out analysis from above
    textfile.write("Financial Analysis\n")
    textfile.write("------------------------------------\n")
    textfile.write(f'Total Months: {total_months} \n')
    textfile.write(f'Total: ${net_profits}\n')
    textfile.write(f'Average Change: ${avg_change:.2f}\n')
    textfile.write(f'Greatest Increase in Profits: {max_month_increase}, (${highest})\n')
    textfile.write(f'Greatest Decrease in Profits: {max_month_decrease}, (${lowest})\n')

