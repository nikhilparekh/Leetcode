class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        # cmax = 0
        for i in logs:
            if i[0:2]==".." and stack:
                stack.pop()
            elif i[0]!=".":
                stack.append(i)
        return len(stack)