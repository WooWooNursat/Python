import math
a = int(input())
for i in range(2, int(math.sqrt(a)) + 1, 1):
    if(a % i == 0):
        print(i)
        break
    if i == int(math.sqrt(a)):
        print(a)