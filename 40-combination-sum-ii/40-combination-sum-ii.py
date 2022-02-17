class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # seen = []
        candidates.sort(reverse=True)
        res = []
        def dfs(index,cur,target):
            if target==0:
                # if cur not in seen:
                # seen.append(cur)
                res.append(cur.copy())
                
            if target<=0:
                return
            prev = -1
            for i in range(index,len(candidates)):
                if candidates[i]== prev:
                    continue
                cur.append(candidates[i])
                dfs(i+1,cur,target-candidates[i])

                cur.pop()
                # dfs(index+1,cur,total)
                prev = candidates[i]
        
        
        dfs(0,[],target)
        return res