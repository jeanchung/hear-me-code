# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries, create a function that will open a CSV file and return the result as a nested list.

def CSVtoList(filename, delimiter=","):
    with open(filename, "r") as filetext:
        newList = filetext.read().split("\n")
    
    for i,line in enumerate(newList):
        newList[i] = line.split(delimiter)
    return newList
