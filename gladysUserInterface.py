import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Sindy Ken and Rafael Payan
	Module: gladysUserInterface
	Description: This module does …
"""
# Start code by Rafael Payan
def int_validation(number):
	"""
		Checks if an input is an ineger between 0-99
	"""
	try:
		int(number)
	except ValueError:
		return False
	else: 
		if(0<=int(number)<=99):
			return int(number)
		else:
			return False
# End code by Rafael Payan
# Start code enhancements by Rafael Payan
# Added prompts for Tests
# Added the get GPS Values test
def runTests():
	"""
		tests some module functions
	"""

	print("Running a few tests:")
	# Average Test
	print("Test 1: Average")
	average = compute.gpsAverage(4, 5)
	print("average = ", average)
	# Login Test
	print("Test 2: Login")
	print(userLogin.login())
	
	print("Test 3: Read Satellites")
	print(readSat("longitude"))

	print("Test 4: Get GPS Values")
	print(gpsValue(34,54,"latitude"))

	print("All Tests Completed")
	input("Press Enter to continue...")
# End code enhacements by Rafael Payan

def start():
	"""
		logs the user in, and runs the app
	"""

	userName = userLogin.login()

	runApp(userName)


def runApp(userName):
	"""
		runs the app
	"""
	# initialize position parameters
	cX = cY = dX = dY = -1
	distance = 0
	# loop until user types q
	userQuit = False
	while (not userQuit):
# Start code enhancements by Rafael Payan
# Converted multi-print menu into a single print with a multi-line string variable
		# menu
		mainMenu = """
-------------------
Gladys West Map App
-------------------

current position     : x = {0} , y = {1}
destination position : x = {2} , y = {3}
distance             : {4}

[c] to set current position
[d] to set distantion position
[m] to map - which tells the distance
[t] to run module tests
[q] to quit
		"""
		print (mainMenu.format(cX,cY,dX,dY,distance))

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure
		# quit
		if firstChar == 'q':
			userQuit = True
# Added error handling for numbers not between 0 and 99
		#ask user for current position
		elif firstChar == "c":
				cX = input("Enter the current X coordinate:")
				while int_validation(cX) is False:
					print("Only integers between 0-99 are allowed.")
					cX = input("Enter the current X coordinate:")
				cY = input("Enter the current Y coordinate:")
				while int_validation(cY) is False:
					print("Only integers between 0-99 are allowed.")
					cY = input("Enter the current Y coordinate:")
		#ask user for destination position
		elif firstChar == "d":
				dX = input("Enter the destination X coordinate:")
				while int_validation(dX) is False:
					print("Only integers between 0-99 are allowed.")
					dX = input("Enter the destination X coordinate:")
				dY = input("Enter the destination Y coordinate:")
				while int_validation(dY) is False:
					print("Only integers between 0-99 are allowed.")
					dY = input("Enter the destination Y coordinate:")
		elif firstChar == "m":
					distance = compute.distance(compute.gpsAverage(cX,cY),compute.gpsAverage(dX,dY))
					print("-------------------")
					print("Distance: " + distance)
					print("-------------------")
		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
