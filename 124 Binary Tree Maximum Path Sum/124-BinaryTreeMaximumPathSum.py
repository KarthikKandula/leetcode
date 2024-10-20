# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    use dfs recursive traversal with extra logic to solve the problem
        we need to update the max sum at any node
        get the max sum for left & right subtrees
    
    use a recursive function to effectively implement
        get the max value for left subtree
            if value is negative, replace with 0
        get the max value for right subtree
            if value is negative, replace with 0
        
        calculate max path value for current node -- curr.val + left + right
            replace global result variable with max value

        return curr.val + max of left, right subtree
            since we only need one path's value
    
    return result variable at the end
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # create global output variable
        self.res = root.val

        # create helper function
        def dfs(curr):
            # check if curr is none
            if not curr:
                return 0
            
            # get values for left & right subtree
            # left subtree recursive call
            leftMax = dfs(curr.left)
            # right subtree recursive call
            rightMax = dfs(curr.right)

            # handle if leftMax & rightMax are negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute the max value at curr node
            maxVal = curr.val + leftMax + rightMax

            # replace res
            self.res = max(self.res, maxVal)

            # return curr value + max of left & right paths
            return curr.val + max(leftMax, rightMax)
        
        # initial recursive function call with root
        dfs(root)

        # return result variable -- holds max path value
        return self.res
