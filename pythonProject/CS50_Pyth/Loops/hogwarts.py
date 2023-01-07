students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}, # * Keyword None
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# students = { # * Dictionary
#     "Hermione": "Gryffindor", 
#     "Harry": "Gryffindor", 
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")

# print(students["Hermione"]) # * Dicts use words instead of number
# print(students["Harry"])
# print(students["Ron"])
#print(students["Draco"])

# students = ["Hermione", "Harry", "Ron", "Draco"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# for student in students:
#     print(student)