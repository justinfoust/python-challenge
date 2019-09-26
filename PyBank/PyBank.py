###---------------------------------------------------------###
###   Python Challenge HW  --  PyBank                       ###
###   Justin Foust  --  09/26/2019  --  Data Boot Camp      ###
###---------------------------------------------------------###


import os   #File pointing functions
import csv   #CSV file handling functions

dataFile = os.path.join('resources','budget_data.csv')   #Path to CSV read file
writeFile = os.path.join('budget_data_analysis.txt')   #Path to text write file

with open(dataFile, mode='r') as csvFile:   #Open read file in read mode and set to 'csvFile' variable
    csvReader = csv.reader(csvFile, delimiter=',')   #Set contents of read file to 'csvReader' variable; data separated by [,]
    
    header = next(csvReader)   #Skip first row of data, which contains column headers
    
    monthTotal = 0   #Define 'monthTotal' varible and set to 0
    netChange = 0   #Define 'netChange' varible and set to 0
    greatestChange = {   #Define 'greatestChange' dict
        'iValue': 0,   #Define 'iValue' (profit increase value) key, set value to 0
        'iDate': '',   #Define 'iDate' key, no value set
        'dValue': 0,   #Define 'dValue' (profit decrease value) key, set value to 0
        'dDate': ''   #Define dDate key, no value set
    }
    results = []   #Define 'results' array
    
    for line in csvReader:   #Increment through rows of file data
        monthTotal += 1   #Add 1 to 'monthTotal' value
        netChange += int(line[1])   #Convert "Profit/Losses" value from file to intger and add to 'netChange' variable
        if int(line[1]) > greatestChange['iValue']:   #If "Profit/Losses" value is greater than 'iValue'...
            greatestChange['iValue'] = int(line[1])   #... set this as value for 'iValue' key ...
            greatestChange['iDate'] = line[0]   #... set "Date" value from file as value for 'iDate' key ...
        elif int(line[1]) < greatestChange['dValue']:   #... Else if "Profit/Losses" value is less than 'dValue'...
            greatestChange['dValue'] = int(line[1])   #... set this value for 'dValue' key ...
            greatestChange['dDate'] = line[0]   #... set "Date" value from file as value for 'dDate' key
        
    #Create list containing results    
    results = [\
        'Total Months: ' + str(monthTotal) + '\n', \
        'Total: $' + str(netChange) + '\n', \
        'Average Change: $' + str(netChange/monthTotal) + '\n', \
        'Greatest Increase in Profits: ' + greatestChange["iDate"] + ' ($'+str(greatestChange["iValue"]) + '\n', \
        'Greatest Decrease in Profits: ' + str(greatestChange["dDate"]) + ' ($' + str(greatestChange["dValue"]) + ')' \
    ]

with open(writeFile, mode='w') as txtFile:   #Open text write file in write mode and set to 'txtFile' variable
    txtFile.writelines(results)   #Write 'results' variable to file

with open(writeFile, mode='r') as txtFile:   #Open text write file in read mode and set to 'txtFile' variable
    print(txtFile.read())   #print contents of text write file to console