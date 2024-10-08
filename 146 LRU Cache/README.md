# 146. LRU Cache

1 possible solution for this problem  

writeup later

## Method 1

To efficiently implement an LRU (Least Recently Used) cache, we use a combination of a **doubly linked list** and a **hashmap**. This approach allows us to achieve **O(1)** time complexity for both the `get` and `put` operations.

#### 1. **Data Structures**:
   - **Doubly Linked List**: Helps maintain the order of usage (least recently used to most recently used).
     - Each node has:
       - `key`: The key of the cached item.
       - `val`: The value associated with the key.
       - `prev`: Pointer to the previous node.
       - `next`: Pointer to the next node.
   - **Hashmap**: Maps keys to nodes in the doubly linked list, enabling O(1) access to any node.

#### 2. **Pointers**:
   - **left** (Least Recently Used - LRU): Always points to the least recently used node.
   - **right** (Most Recently Used - MRU): Always points to the most recently used node.

#### 3. **Helper Functions**:
   - **insert(node)**: Inserts a node at the `right` pointer, making it the most recently used node.
   - **delete(node)**: Deletes a node from any position in the linked list and re-establishes pointer connections.

#### 4. **Operations**:

1. **Initialization**:
   - Set up the doubly linked list with two dummy nodes: `left` (LRU) and `right` (MRU).
   - Initialize the hashmap to store key-node pairs for O(1) access.

2. **`get(key)`**:
   - If the key exists in the hashmap:
     - Retrieve the node.
     - Move the node to the `right` (make it the most recently used).
     - Return the value.
   - If the key does not exist, return `-1`.

3. **`put(key, value)`**:
   - If the key exists:
     - Update the node’s value.
     - Move the node to the `right`.
   - If the key does not exist:
     - Create a new node and insert it at the `right`.
     - Add this new node to the hashmap.
     - If the cache exceeds its capacity:
       - Remove the least recently used node (node at the `left` pointer) and delete it from the hashmap.

#### 5. **Complexity**:
   - **Time Complexity**: **O(1)** for both `get` and `put` operations.
   - **Space Complexity**: **O(n)** where `n` is the capacity of the cache.

This implementation ensures efficient insertion, deletion, and access, maintaining the correct order of least and most recently used elements in constant time.

### Self Notes
we can solve this problem by create a double linked list form the given input. we create a new class to implement nodes, it has 2 values - key & val, 2 pointers - prev & next. since we need to keep track of least recently used value we create two pointers, left - always is connected to least recently used node, right - always is connected to the most recently used node. also we take a hashmap to save all inputs, values will be saved to hashmap in this format - key:node. along with these we take two helper functions, insert - to insert nodes at the right since it's the most recently used node, delete - can delete anynode from anywhere - kills & reestablishes pointer connections. Now the get function returns value if key exists and makes that node the most recently visited node, if it doesn't returns 0. the put function updates the key value if it exists, also makes it the most recently visited node, if it doesn't creates a new nodes & inserts making sure it doesn't violate capacity, if it does deleted the least recently used node.   

```
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
```