class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = []
        for i in range(97,123):
            alpha.append(chr(i))
        alpha = "".join(alpha)
        key = key.replace(" ","")
        k = ""
        for i in key:
            if i not in k:
                k= k+i
        print(k)
        code = dict(zip(k,alpha))
        print(code)
        res = ""
        for i in message:
            if i in code:
                # print(i,code[i])
                res = res+code[i]
            else:
                res = res+" "
        return res
                
            