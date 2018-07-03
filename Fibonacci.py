
def Fibonacci(number):
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


print Fibonacci(10)
