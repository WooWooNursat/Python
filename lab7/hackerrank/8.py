from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    l = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        l.append([name, score])
    min1 = 99999999
    min2 = 99999999
    for i in range(len(l)):
        if min1 > l[i][1]:
            min2 = min1
            min1 = l[i][1]
        elif min2 > l[i][1] and min1 < l[i][1]:
            min2 = l[i][1]
    names = []
    for i in range(len(l)):
        if l[i][1] == min2:
            names.append(l[i][0])
    names.sort()
    for i in range(len(names)):
        print(names[i])
