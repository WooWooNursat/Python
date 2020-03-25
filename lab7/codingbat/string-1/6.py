def first_two(str):
    if len(str) < 1:
        return ""
    elif len(str) < 2:
        return str[0]
    else:
        return (str[0] + str[1])
