print("Hello, welcome to NetworkChuck Coffee!!!!")

name = input("What is your name?\n")



if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done?\n"))

    if evil_status == "Yes" and good_deeds < 4:

        print("You're not welcome here evil " + name + "!! Get out!")
        exit()
    else:
        print("Hello " + name + ", thank you so much for coming in today!")
else:
    print("Hello " + name + " thank you so much for coming in today.\n\n\n")

exit()

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

order = input(name + ", what would you like from our menu today? Here is what we are serving\n" + menu + "\n")

quantity = int(input("How many coffees would you like?\n"))

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    whipped_cream = input("Would you like extra Whipped Cream? Y/N\n")
    if whipped_cream == "Y":
        price = 11
    else:
        price = 9

elif order == "Cappucino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    price = 0
print(price*quantity)

