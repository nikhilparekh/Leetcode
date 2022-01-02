class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        
        def findfirst(nums,target):
            lo = 0 
            hi = len(nums)
            while lo<hi:
                mid = lo+(hi-lo)//2
                if nums[mid]==target:
                    hi = mid
                elif nums[mid]<target:
                    lo = mid+1
                else:
                    hi = mid
            return lo
        
        def findlast(nums,target):
            lo = 0
            hi = len(nums)
            while (lo<hi):
                mid = lo+(hi-lo)//2
                if nums[mid]==target:
                    lo = mid+1
                elif nums[mid]<target:
                    lo = mid+1
                else:
                    hi=mid
            return lo-1
        a = findfirst(nums,target)
        b = findlast(nums,target)
        s = []
        for i in range(a,b+1):
            s.append(i)
        return s
    
                    