#Import the required packages
import os
import csv

#Declare and Initialize File Path,Lists
file_path = "03-Python/Homework/Instructions/PyPoll/Resources"
voter_id = []
county = []
candidate = []
unique_list = []
unique_list_count = []
unique_list_percentage = []

#Read Data
file_to_read = os.path.join(file_path,"election_data.csv")
with open(file_to_read,mode="r",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #Skip Header
    next(csvreader,None)
    #Populate Voter-Id,County and Candidate
    for row in csvreader:
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

#Total Number of Votes
total_votes = len(voter_id)

#Find Unique Candidate Name
for row in candidate:
    if row in unique_list:
        continue
    else:
        unique_list.append(row)    

#For each unique candidate calculate winning percentage and total votes won
for x in unique_list:
    count = 0
    percentage = 0
    for y in candidate:
        if x == y:
            count = count + 1
    #Calculate Percentage                
    percentage = round((count/total_votes) * 100,2)
    unique_list_percentage.append(percentage)
    #Votes Won
    unique_list_count.append(count)

#Write to a text file
with open(os.path.join(file_path,"PyPoll.txt"),mode="w",newline="") as PyPollWrite:
    PyPollWrite.writelines("Election Results\n")
    PyPollWrite.writelines("-------------------------\n")
    PyPollWrite.writelines(f"Total Votes: {total_votes}\n")
    PyPollWrite.writelines("-------------------------\n")
    for i,j,k in zip(unique_list,unique_list_percentage,unique_list_count):
        PyPollWrite.writelines(f'{i}: {j}00% ({k})\n')
    PyPollWrite.writelines('-------------------------\n')
    PyPollWrite.writelines(f'Winner: {unique_list[unique_list_count.index(max(unique_list_count))]}\n')
    PyPollWrite.writelines('-------------------------\n')

#Read and Display on Console
with open(os.path.join(file_path,"PyPoll.txt"),mode="r",newline="") as PyPollRead:
    print(PyPollRead.read())










