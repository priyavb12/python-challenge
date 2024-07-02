import os
import csv


#analysis_csv = os.path.join('.','resources','budget_data.csv')
csv_path = os.path.join('resources','budget_data.csv')
OUTPUT_PATH = os.path.join('analysis','output.txt')
total_months  = 0
monthly_change=[]
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999]
net_total = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csv_path, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    #next(csvreader)
    #print(csvreader)
  
    header = next(csvreader)
    first_row = header
    prev_net = int(csvreader[0][1])

    for row in csvreader:

        total_months +=1
        net_total += row[1]

        net_change = row[1] - prev_net
        prev_net = int(row[1]) # update the new prev net
        net_change_list += [net_change]
        monthly_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


# total_profit_losses = sum(INPUT_PATH.values())

print(f"Total number of months: {total_months}")


average_change = sum(net_change_list) / len(net_change_list)
print(average_change)

# Print the results
# print("Financial Analysis")
# print("----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${net_total}")
# print(f"Average Change: ${average_change:.2f}")
# print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
# print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# # Export the results to a text file
# with open('financial_analysis.txt', 'w') as output_file:
#     output_file.write("Financial Analysis\n")
#     output_file.write("----------------------------\n")
#     output_file.write(f"Total Months: {total_months}\n")
#     output_file.write(f"Total: ${net_total}\n")
#     output_file.write(f"Average Change: ${average_change:.2f}\n")
#     output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
#     output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")




           















total_months = len(csv_path)
# total_profit_losses = sum(INPUT_PATH.values())

print(f"Total number of months: {total_months}")
# #print(f"Total Profit/Losses: ${total_profit_losses}")

# changes = []
# previous_value = None

# for month, value in data.items():
#     if previous_value is not None:
#         change = value - previous_value
#         changes.append(change)
#     previous_value = value

# # Calculate average of changes
# average_change = sum(changes) / len(changes)

# #print(f"Changes in Profit/Losses over the entire period: {changes}")
# #print(f"Average of changes: ${average_change:.2f}")

# max_increase = 0
# max_increase_month = ""
# max_decrease = 0
# max_decrease_month = ""
# previous_value = None

# for month, value in data.items():
#     if previous_value is not None:
#         change = value - previous_value
#         if change > max_increase:
#             max_increase = change
#             max_increase_month = month
#         if change < max_decrease:
#             max_decrease = change
#             max_decrease_month = month
#     previous_value = value

# analysis = (
#     f"Total number of months: {total_months}\n"
#     f"Total Profit/Losses: ${total_profit_losses}\n"
#     f"Average of changes: ${average_change:.2f}\n"
#     f"The greatest increase in profits occurred in {max_increase_month} with ${max_increase}"
#     f"The greatest decrease in profits occurred in {max_decrease_month} with ${max_decrease}")
# analysis = "test" 

# with open(OUTPUT_PATH,'w') as output_file:
#     output_file.write(analysis) 
# print(analysis)

      
    