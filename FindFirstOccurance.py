def findFirst(arr,k):
    lo = 0
    hi = len(arr)-1
    while(lo<hi):
        mid = lo+(hi-lo)//2
        if arr[mid]==k:
            hi=mid
        elif arr[mid]>k:
            hi=mid
        else:
            lo=mid+1
    return lo



arr = [1,2,2,2,2,3,4,5,5,5,5,5,5,5,5,5,5,5,6]
print(findFirst(arr,5))
