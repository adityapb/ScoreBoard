from score import score

def chooseMatches():
	data = score()
	for i in range(len(data)):
		print str(i+1) + " " + str(data[i])
	choice = input("Choose a match: ")
	return choice - 1