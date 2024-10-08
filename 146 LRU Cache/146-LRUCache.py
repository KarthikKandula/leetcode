class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

"""
we can solve this problem by creating a doubly linked list
    create new class for nodes
        has 2 values -- key & val
        has 2 pointer - prev & next

before building the double linked list, we'll take two pointers 
    left -- always is connected to the least recently used node
    right -- always is connected to the most recently used node

save all inputs to a hashmap

create all wanted variables in the init function 
    make connections for left & right with each other -- since there are no node's between them
    
take two helper functions 
    insert - always insert to the right since it's the most recently used node
    delete - can delete any node from anywhere -- kill & reestablish pointer connections

get function
    if the input key exists, return the value for that key
        before returning, we need to make that node most recently used node
        to do this, we delete the node & insert it
    return -1 if doesn't exist

put function
    if input key exists, update the value for that key
        before returning, we need to updaet that node's value with input value
        to do this, we delete the node & insert it
    if doesn't exist, create a new node & insert it

    check if inserting new node exceeds capacity
        if it does, delete least recently used node 
            it is attached to left
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity # hold capacity of the list
        self.cache = {} # hashmap to keep track of nodes -- save in format key: node
        # left pointer that is always connected to the least recently used node
        self.left = Node(0, 0) # create dummy node with value 0
        # right pointer that is always connected to the most recently used node
        self.right = Node(0, 0) # create dummy node with value 0

        # initially assign left & right to each other -- any other nodes will be inserted between these two
        self.left.next = self.right # assign left's next to right
        self.right.prev = self.left # assign right's prev to right

    # helper function to insert nodes into list -- always inserts to the right
    def insert(self, node: Node):
        prev = self.right.prev # get right's prev node
        nxt = self.right # assign right node to temp variable

        # connect outside node's to node
        prev.next = node # assign node to prev node's next pointer
        nxt.prev = node # assign node to right's prev pointer

        # make connections from node to outside
        node.next = nxt # assign node's next pointer to right
        node.prev = prev # assign prev pointer to previous node 

    # helper function to delete nodes into list
    def delete(self, node: Node):
        # get previous & next node to temp variables
        prev = node.prev
        nxt = node.next

        # delete & reestablish connections from node to outside
        prev.next = nxt # change next pointer
        nxt.prev = prev # change prev pointer

    def get(self, key: int) -> int:
        # check if key exists in hashmap -- if it does, return value & update node to recently visited
        if key in self.cache:
            # update node to recently visited before returning value
            # here we do it by deleting node from whereever & insert the node again at right
            # delete node 
            self.delete(self.cache[key])

            # insert node -- all inserts are done at right
            self.insert(self.cache[key])

            # return key's value
            return self.cache[key].val
        
        # if key doesn't exist in hashmap, return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key exists in hashmap -- if it does, update value & update node to recently visited
        if key in self.cache:
            # delete node -- will insert again below
            self.delete(self.cache[key])

        # create new node, & assign to key -- if exists, assign to same key since already deleted above
        self.cache[key] = Node(key, value)
        # insert node -- all inserts are done at right
        self.insert(self.cache[key])

        # check if adding that node made the length more than capacity
        if len(self.cache) > self.cap:
            # if it did, get the least recently used node that is attached to left
            lru = self.left.next
            # delete node
            self.delete(lru) # since left's next pointer is the least recently used node
            # delete the key from hashmap
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)