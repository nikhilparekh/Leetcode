class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        cval = 0
        for i in operations:
            if i[1] =="-":
                cval-=1
            else:
                cval+=1
        return cval
                