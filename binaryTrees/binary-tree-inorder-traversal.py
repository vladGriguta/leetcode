# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack, output = [], []
        
        # stop when stack is closed and root is None
        while root or stack:
            # iterate to the left-most node
            while root:
                stack.append(root)
                root = root.left
            # get the latest node in the stack and append to output
            root = stack.pop()
            output.append(root.val)
            
            # check if the path is closed (already verified that you cannot go left anymore)
            root = root.right
        return output