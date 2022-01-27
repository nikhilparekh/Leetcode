class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        st = sorted(x[0] for x in intervals)
        end = sorted(x[1] for x in intervals)
        i=j=0
        count = 0
        while i<len(intervals):
            if st[i]>=end[j]:
                count-=1
                j+=1
            count+=1
            i+=1
        return count