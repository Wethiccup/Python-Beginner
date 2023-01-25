def dollars_to_cents(dollar_value):
    total = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    while dollar_value >= 25:
        quarters += 1
        dollar_value -= 25
    while dollar_value >= 10:
        dimes += 1
        dollar_value -= 10
    while dollar_value >= 5:
        nickles += 1
        dollar_value -= 5
    while dollar_value >= 1:
        pennies += 1
        dollar_value -= 1
    total = pennies + nickles + dimes + quarters

    coins = [quarters, dimes, nickles, pennies]

    return coins


def main():
    dollar_amount = int(input("Enter a dollar amount you would like to convert: "))
    coins = dollars_to_cents(dollar_amount)
    print(
        f"There are {coins[0]} quarters, {coins[1]} dimes, {coins[2]} nickles, and {coins[3]} pennies"
    )


if __name__ == "__main__":
    main()
