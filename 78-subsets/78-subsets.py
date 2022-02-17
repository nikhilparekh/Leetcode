class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         Backtrack problem
            """
                    Decision Tree, one side we will include that number, other side we will not include

                                [1,2,3]
                              1 /                  \[]
                            [1]                     []
                            2/   \1              2/      \[]
                        [1,2]    [1]            [2]         []
                        3/  \[]
                [1,2,3]      [1,2]

            """
            res = []
            curSubset = []
            def dfs(index):
                if index>=len(nums):
                    res.append(curSubset.copy())
                    return

                #codition for including the number
                curSubset.append(nums[index])
                dfs(index+1)

    #             condition to ignore current number
                curSubset.pop()
                dfs(index+1)

            dfs(0)
            return res
                    
                