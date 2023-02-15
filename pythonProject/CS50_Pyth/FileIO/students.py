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

# #! Interpretes the CVS file 4.0 with sorting
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} # simplifies the dictionary

#         # student = {}
#         # student["name"] = name
#         # student["house"] = house

#         students.append(student)

# def get_name(student):
#     return student["name"]

# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}") # use single quotes to differentiate

# #! Using Lambda for Sorting the CSV file
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}  # simplifies the dictionary
#         students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# #! Using Lambda for Sorting the CSV file 2.0
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# #! Using Lambda for Sorting the CSV file 3.0
# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# #! Write the CSV file
# import csv

# name = input("What is your name? ")
# home = input("Where is your home? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

#! Write the CSV file 2.0

import csv

name = input("What is your name? ")
home = input("Where is your home? ")
# With Dict Writer the order does not matter

with open("students.csv", "a", newline="\n") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})  # Order here
