# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can solve this using dfs recursive approach with a slight twist
        modify the return value -- returning [boolean (if tree is balanced), max height of subtree]

    in recursive function
        make function calls for left & right subtrees
        check if tree is balanced for that node
            check the first element of response -- boolean
            check the difference between left & right values -- should be less than or equal to 1
            if they're not, in the return value put false -- if this is false none of the other parent nodes will be true
        return with [True/False, max height of subtree]

    in the end return the helper function response -- the first element that is boolean
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # helper function to implement dfs recursively
        def dfs(root):
            # if root is empty
            if not root:
                return [True, 0] # return True since this node is balanced
            
            # get height for left subtree
            left = dfs(root.left)
            # get height for right subtree
            right = dfs(root.right)

            # check if current node is balanced
            # if left subtree & right subtree are balanced & difference is less than 1
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                balanced = True # return True
            else:
                balanced = False # return False

            # get max height at this node
            height = 1 + max(left[1], right[1])

            # return if tree is balanced or not at this pointer & the height of the tree
            return [balanced, height]

        # return first value of dfs' return value 
        return dfs(root)[0]