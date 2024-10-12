# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Recursive solution

    we use basic dfs recursion algorithm with a change to return values
        in each function call, we need to do below things
            compare if both nodes are equal -- null is equal
            if one node has a value & the other doesn't -- not equal - return false
            perform recursive function call for left & right trees
            return true if all true conditions are met
            return false if even one false condition is met
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p and q are null -- base condition
        if not p and not q:
            return True # return true, since they're same
        # if one has a node & other is null
        if not p or not q:
            return False # return false, since they're not same
        
        # if reaches this point, it means both nodes have value
        # compare values on p & q
        if p.val != q.val:
            return False # if they're not equal, return false

        # recursive call to the left & right nodes, put and here since both of them should be true
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    """
    Iterative solution

    we use basic bfs iterative traversal to solve this problem
        the twist is push to queue in pairs, so nodes from similar positions are together in queue -- easier for comparision
            compare if both nodes are equal -- null is equal
            if one node has a value & the other doesn't -- not equal - return false
            insert left node pair & right node pair to queue
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # take a queue -- using BFS to implement this problem
        queue = [[p, q]] # insert into queue in a pair format, nodes from a similar position are in a pair 

        # loop while queue is not empty
        while queue:
            # pop first value from queue
            popP, popQ = queue.pop(0)

            # check to make sure either node has a value, if both nodes are none, don't need to do comparisions
            if popP or popQ:
                # check if either p or q doesn't have a value or if p & q are not same
                if not popP or not popQ or popP.val != popQ.val:
                    return False # return false if any of above is true

                # if reaches this point, it means they're same
                # append left nodes to queue
                queue.append([popP.left, popQ.left])
                # append right nodes to queue
                queue.append([popP.right, popQ.right])

        # if reaches this point, it means trees are same
        return True # return True
