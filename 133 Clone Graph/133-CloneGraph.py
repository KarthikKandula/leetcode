"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    """
    we can solve this problem using dfs graph traversal
        since we need to create a copy for each node & assign neighbors to each one, this is a recursive problem
        the basic idea is to create a copy & then call the recursive function for each neighbor to do the same
    
    create a hashmap to track old nodes for new nodes

    create a helper function that implements recursive dfs
        input is the node currently processed
        check if it already exists in hashmap
            if it does, return the new node
        if the node doesnt exist in the hashmap
        create a copy for the node
        insert it into the hashmap
            assign value to old node
        loop for each neighbor of old node
            recursively call for each node
            append the returned node (value) to copy node's neighbors array
        return copy node  

    once all recursive functions are created, each & every node should be created & connections established.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if input node is null, return none
        if not node:
            return None
        
        # create hashmap to keep track of old & new nodes
        oldToNew = {} # oldNode : New Node

        # create helper function
        def clone(node):
            # check if node already exists in hashmap
            if node in oldToNew:
                return oldToNew[node] # return new node value from hashmap

            # if code reaches this point, it means need to create a new node
            # create new node
            copy = Node(node.val, []) # create with emtpy neighbors for now

            # assign new copy node's value to original node in hashmap
            oldToNew[node] = copy

            # Loop for each neighbour in node
            for nei in node.neighbors:
                # recursive call for each neighbor
                # append the return result of each function call to neighbors - those are the copied nodes
                copy.neighbors.append(clone(nei))     
                # This makes sure, all neighbours are being created & connections are being made

            # Return copy
            return copy

        return clone(node)

