def main():
    print("1. Binary to Decimal\n2. Decimal to Binary")

    decision = input("Pick an option: ")

    if decision == "1":
        n = input("Enter binary: ")
        print(binary2dec(n))
    if decision == "2":
        n = input("Enter a decimal: ")
        decimal2bin(n)


def binary2dec(x):
    decimal = 0
    for i in range(len(x)):
        decimal += int(x[i]) * (2 ** (len(x) - i - 1))
    return decimal


if __name__ == "__main__":
    main()
