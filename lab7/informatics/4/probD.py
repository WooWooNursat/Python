n = int(input())
a = []
k = 0
for i in range(0, n, 1):
    a.append(int(input()))
for i in range(1, n, 1):
    if a[i] > a[i-1]:
        k = k + 1
print(k)
