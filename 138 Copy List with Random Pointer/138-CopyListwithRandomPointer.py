"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    use basic linked list traversal along with a hashmap to solve the problem
        trick is to traver list 2 times 
            1st -- to create copy nodes & save them to hashmap
            2nd -- to make next & random connections to nodes 

    first pass
    loop thru the list
        create a copy node for each node
        add copy node to hashmap for the original node -- original node: copy node

    second pass
    loop thru the list
        get copy node from hashmap for curr node i.e original node
        replicate next & random connection of the original node to the copy node
            can do it by accessing those nodes from hashmap as well

    in the end return head's node value from hashmap since that's copy list's first node 
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a hashmap to keep record of the copy nodes created for each original
        oldToCopy = {None: None} # saved in the format original node: copy node

        # take a variable curr & assign to head
        curr = head
        
        # loop while curr is valid
        while curr:
            # create a copy node of the current node
            copy = Node(curr.val)
            oldToCopy[curr] = copy # add the curr node to hashmap & assign the copy node

            # make curr the next node -- for next iteration
            curr = curr.next
        
        # pass list again to connect nodes
        # take a variable curr & assign to head
        curr = head

        # loop while curr is valid
        while curr:
            # get current node's copy node form hashmap
            copy = oldToCopy[curr]

            # make links for the copy nodes
            copy.next = oldToCopy[curr.next] # assign current node's next node from hashmap to copy node -- it's already going to exist after above loop
            copy.random = oldToCopy[curr.random] # assign current node's random node from hashmap to copy node -- it's already going to exist after above loop

            # make curr the next node -- for next iteration
            curr = curr.next

        # we need to return the head of the copy list, we can return the value from hashmap for original node's head
        return oldToCopy[head]
