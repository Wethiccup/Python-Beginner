def _largest(arr):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def main():
    arr = [15, 25, 32, 15, 74]

    largest_num = _largest(arr)

    print(largest_num)


main()
