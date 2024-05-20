# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        Lroot = root
        Rroot = root

        
       
        def bothTraverse(Lroot, Rroot):
            if not Lroot and not Rroot:return True
            if not Lroot or not Rroot:return False
            if Lroot.val != Rroot.val:return False
            return bothTraverse(Lroot.left, Rroot.right) and bothTraverse(Lroot.right, Rroot.left)
        
        return bothTraverse(Lroot,Rroot)
        
     
            
            