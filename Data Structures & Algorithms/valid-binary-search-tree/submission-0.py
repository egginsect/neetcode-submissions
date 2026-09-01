# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValidBST(self, root: Optional[TreeNode], max_val=-(sys.maxsize-1),min_val=sys.maxsize) -> bool:
        if not root:
            return True
        if not (max_val < root.val < min_val):
            return False
        return self.isValidBST(root.left, max_val, root.val) and self.isValidBST(root.right, root.val, min_val)
        
        