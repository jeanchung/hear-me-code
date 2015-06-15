# Prints "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

ingredient_names = ["bread", "peanut butter", "jelly"]
bread = 5
peanut_butter = 4
jelly = 3
i = 1

while bread >= 2 and peanut_butter >= 1 and jelly >= 1:
	print "Making sandwich #{0}...".format(i)
	bread = bread - 2
	peanut_butter = peanut_butter - 1
	jelly = jelly - 1
	i = i + 1
	ingredients = [bread / 2, peanut_butter, jelly]
	
	if bread < 2 or peanut_butter < 1 or jelly < 1:
		for number, item in enumerate(ingredients):
			if item < 1:
				print "All done; I ran out of {0}.".format(ingredient_names[number])

# above for loop could also be replaced with:
#		for j in range(len(ingredients)):
#			ingredient = ingredients[j]
#			if ingredient < 1:
#				print "All done; I ran out of {0}.".format(ingredient_names[j])for item in ingredients:

	else:
		print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread,peanut_butter,jelly)

# Instructions for exercise below:

# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.
