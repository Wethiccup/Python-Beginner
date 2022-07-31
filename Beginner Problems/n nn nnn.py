def main():
    x = int(input("Enter a single digit integer: "))

    print(n_nn_nnn(x))

def n_nn_nnn(n):
    n1 = int("{}".format(n))
    n2 = int("{}{}".format(n,n))
    n3 = int("{}{}{}".format(n,n,n))

    result = n1 + n2 + n3
    return result
main()
