# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
for i in range(n):
    a = int(input())
    flag = 0
    if a == 1:
        print("Not prime")
    elif a==2:
        print("Prime")
    else:
        if a%2 == 0:
            flag = 1
        else:  
            for i in range(3,math.floor(math.sqrt(a))+1,2):
                if a%i == 0:
                    flag = 1
                    break
        if flag == 0:
            print("Prime")
        else:
            print("Not prime")
