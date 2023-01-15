import os
import csv

csvpath = os.path.join('Resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)

    months = 0
    totalProfitLoss = 0

    lastRowPL = 0
    totalMonthlyChanges = 0

    greatestInc = 0
    greatestIncDate = ""
    greatestDec = 0
    greatestDecDate = ""

    for row in csvreader:

        plDate = row[0]
        pl = int(row[1])

        totalProfitLoss += pl

        monthlyDiff = pl - lastRowPL

        if(monthlyDiff > greatestInc):
            greatestInc = monthlyDiff
            greatestIncDate = plDate

        if(monthlyDiff < greatestDec):
            greatestDec = monthlyDiff
            greatestDecDate = plDate

        lastRowPL = pl

        if(months > 0):
            totalMonthlyChanges += monthlyDiff

        months += 1

    netPLavg = round(float(totalMonthlyChanges)/(months-1), 2)


outputPath = os.path.join("analysis/output.txt")

with open(outputPath, "w", newline='') as datafile:
    datafile.writelines("Financial Analysis\n")

    datafile.writelines("---------------------\n")

    datafile.writelines(f"Total Months: {months}\n")
    datafile.writelines(f"Total: ${totalProfitLoss}\n")
    datafile.writelines(f"Average Change: ${netPLavg}\n")
    datafile.writelines(f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})\n")
    datafile.writelines(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})\n")

    datafile.close()

    print(f"Financial Analysis")

    print(f"---------------------")

    print(f"Total Months: {months}")
    print(f"Total: ${totalProfitLoss}")
    print(f"Average Change: ${netPLavg}")
    print(f"Greatest Increase in Profits: {greatestIncDate} (${greatestInc})")
    print(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDec})")