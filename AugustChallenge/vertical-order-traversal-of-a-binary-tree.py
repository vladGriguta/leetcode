# Day 7 - August Challenge


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        import bisect
        
        res = defaultdict(dict)
        
        if root:
            res[0][0] = [root.val]
        else:
            res = {}
        
        def mapTree(root,X,Y):
            if root.left:
                if X-1 not in res:
                    res[X-1][Y-1] = [root.left.val]
                else:
                    if Y-1 not in res[X-1]:
                        res[X-1][Y-1] = [root.left.val]
                    else:
                        bisect.insort(res[X-1][Y-1], root.left.val)
                mapTree(root.left,X-1,Y-1)
                
            if root.right:
                if X+1 not in res:
                    res[X+1][Y-1] = [root.right.val]
                else:
                    if Y-1 not in res[X+1]:
                        res[X+1][Y-1] = [root.right.val]
                    else:
                        bisect.insort(res[X+1][Y-1], root.right.val)     
                mapTree(root.right,X+1,Y-1)
        
        mapTree(root,0,0)
        
        finalRes = []
        for key1 in sorted(res.keys()):
            temp = []
            for key2 in sorted(res[key1].keys(),reverse=True):
                temp = temp + res[key1][key2]
            
            finalRes.append(temp)
        
        return finalRes
        
        
        
        
