class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        r= []
        r1 = []
        di = {}
        for i in words1:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        for i in di:
            if di[i]==1:
                r.append(i)
        di = {}
        for i in words2:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        for i in di:
            if di[i]==1:
                r1.append(i)
        print(r,r1)
        res = [i for i in r if i in r1]
        return len(res)