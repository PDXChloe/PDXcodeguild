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




find_words = ["find", "f"]
stop_words = ["stop", "quit", "no", "q", "n", "done", "exit", "end", "none"]
do_words = ["create", "new", "enter contact", "enter", "start"]
header = ["first name", "last name", "color", "fruit"]


contacts = [] #the main list the individual dictionaries are stored in.



while True:
    command = input('What is your command? "find" or "f", "quit" or "q", "create" or "c", "delete" or "d".').lower()
    if command == 'quit' or command == 'q':
        print('Goodbye')
        break

    elif command == 'create' or command == 'c':
        new_contact = []  # the list the user input is appended to during the loop
        contact_info = {}  # individual dictionaries the new contact info is looped into.

        for i in range(len(header)):
            attr = input('Enter your ' + header[i] + '. >>>')
            contact_info[header[i]] = attr
            #contact_info[header[i]] = new_contact[i]
        contacts.append(contact_info)
        print(contacts)

    elif command in find_words:
        who_for = input('Enter the first name of the person you are looking for >>> ')
        for i in range(len(contacts)):
            if who_for == contacts[i]['first name']:
                print('Its here: ' + str(contacts[i]))
                while True:

                    sub_command = input('Would you like to edit this contact, "Y" or "N"')
                    if sub_command == 'Y' or sub_command == 'y':
                        attribute = input('Enter edit: "first name", "last name", "color" or "fruit"?').lower()
                        value = input('Change ' + attribute + ' to:  ')
                        contacts[i][attribute] = value
                        print(str(contacts[i]))


                    if sub_command == 'N' or sub_command == 'n':
                        print('Done editing ' + str(contacts[i]) + '.')
                        break

    elif command == 'delete' or command == 'd':
        who_for = input('Enter the first name of the contact you wish to delete. >>> ')
        for contact in contacts:
            if who_for == contact['first name']:
                assurance = input('Are you sure you want to permanently delete ' + str(
                    contact['first name']) + ' from database? "Y" or "N"')
                if assurance == "Y" or assurance == "y":
                    contacts.remove(contact)
                    print('Contact has been deleted')
                    print(contacts)
                    break
                if assurance == 'N' or assurance == 'n':
                    break

    else:
        print('Command not recognized. Please enter "create" or "done".').lower()






