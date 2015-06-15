# Challenge Level: Beginner

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

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
