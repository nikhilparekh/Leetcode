def subArray(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            res.append(arr[i:j+1])
    return res


arr = [-1,4,7,2]

print(subArray(arr))