def main():
    # Write code here

    num = int(input())
    val = [int(x) for x in input().split()]
    maxCount = 0
    index = -1
    for i in range(num):
        counter = 0
        for j in range(num):
            if val[i] == val[j]:
                counter += 1

        if counter > maxCount:
            maxCount = counter
            index = i
    if maxCount > num / 2:
        print(str(val[index]),end='')


main()
