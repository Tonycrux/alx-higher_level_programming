#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    average = 0
    result = 0
    for i in my_list:
        result += i[0] * i[1]

        average += i[1]

    return result / average
