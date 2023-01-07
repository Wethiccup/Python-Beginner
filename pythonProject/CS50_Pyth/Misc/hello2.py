def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):  # defining the variable as value makes it the default if the programmer doesn't call a value
    print("Hello,", to)


main()
