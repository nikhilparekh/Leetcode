class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] not in seen:
                    if abs(nums[j]-nums[i])>k:
                        break
                    elif abs(nums[j]-nums[i])==k:
                        seen.add(nums[i])
                        # print(nums[j],nums[i])
                        count+=1
                        break
        return count
                    