###---------------------------------------------------------###
###   Python Challenge HW  --  Extra Content -- PyParagraph ###
###   Justin Foust  --  09/26/2019  --  Data Boot Camp      ###
###---------------------------------------------------------###


import os   #file pointing functions
import re   #RegEx functionality
from statistics import mean  #Import only mean() from statistics module

readFilePath = os.path.join('raw_data','paragraph_2.txt')   #Path to text file to analyze

wordCount = 0   #Set initial word count
sentenceCount = 0   #Set initial sentence count
wordCharCounts = []   #Create array to hold letter count of each word encountered
sentenceWordCounts = []   #Create array to hold word count for each sentence encountered


with open(readFilePath, 'r') as txtFile:   #Open file and set it as 'txtFile' variable
    paragraph = txtFile.read()   #Set contents of opened file as 'paragraph'
    
    wordPattern = re.compile(r'\w+')   #Set variable 'wordPattern' as RegEx search pattern looking for 1 or more non-whitespace characters
    sentencePattern = re.compile(r'(?<=[a-z][.!?])\W+')   #Set variable 'sentencePattern' as RegEx search pattern looking for lowercase letter followed by either [. ! ?] followed by 1 or more whitespace characters
    characterPattern = re.compile(r'\w')   #Set variable 'characterPattern' as RegEx search for single non-whitespace character
    
    for string in re.split(r' +', paragraph):   #Split contents of file when encountering 1 or more spaces
        if wordPattern.search(string):  #If one or more non-whitespace characters are encountered...
            wordCount += 1   #...increment word count by 1
            wordCharCounts.append(len(characterPattern.findall(string)))   #Find all non-whitespace characters in word, return into tuple, and append tuple length into array
    
    for string in re.split(sentencePattern, paragraph):   #Split contents of file when either [. ! ?] followed by one or more spaces is encounterd
        sentenceCount += 1   #Increment sentence count by 1
        sentenceWordCounts.append(len(wordPattern.findall(string)))   #Find all strings of non-whitespace characters, return into tuple, and append tuple length into array
    
    print(f'Word Count:  {wordCount}')   #print to the console word count
    
    print(f'Sentence Count:  {sentenceCount}')   #print to the console sentence count
    
    print(f'Average Characters per Word:  {round(mean(wordCharCounts))}')   #Print to the console rounded average of character counts per word
    
    print(f'Average Words per Sentence:  {round(mean(sentenceWordCounts))}')   #Print to the console rounded average of words per sentence
        
