# -*- coding: utf-8  -*-
def Fabonacci(number):
    a=0
    b=1
    print a
    print b

    while(b<number):
        temp = a
        a = b
        b = b+temp
        print b
Fabonacci(5)

def jumpfloor(number):
    if number == 0:
        return  0
    if number == 1:
        return  1
    if number == 2:
        return 2

    a = 1
    b = 2
    while number>2:
        temp = a
        a = b
        b = b + temp
        number = number -1

    return b

# print jumpfloor(1)
# print jumpfloor(2)
# print jumpfloor(3)
# print jumpfloor(4)
# print jumpfloor(5)

def get_Fibonacci_byidx(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    arr = [0, 1]
    a = 0
    b = 1
    while len(arr) <= number:
        temp = a
        a = b
        b = b + temp
        arr.append(b)

    if len(arr)> number:
        return arr[number]


print get_Fibonacci_byIdx(10)
