class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        temp = []
        idx = 0
        for i in mat:
            temp.append((idx,i.count(1)))
            idx+=1
        temp = sorted(temp, key = lambda x:x[1])
        res = []
        for i in range(k):
            res.append(temp[i][0])
        return res
        
            
                   
            