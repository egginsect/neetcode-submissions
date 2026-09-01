# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        common_ancestor = [None]
        def traverse(node):
            if not node:
                return False
            is_left_match = traverse(node.left)
            is_right_match = traverse(node.right)
            is_node_match = node.val==p.val or node.val == q.val
            if is_node_match:
                if is_left_match or is_right_match:
                    if not common_ancestor[0]:
                        common_ancestor[0] = node
            elif is_left_match and is_right_match:
                    if not common_ancestor[0]:
                        common_ancestor[0] = node
            return any([is_node_match, is_left_match, is_right_match])
        traverse(root)
        return common_ancestor[0]