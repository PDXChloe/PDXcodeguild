


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    #print(lines)

header = lines[0].split(",")

#convert into a list of dictionaries, one dictionary for each user.
contacts = []
for i in range(1, len(lines)):
    contact = lines[i].split(",")
    # print(contact)
    #new_contact = {header[0] : contact[0], header[1] : contact[1], header[2] : contact[2]}
    new_contact = {}
    for i in range(len(header)):
        new_contact[header[i]] = contact[i]
    contacts.append(new_contact)
print(contacts)


