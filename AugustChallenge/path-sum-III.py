# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # 
        
        # straight forward case that I always miss
        if not root:
            return 0
        
        # declare the number of paths as a list to make it mutable
        nPaths = [0]
        def explorePath(rootLocal,sumLocal,sum):
            
            if rootLocal.val == sumLocal:
                nPaths[0] += 1
                
            if rootLocal.left:
                # continue exploring current path
                explorePath(rootLocal.left,sumLocal-rootLocal.val,sum)

            if rootLocal.right:
                # continue exploring current path
                explorePath(rootLocal.right,sumLocal-rootLocal.val,sum)
                # start a new exploration with the next node
        
        def exploreTree(node):
            # start a new exploration with the next node
            explorePath(node,sum,sum)
            if node.left:
                exploreTree(node.left)
            if node.right:
                exploreTree(node.right)
        
        exploreTree(root)
        
        
        return nPaths[0]


"""
Test cases

[1,null,2,null,3,null,4,null,5]
3

[1,-2,-3,1,3,-2,null,-1]
3

[1,-2,-3,1,3,-2,null,-1]
-1
"""
