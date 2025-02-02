"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    """
    the idea is to implement the intersection of two linked lists algorithm to this
        we need the node that's common in p & q's path to root
        instead of saving the path in a set
            we can use the depth aka the no. of nodes between p/q to root
        by using depth values we know the no. of nodes each node is seperated from the root
        now, we move the nodes to make them equal in depth from the root
        after their depth's match, move each towards the root in one step at a time until they meet
        once they meet, that node is the LCA
    """
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # recursive function to get depth
        def getDepth(node):
            depth = 0 # initialize value to 0

            # loop while node is valid
            while node:
                depth += 1 # increment depth by 1

                node = node.parent # reassign node to it's parent

            return depth # return depth value

        pDepth = getDepth(p) # get p node's depth
        qDepth = getDepth(q) # get q node's depth

        # get both nodes at the same depth
        # if p if higher
        for i in range(pDepth - qDepth):
            p = p.parent

        # if q if higher
        for i in range(qDepth - pDepth):
            q = q.parent

        # keep decreasing one at a time until they meet
        while p != q:
            p = p.parent
            q = q.parent

        return p

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        path = set() # create set to get node values from p --> root

        # loop while p is valid
        while p:
            path.add(p.val) # add this node's value to set
            p = p.parent # update p node to it's parent's value
        
        # loop while q's value is in set
        while q.val not in path:
            q = q.parent # update q node to it's parent's value
        
        # return q node
        return q
