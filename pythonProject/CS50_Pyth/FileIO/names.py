# names = []

# for _ in range(3):
#     names.append(input("What's your name? "))  # Adds names to the list

# for name in sorted(names):
#     print(f"Hello, {name}")

# name = input("What's your name? ")

# # ! Make a file with names in a new line list
# # the name of the file I want and "w" to write to it "a" is append
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# #! Read an Existing File
# with open("names.txt", "r") as file:
#     lines = file.readlines()  # reads all the lines

# for line in lines:
#     print(f"hello, {line.strip()}")  # uses strip to let print do all the work

# #! Read an Existing File 2.0
# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

# #! Read and sort an Existing File
# names = []

# with open("names.txt") as file:  # dont need r if reading it is default
#     for line in file:
#         names.append(line.rstrip()) # writes to the names[] list from the file

# for name in sorted(names): # sorts and prints each element in the list
#     print(f"hello, {name}")

#! Read and sort an Existing File 2.0
with open("names.txt") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")
