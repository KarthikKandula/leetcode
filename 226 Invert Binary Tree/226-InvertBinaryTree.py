# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursive Solution

    For every recursive function, there exists three mandatory things
        base condition -- checking if root is none
        recursive function call -- calling with both left & right node
        return statement - returning the input root node
    
    in addition to these, also implementing logic to reverse nodes
        left to right & right to left
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if root in empty -- recursive base condition
        if not root:
            return None # return None

        # inverse nodes using temp variable
        # temp = root.right
        # root.right = root.left
        # root.left = temp

        # better way to inverse nodes
        root.left, root.right = root.right, root.left

        # recursive function call for left node
        self.invertTree(root.left)
        # recursive function call for right node
        self.invertTree(root.right)

        # return root at the end
        return root

    """
    Iterative Solution

    using BFS for the iterative solution, hence using a queue
        Initialize the queue with root at start

    loop while queue is not empty
        pop the first value & reverse it's nodes
        if left exists - insert into queue
        if right exists - insert into queue

    return root at the end
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if root is empty
        if not root:
            return None # return None

        # initialize queue with root -- this is a BFS operation hence using queue
        queue = [root]

        # loop while queue is not empty
        while queue:
            # pop from queue
            curr = queue.pop(0)

            # inverse nodes using temp variable
            # temp = curr.right
            # curr.right = curr.left
            # curr.left = temp

            # better way to inverse nodes
            curr.left, curr.right = curr.right, curr.left

            # check if curr node has a left node
            if curr.left:
                queue.append(curr.left) # append to stack if it does
            # check if curr node has a right node
            if curr.right:
                queue.append(curr.right) # append to stack if it does

        # return root at end 
        return root
