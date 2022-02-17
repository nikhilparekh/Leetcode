class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        res = []
        cur = []
        def dfs(index):
            if index>n+1:
                return
            if len(cur)==k:
                res.append(cur.copy())
                return
            
            cur.append(index)
            dfs(index+1)
            
            cur.pop()
            dfs(index+1)
        dfs(1)
        return res
            
            