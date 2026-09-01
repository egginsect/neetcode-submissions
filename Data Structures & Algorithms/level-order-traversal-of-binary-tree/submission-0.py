# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        buf = [(0, root)]
        out = []
        while(buf):
            level, node = buf.pop(0)
            if level>=len(out):
                out.append([])
            out[level].append(node.val)
            if node.left:
                buf.append((level+1, node.left))
            if node.right:
                buf.append((level+1, node.right))
        return out
        