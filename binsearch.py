def binsearch(arr, start, end, value):
    l = start
    u = end-1
    while(l < u):
        mid = l+(u-l)/2+1
        if value < arr[mid]:
            u = mid
        elif value > arr[mid]:
            l = mid
        else:
            return mid

print binsearch([0,1,2,5,6,8,9], 0, 6, 2)

