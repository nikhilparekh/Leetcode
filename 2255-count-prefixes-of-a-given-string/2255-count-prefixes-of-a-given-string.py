class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        y = len(s)
        for i in words:
            if len(i)<y:
                if s[:len(i)]==i:
                    count+=1
            else:
                if i==s:
                    count+=1
        return count
            