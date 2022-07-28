class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for idx,val in enumerate(nums):
            if target-val in di:
                return [di[target-val],idx]
            else:
                di[val] = idx
            # print(di)