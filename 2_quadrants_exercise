#Asks user for 3 addresses and sorts each address into a list based on D.C.'s quadrant grid.
#Tells user how many addresses were in each quadrant.

northwest = []
northeast = []
southwest = []
southeast = []
quadrants = [northwest, northeast, southwest, southeast]
quadrants_strings = ["NW", "NE", "SW", "SE"]

addresses = []

for number in range (3):
	print "Please enter an address."
	addresses.append(raw_input())

for address in addresses:
	if 'NW' in address:
		northwest.append(address)
	elif 'NE' in address:
		northeast.append(address)
	elif 'SW' in address:
		southwest.append(address)
	elif 'SE' in address:
		southeast.append(address)

for i in range(len(quadrants)):
	quadrant = quadrants[i]
	if len(quadrant) > 0:
		print "There were {0} addresses in the {1} quadrant. Those addresses were: {2}.".format(len(quadrant),quadrants_strings[i],quadrant)
