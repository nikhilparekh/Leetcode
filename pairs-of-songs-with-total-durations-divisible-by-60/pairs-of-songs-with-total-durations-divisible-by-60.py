class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = defaultdict(int)
        count = 0
        for i in time:
            if i%60==0:
                count+=res[0]
            else:
                count+=res[60-i%60]
            res[i%60]+=1
        return count