# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dig(tn):
            while tn:
                if not tn.left and not tn.right:
                    return 1
                return max(dig(tn.left), dig(tn.right)) + 1
            return 0
        
        return dig(root)