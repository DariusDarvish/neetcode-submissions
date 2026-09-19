# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #iterate through tree till we find matching sub root
        def checkSubRoot(root,subRoot):
            if subRoot == None and root ==None:
                return True
            if subRoot == None and root:
                return False
            if root ==None and subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return checkSubRoot(root.left,subRoot.left) and checkSubRoot(root.right,subRoot.right)
        
            
        if root:
            if(root.val==subRoot.val):
                value=checkSubRoot(root,subRoot)
                if value==True:
                    return True
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False
