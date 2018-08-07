# Import modules
import os
import csv

# Define file path; script will be run from python-challenge
csv_path = os.path.join('.', 'PyBank', 'budget_data.csv')
output_path = os.path.join(".", 'PyBank', "output.txt")

# Initialize lists
date = []
revenue = []

with open(csv_path, newline = '', encoding = 'utf8') as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter = ',')
   
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)

    # Read each row of data after the header
    for row in csv_reader:
        date.append(row[0])
        revenue.append(int(row[1]))

# Get stats
total_months = len(date)
net_earnings = sum(revenue)
# average_change 
max_earnings = max(revenue)
max_date = date[revenue.index(max_earnings)]
min_earnings = min(revenue)
min_date = date[revenue.index(min_earnings)]

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_earnings}")
#print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_earnings})")
print(f"Greatest Increase in Profits: {min_date} (${min_earnings})")

# Write to text file
txt = open(output_path, 'w')
txt.write("Financial Analysis\n")
txt.write("----------------------------\n")
txt.write(f"Total Months: {total_months}\n")
txt.write(f"Total: ${net_earnings}\n")
# Add average change
txt.write(f"Greatest Increase in Profits: {max_date} (${max_earnings})\n")
txt.write(f"Greatest Increase in Profits: {min_date} (${min_earnings})")
txt.close()