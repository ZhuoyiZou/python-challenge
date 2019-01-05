# Import module 
import csv
import os
import numpy as np


# Select the csv file through directory 
pybank_data = os.path.join(".", "PyBank_Resources_budget_data.csv") 


column_1 = []
column_2 = []
total_amount = 0
# Read the csv file 
with open (pybank_data, newline = "") as csvfile:
    pybank_data_reader = csv.reader(csvfile, delimiter = ",")
    for row in pybank_data_reader:
        column_1.append(row[0])
        column_2.append(row[1])

        
# Calculate the number of months.
total_month = len(column_1) - 1


# Calculate the total net amount profit/loss
total_net_amount = 0
for i in column_2[1:]:
    total_net_amount = total_net_amount + int(i)

    
# Calculate the average changes 
converted_column_2 = [int(i) for i in column_2[1:]]
changes = []
for i in range(len(converted_column_2)):
    changes.append(converted_column_2[i] - converted_column_2[i-1])
average_changes = round(np.mean(changes[1:]),2)


# Find the greatest increase and greatesr decrease in profit
greatest_increase = max(changes)
greatest_decrease = min(changes)
for i in range(len(changes)):
    if changes[i] == greatest_increase:
        increase_month = i + 1
    elif changes[i] == greatest_decrease:
        decrease_month = i + 1
greatest_increase_month = column_1[increase_month]
greatest_decrease_month = column_1[decrease_month]


# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_net_amount}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
        