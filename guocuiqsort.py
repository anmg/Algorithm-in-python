def qsort(arry,left,right):
    i=left
    j=right
    if i>=j:
        return arry
    key=arry[i]
    while i<j:
        while i<j and arry[j]>=key:
	    j=j-1
	arry[i]=arry[j]
        while i<j and arry[i]<=key:
	    i=i+1
        arry[j]=arry[i]
    arry[i]=key
    
    qsort(arry,left,i-1)
    qsort(arry,j+1,right)
    return arry


a=[2,1,3,5,8,4,9,0]
print a
qsort(a,0,7)

