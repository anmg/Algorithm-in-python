def binsearch(arr, start, end, value):
    l = start
    u = end
    while(l < u):
        mid = l+(u-l)/2+1
        if value < arr[mid]:
            u = mid
        elif value > arr[mid]:
            l = mid
        else:
            return mid

print binsearch([0,1,2,5,6,8,9], 0, 6, 9)

def binsearch_all(arr, value):
    l = 0
    r = len(arr)
    while l <= r:
        mid = (r+l)/2
        if value < arr[mid]:
            r = mid - 1
        elif value > arr[mid]:
            l = mid + 1
        else:
            return mid
    return -1
    
print binsearch_all([0,1,2,5,6,8,9], 4)
