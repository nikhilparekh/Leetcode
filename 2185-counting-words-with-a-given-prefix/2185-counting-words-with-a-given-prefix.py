class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        t = len(pref)
        count=0
        for i in words:
            if i[:t]==pref:
                count+=1
        return count