

print("Enter a String")
value = str(input())


def isPalindrome(value):
    
    for i in range(0,int(len(value)/2)):
        if(value[i] != value[len(value) -i-1]):
            return False
    return True

    
result = isPalindrome(value)

print(result)