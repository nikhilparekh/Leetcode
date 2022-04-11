class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def move(grid):
            m = len(grid)
            n = len(grid[0])
            res = []
            temp = []
            temp.append(grid[m-1][n-1])
            for i in range(m):
                for j in range(n):
                    if len(temp)%n==0:
                        res.append(temp)
                        temp = []
                    temp.append(grid[i][j])
            return res
        
        for i in range(k):
            grid = move(grid)
        return grid