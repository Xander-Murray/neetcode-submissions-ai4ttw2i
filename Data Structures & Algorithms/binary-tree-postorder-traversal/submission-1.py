# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        order = []
        
        def dfs(order, node):
            if not node:
                return 
            dfs(order, node.left)
            dfs(order, node.right)
            order.append(node.val)
        dfs(order, root)
        return order
