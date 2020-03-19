import math
from queue import LifoQueue
a = int(input())
stack = LifoQueue()
b = 0
for i in range(1, int(math.sqrt(a))+1, 1):
    if(a % i == 0):
        if a/i != i:
            stack.put(a/i)
        b = b + 1
print(b + stack.qsize())
