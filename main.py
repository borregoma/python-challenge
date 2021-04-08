import csv

def budget_data ():
    with open("../budget_data.csv") as datafile:
    reader = csv.reader(datafile)
    for row in reader:
        print (row)

readersample()

