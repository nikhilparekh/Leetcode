class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uni = set()
        seen = set()
        for i in nums:
            if i not in seen:
                uni.add(i)
                seen.add(i)
            elif i in uni:
                uni.remove(i)
        return list(uni)[0]