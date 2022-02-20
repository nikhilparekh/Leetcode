class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:(x[0],x[1]))
        res = [intervals[0]]
        print(intervals)
        for i in intervals[1:]:
            if i[0]>res[-1][0] and i[1]>res[-1][1]:
                res.append(i)
            elif i[0]<=res[-1][0] and i[1]>=res[-1][1]:
                while res and i[0]<=res[-1][0] and i[1]>=res[-1][1]:
                    res.pop()
                if not res or (i[0]>res[-1][0] and i[1]>res[-1][1]):
                    res.append(i)
            print(res)
        return len(res)