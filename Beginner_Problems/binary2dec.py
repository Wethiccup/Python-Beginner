def main():
    print("1. Binary to Decimal\n2. Decimal to Binary")

    decision = input("Pick an option: ")

    if decision == "1":
        n = input("Enter binary: ")
        binary2dec(n)
    if decision == "2":
        n = input("Enter a decimal: ")
        decimal2bin(n)


def binary2dec(x):
    num_list = [0]
    num_list = [eval(i) for i in x]
    print(x)
    print(num_list)
    # for i in range(len(num_list)):
    if all(num_list) != "1" or "0":
        print(num_list)
        print("What is entered is not binary")

    else:
        print("balls")
        for i in range(x):
            if int_list(x):
                return


if __name__ == "__main__":
    main()
