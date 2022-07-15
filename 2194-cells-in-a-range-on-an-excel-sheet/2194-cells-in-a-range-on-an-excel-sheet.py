class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        num = [int(s[1]),int(s[4])]
        c = [ord(s[0]),ord(s[3])]
        res = []
        x = c[0]
        while x<=c[1]:
            for i in range(num[0],num[1]+1):
                res.append(chr(x)+str(i))
            x+=1
        return res
        