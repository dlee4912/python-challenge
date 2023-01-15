import os
import csv

# Read in the source dataset
csvpath = os.path.join('Resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    # Create variables for total months and PL
    months = 0
    totalProfitLoss = 0 

    # Variables to store changes between months
    lastRowPL = 0
    totalMonthlyChanges = 0

    # Varaibles for the greatest increase and decrease
    greatestInc = 0
    greatestIncDate = ""
    greatestDec = 0
    greatestDecDate = ""

    # Iterate through each row of the csv
    for row in csvreader:

        # Store the date and PL
        plDate = row[0]
        pl = int(row[1])

        # Calculate total PL and add it to the total
        totalProfitLoss += pl
        
        # Compare the change between the last and current month's PL
        monthlyDiff = pl - lastRowPL

        # Update greatest increase/decrease values
        if(monthlyDiff > greatestInc):
            greatestInc = monthlyDiff
            greatestIncDate = plDate

        if(monthlyDiff < greatestDec):
            greatestDec = monthlyDiff
            greatestDecDate = plDate

        # Store the value of the current row for the next iteration
        lastRowPL = pl

        # Skip the first month's value because there is no previous month to compare the change
        if(months > 0):
            totalMonthlyChanges += monthlyDiff
        
        # Increment the month
        months += 1

# Calculate the average change in PL. One less month for the total because we skipped the first month. Round to 2 decimals.
netPLavg = round(float(totalMonthlyChanges)/(months-1), 2)

# Set the output path
outputPath = os.path.join("analysis/output.txt")

with open(outputPath, "w", newline='') as datafile:
    # Write all the lines to the text file
    datafile.writelines("Financial Analysis\n")

    datafile.writelines("---------------------\n")

    datafile.writelines(f"Total Months: {months}\n")
    datafile.writelines(f"Total: ${totalProfitLoss}\n")
    datafile.writelines(f"Average Change: ${netPLavg}\n")
    datafile.writelines(f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})\n")
    datafile.writelines(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})\n")

    # Close the output file
    datafile.close()

    # Print results to the console
    print(f"Financial Analysis")

    print(f"---------------------")

    print(f"Total Months: {months}")
    print(f"Total: ${totalProfitLoss}")
    print(f"Average Change: ${netPLavg}")
    print(f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})")
    print(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})")