class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        flag = "n"
        count = 0
        prev = arr[0]
        for i in arr[1:]:
            if i==prev:
                return False
            elif flag=="n" and i<prev:
                return False
            elif flag=="up" and i<prev:
                flag="dn"
                # count+=1
            elif flag=="n" and i>prev:
                flag="up"
            elif flag=="dn" and i>=prev:
                return False
            elif flag=="up" and i<=prev:
                return False
            # elif flag==2 and i>prev:
            #     return False
            prev = i
        print(flag)
        return flag=="dn"
            