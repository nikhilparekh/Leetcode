class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c= cmax = nums[0]
        for i in nums[1:]:
            c=max(i,c+i)
            cmax = max(c,cmax)
        return cmax
        