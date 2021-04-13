#Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv.
# The dataset is composed of two columns: Date and Profit/Losses.

### We will create a Python script that analyzes the PyBank records to calculate each of the following:

########### The total number of months included in the dataset
########### The net total amount of "Profit/Losses" over the entire period
########### The average of the changes in "Profit/Losses" over the entire period
########### The greatest increase in profits (date and amount) over the entire period
########### The greatest decrease in losses (date and amount) over the entire period
########### Print the analysis to the terminal and export a text file with the results


#modules 
import os
import csv

#Where used of File for this homework

data_File_csv_path = os.path.join("budget_data.csv")

#List of data

Date = []
Profit_Losses = []
Monthly_Changes = []

#Definiing Variables

Total_Months = 0
Total_Profit_Losses = 0
Change_initial = 0
Change_Profit_Losses = 0

#Open file

with open(data_File_csv_path, newline="" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    data_header = next(csvreader)

    #instructing the calculation and creation of Variables

    for row in csvreader:

        Total_Months = Total_Months + 1

        Date.append(row[0])

        Profit_Losses.append(row[1])
        Total_Profit_Losses = Total_Profit_Losses + int(row[1])

        Change_Final= int(row[1])
        Monthly_Changes_Profit = Change_Final - Change_initial

        Monthly_Changes.append(Monthly_Changes_Profit)

        Change_Profit_Losses = Change_Profit_Losses + Monthly_Changes_Profit
        Change_initial = Change_Final

        Avg_Change= (Change_Profit_Losses/Total_Months)

        Greatest_Increase_Profits = max (Monthly_Changes)
        Greatest_Decrease_Profits = min (Monthly_Changes)

        Increase_Date = Date[Monthly_Changes.index(Greatest_Increase_Profits)]
        Decrease_Date = Date[Monthly_Changes.index(Greatest_Decrease_Profits)]
        
#Showing Results
    print ("Total Months: " + str(Total_Months))
    print ("Total Profits: " + str(Total_Profit_Losses))
    print ("Average Change: " + "$" + str(int(Avg_Change)))
    print ("Greatest Increase in Profits: " + str(Increase_Date) + " ($" + str(Greatest_Increase_Profits) + ") ")
    print ("Greatest Decrease in Profits: " + str(Decrease_Date) + " ($" + str(Greatest_Decrease_Profits) + ") ")

with open('analysis''results.txt', 'w') as text:
    text.write("Total Months: " + str(Total_Months) + "\n")
    text.write ("Total Profits: " + str(Total_Profit_Losses) + "\n")
    text.write ("Average Change: " + "$" + str(int(Avg_Change)) + "\n")
    text.write ("Greatest Increase in Profits: " + str(Increase_Date) + " ($" + str(Greatest_Increase_Profits) + ") + \n")
    text.write ("Greatest Decrease in Profits: " + str(Decrease_Date) + " ($" + str(Greatest_Decrease_Profits) + ") + \n")