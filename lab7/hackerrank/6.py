from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    arr = []
    for i in range(0, x+1, 1):
        for j in range(0, y+1, 1):
            for k in range(0, z+1, 1):
                if i + j + k != n:
                    arr.append([i,j,k])
    print(list(arr))
