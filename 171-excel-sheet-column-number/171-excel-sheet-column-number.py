class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        for idx, val in enumerate(columnTitle):
            count*=26
            count += ((ord(val)-64))
        return count
        