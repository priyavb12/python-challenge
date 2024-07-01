import os
import csv


#analysis_csv = os.path.join('.','resources','budget_data.csv')
INPUT_PATH = os.path.join('resources','budget_data.csv')


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(INPUT_PATH, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #print(csvreader)
    for row in csvreader:
        print(row)
    #header = next(csvreader)

total_months = len(data)
total_profit_losses = sum(data.values())

#print(f"Total number of months: {total_months}")
#print(f"Total Profit/Losses: ${total_profit_losses}")

changes = []
previous_value = None

for month, value in data.items():
    if previous_value is not None:
        change = value - previous_value
        changes.append(change)
    previous_value = value

# Calculate average of changes
average_change = sum(changes) / len(changes)

#print(f"Changes in Profit/Losses over the entire period: {changes}")
#print(f"Average of changes: ${average_change:.2f}")

max_increase = 0
max_increase_month = ""
max_decrease = 0
max_decrease_month = ""
previous_value = None

for month, value in data.items():
    if previous_value is not None:
        change = value - previous_value
        if change > max_increase:
            max_increase = change
            max_increase_month = month
        if change < max_decrease:
            max_decrease = change
            max_decrease_month = month
    previous_value = value

analysis = (
    f"Total number of months: {total_months}\n"
    f"Total Profit/Losses: ${total_profit_losses}\n"
    f"Average of changes: ${average_change:.2f}\n"
    f"The greatest increase in profits occurred in {max_increase_month} with ${max_increase}"
    f"The greatest decrease in profits occurred in {max_decrease_month} with ${max_decrease}")

print(analysis)
      
    