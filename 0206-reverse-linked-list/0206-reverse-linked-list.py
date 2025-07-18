# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], acc: Optional[ListNode] = None) -> Optional[ListNode]:
        if head is None:
            return acc
        next_node = head.next
        head.next = acc
        return self.reverseList(next_node, head)
