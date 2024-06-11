# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def search(root,target, val = None):
            if not root:
                return val
            value = root.val
            if not val or abs(value -target) < abs(val-target) or (abs(value -target) == abs(val -target) and value < val):
                val = value
            lval = search(root.left,target,val)
            rval = search(root.right,target,val)
            if abs(lval - target) < abs(val - target) or (abs(lval -target) == abs(val -target) and lval < val) :
                val = lval
            if abs(rval - target) < abs(val - target) or (abs(rval -target) == abs(val -target) and rval < val):
                val =rval
            return val
        
        return search(root,target)