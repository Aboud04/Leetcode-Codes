# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        top = head.next
        sm = 0

        while top:
            if top.val == 0:
                res.next = ListNode(sm)
                res = res.next
                sm = 0
            else:
                sm += top.val
            top = top.next

      
        return dummy.next