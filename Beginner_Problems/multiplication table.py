# Make a multiplication table for a number


def main():
    num = int(input("Enter a number: "))
    mult_table(num)


def mult_table(num):
    table = lambda num: print(f"{num} x {i} equals {num * i}")

    for i in range(1, 11):
        table(num)


if __name__ == "__main__":
    main()
