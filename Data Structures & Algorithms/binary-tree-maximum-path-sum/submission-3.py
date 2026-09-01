# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def traverse(node:Optional[TreeNode]):
            current_max = node.val
            branch_max = node.val
            lr_path_sum = node.val
            if node.left:
                left_branch_max, left_max = traverse(node.left)
                branch_max = max(branch_max, node.val+left_branch_max)
                current_max = max(current_max, left_max)
                lr_path_sum += left_branch_max
            if node.right:
                right_branch_max, right_max = traverse(node.right)
                branch_max = max(branch_max, node.val+right_branch_max)
                current_max = max(current_max, right_max)
                lr_path_sum += right_branch_max
            return branch_max, max(current_max, branch_max, lr_path_sum)
        _, max_sum = traverse(root)
        return max_sum