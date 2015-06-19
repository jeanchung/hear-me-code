# Challenge Level: Beginner

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.
# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# Open text file of states and save as list
with open("states.txt", "r") as states_file:
	all_states = states_file.read().split("\n")

# Split each state entry into a list of abbreviation, full state name
for idx, state in enumerate(all_states):
	all_states[idx] = state.split("\t")

# Write to HTMl file
with open("states.html", "w") as html_file:
	html_file.write("<select>")
	for state in all_states:
		html_file.write("""<option value="{0}">{1}</option>""".format(state[0], state[1]))
	html_file.write("</select>")
	
# Open CSV file of state info and save as a list
with open("state_info.csv", "r") as state_info_file:
	states_info = state_info_file.read().split("\n")
	
# Split each entry into its own list at comma
for idx, entry in enumerate(states_info):
	states_info[idx] = entry.split(",")

# Remove extra quotes from state name and percent
for state in states_info:
	state[1] = state[1][1:-1]
	state[4] = state[4][1:-1]
	
# Write to HTML file
with open("state_info.html", "w") as html_file:
	html_file.write("""<table border="1">""")
	for state in states_info[1:]:	
		html_file.write("""<tr>""")
		html_file.write("""<td colspan="2"><b> {0} </b></td>""".format(state[1]))
		html_file.write("""</tr>""")
		html_file.write("""<tr>""")
		html_file.write("""<td> Rank: {0} </td>.""".format(state[0]))
		html_file.write("""<td> Percent: {0} </td>""".format(state[4]))
		html_file.write("""</tr>""")
		html_file.write("""<tr>""")
		html_file.write("""<td> U.S. House Members: {0} </td>""".format(state[3]))
		html_file.write("""<td> Population: {:,d} </td>""".format(int(state[2])))
		html_file.write("""</tr>""")
	html_file.write("""</table>""")
