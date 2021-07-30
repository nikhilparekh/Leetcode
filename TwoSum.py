def TwoSum(arr,k):
    di = {}
    for idx, num in enumerate(arr):
        if k-num in di:
            return idx, di[k-num]
        di[num] = idx
    return -1


arr = [1,2,7,3,0]

print(TwoSum(arr,9))