# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced=True
        balaned_set={-1,0,1}
        def dfs(root):
            nonlocal balanced
            if root is None:
                return 0
    
            # Recursively calculate depth of left and right subtrees
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            
            if right_depth-left_depth not in balaned_set:
                balanced=False
            
            # Take the larger depth and add 1 for the current node
            return 1 + max(left_depth, right_depth)
            
            
            
        dfs(root)
        
        return balanced
           