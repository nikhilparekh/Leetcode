from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in di:
                di[x].append(i)
            else:
                di[x] = [i]
        res = []
        for i in di:
            res.append(di[i])
        return res
            