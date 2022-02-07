class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        i=j=0
        res = 0
        csum = 0
        while j<len(calories):
            csum+=calories[j]
            if (j-i)>=k:
                csum-=calories[i]
                i+=1
            if (j-i)==k-1:
                if csum<lower:
                    res-=1
                if csum>upper:
                    res+=1
            j+=1
        return res
                
                
            
                    