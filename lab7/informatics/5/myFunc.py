n = int(input())
def fact(n):
    k = 1
    while n:
        k = k * n
        n = n - 1
    return k
print(fact(n))