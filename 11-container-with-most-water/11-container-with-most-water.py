class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j = len(height)-1
        cmax = -1
        while(i<j):
            cur = (j-i)*(min(height[i],height[j]))
            cmax= max(cmax,cur)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return cmax