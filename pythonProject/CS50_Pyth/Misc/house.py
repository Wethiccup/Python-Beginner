name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # If nothing is applicable to case. Catch all
        print("Who?")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")