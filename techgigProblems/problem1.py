


def findPair():
    n = int(input())

    array = [int(x) for x in input().split()]

    res = int(input())
    counter = 0
    for i in range(len(array)):
        for j in range(len(array) - i):

            if array[i] + array[j+i] == res:
                counter += 1

    print(str(counter))










findPair()