from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    summa = 0
    for i in range(len(student_marks[query_name])):
        summa = summa + student_marks[query_name][i]
    print("{0:.2f}".format(summa/len(student_marks[query_name])))
