# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name

# first, last = name.split(" ")

# Remove white space from string and capitalize user's name (String method)
# name = name.strip().title()

# Capitalize user's name
# name = name.capitalize() # Capitalize only does first name by default

# name = name.title() # Capitalize all word like a title
# Say hello to user

""" # String formatting and concatenation
print("Hello, " + name)

print("Hello,", name) # When you pass multiple arguments to print, spaces are auto added with sep argument
print("Hello,", name, sep="???") # Changes "sep" to ??? instead of the default " "

print("Hello, ", end="") # Overriding default value for end which is end=" " according to official python documentation
print(name)
"""
print(f"Hello, {first}")
