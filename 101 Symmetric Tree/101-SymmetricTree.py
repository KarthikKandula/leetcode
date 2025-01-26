# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # recursive function to implement bfs
        def dfs(l, r):
            # if both left & right nodes are empty, it's a match
            if not l and not r:
                return True # return true, since they're same

            # if one of the nodes is missing, they're not matching
            if not l or not r:
                return False # return false, since they're not same

            # previous code implementing above code
            # if not l and r:
            #     return False
            # if l and not r:
            #     return False

            # if reaches this point, means both nodes exist
            # check if their values are equal
            if l.val != r.val:
                return False # if not, return false, we've found a mismatch
            
            # recursive calls for opposing nodes, since checking for mirror of tree
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        
        # initial call to recur function, call for root's left & right nodes
        return dfs(root.left, root.right)

