#imports libraries os and csv that will be used throughout the code
import os
import csv

#path to the csv file where the data is going to be extracted from
csvpath=os.path.join('Resources', 'election_data.csv')
with open(csvpath) as f:
    csvReader=csv.reader(f,delimiter=',')

    #reads and stores headers in "headers list"
    headers=next(csvReader)
    
    #creates empty lists
    voterId=[]
    candidates=[]
    votes=[]

    countKhan=0
    countCorrey=0
    countLi=0
    countOTooley=0

    #iterates over every row in csvReader and appends values to " voterID list" and "votes list"
    for row in csvReader:
        voterId.append(row[0])
        votes.append(row[2])

        #appends the name of the candidate to "candidates list" only if the name doesn't exist in the list
        if row[2] not in candidates:
            candidates.append(row[2])
    
    totalVotes=len(voterId)

    #counts the number of votes each candidate won
    for i in votes:
        if i=="Khan":
            countKhan=countKhan+1
        elif i=="Correy":
            countCorrey=countCorrey+1
        elif i=="Li":
            countLi=countLi+1
        elif i=="O'Tooley":
            countOTooley=countOTooley+1        
    
    #calculates the percentage of votes each candidate won
    percentageKhan="{:.3f}".format((countKhan/totalVotes)*100)
    percentageCorrey="{:.3f}".format((countCorrey/totalVotes)*100)
    percentageLi="{:.3f}".format((countLi/totalVotes)*100)
    percentageOTooley="{:.3f}".format((countOTooley/totalVotes)*100)
    
    #finds the candidate with most number of votes (the winner)
    totalCounter=[countKhan,countCorrey, countLi, countOTooley]
    if countKhan==max(totalCounter):
        winner="Khan"
    elif countCorrey==max(totalCounter):
        winner="Correy"
    elif countLi==max(totalCounter):
        winner="Li"
    elif countOTooley==max(totalCounter):
        winner="O'Tooley"
    
    #prints out the analysis
    output=(f"Election Results\n--------------------------\nTotal Votes: {totalVotes}\n--------------------------\n{candidates[0]}: {percentageKhan}% ({countKhan}) \n{candidates[1]}: {percentageCorrey}% ({countCorrey})\n{candidates[2]}: {percentageLi}% ({countLi})\n{candidates[3]}: {percentageOTooley}% ({countOTooley})\n--------------------------\nWinner: {winner}\n--------------------------")
    print(output)

#exports the analysis to text file 'election_analysis.txt'   
outputFile=os.path.join('analysis','election_analysis.txt')
with open(outputFile,"w") as txtFile:
    txtFile.write(output)

   