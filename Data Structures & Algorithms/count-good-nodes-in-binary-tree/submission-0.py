# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, current_max=-101):
            count = 0
            if node:
                count += int(node.val >= current_max)
                count += traverse(node.left, max(current_max, node.val))
                count += traverse(node.right, max(current_max, node.val))
            return count
        return traverse(root)