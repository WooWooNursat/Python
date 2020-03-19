n = int(input())
a = []
for i in range(0, n, 1):
    a.append(int(input()))
for i in range(0, n, 1):
    if a[i] % 2 == 0:
        print(a[i])
