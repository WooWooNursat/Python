n = int(input())
a = []
for i in range(0, n, 1):
    a.append(int(input()))
for i in range(1, n, 1):
    if a[i] > 0 and a[i-1] > 0 or a[i] < 0 and a[i-1] < 0:
        print('YES')
        break
    elif i == n - 1:
        print('NO')