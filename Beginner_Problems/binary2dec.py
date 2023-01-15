from int_to_list import int_list


def main():
    print("1. Binary to Decimal\n2. Decimal to Binary")

    decision = input("Pick an option: ")

    if decision == "1":
        n = int(input("Enter binary: "))
        binary(n)
    if decision == "2":
        n = int(input("Enter a decimal: "))
        decimal(n)


def binary(x):
    new = int_list(x)
    print(new)
    for i in range(x):
        if i != 0 and 1:
            print("What is entered is not binary")
            exit()
        else:
            for i in range(x):
                if int_list(x):
                    return


if __name__ == "__main__":
    main()
