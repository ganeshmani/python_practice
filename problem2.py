

class Calculate:
    def __init__(self,num,check):
        self.num = num
        self.check = check
        self.divide(self.num,self.check)

    def divide(self,num,check):
        if num % 2 == 0:
            print("Number is even number")
        if num % check == 0:
            print(str(num)+" is divided by "+str(check))    
        if num % 4 == 0:
            print(str(num)+" is multiple of 4")    


print("Enter a Number")
num = int(input())
print("Enter dividend")
check = int(input())

value = Calculate(num,check)


