def bubble_sort(arry):
    num=len(arry)
    for i in range(num-1):
        for j in range(num-i-1):
            if arry[j]<arry[j+1]:
                arry[j],arry[j+1]=arry[j+1],arry[j]
    return arry
print bubble_sort([2,6,7,9,1,4])
