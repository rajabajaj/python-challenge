import csv
from collections import Counter
import os

with open('election_data.csv', 'r') as elect_poll:
    election_reader = csv.reader(elect_poll, delimiter =",")
    header = next(election_reader)

    votesCounted = Counter()
    candidateList = []
    percentage = []
    answer = []

    for row in election_reader:
        candidateList.append(row[2])

    totalVotes = len(candidateList)

    for name in candidateList:
        votesCounted[name] += 1

        
    winner_pypoll = max(votesCounted.keys()) 
    names_pypoll = tuple(votesCounted.keys())
    votes_pypoll = tuple(votesCounted.values())


    
    for value in votes_pypoll:
        percentage.append((int(value)/totalVotes)*100)
     
    
    

    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')

    for x in range(len(names_pypoll)):
        answer.append(names_pypoll[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes_pypoll[x])  + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' +  winner_pypoll[0]) 
    answer.append('-----------------------')
    print("\n".join((answer)))


FINAL RESULTS

    Election Results
-----------------------
Total Votes: 3521001
-----------------------
Khan: 63.0% (2218231)
Correy: 20.0% (704200)
Li: 14.0% (492940)
O'Tooley: 3.0% (105630)
-----------------------
Winner: Khan
-----------------------
   

