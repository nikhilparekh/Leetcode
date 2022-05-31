class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        r = 2**k
        res = set()
        i = 0
        cur = ""
        while i<len(s):
            cur+=s[i]
            if len(cur)==k:
                res.add(cur)
                cur = cur[1:]
            i+=1
        if len(res)==r:
            return True
        return False
            
        