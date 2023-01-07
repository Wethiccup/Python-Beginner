# import sys  # sys is used a lot for the terminal and is implemented in it for input
# rather than within the code being run
#
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# import sys
# # Can use print, but sys allows for quick and separate error checking from the program
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#
# print("Hello, my name is", sys.argv[1])

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:  # [1:] is a slice that goes from element one to the end
    print("Hello, my name is", arg)
