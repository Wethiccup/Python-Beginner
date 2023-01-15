import math


def main():
    x = float(input("Enter the radius (cm) of the cylinder: "))
    y = float(input("Enter the height (cm) of the cylinder: "))

    print(weight(x, y))


def weight(r, h):

    rmeter = float(r / 100)
    hmeter = float(h / 100)

    volume = (math.pi) * (rmeter**2) * hmeter
    mass = 1000 * volume

    return mass


main()
