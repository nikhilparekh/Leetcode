class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        # c = 1
        res = ""
        temp = ""
        for i in reversed(str(n)):
            if len(res)%4==0:
                res=res+"."
            res=res+i
        for i in reversed(res):
            temp=temp+i
        return temp[:-1]
            