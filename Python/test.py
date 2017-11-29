
find_words = ["find", "get", "look", "search", "retrive"]
stop_words = ["stop", "quit", "no", "q", "n", "done", "exit", "end", "none"]
do_words = ["create", "new", "enter contact", "enter", "start"]
header = ["first name", "last name", "color", "fruit"]
contact_info = {}  # individual dictionaries the new contact info is looped into.
contacts = [] #the main list the individual dictionaries are stored in.
new_contact = []  # the list the user input is appended to during the loop

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

    # elif command in find_words:
    #     who_for = input("Enter the first name of the person you are looking for >>> ")
    #     if contact_info[str(who_for)] in contact_info in contacts:
    #         print("found it")


    else:
        print("Command not recognized. Please enter 'create' or 'done'.").lower()
