a = int(input())
b = int(input())
def power(a,b):
    n = a
    for i in range(1, b, 1):
        n = n * a
    return n
print(power(a, b))