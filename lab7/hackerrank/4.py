from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0, n, 1):
        print( i * i)
