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
-------------------------
# Total Votes: 3521001
-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
-------------------------
#Winner: Khan
-------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the result

#modules 
import os
import csv

#Where used of File for this homework

data_File_csv_path = os.path.join("election_data.csv")

#List of data

No_Votes = []
List_Candidates = []
Percentage_per_Candidate = []
No_Votes_per_Candidate = []
Winner = []

