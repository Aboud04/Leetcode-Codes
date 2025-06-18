# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        res = dummy        
        tmp = head

        while tmp and tmp.next:
            res.next = ListNode(tmp.val)
            res = res.next

            v = gcd(tmp.val, tmp.next.val)
            res.next = ListNode(v)
            res = res.next

            tmp = tmp.next

        
        res.next = ListNode(tmp.val)

        return dummy.next




