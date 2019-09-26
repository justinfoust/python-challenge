###---------------------------------------------------------###
###   Python Challenge HW  --  PyPoll                       ###
###   Justin Foust  --  09/26/2019  --  Data Boot Camp      ###
###---------------------------------------------------------###


import os   #File pointing funcitons
import csv   #CSV file handling functions

dataFile = os.path.join('resources','election_data.csv')   #Path to CSV read file
writeFile = os.path.join('election_results.txt')   #Path to text write file

with open(dataFile, mode='r') as csvFile:  #Open CSV read file and set to 'csvFile' variable
    csvReader = csv.reader(csvFile, delimiter=',')   #Set contents of read file to 'csvReader' variable; data separated by [,]
    
    header = next(csvReader)   #Define 'header' variable and set it as initial row of CSV read file data; increment to next row of CSV read file data
    totalVotes = 0   #Define 'totalVote' variable and set it to 0
    resultsList = {}   #Define 'resultsList' dict
    winner = {'name': '', 'votes': 0}   #Define 'winner' dict and create 'name' and 'votes' keys with undefined and 0 values respectively

    for line in csvReader:   #Increment through lines of CSV read file data
        totalVotes += 1   #Add one to 'totalVotes' variable
        if line[2] not in resultsList.keys():   #If candidates name is not listed as key in 'resultsList' dict ...
            resultsList[line[2]] = {'numVotes': 0, 'percentVotes': 0}   #... create key in 'resultsList' dict labeling as candidates name; set value at a new dict with 'numVotes' and 'percentVotes' keys each with values set to 0
        if line[2] in resultsList.keys():   #If candidates name is listed as a key in 'resultsList' dict ...
            resultsList[line[2]]['numVotes'] += 1   #Add 1 to value of 'numVotes' key in dict of key labeled as candidate's name

    resultsSummary = ['Total Votes: ' + str(totalVotes) + '\n']   #Define 'resultsSummary' list and set it to string containing 'totalVotes' value
    
    for candidate in resultsList.keys():   #Increment through each key (candidate's name) in 'resultsList' dict
        resultsList[candidate]['percentVotes'] = int(resultsList[candidate]['numVotes'] / totalVotes * 100)   #Set 'percentVote' key value as 'numVotes' key value divided by 'totalVotes' variable multiplied by 100
        if resultsList[candidate]['numVotes'] > winner['votes']:   #If 'numVotes' key value is greater than 'votes' key value of 'winner' dict ...
            winner['name'] = candidate   #... set 'name' key value of 'winner' dict to current key value of 'resultsList' dict (candidate's name)
            winner['votes'] = resultsList[candidate]['numVotes']   #... set 'votes' key value of 'winner' dict to 'numVotes' key value
                                   #Append to 'resultsSummary' list: current key of 'resultsList' dict (candidate's name), 'percentVotes' key value (formated to 3 decimal places), and 'numVotes' key value
        resultsSummary.append(\
            candidate + ': ' + \
            "{:.3f}".format(resultsList[candidate]['percentVotes']) + '% (' + \
            str(resultsList[candidate]['numVotes']) + ') ')

    resultsSummary.append('\nWinner: ' + winner['name'])   #Append to 'resultsSummary' list: 'name' key value of 'winner' dict
    
    with open(writeFile, mode='w') as txtFile:   #Open write text file in write mode and set to 'txtFile' variable
        txtFile.writelines(resultsSummary)   #Write each line of 'resultsSummary' list to file

    with open(writeFile, mode='r') as txtFile:   #Open write text file in read mode and set to 'txtFile' variable
        print(txtFile.read())   #Print contents to console