import math
from queue import LifoQueue
a = int(input())
stack = LifoQueue()
for i in range(1, int(math.sqrt(a))+1, 1):
    if(a % i == 0):
        if a/i != i:
            stack.put(a/i)
        print(i)
while stack.empty() != 1:
    print(int(stack.get()))
