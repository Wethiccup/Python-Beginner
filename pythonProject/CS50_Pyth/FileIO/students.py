 # ! Interpretes the CVS file
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")  # splits the csv line into a list
#         print(f"{row[0]} is in {row[1]}")  # prints the student's name and class


#  #! Interpretes the CVS file 2.0
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")  # splits the csv line into a list
#         print(f"{name} is in {house}")  # prints the student's name and class

# #! Interpretes the CVS file 3.0 with sorting
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # simplifies the dictionary

        # student = {}
        # student["name"] = name
        # student["house"] = house

        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}") # use single quotes to differentiate


