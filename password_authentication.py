# Importing the getpass module for secure password input
import getpass

# Database with username-password pairs
database = {"admin": "123456", "host": "123123123"}

# Getting the username and password from the user
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")

# Iterating through the database to verify the credentials
for i in database.keys():
    # Checking if the username exists in the database
    if username == i:
        # Using a while loop to repeatedly ask for the password until it matches the one in the database
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        # Breaking out of the loop once the password is verified
        break

# Printing a message indicating successful verification
print("Verified")
