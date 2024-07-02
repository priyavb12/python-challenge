import os, csv

def CalculateChange(startingValue, endingValue):
    return (endingValue - startingValue) #calculating the difference between the ending value and the starting value


filePath = "C:\\Users\\nprab\\Downloads\\Starter_Code (2)\\Starter_Code\\PyBank\\Resources\\budget_data.csv"

#filePath = os.path.join('resources', 'budget_data.csv')#import csv block of code

with open(filePath) as csvfile: #open the path to the CSV file as a new object
    csvreader = csv.reader(csvfile, delimiter=',') #pass the csvfile object to a new variable, csvreader
    csv_header = next(csvreader) #skipping the header so we get the correct count of rows
    print("Financial Analysis")
    print("----------------------------")
    rowCounter, total, avgChange, maxIncreaseAmount, maxIncreaseMonth, minIncreaseAmount, minIncreaseMonth  = 0, 0, 0, 0, 0, 0, 0
    monthlyValues = [] #declaring empty list to keep track of individual monthly profit/loss values from the CSV
    monthlyChangeAmount = [] #declaring empty list to keep track of the change in profit/loss across each month
    monthlyChangeMonth = [] #declaring empty list to keep track of the month corresponding to the amount of the change in profit/loss

    for row in csvreader:#Read each row of data after the header
        monthlyValues.append(row[1]) #appending value of Profit/Loss column of the CSV to the monthlyValues list
        total += int((row[1])) #calculating total amount of profit/loss over the entire period
        #passing two values to CalculateChange function. the first parameter, startingValue, will be equal to the previous value of the iterator of the loop 
        #which would be the current position in the list monthlyValues - 1. the second parameter, endingValue, will be equal to the current value of the 
        # iterator of the loop. this value is then added to my empty list titled "monthlyChangeAmount"
        monthlyChangeAmount.append(CalculateChange(int(monthlyValues[rowCounter-1]), int(row[1])))
        monthlyChangeMonth.append(row[0]) #keep track of the months so I can map the name of the month to the value of the change for that month
        #keeping track of the row count for two reasons: 1. to be able to get the proper index for my list 
        #and 2. to count the number of months of data (each month has its own row in the CSV) 
        rowCounter +=1 
    #calculating average by taking the sum of the list divided by the length of the list. subtracing one from the length because the value from the first iteration 
    #of the loop will be discarded since the value is zero as there is no prior value to calculate amount change to month one. rounding result to 2 decimal places.
    avgChange =  round(sum(monthlyChangeAmount) / (len(monthlyChangeAmount)-1),2) 
    maxIncreaseAmount = max(monthlyChangeAmount) #maximum value from the monthlyChangeAmount list
    minIncreaseAmount = min(monthlyChangeAmount) #minimum value from the monthlyChangeAmount list
    #getting the index of the max value from the Amounts list and using that value as the index for the Months list since they should be 
    #at the same position since they correspond to the same row in the CSV
    maxIncreaseMonth = monthlyChangeMonth[monthlyChangeAmount.index(max(monthlyChangeAmount))]
    minIncreaseMonth = monthlyChangeMonth[monthlyChangeAmount.index(min(monthlyChangeAmount))]

def GenerateResults(resultType):#function to print the results to terminal or export the results to a text file
    if (resultType == "print"):#print results to terminal
        print(f"Total Months: {rowCounter}\nTotal: ${total}\nAverage Change: ${avgChange}\nGreatest Increase in Profits: {maxIncreaseMonth} (${maxIncreaseAmount})\nGreatest Decrease in Profits: {minIncreaseMonth} (${minIncreaseAmount})")
    elif(resultType == "file"):#export the same information to a text file
       
        #output_path = os.path.join("output", "financialResults.txt")
        
        output_path= "C:\\Users\\nprab\\OneDrive\\Desktop\\repos\\python-challenge\\PyBank\\analysis\\output.txt"
        with open(output_path, 'w') as txtFile:
            txtFile.write(f"Total Months: {rowCounter}\nTotal: ${total}\nAverage Change: ${avgChange}\nGreatest Increase in Profits: {maxIncreaseMonth} (${maxIncreaseAmount})\nGreatest Decrease in Profits: {minIncreaseMonth} (${minIncreaseAmount})")

GenerateResults("print")
GenerateResults("file")       