#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",") # Make a list headings, reading the first line of the csv, seperating by commas. 
    i = 0 # The starting value for the for loop to iterate through
    mark_col = None
    num_col = None
    for head in headings: #Iterate through the size of the list headings
        if head == "Student Number": 
            num_col = i # When the string Student Number is found, set the value of num_col to i
        elif head == "Mark" :
            mark_col = i # When the string Mark is found, set the value of mark_col to i
        i += 1 # Increment i each time the for loop repeats
    if mark_col is None:
        raise ValueError("Could not find Mark column in file")
    elif num_col is None:
       raise ValueError("Could not find Student Number column in file")
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = best_idx = -1 # Initialize best and best_idx to -1 as 0 is a possible mark
    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col]) # Set integer value Mark to value of mark_col in data list
        if mark > best: # If current mark is better than previous best mark, update best mark to current mark, and student number to current position in number column
            best=mark
            best_idx = data[num_col]
    if best > 100:
        raise ValueError("Highest mark above 100")
    return best_idx, best

f = open(sys.argv[1]) # Prompt user for input file name
num_col, mark_col = getCols(f) # Set values of num_col and mark_col using getCols() function
best_idx, best = findTop(f,num_col,mark_col) # Set values of best_idx and best using findTop() function
print("The top student was student number %s with mark %d"%(best_idx,best))
