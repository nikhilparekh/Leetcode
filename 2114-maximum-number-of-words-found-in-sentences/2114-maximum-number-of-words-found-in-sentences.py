class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cmax = 0
        # for i in sentences:
        #     j = i.split(" ")
        #     if len(j)>cmax:
        #         cmax=len(j)
        # return cmax
        for i in sentences:
            c = 0
            for j in i:
                if j==" ":
                    c+=1
            cmax = max(cmax,c+1)
        return cmax
                    