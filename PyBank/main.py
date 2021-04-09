import statistics
import csv
import array

def budget_csv ():
    with open("budget_data.csv") as dataFile:
        data= array.array('f'), [])

    reader = csv.reader(dataFile, delimiter=",")
    curLine = 0

    for row in reader:
        if curLine == 0:
            pass
        else:
            item = float(row[2])
            data.append(item)
        print (row)

readersample()

def calcStats

    data=budget_csv

    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    data_std = round(statistics.stdev(data), 2)
    data_var = round(statistics.variance(data), 2)

    print("Total Ampunt of Profit/Losses is: ", data_sum)
    print("The average of change: ", data_mean)
    print("The Maximum amount in this datasheet is: ", data_max)
    print("The Minimum amount in this datasheet is: ", data_min)

calcStats()