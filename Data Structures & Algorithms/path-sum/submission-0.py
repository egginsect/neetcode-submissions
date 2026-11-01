# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == targetSum
        left_has_sum = self.hasPathSum(root.left, targetSum-root.val) if root.left else False
        right_has_sum = self.hasPathSum(root.right, targetSum-root.val) if root.right else False
        return left_has_sum or right_has_sum
        