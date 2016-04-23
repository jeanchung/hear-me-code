# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

def textfile_to_string(filename):
    """ This function opens a text file and reads it as a string. """
    with open(filename, "r") as filetext:
        text = filetext.read()   
    return text
    

def listDeduplicator(file1, file2):
    """ This function combines the contents of two text files and removes duplicate items."""
    list1 = textfile_to_string(file1).split("\n")
    list2 = textfile_to_string(file2).split("\n")
    combinedList = list(set(list1 + list2))
    return combinedList
    
print "Here is a de-duplicated list of all of the people who have come to my events:\n"
print listDeduplicator("film_screening_attendees.txt", "happy_hour_attendees.txt")

# Goal 2: Who came to *both* your Film Screening and your Happy hour?

def listIntersector(file1, file2):
    list1 = textfile_to_string(file1).split("\n")
    list2 = textfile_to_string(file2).split("\n")
    newList = []    
    for item in list1:d
        if item in list2:
            newList.append(item)
    return newList

print "Here is the list of people who came to both my events:\n"
print listIntersector("film_screening_attendees.txt", "happy_hour_attendees.txt")
