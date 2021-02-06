# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        d = {}
        def iterateRec(root, prev_steps=''):
            rank = len(prev_steps) + 1
            if rank not in d:
                # initialise dict for first node in rank
                d[rank] = (prev_steps, root.val)
            elif d[rank][0] < prev_steps:
                # overwrite dict if current node is right of the node stored in dict
                d[rank] = (prev_steps, root.val)
            if root.left:
                iterateRec(root.left,prev_steps+'0')
            if root.right:
                iterateRec(root.right,prev_steps+'1')
        
        iterateRec(root, '')
        
        return [val[1] for _,val in d.items()]