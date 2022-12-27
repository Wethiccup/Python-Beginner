# Find sum of elements in an array

def _sum(array):
    total = 0
    for i in array:
        total += i

    return(total)

def main():
    array = [12, 12, 1]

    ans = _sum(array)

    print(ans)

main()