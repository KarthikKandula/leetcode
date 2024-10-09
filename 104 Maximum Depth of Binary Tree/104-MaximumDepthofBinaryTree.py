# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Iterative Solution

    we can solve this problem in iterative approach using basic DFS tree traversal
        with slight change on adding nodes to stack
    
    add nodes to stack in this format - [node, depth until that node]
        this is to have an idea of the depth for each node

    loop while stack is not empty
        get latest value from stack
        get max value of depth from the popped node's tempdepth
        append popped node's left & right nodes to stack for further processing
    
    in the end max depth will be stored in depth variable, return at end
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # check if root is none
        if not root:
            return 0 # return 0 -- depth is 0 if root is none

        # initialize stack with root -- values in stack are going to be in format [node, depth until that node]
        stack = [[root, 1]]
        depth = 1 # result variable, initially at 1

        # loop while stack is not empty
        while stack:
            # pop from stack, save node & depth in temp variables
            tempNode, tempDepth = stack.pop()

            # if tempNode is not empty
            if tempNode:
                # get max depth value
                depth = max(depth, tempDepth)

                # check if right node is not null
                if tempNode.right:
                    # append right node to stack, add 1 to depth since a node has been added
                    stack.append([tempNode.right, tempDepth + 1])
                # check if left node is not null
                if tempNode.left:
                    # append left node to stack, add 1 to depth since a node has been added
                    stack.append([tempNode.left, tempDepth + 1])

        # return depth
        return depth

    """
    Recursive Solution

    we can solve this problem in recursive approach using basic DFS tree traversal
        with slight change on return values
    
    we don't return the root node itself, instead
        we return the depth at that particular node
            add 1 to include the current node as well along with the max of left & right nodes
    """
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # check if root is none
    #     if not root:
    #         return 0 # return 0

    #     # get left subtree's max depth
    #     left = self.maxDepth(root.left)
    #     # get right subtree's max depth
    #     right = self.maxDepth(root.right)

    #     # adding 1 to include current node
    #     return 1 + max(left, right)
