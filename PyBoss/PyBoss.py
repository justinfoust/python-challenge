###---------------------------------------------------------###
###   Python Challenge HW  --  Extra Content -- PyBoss      ###
###   Justin Foust  --  09/26/2019  --  Data Boot Camp      ###
###---------------------------------------------------------###


import os   #File pointing functions
import csv   #CSV file handling functions

dataFilePath = os.path.join('employee_data.csv')   #Path to read file
writeFilePath = os.path.join('employee_data_converted.csv')   #Path to write file

us_state_abbrev = {   #Dict used to match state names with abbreviations
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

resultsList = [['Emp', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]   #Create list with initial row of column titles

with open(dataFilePath, mode='r') as csvFile:   #Open file in read mode and set it as 'csvFile' variable
    csvReader = csv.reader(csvFile, delimiter=',')   #Set contents of open file as 'csvReader'; data separated by [,]
    
    next(csvReader)   #Skip first row of headers
    
    for line in csvReader:   #Increment through each row of data in open file
        resultsRow = []   #Clear any unwanted values from 'resultsRow' list
        resultsRow.append(line[0])   #Append 'resultsRow' list with employee number
        resultsRow.append(line[1].split(' ')[0])   #Split name when encountering space and append 'resultsRow' list with the first word from split
        resultsRow.append(line[1].split(' ')[1])   #Split name when encountering space and append 'resultsRow' list with the second word from split
        resultsRow.append(line[2].split('-')[1] + '/' + line[2].split('-')[2] + '/' + line[2].split('-')[0])   #Split date when encountering [-] and append 'resultsRow' list with second value from split, first value from split, and third value from split each separated by [/]
        resultsRow.append('###-##-' + line[3].split('-')[2])   #Split SSN when encountering [-] and append 'reslutsRow' with [###-##-] followed by third value from split
        resultsRow.append(us_state_abbrev[line[4]])   #Use state name as key in 'us_state_abbrev' dict to refence corresponding value (state's abbreviation) and append to 'resultsRow' list
        resultsList.append(resultsRow)   #Append 'resultsRow' list to 'resultsList' list

        
with open(writeFilePath, 'w', newline='') as csvFile:   #Open file in write mode and set it as 'csvFile' variable
    csvWriter = csv.writer(csvFile)   #Invoke writing function as 'csvWriter' variable
    csvWriter.writerows(resultsList)   #Write each value of 'resultsList' (each of which is also a list of values) to open file
        
with open(writeFilePath, mode='r') as csvFile:   #Open file in read mode and set it as 'csvFile' variable
    csvReader = csv.reader(csvFile, delimiter=',')   #Set contents of open file as 'csvReader'; data separated by [,]
    for line in csvReader:   #Increment through each row of data in open file
        print(line)   #Print each line to the console