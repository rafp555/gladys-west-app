import io
#import regular expression module
import re

"""
	Student: Chunhua Liu and Rafael Payan
	Module: gladysUserLogin
	Description: This module does establishes the login proces to use the app.
"""
# start code enhancements by Rafael Payan
# enhanced  Chunhua Liu's original code to include password checking and error handling
def login():
	"""
		This function takes an input and validates that it is an e-mail
		Next, it checks that the password is correct and logs the user in if true.
	"""
	while True:
		loginInput = input("Enter an e-mail to login:")
		password = "Python1"
		passwordInput = ""
		email_format = str(r"(^[a-zA-Z0-9'_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
		if re.match(email_format, loginInput):
			print("Welcome, " + loginInput + "!")
			while passwordInput != password:
				passwordInput = input("Enter your password *Password for demo is: Python1* : ")
				if passwordInput != password:
					print("The password is incorrect.")
			return loginInput
		else:
			print("The e-mail was not valid")
#end code enhancements by Rafael Payan