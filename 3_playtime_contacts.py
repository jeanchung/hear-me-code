# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

contacts = {
	'Jean': {'phone': '952-555-5555', 'twitter': '@jxchung', 'github': '@jeanchung'},
	'Sulley': {'phone': '404-123-4567', 'twitter': '@sulleythedog', 'github': '@woof'},
	'Violet': {'phone': '202-987-6543', 'twitter': '@vivi', 'github': '@doxiethatcodes'}
}

for key in contacts.keys():
	print "{0}'s contact information is:".format(key)
	print "\t Phone: {0}".format(contacts[key]["phone"])
	print "\t Twitter: {0}".format(contacts[key]["twitter"])
	print "\t Github: {0}".format(contacts[key]["github"])
