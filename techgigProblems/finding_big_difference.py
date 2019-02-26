
def main():

 n = int(input())
 res = [int(x) for x in input().split()]
 if(len(res) != n):
     exit()
 result = 0
 for i in range(n):
     for j in range(n - i):

        if abs(res[i] - res[j+i]) > result:
            result =  abs(res[i] - res[j+i])


 print(str(result),end='')



main()


