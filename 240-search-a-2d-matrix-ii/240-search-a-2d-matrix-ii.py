class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(arr):
            lo = 0
            hi = len(arr)
            while lo<hi:
                mid = lo+(hi-lo)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    lo =mid+1
                else:
                    hi=mid
            return False
        for i in matrix:
            if binary(i):
                return True
        return False