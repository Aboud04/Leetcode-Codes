# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def howMany(root):
            if root == None:
                return 0
            return 1 + howMany(root.left)
        if howMany(p) != howMany(q):
            return False
        def inorder(root):
            if root == None:
                return [root]
            if root.left == None and root.right == None:
                return [root.val]

            return inorder(root.left)+ [root.val]+ inorder(root.right)
        arrp = inorder(p)
        arrq = inorder(q)
        if len(arrp) != len(arrq):
            return False

        for i in range(len(arrp)):
            if arrp[i] != arrq[i]:
                return False
        return True