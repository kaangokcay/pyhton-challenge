import os
import csv 
from operator import itemgetter

budget_csv = os.path.join('..','Resources', 'election_data.csv')
text_file = "election_summary.txt"

Total_Votes = 0
Total_Candidates = 0
Candidates =[]
Candidate_Votes = {}

with open(budget_csv, newline="") as file:
    csvreader = csv.reader(file, delimiter=",")

    csv_header = next(file)

    for row in csvreader: 
        Total_Votes +=1
        Total_Candidates = row[2]

        if row[2] not in Candidates:
            Candidates.append(row[2])
            Candidate_Votes[row[2]] = 1
        
        else: 
            Candidate_Votes[row[2]] = Candidate_Votes[row[2]] + 1

    print()
    print()
    print("Election Results")
    print("----------------------------")
    print("Total Votes:" + str(Total_Votes))
    print("----------------------------")

    for Candidate in Candidate_Votes:
        print(Candidate + " " + str(round(((Candidate_Votes[Candidate]/Total_Votes)*100))) + "%" + " (" + str(Candidate_Votes[Candidate]) + ")")


winner = sorted(Candidate_Votes.items(), key=itemgetter(1), reverse=True)

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")


with open(text_file, "w") as txt_file:

    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(Total_Votes))
    txt_file.write("\n")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    txt_file.write("-------------------------")

