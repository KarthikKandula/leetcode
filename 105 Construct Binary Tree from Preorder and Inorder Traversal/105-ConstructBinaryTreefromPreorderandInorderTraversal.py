# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # check if preorder & inorder lists are empty
        if not preorder and not inorder:
            return None
        
        # get first value
        firstVal = preorder[0]

        # create node with first value -- this is root node
        root = TreeNode(firstVal)

        # find location of root in inorder -- get mid value
        mid = inorder.index(firstVal)

        """
        Everything to the left of root in inorder is the left subtree
        Everything to the right of root in inorder is the right subtree
        """

        # recursive call to create left subtree -- also establishing left connection
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # recursive call to create right subtree  -- also establishing left connection
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root node
        return root
