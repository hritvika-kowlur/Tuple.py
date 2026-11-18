
groups = []  

for i in range(5):
    print("Enter details for group", i + 1)

    groupname = input("Group name: ")
    size = input("Size of the group: ")
    date = input("Date of the competition: ")
    venue = input("Venue: ")
    medal = input("Type of medal won: ")


    record = (groupname, size, date, venue, medal)


    groups.append(record)

print("All group records:")
for i in groups:
    print(i)