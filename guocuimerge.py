def merge(arry1,arry2):
    l1=len(arry1)
    l2=len(arry2)
    arry3=[]
    i=0
    j=0
    while(i<l1 and j<l2):
        
        if arry1[i]<=arry2[j]:
            arry3.append(arry1[i])
            i=i+1
        elif arry1[i]>=arry2[j]:
            arry3.append(arry2[j])
            j=j+1
    if i==l1:
        arry3.extend(arry2[j:])
    if j==l2:
        arry3.extend(arry1[i:])
    return arry3
a=[2,3,6]
b=[1,4,5,6,7,8,9]
print merge(a,b)
