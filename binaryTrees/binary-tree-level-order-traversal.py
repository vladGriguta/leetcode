# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        self.res = {0:[root.val]}
        
        self.helper(root,1)
        
        return [self.res[key] for key in sorted(self.res.keys())]
        
    def helper(self,root,level):
        if root.left:
            if level not in self.res:
                self.res[level] = [root.left.val]
            else:
                self.res[level].append(root.left.val)
            
            self.helper(root.left,level+1)
            
        if root.right:
            if level not in self.res:
                self.res[level] = [root.right.val]
            else:
                self.res[level].append(root.right.val)
                
            self.helper(root.right,level+1)