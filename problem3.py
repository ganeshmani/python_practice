

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Enter a number")
value = int(input())
b = [num for num in a if num < value]

print(b)