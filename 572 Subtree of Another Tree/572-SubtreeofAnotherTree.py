# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    to solve this problem use basic tree dfs tree traversal with a couple additional steps
        breaking up this problem into subproblems reveals this is the Same Tree problem
        we need to check if root & subRoot are the same tree at any given node
            if they are not, check for root's left & right nodes with entire subRoot

        for this, create a helper function that implements same tree algorithm

    in the main function
        cover couple edge cases like
            if subRoot is none -- can be subtree of any node, return True
            if root is none -- no tree can be subree, return false

        check if trees are same at current node
            if not recursive call same function with left & right nodes but entire subRoot 
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is None, can be subtree of any tree, hence true
        if not subRoot:
            return True
        # if root is None, no tree can be a subtree, hence false
        if not root:
            return False

        # check if current root & subRoot are same tree, return True if they are
        if self.isSameTree(root, subRoot):
            return True

        # if reaches this point, current root & subRoot are not equal
        # recursive call to compare left subtree of root with subRoot & right subtree of root with subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    """
    function to compare if both trees are same
    """
    def isSameTree(self, r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
        # if both nodes are None, they are same Tree, return True
        if not r and not sr:
            return True
        # if one of the nodes is None, they are not same, return False
        if not r or not sr:
            return False

        # if values for nodes are not same, return False
        if r.val != sr.val:
            return False

        # if reaches this point, means values are same -- nodes until this point match
        # recursive call to isSameTree func with left & right subtrees
        return self.isSameTree(r.left, sr.left) and self.isSameTree(r.right, sr.right)
