import os
import csv


# Path for Input File
csv_input_path = os.path.join('Resources', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')


candidates, total_candidates, candidate_perc, candidate_total_vote, summaries = ([] for i in range(5))


with open(csv_input_path, mode='r', newline='') as poll_data:
    reader = csv.reader(poll_data, delimiter=',')

    next(reader)

    num_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1


# sorted list of total_candidates
sorted_candidates = sorted(total_candidates)

for i in range(num_rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])


print("\nElection Results")
print("-" * 40)
print("Total Votes:", num_rows)
print("-" * 40)


for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1

    candidate_perc.append(round(candidate_count / num_rows * 100, 3))
    candidate_total_vote.append(candidate_count)

#Sort values so that on console it can be displayed in descending order    
zippedsummary = list(zip(candidate_total_vote,candidate_perc,candidates))
zippedsummary_sort = sorted(zippedsummary,reverse=True)

for row in zippedsummary_sort:
    print(row[2] + ":" , str(row[1]) + "00%", "(" + str(row[0]) + ")")
    summary = (row[2] + ": ", str(row[1]) + "00%", " (" + str(row[0]) + ")")
    summaries.append(summary)


for k in range(len(candidate_perc)):
    if candidate_total_vote[k] > candidate_total_vote[k - 1]:
        winner = candidates[k]


print("-" * 40)
print("Winner:", winner)
print("-" * 40)
print("\n\n")

#Output File Path
csv_output_path = os.path.join('Output', 'pypoll.txt')
with open(csv_output_path, mode='w', newline='') as posted_summaries:
    writer = csv.writer(posted_summaries)

    writer.writerows([
        ["Election Results" ],
        ["-" * 40],
        ["Total Votes: " + str(num_rows)],
        ["-" * 40]
    ])
    writer.writerows(summaries)
    writer.writerows([
        ["-" * 40],
        ["Winner: " + str(winner)],
        ["-" * 40]
    ])

#This Operation is to remove commas getting written into text file
with open(csv_output_path, mode='r') as infile:

     #open(csv_output_path, mode='w') as outfile:
    data = infile.read()
    data = data.replace(",", "")

with open(csv_output_path,mode='w') as outfile:
    outfile.write(data)