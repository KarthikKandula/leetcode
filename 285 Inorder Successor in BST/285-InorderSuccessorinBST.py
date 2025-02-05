# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    we use an implementation of in-order traversal in this problem
        we can use bst characteristics to implement this easily
        to find any successor, we have to eliminate either left or right subtree
        if current value is less than target p value
            we search in right tree, eliminate left tree
        if current value is greater than target p value
            search in left tree, eliminate right tree
    """
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        # pointer for prev node
        prev = None
        cur = root # pointer for cur node

        # loop while cur node is valid
        while cur:
            # if p value is greater than current value
            if p.val >= cur.val:
                # search towards right
                cur = cur.right
            # if p value is less than current value
            elif p.val < cur.val:
                # update cur value to prev, since this is highest value to this left subtree, this can be a successor
                prev = cur
                # search towards left
                cur = cur.left

        # return prev node
        return prev
