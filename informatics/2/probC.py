a = int(input())
b = int(input())

if int(a/1000) == a%10 and int(a/100%10) == int(a/10%10):
    a = 1
else:
    a = 0
if b == a or b != 1 and a != 1:
    print('YES')
else:
    print('NO')