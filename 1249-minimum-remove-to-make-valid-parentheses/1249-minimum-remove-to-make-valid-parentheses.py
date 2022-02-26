class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        # flag=0
        ans = []
        brac = []
        op = []
        skip = 0
        for idx,i in enumerate(s):
            if i==")" and not res:
                skip+=1
                continue
            elif i=="(":
                res.append(i)
                # ans.append(i)
                op.append(idx)
            elif i==")" and res:
                res.pop()
                ans.insert(op.pop(0)-skip,'(')
                ans.append(')')
            else:
                ans.append(i)
            # print(op)
        return "".join(ans)
                