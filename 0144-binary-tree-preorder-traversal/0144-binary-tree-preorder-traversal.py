# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left or not root.right:
            return [root.val] + self.preorderTraversal(root.right) +self.preorderTraversal(root.left)
        return [root.val] + self.preorderTraversal(root.left) +self.preorderTraversal(root.right)