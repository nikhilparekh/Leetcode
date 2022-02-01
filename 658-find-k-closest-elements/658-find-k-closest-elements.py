class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        di = {}
        res = []
        i = 0
        for index,num in enumerate(arr):
            di[index] = abs(num-x)
        di = dict(sorted(di.items(), key=lambda x:x[1]))
        for i in di:
            res.append(arr[i])
        return sorted(res[:k])
            
                
            
        
        