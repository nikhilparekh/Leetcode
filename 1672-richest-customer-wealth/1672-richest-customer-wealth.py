class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cmax = float("-inf")
        for i in accounts:
            if sum(i)>cmax:
                cmax = sum(i)
        return cmax