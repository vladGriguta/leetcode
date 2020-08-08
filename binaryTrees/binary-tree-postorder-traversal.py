# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack, output = [], []
        
        # stop when stack is closed and root is None
        while root or stack:
            # iterate to the left-most node
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
                
            # get the latest node in the stack
            root = stack.pop()
            
            # if there is a deeper path to the right which was not yet explored
            # then explore that path first
            # else, we are at the deepest left-most node, so append to the output
            if stack and root.right==stack[-1]:
                stack[-1] = root
                root = root.right
            else:
                output.append(root.val)
                root = None
                
        return output