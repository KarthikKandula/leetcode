# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    solve the problem using dfs recursive approach
        since we need left & right values to be returned first
    
    take a helper function to help with the recursive dfs functions
    also need a variable to store the maxDiameter -- make this a global variable

    in helper function
        get max depth of each subtree, left & right
        max diameter at that node is left + right, update global variable with max value
        return max depth at this node to help calculate maxDiameter for parent node
    
    return max diameter (global variable) in the end
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # create a variable for storing maxDiameter
        self.maxDiameter = 0

        # helper function for recursive dfs calls
        def dfs(curr):
            # if curr node is null
            if not curr:
                return 0 # return 0, since no depth

            # get max depth of left subtree 
            left = dfs(curr.left)
            # get max depth of right subtree 
            right = dfs(curr.right)

            # get max diameter -- for this node max diameter is left + right
            self.maxDiameter = max(self.maxDiameter, left + right)

            # returning max depth to calculate max diameter for parent node
            return 1 + max(left, right)

        # first function call with root
        dfs(root)

        # return maxDiameter variable
        return self.maxDiameter
