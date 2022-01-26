class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text)<7:
            return 0
        di = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in di:
                di[i]+=1
        di['l']//=2
        di['o']//=2
        mn = float("inf")
        for i in di:
            if di[i]<mn:
                mn = di[i]
        return mn
            