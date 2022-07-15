# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        di = {}
        i = 0
        temp = head
        target = None
        while temp:
            # print(temp.val)
            if temp in di:
                target = di[temp]
                break
            else:
                di[temp] = i
            i+=1
            temp = temp.next
        if target==None:
            # return -1
            return None
        # print(target)
        for i in range(target):
            head=head.next
        return head