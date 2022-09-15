class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        def dfs(cur,i):
            if i<len(nums):
                
                # res.append(cur.copy())
                cur.append(nums[i])
                if cur not in res:
                    res.append(cur.copy())
                dfs(cur,i+1)
                
                cur.pop()
                
                dfs(cur,i+1)
        dfs([],0)
        res.append([])
        return res