# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    we can solve this problem using in order tree traversal
        input is a binary search tree, we use bst's characteristics to our advantage
    
        problem is to find kth element in a bst
            since bst's values are always in sorted order -- if done an in-order traversal
        
    use a stack to keep track of nodes -- standard dfs solution
    use a int variable to keep track of num of nodes visited
        at any point if count == k (input) -- return that value

    loop while stack has values or curr node is valid
        check if curr node is valid
            if it is, we need to go further left
        if curr node is not valid
            pop last node from stack & visit it
            increment count value
            check if count == k (input)
                return than value if yes
            if not, shift curr right since we need to go further right
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using stack since implementing in-order traversal
        stack = []
        count = 0 # variable to store count -- of nodes visited

        # create a temp node variable curr
        curr = root

        # loop while curr is valid or stack has nodes in it
        while stack or curr:
            # check if curr is a valid node -- need to go as far left as possible 
            if curr:
                stack.append(curr) # append current node to stack -- need to visit it later
                curr = curr.left # shift curr left
            # if reaches this point, it means curr is a null node, we need to pop from stack & visit that node
            else:
                # pop last node from stack 
                tempNode = stack.pop()
                count += 1 # increment count since we're visiting a node

                # check if count == k
                if count == k:
                    return tempNode.val # if yes, we've found the kth value

                # shift curr right
                curr = tempNode.right

    """
    same concept as above with slightly different code
    """
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # using stack since implementing in-order traversal
        # stack = []
        # count = 0 # variable to store count -- of nodes visited

        # # create a temp node variable curr
        # curr = root

        # # loop while curr is valid or stack has nodes in it
        # while curr or stack:
        #     # loop for the duration curr is a valid node -- going as far left as possible
        #     while curr:
        #         stack.append(curr) # append current node to stack -- since we want to visit this node again later
        #         curr = curr.left # shift curr left

        #     # if reached this point, it means curr is null
        #     # pop last node from stack 
        #     tempNode = stack.pop()
        #     count += 1 # increment count since we've visited a node

        #     # check if count == k
        #     if count == k:
        #         return tempNode.val # if yes, we've found the kth element

        #     # shift curr right 
        #     curr = tempNode.right
