

class Divisor:
    def __init__(self,number):
        self.number = number
        

    def calculate(self):
        values = []
        for x in range(1,self.number):
            if(self.number % x == 0):
                values.append(x)
        self.printValues(values)

    def printValues(self,values):
        print(values)

print("Enter a Number")
val = int(input())

number = Divisor(val)

number.calculate()


