class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        
        x = -1
        res = -1
        for i in di:
            if di[i]>x:
                x=di[i]
                res=i
        return res