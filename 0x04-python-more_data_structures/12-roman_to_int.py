#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    n = []
    for i in roman_string:
        if i == 'I':
            n.append(1)
        if i == 'V':
            n.append(5)
        if i == 'X':
            n.append(10)
        if i == 'L':
            n.append(50)
        if i == 'C':
            n.append(100)
        if i == 'D':
            n.append(500)
        if i == 'M':
            n.append(1000)
    result = 0
    bool = False
    for x in range(len(n)):
        if bool is True:
            bool = False
            continue
        if (x + 1) < len(n):
            if n[x] < n[x + 1]:
                result += n[x + 1] - n[x]
                bool = True
                continue
            else:
                result += n[x]
        if (x + 1) == len(n):
            result += n[x]
    return result
