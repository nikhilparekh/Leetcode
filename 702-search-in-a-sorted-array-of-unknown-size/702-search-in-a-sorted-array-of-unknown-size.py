# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo = 0
        hi = 10**4
        while lo<hi:
            mid = lo+(hi-lo)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)<target:
                lo=mid+1
            else:
                hi = mid
        return -1
            