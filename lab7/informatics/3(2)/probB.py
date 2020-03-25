import math
a = int(input())
i = 2
while i <= math.sqrt(a):
    if(a % i == 0):
        print(i)
        break
    if i == int(math.sqrt(a)):
        print(a)
    i = i + 1