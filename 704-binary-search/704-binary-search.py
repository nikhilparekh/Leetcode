class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums)
        lo = 0
        while lo<hi:
            mid = lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                hi = mid
            else:
                lo=mid+1
        return -1
        