class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li = sentence.split(" ")
        t = len(searchWord)
        for idx,val in enumerate(li):
            if val[:t]==searchWord:
                return idx+1
        return -1