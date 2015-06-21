# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234


employee_info = {}

with open("all_employees.csv", "r") as company_file:
	all_employees = company_file.read().split("\n")

for idx, person in enumerate(all_employees):
	all_employees[idx] = person.split(",")

for person in all_employees[1:]: # puts info from all_employees into dictionary
	employee_info[person[1].lstrip()] = [x.lstrip() for x in person]
	
with open("survey.csv", "r") as survey_file:
	survey_ppl = survey_file.read().split("\n")

for idx, person in enumerate(survey_ppl):
	survey_ppl[idx] = person.split(",")

for person in survey_ppl[1:]:
	if person[0] in employee_info:
		print "{0} took the survey! Here is their contact information: Twitter: {1} Github: {2} Phone: {3}".format(employee_info[person[0]][0], person[1], person[2], employee_info[person[0]][2])
