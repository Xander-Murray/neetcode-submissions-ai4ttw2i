# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       
        
        
        def search(root, maxVal):
            if not root:
                return 0
            
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += search(root.left, maxVal)
            res += search(root.right, maxVal)
            return res
        return search(root, root.val)
