# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    we can solve this using dfs tree traversal
        since we need to find two nodes & the LCA for both nodes
        we need the latest node where both nodes have been found
            so if both nodes are found at any node, that node is the LCA, return that node
        if both nodes are in a single sub-tree
            we need to return the highest placed node as the LCA
        if a node doesn't match either p or q
            search left & right tree
            if left tree isn't found
                return right node as the LCA 
                since it means both nodes exist in the right tree
            same with right
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base condition
        # if root is empty
        if not root:
            return None # return null node
        
        #if current node if either p or q
        if root == p or root == q:
            return root # return current node
        
        # if reaches here, 
        # search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # search right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # if didn't find either node in left
        if not left:
            return right # return right as LCA
        # if didn't find either node in right
        if not right:
            return left # return right as LCA
        
        # return root if value is match to both left & right
        return root
