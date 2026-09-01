# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

        # return val, k
    def traverse_iter(self, node):
        if node:
            if node.left:
                yield from self.traverse_iter(node.left)
            yield node.val
            if node.right:
                yield from self.traverse_iter(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traverse_iter = self.traverse_iter(root)
        for _ in range(k):
            val = next(traverse_iter)
        return val
