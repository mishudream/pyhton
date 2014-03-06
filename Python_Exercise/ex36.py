from sys import exit
	
def man_preferences():
	print "Welcome to the survey!"
	print "You should like sports."
	print "Do you like basketball or football or skydiving?"
	
	sports = raw_input("> ")
	
	if sports == "basketball":
		print "You should be great idol Jordan!"
	elif sports == "football":
		print "Should be your idol Ronaldinho!"
	elif sports == "skydiving":
		print "You are a madman!"
		# ending("Thank you for the survey!")
	else:
		ending("You are a lazy guy!")
		
def women_preferences():
	print "Welcome to the survey!"
	print "You should like beautiful clothes."
	print "Do you like a hat or Skirt or shoes?"
	
	clothes = raw_input("> ")
	
	if clothes == "hat":
		print "You're a lovely girl!"
	elif clothes == "Skirt":
		print "You are a beautiful girl!"
	elif clothes == "shoes":
		print "You're narcissistic!"
		# ending("You're narcissistic")
	else:
		ending("You are very simple!")

def ending(why):
	print why, "Good luck!"
	exit(0)
	
def start():
	print "This is a questionnaire!"
	print "Understanding the preferences of boys and girls!"
	print "What is your gender? Male or female."
	
	sex = raw_input("> ")
	
	if sex == "male":
		man_preferences()
	elif sex == "female":
		women_preferences()
	else:
		ending("You come from Thailand!")
		
start()