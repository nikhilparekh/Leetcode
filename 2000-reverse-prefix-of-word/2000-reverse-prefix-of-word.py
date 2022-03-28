class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        j=0
        for i in word:
            if i!=ch:
                j+=1
            else:
                break
        # print(j)
        res = ""
        temp = j
        while temp!=-1:
            res+=word[temp]
            temp-=1
        res+=word[j+1:]
        
        return res