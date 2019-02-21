import random


# randomly generated list 
list1 = random.sample(range(30),10)

list2 = random.sample(range(25),10)


print(*[item for item in list1 if item in list2],sep='\n')


       
