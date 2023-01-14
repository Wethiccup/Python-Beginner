def main():
    name = input("What's your name? ")
    print(hello(name))  # prints the value


def hello(to="world"):
    return(f"hello, {to}")  # changed to a return to have a value


if __name__ == "__main__":
    main()