class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        words = text.split(" ")
        spaces = text.count(" ")
        
        word = []
        for i in words:
            if i!="":
                word.append(i)
        if len(word)==1:
            res = word[0]+" "*spaces
            return res
        space = spaces//(len(word)-1)
        res = word[0]
        for i in word[1:]:
            res = res+" "*space
            res = res+i
        extra = spaces%(len(word)-1)
        res = res+" "*extra
        print(extra,space)
        return res
        
        