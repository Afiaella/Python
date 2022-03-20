import os
import csv
months_count = 0
profit_Loss_sum = 0
profit_loss_change = 0
months_change = []
prev_profit_loss = 0
profit_loss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

csvpath = os.path.join("Resources", "budget_data.csv")
# print(os.path.abspath(csvpath))
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    months_count += 1
    profit_Loss_sum += int(first_row[1])
    prev_profit_loss = int(first_row[1]) 

    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        months_count += 1
        profit_Loss_sum += int(row[1])

     
#Calculate net profit loss and profit loss change
    
    profit_loss_change = int(row[1]) - prev_profit_loss
    prev_profit_loss = int(row[1])
    profit_loss_change_list += [profit_loss_change]
    months_change += (row[0])

    #Calculate greatest increase and decrease

if(profit_loss_change > greatest_increase[1]):
        greatest_increase[0] = row[0]
        greatest_increase[1] = profit_loss_change

if(profit_loss_change < greatest_decrease[1]):
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = profit_loss_change 

#Analysis Output 

finaloutput = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_count}\n"
    f"Total: ${profit_Loss_sum}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


# Print the output (to terminal)
print(finaloutput)