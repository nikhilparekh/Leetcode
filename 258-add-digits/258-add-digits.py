class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            csum = 0
            for i in str(num):
                csum+=int(i)
            num = csum
        return num
                