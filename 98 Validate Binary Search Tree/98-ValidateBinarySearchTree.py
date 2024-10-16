# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can solve this using basic tree traversal with a slight twist
        the problem is to check if input is a valid bst
        for this, we need to keep track of the min & max values that any particular node is allowed to be in
    
    create a recursive function that takes node, low & high values
        check if curr node's value is between low & high
            if not, return False
        recursive call to left subtree
            since left node is supposed to be less than parent node
            change high value in func call to parent node's value
        recursive call to right subtree
            since right node is supposed to be greater than parent node
            change low value in func call to parent node's value
        
        function return value is True/False -- if that node is valid & is a bst or not
            we need all function return values to be Tre
        return True if left subtree & right subtree are bst's
            else False
    
    root node's return value is the answer to whether the tree is bst
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, low, high):
            # check if curr node isn't valid -- # Base condition if node doesn't exist
            if not curr:
                return True # An empty node is always valid BST
            # check if curr node's value is not between low & high
            if not low < curr.val < high:
                return False # If not, return False
            
            # Recursive call for left sub-tree
            left = dfs(curr.left, low, curr.val)
            # Recursive call for right sub-tree
            right = dfs(curr.right, curr.val, high)

            # return True if both left & right are true, else false
            return True if left and right else False

        # Call recursive function with 32 int min & max values
        return dfs(root, -2**31-1, 2**31)
