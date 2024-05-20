# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        lval = self.minDepth(root.left) 
        rval = self.minDepth(root.right) 
        if (lval == 0 or rval == 0): return max(lval,rval)  + 1

        return min(lval,rval) + 1