class Solution:
    def entityParser(self, text: str) -> str:
        di = {"&quot;":"\"","&apos;":"\'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        # x = text.split(" ")
        res = ""
        i = 0
        while i<len(text):
            if text[i]=="&":
                temp = ""
                while i<len(text) and text[i]!=";":
                    temp=temp+text[i]
                    i+=1
                    if i<len(text) and text[i]=="&":
                        break
                if i<len(text) and text[i]==";":
                    temp=temp+text[i]
                    i+=1
                if temp in di:
                    res = res +di[temp]
                else:
                    res = res+temp
            else:
                res = res+text[i]
                i+=1
        # return res
        print()
            
        return res
                
                
        