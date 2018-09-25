def mergeArr(arr1, arr2):
    idx1 = 0
    idx2 = 0
    res = []
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] <= arr2[idx2]:
            res.append(arr1[idx1])
            idx1 += 1
        elif arr1[idx1] > arr2[idx2]:
            res.append(arr2[idx2])
            idx2 += 1

    if idx1 == len(arr1):
        res.extend(arr2[idx2:])

    if idx2 == len(arr2):
        res.extend(arr1[idx1:])
    return res
print mergeArr([1,4,8],[2,5,7])
print [1,4,8].extend([2,5,7])
