class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        uni = set()
        for i in nums:
            if i not in uni:
                uni.add(i)
            else:
                uni.remove(i)
        return list(uni)