class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalin(s):
            i=0
            j=len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        for i in words:
            if checkPalin(i):
                return i
        return ""