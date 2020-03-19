a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min(a, b, c, d):
    if a > b:
        if c > d:
            if b > d:
                return d
            else:
                return b
        else:
            if b > c:
                return c
            else:
                return b
    else:
        if c > d:
            if a > d:
                return d
            else:
                return a
        else:
            if a > c:
                return c
            else:
                return a
print(min(a,b,c,d))