class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(" ")
        count = 0
        res = []
        for i in words:
            flag = 0
            if i!="":
                if flag==0 and "-" in i:
                    k = i.index("-")
                    if k-1<0 or k+1>=len(i) or not i[k+1].isalpha() or  not i[k-1].isalpha() or i.count("-")>1:
                        flag=1
                if flag==0 and "." in i or "!" in i or "," in i:
                    if ("." in i and i[-1]!=".") or i.count(".")>1:
                        flag=1
                    if ("," in i and i[-1]!=",") or i.count(",")>1:
                        flag=1
                    if ("!" in i and i[-1]!="!") or i.count("!")>1:
                        flag=1
                if flag==0:
                    for k in i:
                        if k.isdigit():
                            flag=1
                            break

                if flag==0:
                    res.append(i)
                    count+=1
        for i in res:
            print(i)
        return count
                
            
                