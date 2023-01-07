# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# while True:  # Adds a way to loop the function until an integer is called
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break  # Break out of loop because integer was called and else is used
#
# print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")
#
# def get_int():
#     while True:  # Adds a way to loop the function until an integer is called
#         try:
#             return int(input("What's x? "))  # Return also works as a break and returns the value.
#             # Can put into one line without defining variable
#         except ValueError:
#             print("x is not an integer")
#
# main()

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:  # Adds a way to loop the function until an integer is called
        try:
            return int(input(prompt))  # Return also works as a break and returns the value.
            # Can put into one line without defining variable
        except ValueError:
            pass  # Still catches the error but "passes" on saying anything; just loops


main()
