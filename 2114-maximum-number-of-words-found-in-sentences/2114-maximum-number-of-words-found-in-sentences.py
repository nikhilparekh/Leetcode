class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cmax = 0
        for i in sentences:
            j = i.split(" ")
            if len(j)>cmax:
                cmax=len(j)
        return cmax