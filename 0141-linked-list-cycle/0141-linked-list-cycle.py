# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        def recurse(head1,head2):
            if not head1 or not head2 or not head2.next: return False
            if head1 == head2: return True
            return recurse(head1.next,head2.next.next)
        
        if not head:
            return False
        return recurse(head,head.next)
            