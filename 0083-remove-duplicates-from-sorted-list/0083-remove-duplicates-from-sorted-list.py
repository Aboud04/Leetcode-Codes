# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = head
        curr = head.next
        while curr !=None:
            if curr.val == prev.val:
                prev.next = curr.next
                if prev.next !=None:
                    curr = prev.next
                else:
                    curr = None
            else:
                curr = curr.next
                prev = prev.next
        
        return head
                
            
        