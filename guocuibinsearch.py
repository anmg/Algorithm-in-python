def binsearch(arry,start,end,value):
    l=end
    r=start
    mid=l+(r-l)/2
    while l<=r:
        if value < arry[mid]:
           r=mid
        if value > arry[mid]:
	   l=mid
    return mid
print binsearch([2,3,4,6,7,8,9,11],0,8,7)
