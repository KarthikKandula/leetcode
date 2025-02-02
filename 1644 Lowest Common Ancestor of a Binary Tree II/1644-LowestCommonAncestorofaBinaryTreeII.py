# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    The idea is to see if both nodes are in the tree while finding their LCA
        implementing a plain LCA exits if it find either of the nodes
            if it's not able to find it in a parallel subtree
            it means the first found node is the LCA & the other node is it's child
        we need to make sure to search again for the other node in the first found node
        just call the recursive function again
            search in first found node's left & right trees
        doing this we're not doing any double work since we're traversing all nodes only once
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # recursive function
        def dfs(node):
            # base conditions
            # if node is null, return nothing
            if not node:
                return None

            # if this node is either of the wanted nodes, return this
            if node == p or node == q:
                return node

            # search in left subtree
            left = dfs(node.left)
            # search in right subtree
            right = dfs(node.right)

            # if couldn't find anything in left tree
            if not left:
                return right # return right, since it might be the LCA, might exist in parallel sub-tree
            # if couldn't find anything in right tree
            if not right:
                return left # return left, since it might be the LCA, might exist in parallel sub-tree

            # if reaches this point, it means both nodes are initialized, both have been found
            # this is the first node that's common between them
            return node
        
        # first check for an LCA
        result = dfs(root)

        # if the above LCA isn't either target nodes, it means we've found the actual LCA
        if result != p and result != q:
            return result # return the result
        
        # if not, it means one node is potentially not found
        # call for the result nodes left & right subtrees to find the other node
        # if either call returns true, it means we've found the other node
        if dfs(result.left) or dfs(result.right):
            return result # return result since it's the true LCA
        else: # if no call returns a Node, the other node can't be found
            return None # return none
