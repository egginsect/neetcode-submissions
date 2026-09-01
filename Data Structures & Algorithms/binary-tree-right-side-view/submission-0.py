# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        buf = [(0, root)] if root else []
        prev = -1
        while buf:
            current, node = buf.pop(0)
            if current != prev:
                out.append(node.val)
                prev = current
            if node.right:
                buf.append((current+1, node.right))
            if node.left:
                buf.append((current+1, node.left)) 
        return out
        