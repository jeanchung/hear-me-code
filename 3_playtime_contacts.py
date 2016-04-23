# Reads contact information from contacts.csv and writes HTML code to display the information in a table to contacts.html

with open("contacts.csv", "r") as contacts_data:
	contacts = contacts_data.read().split("\n")
	
for idx, item in enumerate(contacts):
	contacts[idx] = item.split(",")

with open("contacts.html", "w") as contacts_page:
	contacts_page.write("""<table border="1">""")
	for item in contacts[1:]:
		contacts_page.write("""<td colspan="2"> <b>{0}</b> </td>""".format(item[0]))
		contacts_page.write("""</tr>""")
		contacts_page.write("""<tr>""")
		contacts_page.write("""<td> Phone: {0} </td>""".format(item[1]))
		contacts_page.write("""</tr>""")
		contacts_page.write("""<tr>""")		
		contacts_page.write("""<td> Twitter: {0} </td>""".format(item[3]))
		contacts_page.write("""</tr>""")
		contacts_page.write("""<tr>""")
		contacts_page.write("""<td> Github: {0} </td>""".format(item[2]))
		contacts_page.write("""</tr>""")
	contacts_page.write("""</table>""")		
