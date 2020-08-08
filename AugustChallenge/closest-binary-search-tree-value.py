# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        currentBest = [root.val]
        
        def findValue(node):
            if abs(node.val-target) < abs(currentBest[0]-target):
                currentBest[0] = node.val
                
            if node.left:
                findValue(node.left)
                
            if node.right:
                findValue(node.right)
        
        findValue(root)
        
        return currentBest[0]