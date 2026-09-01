# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def contains_node(node):
            nonlocal ans
            if not node:
                return False
            left_contains_node = contains_node(node.left)
            right_contains_node = contains_node(node.right)
            is_node = node.val == p.val or node.val == q.val
            if (is_node and left_contains_node) or (is_node and right_contains_node) or (left_contains_node and right_contains_node):
                if ans is None: 
                    ans = node
            return is_node or left_contains_node or right_contains_node
        contains_node(root)
        return ans

        
        