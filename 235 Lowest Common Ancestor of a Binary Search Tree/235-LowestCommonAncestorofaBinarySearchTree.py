# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Iterative solution

    we can solve this problem using basic tree traversal
        the twist here is, input is a bst
            means left node is less than parent & right node is greater than parent
        we can use bst characteristics to effectively search for LCA
    
    the idea is to reduce the problem to making a decision on which subtree to search in 
        Check if curr node value < than p & q
            check the right subtree
        Check if curr node value > than p & q
            check the left subtree
        Else
            LCA is the curr node
            This else covers below 
                If curr value is > than one & < than the other
                Or equal to one & > than one or < than the other
            It means this is the LCA, we don't have to look further
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # create a variable that holds root
        curr = root

        # loop while curr is valid
        while curr:
            # check if p & q are > than curr value
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right # check right subtree
            # check if p & q are < than curr value
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left # check left subtree
            # if reaches this point, means one value is < & one value is >, so curr node is the LCA 
            else:
                return curr # return current value as LCA


    """
    My recursive solution
    """
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

    #     # Recursive dfs function
    #     def dfs(root):
    #         # Base condition - if root is empty, return None
    #         if not root:
    #             return None

    #         # Check if root is equal to either p or q
    #         if root == p or root == q:
    #             return root # If yes, return root

    #         left = dfs(root.left) # Recursive call for left sub-tree
    #         right = dfs(root.right) # Recursive call for right sub-tree

    #         # If the node doesn't exist in left node, it's possible it exists in the right node
    #         if not left:
    #             return right
    #         # If the node doesn't exist in right node, it's possible it exists in the left node
    #         if not right:
    #             return left

    #         # If left & right are not none, it means this node is the LCA
    #         return root

    #     return dfs(root)
