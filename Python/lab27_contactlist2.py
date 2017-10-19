#Version 2 CRUD REPL
# Version 2
#
# Implement a CRUD REPL
#
# Create a record: ask the user for each attribute,
# add a new contact to your contact list with the attributes that the user entered.
#
# Retrieve a record: ask the user for the contact's name,
# find the user with the given name, and display their information
#
# Update a record: ask the user for the contact's name,
# then for which attribute of the user they'd like to update and the
# value of the attribute they'd like to set.
#
# Delete a record: ask the user for the contact's name,
# remove the contact with the given name from the contact list.
#
# Version 3
#
# When REPL loop finishes, write the updated contact info to the CSV file to be saved.



stop_words = ["stop", "quit", "no", "q", "n", "done", "exit", "end", "none"]
do_words = ["create", "new", "enter contact", "enter", "start"]
header = ["first name", "last name", "color", "fruit"]
new_contact = [] #the list the user input is appended to during the loop
contact_info = {} #individual dictionaries the new contact info is looped into.
contacts = [] #the main list the individual dictionaries are stored in.

while True:
    command = input("What is your command?").lower()
    if command in stop_words:
        print("Goodbye")
        break
    elif command in do_words:

        f_name = input("Enter your first name. >>> ")
        new_contact.append(f_name)
        l_name = input("Enter your last name. >>> ")
        new_contact.append(l_name)
        color = input("Enter your favorite color. >>> ")
        new_contact.append(color)
        fruit = input("Enter your favorite fruit. >>> ")
        new_contact.append(fruit)

        for i in range(len(header)):
            contact_info[header[i]] = new_contact[i]
        contacts.append(contact_info)
        print(contacts)
        #return contacts

    else:
        print("Command not recognized. Please enter 'create' or 'done'.").lower()

#find_words = ["retrive", "find", "get"]
# new_contact = {}
#     for i in range(len(header)):
#         new_contact[header[i]] = contact[i]
#     contacts.append(new_contact)
# print(contacts)
