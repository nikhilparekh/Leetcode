class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        i = 0
        lines = 0
        while i<len(s):
            c = 0
            while i<len(s) and c+widths[ord(s[i])-97]<=100:
                c+=widths[ord(s[i])-97]
                # print(c)
                i+=1
            lines+=1
            # if i==len(s)-1:
            #     return [lines,c]
        return [lines,c]
            
                