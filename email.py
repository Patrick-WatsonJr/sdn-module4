"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""

#curly brackets indicate this is a start of dictionary
addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#asks users to for email address to enter
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
#Asks user to input another address
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#prints email addresses    
print(addresses)

#print emails

# url to add new user to the room
add_membership_url = 'https://web.webex.com/spaces/aHR0cHM6Ly9jb252LWEud2J4Mi5jb20vY29udmVyc2F0aW9uL2FwaS92MS9jb252ZXJzYXRpb25zL2U2OTJkOWMwLTBlMjMtMTFlYi05MjZiLTg3N2ZlMzEyNjUxYw==
'

print
for email in emails: # every email address in the lines list
    try:
        param = {
        "roomId": SDN Postman Room,
        "personEmail": destinijackson2013@yahoo.com,
        }