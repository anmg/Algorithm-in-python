# _*_ encoding:utf-8 _*_
#3,4,5,6,1,3,8

def qsort(arr, low, high):
    if low >= high:
        return

    value = arr[low]    
    l = low
    r = high
    while l < r:
        while l < r and value < arr[r]:
            r-=1
        arr[l] = arr[r] 

        while l < r and value >= arr[l]:
            l+=1
	arr[r] = arr[l]

    arr[l] = value

    qsort(arr, low, l-1)
    qsort(arr, l+1, high)
    print arr

qsort([3,4,5,6,1,3,8], 0, 6)
