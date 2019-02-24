
import random

def getData():

    random_num = random.randrange(1,9)
    print("Guess the Number(Hint : number between 1 to 9")
    value = int(input())
    print(random_num)
    return  random_num,value

def checkAnswer(randomnum,value):
    if value == randomnum:
        print("yay!!!! Correct Answer")
    if value < randomnum:
        print("Guessed number is lower than Answer")
    elif value > randomnum:
        print("Guessed number is higher than Answer")
    random_num, value = getData()
    checkAnswer(random_num, value)

random_num,value = getData()


checkAnswer(random_num,value)
