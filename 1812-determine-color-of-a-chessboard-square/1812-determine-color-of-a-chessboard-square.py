class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        odd = ["b","d","f","h"]
        l = coordinates[0]
        n = coordinates[1]
        if l in odd:
            if int(n)%2!=0:
                return True
            return False
        else:
            if int(n)%2==0:
                return True
            return False