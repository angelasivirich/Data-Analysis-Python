#imports libraries os,csv and math that will be used throughout the code
import os
import csv
import math

#path to the csv file where the data is going to be extracted from
csvpath=os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as f:
    csvReader=csv.reader(f,delimiter=',')

    #reads and stores headers in "headers list"
    headers=next(csvReader)

    #creates three empty lists (date, revenue and change)    
    dates=[]
    revenue=[]
    change=[]

    #iterates over every row in csvReader and appends values to " dates list" and "revenue list"
    for row in csvReader:
        dates.append(row[0])
        revenue.append(float(row[1]))

    totalMonths=len(dates)

    #math.fsum from module math, used to add all numbers in revenue list
    totalRevenue=math.fsum(revenue)

    #calculates the daily revenue change and append the values to "change list"   
    for x in range(len(revenue)-1):
        monthlyChange=float(revenue[x+1]-revenue[x])
        change.append(monthlyChange)

    #calculates average change
    avgChange=round(((math.fsum(change))/(len(change))),2)

    #calculates greates increase and greatest decrease in "change list"
    greatestIncrease=max(change)
    greatestDecrease=min(change)
    
    #finds in "dates list" the dates associated with the greates increase and decrease in "change list"
    greatestIncreaseIndex=change.index(greatestIncrease)
    greatestDecreaseIndex=change.index(greatestDecrease)
    greatestIncreaseDate=(dates[greatestIncreaseIndex+1])
    greatestDecreaseDate=(dates[greatestDecreaseIndex+1])

    #prints out the analysis
    output=(f"Financial Analysis\n--------------------------------\nTotal Months: {totalMonths}\nTotal: ${totalRevenue}\nAverage Change: ${avgChange}\nGreatest Increase in Profits:{greatestIncreaseDate} (${greatestIncrease})\nGreatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})")
    print(output)

#exports the analysis to text file 'budget_analysis.txt'     
outputFile=os.path.join('analysis','budget_analysis.txt')
with open(outputFile,"w") as txtFile:
    txtFile.write(output)
