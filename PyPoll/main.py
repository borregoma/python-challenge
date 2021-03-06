#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
###### The total number of votes cast
###### A complete list of candidates who received votes
###### The percentage of votes each candidate won
###### The total number of votes each candidate won
###### The winner of the election based on popular vote.
###### As an example, your analysis should look similar to the one below:
# Election Results
#
# Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the result

#modules 
import os
import csv

#Where used of File for this homework

data_File_csv_path = os.path.join("election_data.csv")

#List of data

No_Votes = 0
List_Candidates = []
Percentage_per_Candidate = []
No_Votes_per_Candidate = []
Winner = []

#Opening File and setting for Loops to calculate results

with open(data_File_csv_path, newline="" ) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    data_header = next(csvreader)

    for row in csvreader:
        No_Votes = No_Votes + 1

        List_Candidates.append(row[2])

        for x in set(List_Candidates):
            Winner.append(x)
            x2 = List_Candidates.count(x)
            
            No_Votes_per_Candidate.append(x2)

            x3 = (x2/No_Votes) *100
            Percentage_per_Candidate.append(x3)

        Winner_Vote_Total = max(No_Votes_per_Candidate)

    Winner_Candidate = Winner[No_Votes_per_Candidate.index(Winner_Vote_Total)]

    print("Total Votes: " + str(No_Votes))

    for i in range(len(Winner)):
            print(Winner[i] + ": " + str(Percentage_per_Candidate[i]) + "% (" + str(No_Votes_per_Candidate[i]) + ")")
            print("And the Winner is: " + Winner_Candidate)
    

    with open('..', 'analysis', results.txt)
        text.write ("Total Votes: " + str(No_Votes) + "\n")
            for i in range(len(set(Winner))):
                text.write(Winner[i] + ": " + str(Percentage_per_Candidate[i]) + "% (" +str(No_Votes[i]) + ")\n"))
                text.write("And the Winner is: " + Winner_Candidate  + "\n")



