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
        lval = self.minDepth(root.left) + 1
        rval = self.minDepth(root.right) + 1
        if lval == 1: return rval
        if rval == 1: return lval
        return min(lval,rval)