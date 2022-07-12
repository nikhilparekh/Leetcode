class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pair = {"0":"0","1":"1","6":"9","9":"6","8":"8"}
        res = []
        for i in reversed(num):
            if i not in pair:
                return False
            elif num.count(i)!=num.count(pair[i]):
                return False
            res.append(pair[i])
        return num=="".join(res)