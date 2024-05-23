# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h1 = head
        p1 = None
        while h1:
            if p1 and h1.val == val:
                p1.next = h1.next
            else:
                p1 = h1    
            h1 = h1.next
        if head and head.val == val:
            head = head.next
        return head