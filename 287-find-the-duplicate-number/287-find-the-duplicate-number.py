class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if nums[abs(num)-1]<0:
                return abs(num)
            else:
                nums[abs(num)-1] = -nums[abs(num)-1]
            # print(nums)