# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can solve this problem using basic tree traversal with a slight twist
        the problem is to check if any particular node if greater than every other in it's path to the root node
        for this, we need to have the max value in path available to us

    create a recursive function that takes the max value & curr node
        check if curr node's value is greater than or equal to maxValue 
            if it is, increment temp variable
        recursive call left subtree
        recursive call right subtree

        return left + right + curr node's temp variable
    
    root node's return value would have good node count for the entire tree
    """
    def goodNodes(self, root: TreeNode) -> int:
        
        # create an helper function
        def recurGoodNodes(maxVal, curr):
            # base case -- check if curr node is empty
            if not curr:
                return 0 # empty node has no good nodes, hence return 0

            # create a temp variable
            gudNodes = 0
            # check if curr node's value is >= maxVal
            if curr.val >= maxVal:
                gudNodes += 1 # if it is, this is a good node, increment gudNodes value

            # recursive function call to check good nodes for left subtree
            left = recurGoodNodes(max(maxVal, curr.val), curr.left)
            # recursive function call to check good nodes for right subtree
            right = recurGoodNodes(max(maxVal, curr.val), curr.right)

            # return left & right along with if current node is a good node
            return gudNodes + left + right
        
        # function call -- with root as node & root's value as max
        return recurGoodNodes(root.val, root)
