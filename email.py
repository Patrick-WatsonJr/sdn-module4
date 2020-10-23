"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""


addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#asks users to for email address to enter
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
#Asks user to input another address
#If the user has another email address, they enter it, if not the script ends and prints
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#prints email addresses    
print(addresses)
