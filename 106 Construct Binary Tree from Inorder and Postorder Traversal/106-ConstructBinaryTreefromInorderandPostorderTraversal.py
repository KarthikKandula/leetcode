# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can solve this problem combining factors of inorder & postorder together
        root node is always the last in postorder
        everything to the right of root is right subtree
            vice versa to left subtree
        if we breakdown the problems into subproblems passing shorter inputs
            a tree is going to be built eventually
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if in order & post order are empty
        if not inorder and not postorder:
            return None # return None node

        # build root node from last value in post order -- always the root
        root = TreeNode(postorder[-1])

        # find root's index in inorder
        index = inorder.index(postorder[-1])

        # call recur function for left subtree with split inorder & postorder arrays
        root.left = self.buildTree(inorder[:index], postorder[:index])
        
        # call recur function for right subtree with split inorder & postorder arrays
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        # return newly built root node
        return root
