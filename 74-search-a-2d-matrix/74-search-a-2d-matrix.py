class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr):
            l = 0
            h = len(arr)
            while l<h:
                mid = l+(h-l)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    l = mid+1
                else:
                    h = mid
            return False
        
        for i in matrix:
            if binarySearch(i):
                return True
        return False