class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bin(num, ans):
            if num>=1:
                
                bin(num//2,ans)
                ans.append(num%2)
            return ans
        res = []
        for i in range(n+1):
            x = bin(i,[])
            res.append(x.count(1))
        return res                