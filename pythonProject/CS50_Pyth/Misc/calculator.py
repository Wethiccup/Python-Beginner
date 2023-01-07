""""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)

# z = round(x / y, 2)
# print(f"{z:,}") # :, makes it so the commas are added to larger number in thousands (Format)
# print(f"{z:.2f}") # rounds to # of digits
"""

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)  # n * n, n ** 2

main()