# Trying to make a binary code a decimal

def binaryToDecimal(binary):
    decimal, a, c = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, a)
        binary = binary // 10
        a += 1
    print(decimal)

print("This program will convert a binary code into decimal format \n")

binary_code = input("Enter a binary code up to eight digits:\n")

n = str(binary_code)

b = '10'
count = 0

for i in n:
    if i not in b:
        count = 1
        break
    else:
        pass
if count == 1:
    print("The binary code given does not only contain 0s and 1s")
else:
    binaryToDecimal(binary_code)


