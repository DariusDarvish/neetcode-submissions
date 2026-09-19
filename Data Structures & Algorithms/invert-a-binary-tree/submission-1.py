# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return None
        queue=[]
        queue.append(root)
        while(queue):
            root_node=queue.pop()
            right_node=root_node.right if root_node!=None else None
            left_node=root_node.left if root_node!=None else None
            root_node.left=right_node
            root_node.right=left_node 
            if(root_node.right!=None):
                queue.append(root_node.right)
            if(root_node.left!=None):   
                queue.append(root_node.left)
        
        return root
                
            
           
        