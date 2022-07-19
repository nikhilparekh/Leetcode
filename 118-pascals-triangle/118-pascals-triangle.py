class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def recur(n,arr):
            if n==0:
                return [1]
            elif n==1:
                return [1,1]
            temp = []
            temp.append(1)
            for i in range(1,len(arr)):
                temp.append(arr[i-1]+arr[i])
            # print(temp)
            temp.append(1)
            return temp
    
        res = []
        for i in range(numRows):
            if res:
                res.append(recur(i,res[-1]))
            else:
                res.append(recur(i,[]))
            # print(res)
        return res