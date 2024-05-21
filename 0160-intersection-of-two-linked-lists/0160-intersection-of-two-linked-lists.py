# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        arr = set()
        def createCopy(listNode):
            if not listNode:
                return None
            
            cpy_head = ListNode(listNode.val)
            original_ptr = listNode
            cpy_ptr = cpy_head
    
            while original_ptr:
                if original_ptr in arr:
                    return original_ptr
                arr.add(original_ptr)
                original_ptr = original_ptr.next
                if original_ptr:
                    cpy_ptr.next = ListNode(original_ptr.val)
                    cpy_ptr = cpy_ptr.next

            return None
        
        if headA == headB:
            return headA
        createCopy(headA)
        return createCopy(headB)
         
                
                