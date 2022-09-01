import math


def rad2deg(n):
    d = (n * (180 / math.pi))
    return d


def deg2rad(n):
    r = (n * (math.pi / 180))
    return r


def main():
    x = 0
    choice1 = input("What would you like to convert:"
                    " \n1. Radians to Degrees\n2. Degrees to radians \nEnter choice here: ")
    if choice1 == "1":
        x = float(input("Enter your angle here: "))
        print(rad2deg(x))
    else:
        x = float(input("Enter your angle here: "))
        print(deg2rad(x))


main()