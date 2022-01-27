class Solution:
    def countPoints(self, rings: str) -> int:
        di = {}
        for idx, val in enumerate(rings):
            if val in di and val.isdigit():
                print(rings[idx-1], val)
                di[val].add(rings[idx-1])
            else:
                di[val] = set(rings[idx-1])
        count = 0
        print(di)
        for i in di:
            if len(di[i])==3:
                count+=1
        return count
            
            