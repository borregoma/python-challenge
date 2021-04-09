import statistics
import csv

def calcStats():
    with open("budget_data.csv") as dataFile:
        reader = csv.reader(dataFile)
        Date = str(dataFile[0])
        Profit_Losses = int(dataFile[1])
    
            if Profit_Losses == row[1]

            data_sum = round(statistics.sum(dataFile), 2)
            data_mean = round(statistics.mean(dataFile), 2)
            data_max = round(statistics.max(dataFile), 2)
            data_min = round(statistics.min(dataFile), 2)
   
            for row in reader:
            data = readData()

    print("Total Ampunt of Profit/Losses is: ", data_sum)
    print("The average of change: ", data_mean)
    print("The Maximum amount in this datasheet is: ", data_max)
    print("The Minimum amount in this datasheet is: ", data_min)

calcStats()

