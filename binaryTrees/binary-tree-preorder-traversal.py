# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack, output = [root,], []
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                
                # append right and then left nodes to the stack so that they will
                # be appended to the output list in reverse order
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
                    
        return output
            